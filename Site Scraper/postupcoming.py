import csv
import psycopg2
import requests
import re
import time
import sys
import json
import os
import timeit
from datetime import datetime
# import pytz
import time

print('Posting upcoming matches to the database')

conn = psycopg2.connect(user="djpoucmhkewvrh", password="e1a533e45aa586bf82ff18dcc021969e6fb438333e501973f5236ab9257aea9c",
                        host="ec2-174-129-209-212.compute-1.amazonaws.com", port="5432", database="d24ubplectbqas", sslmode='require')
cur = conn.cursor()

input_files = {
    'LCS Upcoming Games.csv',
    'LCK Upcoming Games.csv',
    'LEC Upcoming Games.csv',
    'LCO Upcoming Games.csv',
    # 'LFL Upcoming Games.csv',
    'LVP_SuperLiga Upcoming Games.csv',
    # 'PCS Upcoming Games.csv',
    'LLA Upcoming Games.csv',
    'Ultraliga Upcoming Games.csv',
    'LPL Upcoming Games.csv',
    'NA_Academy_League Upcoming Games.csv',
    'LJL Upcoming Games.csv',
    'TCL Upcoming Games.csv',
    # 'VCS Upcoming Games.csv',
    'CBLOL Upcoming Games.csv'
}

cur.execute("DELETE FROM upcoming;")

for file in input_files:
    print("Adding upcoming matches from " + file + ' to the database')
    with open("./Upcoming Matches/" + file, 'r') as f:
        reader = csv.reader(f)
        for (index, row) in enumerate(reader):
            print(index)
            cur.execute(
                "INSERT INTO upcoming VALUES (%s, %s, %s, %s, %s, %s, %s)", row[:7])

print("Commiting files to the database")
conn.commit()
