import psycopg2
import time
import requests
import re
import sys
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from team_name_mapper import *
from getpass import getpass
import json
import mwclient

def get_page_source(link):
    driver.get(link)

    wait = 15
    try:
        wait_for_page = WebDriverWait(driver, wait).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'expand-contract-button')))
    except TimeoutException:
        print('main page time out')

    show_all = driver.find_element_by_xpath(
        '//*[@id="matchlist-show-all"]')
    show_all.click()

    time.sleep(5)
    driver.implicitly_wait(5)

    show_all_history = driver.find_element_by_xpath('//*[@id="md-table"]/tbody[1]/tr[1]/th[1]/div[1]/div[1]/span[1]')
    show_all_history.click()

    return driver.page_source

def check_if_match_exists(game_date, game_count, blue_team, red_team):
    # for game in matches_played['matches']:
    #     db_date = game['game_date'].split('T')[0]
    #     game_number = (game['game_count'])
    #     team_one = (game['blue_team'])
    #     team_two = (game['red_team'])
    #     if (db_date == game_date) and ((team_one == blue_team) or (team_two == blue_team)) and (game_number == game_count) and ((team_two == red_team) or (team_one == red_team)):
    #         return True
    return False

def convert_month(month_name):
    return get_month[month_name]

matches_to_post = []

list_of_leagues_to_scrape = [
    # 'https://lol.fandom.com/wiki/LCK/2022_Season/Summer_Season', # LCK 1 TODO: Werid format cause bo3
    # 'https://lol.fandom.com/wiki/LEC/2022_Season/Summer_Season', # LEC 2 
    # 'https://lol.fandom.com/wiki/LVP_SuperLiga/2022_Season/Summer_Season', # LVP 3 
    # 'https://lol.fandom.com/wiki/LCO/2022_Season/Split_2', # LCO (Oceania) 4 
    'https://lol.fandom.com/wiki/LFL/2022_Season/Summer_Season', # LFL 5 
    # 'https://lol.fandom.com/wiki/PCS/2022_Season/Summer_Season', # PCS 6 
    # 'https://lol.fandom.com/wiki/LCS/2022_Season/Summer_Season', # LCS 7 
    # 'https://lol.fandom.com/wiki/NA_Academy_League/2022_Season/Summer_Season', # NA Academy 8 TODO: list index out of range Werid format cause 2 games
    # 'https://lol.fandom.com/wiki/LLA/2022_Season/Closing_Season', # LLA 9 
    # 'https://lol.fandom.com/wiki/Ultraliga/Season_8', # Ultraliga 10 
    # 'https://lol.fandom.com/wiki/LPL/2022_Season/Summer_Season', # LPL 11 TODO: Werid format cause bo3
    # 'https://lol.fandom.com/wiki/LJL/2022_Season/Summer_Season', # LJL 12 
    # 'https://lol.fandom.com/wiki/TCL/2022_Season/Summer_Season', # TCL 13 
    # # 'https://lol.fandom.com/wiki/VCS/2022_Season/Summer_Season', # VCS 14 TODO: Werid format cause bo3
    # 'https://lol.fandom.com/wiki/CBLOL/2022_Season/Split_2', # CBLOL 15 
]

page_type = ''

options = webdriver.ChromeOptions()

options.add_argument('--headless')
options.add_argument('--incognito')
options.add_argument("--start-maximized")
options.add_argument("--disable-popup-blocking")
options.add_argument('--disable-extensions')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument("--log-level=3")
driver_location = str(sys.argv[1])
driver = webdriver.Chrome(executable_path=driver_location, options=options)
driver.get(list_of_leagues_to_scrape[0])
driver.implicitly_wait(10)  # not sure if needed

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

# response = requests.get("https://lol-betting-stats.herokuapp.com/games")
# matches_played = json.loads(response.text)

postingAvailable = False

site = mwclient.Site('lol.fandom.com', path='/')

