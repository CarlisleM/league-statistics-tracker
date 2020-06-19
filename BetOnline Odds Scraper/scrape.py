import csv
import psycopg2
import requests
import re
import time
import sys
import json
import os
import argparse
from os import listdir
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

# # /usr/local/bin/chromedriver
# # Get main page (league) source
# def get_page_source (link):
#     options = webdriver.ChromeOptions()
#     options.add_argument('--ignore-certificate-errors')
#     options.add_argument('--disable-extensions')
#     options.add_argument('--incognito')
#     options.add_argument('--headless')
#     driver_location = str(sys.argv[1])
#     driver = webdriver.Chrome(executable_path=driver_location, options=options)
#     driver.get(link)
#     time.sleep(5)
#     print(day)
#     buttons = driver.find_elements_by_class_name('xhsRX')

#     if day == 1:
#         print('day 1')
#     elif day == 2:
#         print('day 2')
#         buttons[1].click()
#     elif day == 3:
#         print('day 3')
#         buttons[2].click()
#     elif day == 4:
#         print('day 4')
#         buttons[3].click()
#     elif day == 5:
#         print('day 5')
#         buttons[4].click()
#     elif day == 6:    
#         print('day 6')
#         buttons[5].click()
#     else:
#         print('day 7')
#         buttons[6].click()

#     time.sleep(5)
#     return driver.page_source


# def load_game_page (link):
#     options = webdriver.ChromeOptions()
#     options.add_argument('--ignore-certificate-errors')
#     options.add_argument('--disable-extensions')
#     options.add_argument('--incognito')
#     options.add_argument('--headless')
#     driver_location = str(sys.argv[1])
#     driver = webdriver.Chrome(executable_path=driver_location, options=options)
#     driver.get(link)
#     time.sleep(5)
#     return driver.page_source

# start = timeit.default_timer()
# days = [1,2,3,4,5,6,7]
# links = []

# # Iterate through each day of the weak to scan for matches
# for day in days:
#     page_source = get_page_source('https://esports-betonline.ultraplay.net/esports/early-markets')
#     soup = BeautifulSoup(page_source, 'html.parser')    

#     # Collcet the links to each individal game
#     newLink = 'True'
#     for link in soup.find_all('a', attrs={'href': re.compile("/esports/league-of-legends")}):
#         if newLink == 'True':
#             newLink = 'False'
#             links.append('https://esports-betonline.ultraplay.net' + link.get('href'))
#         else:
#             newLink = 'True'

#     print('Checking day: ' + str(day) + ' Total games this week so far: ' + str(len(links))) 

# print(links)

# print('Grabbing objectives and odds of each game...')

# # Iterate through each match to get the games objectives and odds
# for idx, match in enumerate(links):
#     page_source = load_game_page(links[idx])
#     soup = BeautifulSoup(page_source, 'html.parser')
#     content = soup.find("div", { "class" : "qLaRB" })

#     print(list(content.strings))

#     league = list(content.strings)[0] 
#     game = list(content.strings)[1]
#     team_one = list(content.strings)[2]
#     team_two = list(content.strings)[4]
#     game_date = list(content.strings)[7].split(' ')[0].replace("/", ".")
#     year = time.strftime('%Y')

#     outfile = game_date + "." + year + " " + team_one + " vs " + team_two + ".csv"
#     outfile = open(outfile, "w")
#     writer = csv.writer(outfile)
#     writer.writerow(['Objective', 'Team 1', 'T1 Odds', 'Team 2', 'T2 Odds'])

#     # Gives us the bet categories
#     objectives = []
#     objective_names = soup.findAll("div", { "class" : "_3Zukk" })
#     for idx, objective in enumerate(objective_names): 
#         objectives.append(objective.text)

#     # Gives us the bet odds
#     objective_odds = []
#     odds = soup.findAll("div", { "class" : "_2rn1X" })
#     for idx, odd in enumerate(odds): 
#         objective_odds.append(list(odd.strings))

#     if len(objectives) == len(objective_odds):
#         for idx, x in enumerate(objectives):
#             writer.writerow([objectives[idx].strip()] + objective_odds[idx])

# stop = timeit.default_timer()
# print('Time taken: ', stop - start)














def load_db_match_history ():
    os.system('curl https://league-statistics-tracker.herokuapp.com/games | json_pp > matches_played.json')   

def check_underdog ():
    for idx, odds in enumerate(all_relevant_odds):
        if all_relevant_odds[idx][2] < all_relevant_odds[idx][4]:
            odds_difference = all_relevant_odds[idx][4] - all_relevant_odds[idx][2]
            underdog = all_relevant_odds[idx][1]
        elif all_relevant_odds[idx][2] > all_relevant_odds[idx][4]: 
            odds_difference = all_relevant_odds[idx][2] - all_relevant_odds[idx][4]
            underdog = all_relevant_odds[idx][3]
        else: # If equal
            odds_difference = 0
        #print(odds_difference)

