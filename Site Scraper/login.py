import csv
import psycopg2
import requests
import re
import time
import sys
import json
import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from team_name_mapper import *
import timeit
from datetime import datetime
import pytz
import time

import re

def get_page_source (link):
    # Load page and grab data
    driver.get(link)

    if page_type == "main page":
        show_all = driver.find_element_by_xpath('//*[@id="matchlist-show-all"]')
        show_all.click()
        time.sleep(5)   # Probably not needed at all or can be greatly reduced
        return driver.page_source
    else:    
        wait = 15 # Give the page 10 seconds to load the graph before timing out
        try:
            time.sleep(10)
            wait_for_graph = WebDriverWait(driver, wait).until(EC.presence_of_element_located((By.CLASS_NAME, 'event-graph')))
            page_status = 'ready'
        except TimeoutException:
            page_status = 'not ready'
        return driver.page_source, page_status    

def check_if_match_exists (game_date, game_count, blue_team, red_team):
    with open('matches_played.json') as json_file:
        data = json.load(json_file)

        for game in data['matches']:
            db_date = game['game_date'].split('T')[0]
            game_number = (game['game_count'])
            team_one = (game['blue_team'])
            team_two = (game['red_team'])

            if (db_date == game_date) and ((team_one == blue_team) or (team_two == blue_team)) and (game_number == game_count) and ((team_two == red_team) or (team_one == red_team)):                
                print(db_date + ' ' + team_one + ' ' + team_two)
                does_exist = True
                return does_exist

def process_data (split_objective_data, blue_team, red_team):
    split_data = []
    objective_timer = []

    for entries in split_objective_data:
        split_data.append(entries.split())

    for idx, rows in enumerate(split_data):
        objective_timer.append([re.sub("[^0-9.]", "", split_data[idx][4]), re.sub("[^0-9.]", "", split_data[idx][6])])

    for i in objective_timer:
        if i[0] == min(x[0] for x in objective_timer):
            first_objective = int(i[1])
            if first_objective == 0:
                return blue_team
            else:
                return red_team

def convert_month(month_name):
    return get_month[month_name]         

def load_db_match_history ():
    os.system('curl https://league-statistics-tracker.herokuapp.com/games | json_pp > matches_played.json') 

#### THIS SECTION LOGS US IN TO THE LEAGUE OF LEGENDS WEBSITE ###

page_type = 'hi'    
login_url = 'http://account.riotgames.com/'

options = webdriver.ChromeOptions()
#options.add_argument("user-data-dir=/Users/Carlisle/Desktop/Chrome")
options.add_argument('--headless')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--disable-extensions')
driver = webdriver.Chrome(executable_path = '/Users/Carlisle/Desktop/OmegleV2/chromedriver', options = options)
#driver_location = str(sys.argv[1])
#driver = webdriver.Chrome(executable_path=driver_location, options=options)
driver.get(login_url)
driver.implicitly_wait(10) # not sure if needed

# login stuff 
wait_for_login = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'password-field')))
text_area = driver.find_elements_by_class_name('field__form-input')
text_area[0].send_keys("KamiStriker")
text_area[1].send_keys("c04dcfbaceKAMI")

time.sleep(2)

remember_me = driver.find_element_by_xpath("//input[@data-testid='checkbox-remember-me']")
remember_me.click()
remember_me.send_keys(Keys.RETURN)

# Allows user to enter the verification code from their e-mail used to login to allow access to the matchhistory
print("Please enter the verifcation code: ")
verification_code = input() 
verify_boxes = driver.find_element_by_class_name('mfafield__input')
verify_boxes.send_keys(verification_code)
verify_boxes.send_keys(Keys.RETURN)
# Perform a check to check if the code is 5 letters/numbers, reask for input if incorrect
# Check if len() = 5

time.sleep(5)

print("Login complete")

#################################################################

############ THIS SECTION GETS THE MOST CURRENT DATA ############ 

print("Loading match history from database")
load_db_match_history()

#################################################################

post_lcs = 'false'
post_lck = 'false'
post_lec = 'false'
post_opl = 'false'
post_lfl = 'false'
post_lvp = 'false'
post_lms = 'false'
post_na_academy = 'false'
post_lla = 'false'
post_ultraliga = 'false'
post_lpl = 'false'