for league_url in list_of_leagues_to_scrape:
    page_type = "main page"

    league = league_url.split("/")

    league = league[4]

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
    skip_games = []

    tables = soup.find('table', id="md-table")

    initalRows = tables.findAll('tr')[:3]

    columnCounter = 0
    match_history_index = 0
    blue_team_index = 0
    red_team_index = 0
    for column in initalRows[2].findAll('th'):
        if column.getText() == "MH" and match_history_index == 0:
            match_history_index = columnCounter
        if column.getText() == "Blue" and blue_team_index == 0:
            blue_team_index = columnCounter
            red_team_index = columnCounter + 1
        columnCounter = columnCounter + 1

    rows = tables.findAll('tr')[3:]
    match_counter = 0
    increment_counter = 0

    # Get list of matches for entire split (dates, teams and score)
    for week in range(1, 22): # TODO: was 15
        class_string_1 = 'ml-allw ml-w' + str(week) + ' ml-row'
        class_string_2 = 'ml-allw ml-w' + \
            str(week) + ' ml-row matchlist-newday'

        games = soup.find_all(
            attrs={"class": [class_string_1, class_string_2]})

        for game in games:
            currentRow = rows[match_counter]

            currentRowColumns = currentRow.findAll('td')

            if (len(currentRowColumns) >= 9):
                if currentRowColumns[match_history_index].getText() != "Link":
                    skip_games.append(increment_counter)

                currentRowBlueTeam = currentRowColumns[blue_team_index].getText()
                currentRowRedTeam = currentRowColumns[red_team_index].getText()

                match_blue_team = currentRowBlueTeam.lower()
                match_red_team = currentRowRedTeam.lower()
            else:
                match_counter = match_counter + 2  

                currentRow = rows[match_counter]

                currentRowColumns = currentRow.findAll('td')

                currentRowBlueTeam = currentRowColumns[blue_team_index].getText()
                currentRowRedTeam = currentRowColumns[red_team_index].getText()

                match_blue_team = currentRowBlueTeam.lower()
                match_red_team = currentRowRedTeam.lower() 

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
                match_data.append([game_date, (idx+1), match_blue_team, match_red_team])

            match_counter = match_counter + 1
            increment_counter = increment_counter + 1
      
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

    links = soup.find_all('a', attrs={'href': re.compile("wiki/V5_metadata")})

    for link in links:
        if counter in skip_games:
            match_data[counter].append("")
            match_data[counter+1].append(link.get('title').replace("meta", "") + "/Timeline")
            counter = counter+2
        else:
            if link.text == "Link":
                match_data[counter].append(link.get('title').replace("meta", "") + "/Timeline")
                counter = counter+1
            else:
                print("Dont increase")
                altered = altered+1
    
    number_of_match_links = len(soup.find_all('a', attrs={'href': re.compile("wiki/V5_metadata")}))-altered

    page_type = "matchhistory page"

    # if number_of_match_links == len(match_data):
    # print("Continue because the number of match links matches the number of games found")

    # Retrieve data from each match history link
    for match in match_data:
        gameDate = match[0].replace('-', '/')
        gameNumber = match[1]
        blueTeam = match[2]
        redTeam = match[3]

        if len(match) != 6:
            match.append("")

        if match[5] != "":
            blue_team_id = 100
            red_team_id = 200

            response = site.api('query',
                format = 'json',
                prop = 'revisions',
                rvprop = 'content',
                rvslots = 'main',
                titles = match[5]
            )

            pageId = ""

            for key in response["query"]["pages"].keys(): 
                pageId = key

            data = response["query"]["pages"][pageId]["revisions"][0]["slots"]["main"]["*"]

            data_obj = json.loads(data)

            firstTowerKilledByTeam = -1
            firstInhibitorKilledByTeam = -1
            firstDragonKilledByTeam = -1
            firstRiftHeraldKilledByTeam = -1
            firstBaronKilledByTeam = -1
            firstBloodKilledByTeam = -1
            blueTeamKillCount = 0
            redTeamKillCount = 0
            winningTeam = -1
            losingTeam = -1

            for event in data_obj["frames"]:
                for specificEvent in event["events"]:
                    if ("monsterType" in specificEvent) and (specificEvent["monsterType"] == "DRAGON") and (firstDragonKilledByTeam == -1):
                        firstDragonKilledByTeam = specificEvent["killerTeamId"]
                    if ("monsterType" in specificEvent) and (specificEvent["monsterType"] == "RIFTHERALD") and (firstRiftHeraldKilledByTeam == -1):
                        firstRiftHeraldKilledByTeam = specificEvent["killerTeamId"]
                    if ("monsterType" in specificEvent) and (specificEvent["monsterType"] == "BARON_NASHOR") and (firstBaronKilledByTeam == -1):
                        firstBaronKilledByTeam = specificEvent["killerTeamId"]
                    if ("killType" in specificEvent) and (specificEvent["killType"] == "KILL_FIRST_BLOOD") and (firstBloodKilledByTeam == -1):
                        if specificEvent["killerId"] > 5:
                            firstBloodKilledByTeam = 200
                        else:
                            firstBloodKilledByTeam = 100
                    if ("type" in specificEvent) and (specificEvent["type"] == "BUILDING_KILL"):
                        if ("towerType" in specificEvent) and (specificEvent["towerType"] == "OUTER_TURRET") and (firstTowerKilledByTeam == -1):
                            if specificEvent["teamId"] == 100:
                                firstTowerKilledByTeam = 200
                            else:
                                firstTowerKilledByTeam = 100
                        if ("buildingType" in specificEvent) and (specificEvent["buildingType"] == "INHIBITOR_BUILDING") and (firstInhibitorKilledByTeam == -1):
                            if specificEvent["teamId"] == 100:
                                firstInhibitorKilledByTeam = 200
                            else:
                                firstInhibitorKilledByTeam = 100
                    if ("type" in specificEvent) and (specificEvent["type"] == "GAME_END"):
                        winningTeam = specificEvent["winningTeam"]
                        if winningTeam == 100:
                            losingTeam = 200
                        else:
                            losingTeam = 100
                    if ("type" in specificEvent) and (specificEvent["type"] == "CHAMPION_KILL"):
                        if specificEvent["killerId"] > 5:
                            redTeamKillCount = redTeamKillCount + 1
                        else:
                            blueTeamKillCount = blueTeamKillCount + 1

            if firstBloodKilledByTeam == 100:
                firstBloodKilledByTeam = blueTeam
            elif firstBloodKilledByTeam == 200:
                firstBloodKilledByTeam = redTeam
            else:
                firstBloodKilledByTeam = "-"

            if firstTowerKilledByTeam == 100:
                firstTowerKilledByTeam = blueTeam
            elif firstTowerKilledByTeam == 200:
                firstTowerKilledByTeam = redTeam
            else:
                firstTowerKilledByTeam = "-"

            if firstInhibitorKilledByTeam == 100:
                firstInhibitorKilledByTeam = blueTeam
            elif firstInhibitorKilledByTeam == 200:
                firstInhibitorKilledByTeam = redTeam
            else:
                firstInhibitorKilledByTeam = "-"

            if firstDragonKilledByTeam == 100:
                firstDragonKilledByTeam = blueTeam
            elif firstDragonKilledByTeam == 200:
                firstDragonKilledByTeam = redTeam
            else:
                firstDragonKilledByTeam = "-"

            if firstRiftHeraldKilledByTeam == 100:
                firstRiftHeraldKilledByTeam = blueTeam
            elif firstRiftHeraldKilledByTeam == 200:
                firstRiftHeraldKilledByTeam = redTeam
            else:
                firstRiftHeraldKilledByTeam = "-"

            if firstBaronKilledByTeam == 100:
                firstBaronKilledByTeam = blueTeam
            elif firstBaronKilledByTeam == 200:
                firstBaronKilledByTeam = redTeam
            else:
                firstBaronKilledByTeam = "-"

            if winningTeam == 100:
                winningTeam = blueTeam
            elif winningTeam == 200:
                winningTeam = redTeam
            else:
                winningTeam = "-"

            if losingTeam == 100:
                losingTeam = blueTeam
            elif losingTeam == 200:
                losingTeam = redTeam
            else:
                losingTeam = "-"

            matches_to_post.append([league_id, split_id, gameDate, gameNumber, blueTeam, redTeam, firstBloodKilledByTeam, firstTowerKilledByTeam, firstDragonKilledByTeam, firstRiftHeraldKilledByTeam, firstInhibitorKilledByTeam, firstBaronKilledByTeam, blueTeamKillCount, redTeamKillCount, winningTeam, losingTeam])
        else:
            matches_to_post.append([league_id, split_id, gameDate, gameNumber, blueTeam, redTeam, "-", "-", "-", "-", "-", "-", 0, 0, "-", "-"])

        postingAvailable = True
    # else:
    #     print("It seems a matchhistory link for one of the games is missing")

