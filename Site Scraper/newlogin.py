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
# import pytz
from getpass import getpass


def get_page_source(link):
    driver.get(link)

    response = requests.get(link)
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')

    if page_type == "main page":
        #        time.sleep(10)   # Probably not needed at all or can be greatly reduced
        wait = 15
        try:
            wait_for_graph = WebDriverWait(driver, wait).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'expand-contract-button')))
        except TimeoutException:
            print('main page time out')

        # wait = 10
        # try:
        #     wait_for_graph = WebDriverWait(driver, wait).until(EC.presence_of_element_located((By.CLASS_NAME, 'expand-contract-button')))
        # except TimeoutException:
        #     print('main page time out')

        # print(len(soup.find_all('a', attrs={'href': re.compile("matchhistory")})))

        show_all = driver.find_element_by_xpath(
            '//*[@id="matchlist-show-all"]')
        show_all.click()
#        time.sleep(10)   # Probably not needed at all or can be greatly reduced
        return driver.page_source
    else:
        wait = 15  # Give the page 15 seconds to load the graph before timing out
        try:
            #            time.sleep(10)
            #            wait_for_graph = WebDriverWait(driver, wait).until(EC.presence_of_element_located((By.CLASS_NAME, 'event-graph')))
            wait_for_graph = WebDriverWait(driver, wait).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'card-name')))
            page_status = 'ready'
        except TimeoutException:
            page_status = 'not ready'
        return driver.page_source, page_status


def check_if_match_exists(game_date, game_count, blue_team, red_team):
    # for game in matches_played['matches']:
    #     db_date = game['game_date'].split('T')[0]
    #     game_number = (game['game_count'])
    #     team_one = (game['blue_team'])
    #     team_two = (game['red_team'])
    #     if (db_date == game_date) and ((team_one == blue_team) or (team_two == blue_team)) and (game_number == game_count) and ((team_two == red_team) or (team_one == red_team)):
    #         return True
    return False


def process_data(split_objective_data, blue_team, red_team):
    split_data = []
    objective_timer = []

    for entries in split_objective_data:
        split_data.append(entries.split())

    for idx, rows in enumerate(split_data):
        objective_timer.append([re.sub(
            "[^0-9.]", "", split_data[idx][4]), re.sub("[^0-9.]", "", split_data[idx][6])])

    for i in objective_timer:
        if i[0] == min(x[0] for x in objective_timer):
            first_objective = int(i[1])
            if first_objective == 0:
                return blue_team
            else:
                return red_team


def convert_month(month_name):
    return get_month[month_name]


page_type = 'hi'
login_url = 'http://account.riotgames.com/'

options = webdriver.ChromeOptions()

options.add_argument('--headless')
options.add_argument('--incognito')
options.add_argument("--start-maximized")
options.add_argument("--disable-popup-blocking")
options.add_argument('--disable-extensions')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
# options.add_argument('--hide-scrollbars')
# options.add_argument('--disable-gpu')
options.add_argument("--log-level=3")
driver_location = str(sys.argv[1])
driver = webdriver.Chrome(executable_path=driver_location, options=options)
driver.get(login_url)
driver.implicitly_wait(10)  # not sure if needed

# login stuff
wait_for_login = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'password-field')))
text_area = driver.find_elements_by_class_name('field__form-input')

lol_username = input("Please enter your League of Legends username: ")
text_area[0].send_keys(lol_username)

lol_password = getpass("Please enter your League of Legends password: ")
text_area[1].send_keys(lol_password)

# Insert check here to see if the login was sucessful. Otherwise prompt to re-enter account info

remember_me = driver.find_element_by_xpath(
    "//input[@data-testid='checkbox-remember-me']")
remember_me.click()
remember_me.send_keys(Keys.RETURN)

# Allows user to enter the verification code from their e-mail used to login to allow access to the matchhistory
while True:
    verification_code = input("Please enter the verifcation code: ")
    if len(verification_code) > 5:
        print("The verification code you entered is too long")
    elif len(verification_code) < 5:
        print("The verification code you entered is too short")
    else:
        break