############ THIS SECTION GATHERS ALL THE MATCH DATA ############ 

list_of_leagues_to_scrape = [
    'https://lol.gamepedia.com/LCS/2020_Season/Summer_Season',
    'https://lol.gamepedia.com/LEC/2020_Season/Summer_Season',
    'https://lol.gamepedia.com/OPL/2020_Season/Split_2',
    'https://lol.gamepedia.com/LPL/2020_Season/Summer_Season', # missing match history links
    'https://lol.gamepedia.com/LLA/2020_Season/Closing_Season', # no games yet
    #'https://lol.gamepedia.com/LFL/2020_Season/Summer_Season' # No schedule yet so now show-all button!
    'https://lol.gamepedia.com/LVP_SuperLiga_Orange/2020_Season/Summer_Season',
    'https://lol.gamepedia.com/Ultraliga/Season_4',
    'https://lol.gamepedia.com/NA_Academy_League/2020_Season/Summer_Season',
    'https://lol.gamepedia.com/TCL/2020_Season/Summer_Season',
    'https://lol.gamepedia.com/CBLOL/2020_Season/Split_2',
    'https://lol.gamepedia.com/LJL/2020_Season/Summer_Season',
    'https://lol.gamepedia.com/VCS/2020_Season/Summer_Season',
    'https://lol.gamepedia.com/LCK/2020_Season/Summer_Season',
    'https://lol.gamepedia.com/PCS/2020_Season/Summer_Season' 
]

for league_url in list_of_leagues_to_scrape:

    page_type = "main page"

    league = league_url.split("/")

    league = league[3]

    league_id = get_league_id(league)
    split_id = get_split_id(league)
    
    if league == 'LCK':
        get_team_name_from_league = get_lck_name
    elif league == 'LEC':
        get_team_name_from_league = get_lec_name
    elif league == 'OPL':
        get_team_name_from_league = get_opl_name
    elif league == 'LFL':
        get_team_name_from_league = get_lfl_name
    elif league == 'LVP_SuperLiga_Orange':
        get_team_name_from_league = get_lvp_name
    elif league == 'PCS':
        get_team_name_from_league = get_pcs_name
    elif league == 'LCS':
        get_team_name_from_league = get_lcs_name
    elif league == 'LLA':
        get_team_name_from_league = get_lla_name
    elif league == 'Ultraliga':
        get_team_name_from_league = get_ultraliga_name
    elif league == 'LPL':
        get_team_name_from_league = get_lpl_name
    elif league == 'NA_Academy_League':
        get_team_name_from_league = get_na_academy_league_name
    elif league == 'LJL':
        get_team_name_from_league = get_ljl_name
    elif league == 'TCL':
        get_team_name_from_league = get_tcl_name
    elif league == 'VCS':
        get_team_name_from_league = get_vcs_name
    elif league == 'CBLOL':
        get_team_name_from_league = get_cblol_name
    else:
        get_team_name_from_league = get_worlds_name
        #get_team_name_from_league = get_name

    outfile = "./" + league + " Data.csv"
    outfile = open(outfile, "w")
    writer = csv.writer(outfile)
    writer.writerow(['League', 'Split', 'Date', 'Game', 'Blue Team', 'Red Team', 'First Blood', 'First Tower',  'First Dragon', 'First Inhibitor', 'First Baron', 'Winner', 'Loser'])

    print('Scraping ' + league + ' main page')

    page_source = get_page_source(league_url)    
    soup = BeautifulSoup(page_source, 'html.parser')

    match_data = []
    tbdcount = 0

    ##### SECTION DIVIDER HERE ##### 

    # Get list of matches for entire split (dates, teams and score)
    for week in range(1, 15):
        class_string_1 = 'ml-allw ml-w' + str(week) + ' ml-row'
        class_string_2 = 'ml-allw ml-w' + str(week) + ' ml-row matchlist-newday'

        games = soup.find_all(attrs={"class": [class_string_1, class_string_2]})