print('Finished scraping!')

driver.close()
driver.quit()

for match_stats in matches_to_post:
    print(match_stats)

if postingAvailable == True:
    # Confirm if the user wants to post to the database or not
    print("Would you like to post the new data to the database (y/n)? ")
    post_data = input()

    if post_data == "y" or post_data == "Y":
        print('Posting to the database')

        conn = psycopg2.connect(user="ezcmimgzrrckca", password="f2a321242d195f37a75a5beefc494bd6fa93729059889e554fffdece504d5f00", host="ec2-34-232-191-133.compute-1.amazonaws.com", port="5432", database="ddpnab9lbjao5d", sslmode='require')
        cur = conn.cursor()

        cur.execute("SELECT MAX(id) FROM games;")
        unique_id = cur.fetchone()

        if not all(unique_id):
            unique_id = 0
        else:
            unique_id = unique_id[0]

        print('unique_id is: ')
        print(unique_id)

        cur.execute("SELECT COUNT(*) FROM games")
        unique_id = cur.fetchone()
        unique_id = unique_id[0]
        # Maybe check id of the last entry here to ensure this works even with deleted entries

        for match_stats in matches_to_post:
            print('sep')
            print(match_stats[:6])
            print(match_stats[6:])
            unique_id = unique_id+1
            cur.execute("INSERT INTO games VALUES (" + str(unique_id) +
                        " , %s, %s, %s, %s, %s, %s)", match_stats[:6])
            cur.execute("INSERT INTO match_results VALUES (" + str(unique_id) +
                        " , %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", match_stats[6:])

        print("Files were committed to the database")
        conn.commit()

