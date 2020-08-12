import csv
import psycopg2
import requests
import re
import time
import sys
import json
import os
from team_name_mapper import *
from datetime import datetime
import pytz
import time

print('Editing database')

conn = psycopg2.connect(user = "djpoucmhkewvrh", password = "e1a533e45aa586bf82ff18dcc021969e6fb438333e501973f5236ab9257aea9c", host = "ec2-174-129-209-212.compute-1.amazonaws.com", port = "5432", database = "d24ubplectbqas", sslmode = 'require')
cur = conn.cursor()

print('What was the date (yyyy-mm-dd) of the match? ')
game_date = input()

print('Which game in the set was the match? ')
game_count = input()

print('What is the name of the first team? ')
game_team_1 = input()

print('What is the name of the second team? ')
game_team_2 = input()

print("SELECT league_id, game_date, game_count, blue_team, red_team, first_blood, first_tower, first_dragon, first_inhibitor, first_baron, winner FROM games, match_results WHERE id = game_id AND game_date = '" + str(game_date) + "' AND game_count = '" + str(game_count) + "' AND (blue_team = '" + str(game_team_1) + "' OR red_team = '" + str(game_team_1) + "') AND (blue_team = '" + str(game_team_2) + "' OR red_team = '" + str(game_team_2) + "');")

cur.execute("SELECT league_id, game_date, game_count, blue_team, red_team, first_blood, first_tower, first_dragon, first_inhibitor, first_baron, winner FROM games, match_results WHERE id = game_id AND game_date = '" + str(game_date) + "' AND game_count = '" + str(game_count) + "' AND (blue_team = '" + str(game_team_1) + "' OR red_team = '" + str(game_team_1) + "') AND (blue_team = '" + str(game_team_2) + "' OR red_team = '" + str(game_team_2) + "');")

# Updates match
# UPDATE match_results SET first_blood = 'fly', first_tower = 'fly', first_dragon = '100', first_inhibitor = 'fly', first_baron = 'fly', winner = '100' FROM games WHERE game_date = '2020-08-01' AND id = game_id AND game_count = '1' AND (blue_team = 'fly' OR red_team = 'fly') AND (blue_team = '100' OR red_team = '100');

# print("Full exexcute here")

# cur.execute("SELECT league_id, game_date, game_count, blue_team, red_team, first_blood, first_tower, first_dragon, first_inhibitor, first_baron, winner FROM games, match_results WHERE id = game_id AND game_date = '2020-08-01' AND game_count = '1' AND (blue_team = 'fly' OR red_team = 'fly') AND (blue_team = '100' OR red_team = '100');")

#             cur.execute("INSERT INTO games VALUES (" + str(unique_id) + " , %s, %s, %s, %s, %s, %s)", row[:6])
#             cur.execute("INSERT INTO match_results VALUES (%s, %s, %s, %s, %s, %s, %s, " + str(unique_id) + ")", row[6:])

# print("Commiting files to the database")
# conn.commit()