def read_csv ():
    with open(name) as csv_file:
        if name not in already_read_csv:
            already_read_csv.append(name)
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            current_map = 1
            for row in csv_reader:
                obj_desc = row[0]
                if 'Map 2' in obj_desc:
                    current_map = 2
                elif 'Map 3' in obj_desc:
                    current_map = 3
                elif 'Map 4' in obj_desc:
                    current_map = 4
                elif 'Map 5' in obj_desc:
                    current_map = 5
                if 'Winner' in obj_desc:
                    team_one_win_odds = float(row[2])
                    team_two_win_odds = float(row[4])
                if 'First Blood' in obj_desc:
                    team_one_firstblood_odds = float(row[2])
                    team_two_firstblood_odds = float(row[4])
                if 'First to 5' in obj_desc:
                    team_one_ft5_odds = float(row[2])
                    team_two_ft5_odds = float(row[4])
                if 'First to 10' in obj_desc:
                    team_one_ft10_odds = float(row[2])
                    team_two_ft10_odds = float(row[4])
                if 'Odd' in obj_desc:
                    odd_kills_odds = float(row[2])
                    even_kills_odds = float(row[4])
                if 'First Tower' in obj_desc:
                    team_one_tower_odds = float(row[2])
                    team_two_tower_odds = float(row[4])
                if 'First Dragon' in obj_desc:
                    team_one_dragon_odds = float(row[2])
                    team_two_dragon_odds = float(row[4])
                if 'First Baron' in obj_desc:
                    team_one_baron_odds = float(row[2])
                    team_two_baron_odds = float(row[4])
                if 'Rift Herald' in obj_desc:
                    team_one_riftherald_odds = float(row[2])
                    team_two_riftherald_odds = float(row[4])
                if 'First Elemental' in obj_desc:
                    elemental_dragon_odds = float(row[2])
                    game_odds.append([current_map, team_one, team_two, team_one_win_odds, team_two_win_odds, team_one_firstblood_odds, team_two_firstblood_odds, team_one_ft5_odds, team_two_ft5_odds, team_one_ft10_odds, team_two_ft10_odds, odd_kills_odds, even_kills_odds, team_one_tower_odds, team_two_tower_odds, team_one_dragon_odds, team_two_dragon_odds, team_one_baron_odds, team_two_baron_odds, team_one_riftherald_odds, team_two_riftherald_odds, elemental_dragon_odds])

def check_if_match_exists (game_date, blue_team, red_team):
    print(name)
    with open('matches_played.json') as json_file:
        data = json.load(json_file)
        for game in data['matches']:
            db_date = (game['game_date'].split('T')[0])
            team_one = convert_name((game['blue_team']))
            team_two = convert_name((game['red_team']))
            if (db_date == game_date) and ((team_one == blue_team) or (team_two == blue_team)) and ((team_two == red_team) or (team_one == red_team)): 
                print('Game matched: ' + db_date + ' ' + team_one + ' ' + team_two)
                # This tells us who won the objective
                objective_winner.append(convert_name(game['first_blood']))
                read_csv()
                does_exist = True
#                return does_exist

def find_csv_filenames( path_to_dir, suffix=".csv" ):
    filenames = listdir(path_to_dir)
    return [filename for filename in filenames if filename.endswith(suffix)]

load_db_match_history()


game_odds = []
already_read_csv = []
all_relevant_odds = []
objective_winner = []

games = []
filenames = find_csv_filenames("/Users/Carlisle/Desktop/league-statistics-tracker/BetOnline Odds Scraper")
for idx, name in enumerate(filenames):
    match_info = name.split(" ", 1)
    date_of_game = match_info[0]
    date_of_game = date_of_game.split(".")
    date_of_game = date_of_game[2] + '-' + date_of_game[0] + '-' + date_of_game[1]
    t1 = match_info[1].split(" vs ")[0]
    t2 = match_info[1].split(" vs ")[1].split(".csv")[0]
    games.append([date_of_game, t1, t2])
    has_match_been_played = check_if_match_exists(date_of_game, t1, t2)

    # if has_match_been_played == True:
    #     print('True')

check_underdog()    # Check who the underdog is and the differnce in odds

total_money = bet_amount
number_of_games = 5
all_games = []


print(game_odds)



#    if has_match_been_played == True:
#        check if win or lose objective
#        add or decrease money accordingly

# for idx, match in enumerate(all_games):
#     if bet_result == 'won':
#         total_money = total_money + (bet_amount*objective_odds)
#     else:
#         total_money = total_money - bet_amount

# print(total_money)

# if (total_money > bet_amount):
#     print('Your total amount would have been: $' + total_money)
#     print('A profit of: $' + (total_money-(number_of_games*bet_amount)))
# else: 
#     print('Your total amount would have been: $' + str(total_money))
#     print('A loss of: $' + str((total_money-(number_of_games*bet_amount))))