#        test_winner = soup.select('.matchlist-winner-team , .matchlist-winner-team')

        ############ THIS SECTION GIVES US THE MOST RECENT GAME PLAYED
        if (len(games) > 0):
            final_match = games[len(games)-1]
            final_match = (final_match.text).split()

            final_match_t1 = final_match[0]
            final_match_t2 = final_match[4]

            for idx, character in enumerate(final_match_t1):
                if final_match_t1[:idx].lower() in get_team_name_from_league:
                    most_recent_game_t1 = final_match_t1[:idx].lower()
                    most_recent_game_t1 = most_recent_game_t1.strip()
        
            for idx, character in enumerate(final_match_t2):
                if final_match_t2[-idx:].lower() in get_team_name_from_league:
                    most_recent_game_t2 = final_match_t2[-idx:].lower()
                    most_recent_game_t2 = most_recent_game_t2.strip()

        ####################################################################################

        number_of_games_played = len(games)
        number_of_games_in_week = int((len(soup.select('.ml-w' + str(week) + ' .ml-team')))/2)

        if (number_of_games_played == 0) or (number_of_games_played != number_of_games_in_week):
            if (tbdcount == 0): # Only get the current week
                # Create a csv file to store upcoming matches
                tbd_outfile = "./" + league + " Upcoming Games.csv"
                tbd_outfile = open(tbd_outfile, "w")
                tbd_writer = csv.writer(tbd_outfile)

                date_class_1 = 'ml-allw ml-w' + str(week) + ' ml-row ml-row-tbd'
                date_class_2 = 'ml-allw ml-w' + str(week) + ' ml-row ml-row-tbd matchlist-newday'

                toggle_number = 1
                length_counter = len(soup.select('.ml-w' + str(week) + '.ofl-toggler-' + str(toggle_number) + '-all span'))

                while (length_counter == 0):
                    toggle_number += 1
                    length_counter = len(soup.select('.ml-w' + str(week) + '.ofl-toggler-' + str(toggle_number) + '-all span'))

                date_teams_class = '.matchlist-tab-wrapper:nth-child(' + str(week) + ') , .team , .ml-w' + str(week) + '.ofl-toggler-' + str(toggle_number) + '-all span'
                
                tbdgames = soup.find_all(attrs={"class": [date_class_1, date_class_2]})
                tbd_teams_dates = soup.select(date_teams_class)

                date_counter = 0
                for data in tbd_teams_dates:
                    split_date = (data.text).split()
                    if (len(split_date) > 10):
                        date_index = date_counter
                    date_counter += 1

                splice_to_week = tbd_teams_dates[date_index+1:len(tbd_teams_dates)]

                index_counter = 0                
                for splice in splice_to_week:
                    if ((re.sub(r'[^a-z]', '', ((splice.text).lower().strip()))) == re.sub(r'[^a-z]', '', (most_recent_game_t1.strip()))):
                        if ((re.sub(r'[^a-z]', '', ((splice_to_week[index_counter+1].text).lower().strip()))) == re.sub(r'[^a-z]', '', (most_recent_game_t2.strip()))):
                            current_game_index = index_counter+2
                            break
                    index_counter += 1

                number_of_days = len(soup.select('.ml-w' + str(week) + '.ofl-toggler-' + str(toggle_number) + '-all span'))
                length_to_splice = (len(tbdgames)*2)+number_of_days

                date_team_vs = []

                if (number_of_games_played == 0):
                    splice_to_current_week = splice_to_week[0:length_to_splice]
                else:
                    splice_to_current_week = splice_to_week[current_game_index:length_to_splice+(number_of_games_played*2)]
                    
                    first_result = (splice_to_week[current_game_index].text).split()

                    search_counter = 0
                    while ('Mon' not in first_result and 'Tue' not in first_result and 'Wed' not in first_result and 'Thu' not in first_result and 'Fri' not in first_result and 'Sat' not in first_result and 'Sun' not in first_result):
                        search_counter += 1
                        first_result = (splice_to_week[current_game_index-search_counter].text).split()
                        
                    if search_counter > 0:
                        match_date = first_result

                team_1 = True

                for data in splice_to_current_week:
                    split_data = (data.text).split()

                    if 'Mon' in split_data or 'Tue' in split_data or 'Wed' in split_data or 'Thu' in split_data or  'Fri' in split_data or 'Sat' in split_data or 'Sun' in split_data:                        
                        match_date = split_data
                    else:
                        tbd_team_name = split_data[0]
                        if (team_1):
                            for idx, character in enumerate(tbd_team_name):
                                if tbd_team_name[:idx].lower() in get_team_name_from_league:
                                    tbd_team_1 = tbd_team_name[:idx].lower()
                            date_team_vs.append(league_id) 
                            date_team_vs.append(match_date[0]) # Add the day of the match
                            date_team_vs.append(match_date[1]) # Add the date of the match
                            date_team_vs.append(tbd_team_1) # Add team 1
                        else:                            
                            for idx, character in enumerate(tbd_team_name):
                                if tbd_team_name[-idx:].lower() in get_team_name_from_league:
                                    tbd_team_2 = tbd_team_name[-idx:].lower()
                            date_team_vs.append(tbd_team_2) # Add team 2        
                            tbd_writer.writerows([date_team_vs])
                            date_team_vs = []

                        team_1 = not team_1

                tbdcount += 1
                ####################################################################################

        for game in games:
            split_game_data = (game.text).split()
            print(split_game_data)
            team_1_score_date = split_game_data[0]
            team_2_string = split_game_data[4]

            for idx, character in enumerate(team_1_score_date):
                if team_1_score_date[:idx].lower() in get_team_name_from_league:
                    blue_team = team_1_score_date[:idx].lower()
                    score_date = team_1_score_date[len(blue_team):len(team_1_score_date)]
                    score_date = score_date.replace(" ", "")
                    score_date = ''.join(e for e in score_date if e.isalnum())

                    blue_team_score = score_date[0]
                    red_team_score = score_date[1]

                    if len(score_date) == 4:
                        date_of_match = score_date[-2:]
                    elif len(score_date) == 3:
                        date_of_match = '0' + score_date[-1:]

                    set_game_count = int(blue_team_score) + int(red_team_score) 

                    month_match_played = split_game_data[1]
                    month_match_played = convert_month(month_match_played)

                    if len(month_match_played) == 1:
                        month_match_played = '0' + month_match_played

                    year_match_played = split_game_data[2]
                    game_date = [year_match_played, month_match_played, date_of_match]
                    game_date = ('-'.join(game_date))

            for idx, character in enumerate(team_2_string):
                if team_2_string[-idx:].lower() in get_team_name_from_league:
                    red_team = team_2_string[-idx:].lower()      

            # Team 1 starts blue side and alternates for each game after the first
            match_data.append([game_date, '1', blue_team, red_team]) 
            if set_game_count >= 2:
                match_data.append([game_date, '2', red_team, blue_team])
            if set_game_count >= 3:
                match_data.append([game_date, '3', blue_team, red_team])
            if set_game_count >= 4:
                match_data.append([game_date, '4', red_team, blue_team])
            if set_game_count == 5:
                match_data.append([game_date, '5', blue_team, red_team])

    for idx, match in enumerate(match_data):
        does_match_already_exist = check_if_match_exists(match[0], int(match[1]), match[2], match[3])
        if does_match_already_exist == True:
            match_data[idx].append("don't scrape")
        else:
            match_data[idx].append("scrape")
            print("New data")
            print(match)

    # Compile a list of matchhistory links
    print('Starting to scrape individual ' + league + ' games')
    response = requests.get(league_url)
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')

    altered = 0
    counter = 0
    for link in soup.find_all('a', attrs={'href': re.compile("matchhistory")}):
        if link.text == "Link":
            match_data[counter].append(link.get('href'))
            counter = counter+1
        else:
            print("Dont increase")
            altered = altered+1

    page_type = "matchhistory page"

    # Collect match statistics (First blood, riftherald, dragon, tower, baron, inhibitor, winner)
    if len(soup.find_all('a', attrs={'href': re.compile("matchhistory")}))-altered == len(match_data):
        print("Continue because the number of match links matches the number of games found")
        # Retrieve data from each match history link
        for match in match_data:
            if match[4] == 'scrape':
                print('Scraping...')
                # print("Idx winner")
                # print((test_winner[idx].text))
                print(match)

                # Reset variables to avoid wrong team being printed if the data cannot be found
                first_blood = ' '
                first_tower = ' '
                first_dragon = ' '
                first_baron = ' '
                first_inhibitor = ' '

                print("Getting page info from")
                print(match[5])
                page_info = get_page_source(match[5])
                page_source = page_info[0]
                page_status = page_info[1]
                print("Got page info")

                if page_status == 'ready':
                    print("Getting new soup")
                    soup = BeautifulSoup(page_source, 'html.parser')
                    print("Got new soup")

                    player_team_names = soup.findAll('div', attrs={'class':'champion-nameplate-name'})
                    for idx, player in enumerate(player_team_names):
                        if idx == 0:
                            blue_team = player.text.strip().split()[0].lower()
                            print(blue_team)
                        if idx == 5:
                            red_team = player.text.strip().split()[0].lower()
                            print(red_team)
                    
                    if blue_team in match[2] and blue_team in match[3]:
                        if red_team in match[3]:
                            blue_team = match[2]
                            red_team = match[3]
                        else:
                            red_team = match[2]
                            blue_team = match[3]
                    elif blue_team in str(match[2]):
                        blue_team = match[2]
                        red_team = match[3]
                    else:
                        red_team = match[2]
                        blue_team = match[3]

                    print("Date: " + match[0] + " Blue team: " + blue_team + " Red team: " + red_team)

                    #game_winner = soup.select('.team-100') # Winner/Loser

                    game_winner = soup.find('div', attrs={'class':'game-conclusion'}).text # Winner/Loser
                    #game_winner = soup.select('.team-100 .game-conclusion') # Winner/Loser
                    #game_winner = soup.select('.team-100') # Winner/Loser
                    # #game_winner = soup.select('.game-conclusion') # Winner/Loser

                    print(game_winner)

                    # print("loop")
                    # for x in game_winner:
                    #     print((x.text).split())
                    # print('end loop')

                    #print(game_winner)

                    # game_winner = [''.join(i.stripped_strings) for i in game_winner if i]
                    # game_winner = game_winner[0]
                    # print("Game winner")
                    # print((game_winner.text).strip())

                    # .team-100 .game-conclusion
                    #//*[contains(concat( " ", @class, " " ), concat( " ", "team-100", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "game-conclusion", " " ))]
                    #soup.select('.team-100 .game-conclusion')

                    if str(game_winner).strip() in 'VICTORY':
                        print("Blue team won")
                        game_winner = blue_team
                        game_loser = red_team
                    else:
                        print("Red team won")
                        game_winner = red_team
                        game_loser = blue_team

                    # Obtain first blood, riftherald, dragon, tower, inhibitor, and baron info
                    objective_data = []
                    victim_data = []

                    for lines in soup.findAll('image'):
                        objective_data.append(str(lines))

                    riftherald_data = [a for a in objective_data if "riftherald" in a]
                    dragon_data = [b for b in objective_data if "dragon" in b]
                    baron_data = [c for c in objective_data if "baron" in c]
                    inhibitor_data = [d for d in objective_data if "inhibitor" in d]

                    # First Blood
                    first_blood = []

                    rows = soup.find_all('tr')
                    for row in rows:
                        first_blood.append(row.get_text())

                    first_blood = re.sub(r'[a-zA-Z]+', '', first_blood[5], re.I)
                    first_blood = first_blood.split('●')[0]

                    if int(first_blood.count('○')) < 5:
                        first_blood = blue_team
                    else:
                        first_blood = red_team

                    # First Tower
                    for victim in soup.findAll('div', attrs={'class':'victim'}):
                        victim_data.append(victim)

                    for victim in victim_data:
                        if 'turret_100' in str(victim_data): # Red team got first tower
                            first_tower = red_team
                        elif 'turret_200' in str(victim_data): # Blue team got first tower
                            first_tower = blue_team   

                    if not dragon_data:
                        first_dragon = ' '
                    else: 
                        first_dragon = process_data(dragon_data, blue_team, red_team)

                    if not baron_data:
                        first_baron = ' '
                    else:
                        first_baron = process_data(baron_data, blue_team, red_team)

                    if not inhibitor_data:
                        first_inhibitor = ' '
                    else:
                        first_inhibitor = process_data(inhibitor_data, blue_team, red_team)

                    # Append to file
                    game_data = []
                    game_data.append([league_id, split_id, match[0].replace('-','/'), match[1], blue_team, red_team, first_blood, first_tower, first_dragon.strip(), first_inhibitor.strip(), first_baron.strip(), game_winner, game_loser])
                    if first_dragon.strip() == '' and first_inhibitor.strip() == '' and first_baron.strip() == '':
                        print("The matchhistory for this match does not load properly and will not be written to file")
                    else:
                        writer.writerows(game_data)
                    print('Completed scraping the match')

                    if league == 'LCK':
                        post_lck = 'true'
                    elif league == 'LEC':
                        post_lec = 'true'
                    elif league == 'OPL':
                        post_opl = 'true'
                    elif league == 'LFL':
                         post_lfl = 'true'
                    elif league == 'LVP_SuperLiga_Orange':
                         post_lvp = 'true'
                    elif league == 'PCS':
                         post_lms = 'true'
                    elif league == 'LCS':
                        post_lcs = 'true'
                    elif league == 'LLA_Clausura':
                        post_lla = 'true'
                    elif league == 'Ultraliga':
                        post_ultraliga = 'true'
                    # elif league == 'LPL':
                    #     post_lpl = 'true'
                    elif league == 'NA_Academy_League':
                        post_na_academy = 'true'
                else:
                    print ("The page did not load correctly, skipping!")
    else:
        print("It seems a matchhistory link for one of the games is missing")

