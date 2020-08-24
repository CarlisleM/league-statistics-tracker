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

# print("SELECT league_id, game_date, game_count, blue_team, red_team, first_blood, first_tower, first_dragon, first_inhibitor, first_baron, winner FROM games, match_results WHERE id = game_id AND game_date = '" + str(game_date) + "' AND game_count = '" + str(game_count) + "' AND (blue_team = '" + str(game_team_1) + "' OR red_team = '" + str(game_team_1) + "') AND (blue_team = '" + str(game_team_2) + "' OR red_team = '" + str(game_team_2) + "');")
# cur.execute("SELECT league_id, game_date, game_count, blue_team, red_team, first_blood, first_tower, first_dragon, first_inhibitor, first_baron, winner FROM games, match_results WHERE id = game_id AND game_date = '" + str(game_date) + "' AND game_count = '" + str(game_count) + "' AND (blue_team = '" + str(game_team_1) + "' OR red_team = '" + str(game_team_1) + "') AND (blue_team = '" + str(game_team_2) + "' OR red_team = '" + str(game_team_2) + "');")

print('Who got first blood? ')
new_fb = input() 

print('Who destroyed the first tower? ')
new_ft = input() 

print('Who killed the first dragon? ')
new_fd = input() 

print('Who destroyed the first inhibitor? ')
new_fi = input() 

print('Who killed the first baron? ')
new_fbaron = input() 

print('Who won the match? ')
new_winner = input() 

print("UPDATE match_results SET first_blood = '" + str(new_fb) + "', first_tower = '" + str(new_ft) + "', first_dragon = '" + str(new_fd) + "', first_inhibitor = '" + str(new_fi) + "', first_baron = '" + str(new_fbaron) + "', winner = '" + str(new_winner) + "' FROM games WHERE game_date = '" + str(game_date) + "' AND id = game_id AND game_count = '" + str(game_count) + "' AND (blue_team = '" + str(game_team_1) + "' OR red_team = '" + str(game_team_1) + "') AND (blue_team = '" + str(game_team_2) + "' OR red_team = '" + str(game_team_2) + "');")

# Updates match
cur.execute("UPDATE match_results SET first_blood = '" + str(new_fb) + "', first_tower = '" + str(new_ft) + "', first_dragon = '" + str(new_fd) + "', first_inhibitor = '" + str(new_fi) + "', first_baron = '" + str(new_fbaron) + "', winner = '" + str(new_winner) + "' FROM games WHERE game_date = '" + str(game_date) + "' AND id = game_id AND game_count = '" + str(game_count) + "' AND (blue_team = '" + str(game_team_1) + "' OR red_team = '" + str(game_team_1) + "') AND (blue_team = '" + str(game_team_2) + "' OR red_team = '" + str(game_team_2) + "');")

conn.commit()