verify_boxes = driver.find_element_by_class_name('mfafield__input')
verify_boxes.send_keys(verification_code)
verify_boxes.send_keys(Keys.RETURN)

wait = 15
try:
    wait_for_graph = WebDriverWait(driver, wait).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'riotbar-bar-content')))
except TimeoutException:
    print("Did not load")

# time.sleep(5)
print("Login complete")

# response = requests.get("https://lol-betting-stats.herokuapp.com/games")
# matches_played = json.loads(response.text)

matches_to_post = []

list_of_leagues_to_scrape = [
    'https://lol.fandom.com/wiki/LCS/2021_Season/Summer_Season',
    'https://lol.fandom.com/wiki/LEC/2021_Season/Summer_Season',
    'https://lol.fandom.com/wiki/LCO/2021_Season/Split_2',
    'https://lol.fandom.com/wiki/LPL/2021_Season/Summer_Season',
    'https://lol.fandom.com/wiki/LLA/2021_Season/Closing_Season',
    'https://lol.fandom.com/wiki/LVP_SuperLiga/2021_Season/Summer_Season',
    'https://lol.fandom.com/wiki/Ultraliga/Season_6',
    'https://lol.fandom.com/wiki/NA_Academy_League/2021_Season/Summer_Season',
    'https://lol.fandom.com/wiki/TCL/2021_Season/Summer_Season',
    'https://lol.fandom.com/wiki/CBLOL/2021_Season/Split_2',
    'https://lol.fandom.com/wiki/LJL/2021_Season/Summer_Season',
    'https://lol.fandom.com/wiki/LCK/2021_Season/Summer_Season'
    # 'https://lol.gamepedia.com/LFL/2020_Season/EM_Qualification',
    # 'https://lol.gamepedia.com/VCS/2020_Season/Summer_Playoffs',
    # 'https://lol.gamepedia.com/PCS/2020_Season/Summer_Playoffs'
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
    elif league == 'LCO':
        get_team_name_from_league = get_lco_name
    elif league == 'LFL':
        get_team_name_from_league = get_lfl_name
    elif league == 'LVP_SuperLiga':
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

    match_data = []

    # Get list of matches for entire split (dates, teams and score)
    for week in range(1, 15):
        match_counter = 0

        class_string_1 = 'ml-allw ml-w' + str(week) + ' ml-row'
        class_string_2 = 'ml-allw ml-w' + \
            str(week) + ' ml-row matchlist-newday'

        games = soup.find_all(
            attrs={"class": [class_string_1, class_string_2]})

        for game in games:
            split_game_data = (game.text).split()
            team_1_score_date = split_game_data[0]
            team_2_string = split_game_data[4]

            for idx, character in enumerate(team_1_score_date):
                if team_1_score_date[:idx].lower() in get_team_name_from_league:
                    blue_team = team_1_score_date[:idx].lower()
                    score_date = team_1_score_date[len(
                        blue_team):len(team_1_score_date)]
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
                    game_date = [year_match_played,
                                 month_match_played, date_of_match]
                    game_date = ('-'.join(game_date))

            for idx, character in enumerate(team_2_string):
                if team_2_string[-idx:].lower() in get_team_name_from_league:
                    red_team = team_2_string[-idx:].lower()

            for idx, _ in enumerate(range(set_game_count)):
                # if check_if_match_exists(game_date, (idx+1), blue_team, red_team) == False:
                match_data.append([game_date, (idx+1), blue_team, red_team])

    for idx, match in enumerate(match_data):
        does_match_already_exist = check_if_match_exists(
            match[0], int(match[1]), match[2], match[3])
        if does_match_already_exist == True:
            match_data[idx].append(0)  # Dont scrape
        else:
            match_data[idx].append(1)  # Scrape

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
    number_of_match_links = len(soup.find_all(
        'a', attrs={'href': re.compile("matchhistory")}))-altered

    page_type = "matchhistory page"

    # Collect match statistics (First blood, riftherald, dragon, tower, baron, inhibitor, winner)
    if number_of_match_links == len(match_data):
        print(
            "Continue because the number of match links matches the number of games found")
        # Retrieve data from each match history link
        for match in match_data:
            if match[4] == 1:
                print(match)

                # Reset variables to avoid wrong team being printed if the data cannot be found
                first_blood = ' '
                first_tower = ' '
                first_dragon = ' '
                first_riftherald = ' '
                first_baron = ' '
                first_inhibitor = ' '

                page_info = get_page_source(match[5])
                page_source = page_info[0]
                page_status = page_info[1]

                if page_status == 'ready':
                    soup = BeautifulSoup(page_source, 'html.parser')
                    player_team_names = soup.findAll(
                        'div', attrs={'class': 'champion-nameplate-name'})
                    if len(player_team_names) > 0:
                        for idx, player in enumerate(player_team_names):
                            if idx == 0:
                                blue_team = player.text.strip().split()[
                                    0].lower()
                            if idx == 5:
                                red_team = player.text.strip().split()[
                                    0].lower()
                    else:
                        blue_team = match[2]
                        red_team = match[3]

                    if 'Academy' in league:
                        blue_team = blue_team + '.a'
                        red_team = red_team + '.a'

                    if (blue_team not in match[2] and blue_team not in match[3]) or (red_team not in match[2] and red_team not in match[3]):
                        blue_team = match[2]
                        red_team = match[3]
                        matches_to_post.append([league_id, match[0].replace(
                            '-', '/'), match[1], blue_team, red_team, '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'])
                    else:
                        game_winner = soup.find(
                            'div', attrs={'class': 'game-conclusion'}).text  # Winner/Loser

                        if str(game_winner).strip() in 'VICTORY':
                            game_winner = blue_team
                            game_loser = red_team
                        else:
                            game_winner = red_team
                            game_loser = blue_team

                        total_kills = soup.findAll(
                            'div', attrs={'class': 'kills'})
                        team_one_kills = total_kills[0].text
                        team_two_kills = total_kills[2].text

                        # Obtain first blood, riftherald, dragon, tower, inhibitor, and baron info
                        objective_data = []
                        victim_data = []

                        for lines in soup.findAll('image'):
                            objective_data.append(str(lines))

                        riftherald_data = [
                            a for a in objective_data if "riftherald" in a]
                        dragon_data = [
                            b for b in objective_data if "dragon" in b]
                        baron_data = [
                            c for c in objective_data if "baron" in c]
                        inhibitor_data = [
                            d for d in objective_data if "inhibitor" in d]

                        # First Blood
                        first_blood = []

                        rows = soup.find_all('tr')
                        for row in rows:
                            first_blood.append(row.get_text())

                        first_blood = re.sub(
                            r'[a-zA-Z]+', '', first_blood[5], re.I)
                        first_blood = first_blood.split('●')[0]

                        if int(first_blood.count('○')) < 5:
                            first_blood = blue_team
                        else:
                            first_blood = red_team

                        # First Tower
                        for victim in soup.findAll('div', attrs={'class': 'victim'}):
                            victim_data.append(victim)

                        for victim in victim_data:
                            # Red team got first tower
                            if 'turret_100' in str(victim_data):
                                first_tower = red_team
                            # Blue team got first tower
                            elif 'turret_200' in str(victim_data):
                                first_tower = blue_team

                        if not dragon_data:
                            first_dragon = ' '
                        else:
                            first_dragon = process_data(
                                dragon_data, blue_team, red_team)

                        if not riftherald_data:
                            first_riftherald = ' '
                        else:
                            first_riftherald = process_data(
                                riftherald_data, blue_team, red_team)

                        if not baron_data:
                            first_baron = ' '
                        else:
                            first_baron = process_data(
                                baron_data, blue_team, red_team)

                        if not inhibitor_data:
                            first_inhibitor = ' '
                        else:
                            first_inhibitor = process_data(
                                inhibitor_data, blue_team, red_team)

                        matches_to_post.append([league_id, match[0].replace('-', '/'), match[1], blue_team, red_team, first_blood, first_tower, first_dragon.strip(
                        ), first_riftherald.strip(), first_inhibitor.strip(), first_baron.strip(), team_one_kills, team_two_kills, game_winner, game_loser])
                else:
                    print("The page ^ did not load correctly, skipping!")

                    page_info = get_page_source(match[5])
                    page_source = page_info[0]
                    page_status = page_info[1]

                    soup = BeautifulSoup(page_source, 'html.parser')
                    player_team_names = soup.findAll(
                        'div', attrs={'class': 'champion-nameplate-name'})

                    for idx, player in enumerate(player_team_names):
                        if idx == 0:
                            blue_team = player.text.strip().split()[0].lower()
                        if idx == 5:
                            red_team = player.text.strip().split()[0].lower()

                    if 'Academy' in league:
                        blue_team = blue_team + '.a'
                        red_team = red_team + '.a'

                    if (blue_team not in match[2] and blue_team not in match[3]) or (red_team not in match[2] and red_team not in match[3]):
                        blue_team = match[2]
                        red_team = match[3]

                    matches_to_post.append([league_id, match[0].replace(
                        '-', '/'), match[1], blue_team, red_team, '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'])
    else:
        print("It seems a matchhistory link for one of the games is missing")

print('Finished scraping!')

driver.close()
driver.quit()

# Confirm if the user wants to post to the database or not

for match_stats in matches_to_post:
    print(match_stats)

print("Would you like to post the new data to the database (y/n)? ")
post_data = input()

if post_data == "y" or post_data == "Y":
    print('Posting to the database')

    conn = psycopg2.connect(user="xtptslvncusnku", password="5261407ebfb09634166d7a969e81ff3686b100aaca5e430b8a901c189b3006f9",
                            host="ec2-54-224-124-241.compute-1.amazonaws.com", port="5432", database="d2fltass8ojj77", sslmode='require')
    cur = conn.cursor()

    cur.execute("SELECT MAX(id) FROM games;")
    unique_id = cur.fetchone()

    print('unique_id is: ')
    print(unique_id)

    if not all(unique_id):
        unique_id = 0
    else:
        unique_id = unique_id[0]

    print(unique_id)

    for match_stats in matches_to_post:
        print('sep')
        print(match_stats[:5])
        print(match_stats[5:])
        unique_id = unique_id+1
        cur.execute("INSERT INTO games VALUES (" + str(unique_id) +
                    " , %s, %s, %s, %s, %s)", match_stats[:5])
        cur.execute("INSERT INTO gamedata VALUES (" + str(unique_id) +
                    " , %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", match_stats[5:])

        # id, league_id, date, team_one_id, team_two_id
        # id, first_blood, first_tower, first_dragon, first_riftherald, first_inhibitor, first_baron, team_one_total_kills, team_two_total_kills, winner, loser

    print("Files were committed to the database")
    conn.commit()

# PGUSER = postgres PGPASSWORD = c04dcfbaceKAMI heroku pg: pull HEROKU_POSTGRESQL_MAGENTA 'lol-stats' - -app 'lol-betting-stats'
# heroku pg: pull DATABASE_URL lol-stats - -app lol-betting-stats

# heroku pg: pull DATABASE_URL lol-stats - -app lol-betting-stats

# heroku pg: pull lol-betting-stats: : RED lol-stats

# ALTER USER carlisle WITH SUPERUSER

# PGUSER = postgres PGPASSWORD = password heroku pg: pull DATABASE_URL mylocaldb - -app lol-betting-stats

# ALTER USER carlisle WITH SUPERUSER
# ALTER USER carlisle WITH CREATEROLE
# ALTER USER carlisle WITH CREATEUSER
# ALTER USER carlisle WITH Replication
# ALTER USER carlisle WITH Bypass RLS


# postgres: // xtptslvncusnku: 5261407ebfb09634166d7a969e81ff3686b100aaca5e430b8a901c189b3006f9@ec2-54-224-124-241.compute-1.amazonaws.com: 5432/d2fltass8ojj77

# pg_dump - -host = ec2-54-224-124-241.compute-1.amazonaws.com - -port = 5432 - -username = xtptslvncusnku - -password - -dbname = lol-betting-stats > output.sql

# heroku pg: backups: capture DATABASE_URL d2fltass8ojj77

# pg_restore - -verbose - -clean - -no-acl - -no-owner - h localhost - d lol-stats production.dump