print('Finished scraping!')

# Close the browser
driver.close() 
driver.quit()

# print("Would you like to post the new data to the database (y/n)? ")

# post_data = input() 

# print(post_data)

# if post_data == "y" or post_data == "Y":
#     print('Posting to the database')

#     conn = psycopg2.connect(user = "djpoucmhkewvrh", password = "e1a533e45aa586bf82ff18dcc021969e6fb438333e501973f5236ab9257aea9c", host = "ec2-174-129-209-212.compute-1.amazonaws.com", port = "5432", database = "d24ubplectbqas", sslmode = 'require')
#     cur = conn.cursor()

#     cur.execute("SELECT COUNT(*) FROM games")
#     unique_id = cur.fetchone()
#     unique_id = unique_id[0]
#     #Maybe check id of the last entry here to ensure this works even with deleted entries

#     input_file = {
#         'LCS Data.csv',
#         'LCK Data.csv',
#         'LEC Data.csv',
#         'OPL Data.csv',
#         #'LFL Data.csv',
#         'LVP_SuperLiga_Orange Data.csv',
#         'PCS Data.csv',
#         'LLA Data.csv',
#         'Ultraliga Data.csv',
#         'LPL Data.csv',
#         'NA_Academy_League Data.csv',
#         'LJL Data.csv',
#         'TCL Data.csv',
#         'VCS Data.csv',
#         'CBLOL Data.csv'
#     }

