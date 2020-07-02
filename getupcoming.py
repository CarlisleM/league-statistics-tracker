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

    print('Scraping ' + league + ' main page')

    page_source = get_page_source(league_url)    
    soup = BeautifulSoup(page_source, 'html.parser')

    tbdcount = 0
    current_match_index = 0

    # Create a csv file to store upcoming matches
    tbd_outfile = "./" + league + " Upcoming Games.csv"
    tbd_outfile = open(tbd_outfile, "w")
    tbd_writer = csv.writer(tbd_outfile)

    # Get list of matches for entire split (dates, teams and score)
    for week in range(1, 15):
        match_counter = 0

        class_string_1 = 'ml-allw ml-w' + str(week) + ' ml-row'
        class_string_2 = 'ml-allw ml-w' + str(week) + ' ml-row matchlist-newday'

        games = soup.find_all(attrs={"class": [class_string_1, class_string_2]})

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

        number_of_games_played = len(games)
        number_of_games_in_week = int((len(soup.select('.ml-w' + str(week) + ' .ml-team')))/2)

        if number_of_games_in_week == number_of_games_played:
            current_match_index += number_of_games_in_week

        if (number_of_games_in_week > 0):
            if (number_of_games_played == 0) or (number_of_games_played != number_of_games_in_week):
                date_class_1 = 'ml-allw ml-w' + str(week) + ' ml-row ml-row-tbd'
                date_class_2 = 'ml-allw ml-w' + str(week) + ' ml-row ml-row-tbd matchlist-newday'
                date_class_3 = 'ml-allw ml-w' + str(week) + ' ml-row ml-row-tbd matchlist-flex'
                date_class_4 = 'ml-allw ml-w' + str(week) + ' ml-row-tbd matchlist-newday matchlist-flex'
                date_class_5 = 'ml-allw ml-w' + str(week) + ' ml-row ml-row-tbd matchlist-newday matchlist-flex'

                toggle_number = 1
                length_counter = len(soup.select('.ml-w' + str(week) + '.ofl-toggler-' + str(toggle_number) + '-all span'))

                while (length_counter == 0):
                    toggle_number += 1
                    length_counter = len(soup.select('.ml-w' + str(week) + '.ofl-toggler-' + str(toggle_number) + '-all span'))

                date_teams_class = '.matchlist-tab-wrapper:nth-child(' + str(week) + ') , .team , .ml-w' + str(week) + '.ofl-toggler-' + str(toggle_number) + '-all span'
                
                match_time_class = 'ofl-toggle-' + str(toggle_number) + '-2 ofl-toggler-' + str(toggle_number) + '-all'
                all_match_time = soup.find_all(attrs={"class": match_time_class}) 

                if number_of_games_played == 0:
                    match_times = all_match_time[current_match_index:current_match_index+number_of_games_in_week]
                else:
                    match_times = all_match_time[current_match_index+number_of_games_played:current_match_index+number_of_games_in_week]

                current_match_index += number_of_games_in_week

                tbdgames = soup.find_all(attrs={"class": [date_class_1, date_class_2]})

                if (len(tbdgames) == 0):
                    tbdgames = soup.find_all(attrs={"class": [date_class_1, date_class_2, date_class_3, date_class_4, date_class_5]})

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
                            date_team_vs.append(str(week)) # Add the week of the match
                            date_team_vs.append(league_id) # Add what league the match is from
                            date_team_vs.append(match_date[0]) # Add the day of the match
                            date_team_vs.append(match_date[1]) # Add the date of the match
                            date_team_vs.append(match_times[match_counter].text) # Add the time of the match
                            date_team_vs.append(tbd_team_1) # Add team 1
                            match_counter += 1
                        else:                            
                            for idx, character in enumerate(tbd_team_name):
                                if tbd_team_name[-idx:].lower() in get_team_name_from_league:
                                    tbd_team_2 = tbd_team_name[-idx:].lower()
                            date_team_vs.append(tbd_team_2) # Add team 2        
                            tbd_writer.writerows([date_team_vs])
                            date_team_vs = []
                        
                        team_1 = not team_1

print('Finished getting upcoming matches!')

# Close the browser
driver.close() 
driver.quit()
