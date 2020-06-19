import csv
import sys
import json
import os
import argparse
import re
from os import listdir
from team_name_mapper import *

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
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    obj_desc = row[0]
                    team_1 = row[1]
                    team_1_odds = float(row[2])
                    team_2 = row[3]
                    team_2_odds = float(row[4])
                    # Search the csv for the odds related to the objective inputted
                    if objective_description.   lower() in obj_desc.lower():
                        all_relevant_odds.append([obj_desc, team_1, team_1_odds, team_2, team_2_odds])

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

# Start of program
objective_description = str(sys.argv[1])
bet_amount = int(sys.argv[2])

odds_difference = 1

load_db_match_history()

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




print(all_relevant_odds)
print(objective_winner)


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