#     # print(post_lck)
#     # print(post_lec)
#     # print(post_opl)
#     # print(post_lfl)
#     # print(post_lvp)
#     # print(post_lms)
#     # print(post_lcs)
#     # print(post_na_academy)
#     # print(post_lla)
#     # print(post_ultraliga)

#     for file in input_file:
#     # if ((file == 'LCK Data.csv' and post_lck == 'true') or (file == 'LEC Data.csv' and post_lec == 'true') or (file == 'OPL Data.csv' and post_opl == 'true') or (file == 'LFL Data.csv' and post_lfl == 'true') or (file == 'LVP_SuperLiga_Orange Data.csv' and post_lvp == 'true') or (file == 'PCS Data.csv' and post_lms == 'true') or (file == 'LCS Data.csv' and post_lcs == 'true') or (file == 'LLA Data.csv' and post_lla == 'true') or (file == 'Ultraliga Data.csv' and post_ultraliga == 'true')):
#             print("Adding matches from " + file + ' to the database')
#             with open(file, 'r') as f:
#                 reader = csv.reader(f)
#                 next(reader) # Skip the header row
#                 # Do something here to check if file is empty
#                 for (index, row) in enumerate(reader):
#                     print(index)
#                     unique_id = unique_id+1
#                     cur.execute("INSERT INTO games VALUES (" + str(unique_id) + " , %s, %s, %s, %s, %s, %s)", row[:6])
#                     cur.execute("INSERT INTO match_results VALUES (%s, %s, %s, %s, %s, %s, %s, " + str(unique_id) + ")", row[6:])

#     print("Commiting files to the database")
#     conn.commit()
# else:
#     print("Not posting")

# Current issues
    # Cant post straight to db after scraping games
