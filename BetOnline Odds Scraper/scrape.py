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

# /usr/local/bin/chromedriver
# Get main page (league) source
def get_page_source (link):
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--disable-extensions')
    options.add_argument('--incognito')
    options.add_argument('--headless')
    driver_location = str(sys.argv[1])
    driver = webdriver.Chrome(executable_path=driver_location, options=options)
    driver.get(link)
    time.sleep(5)
    print(day)
    buttons = driver.find_elements_by_class_name('xhsRX')

    if day == 1:
        print('day 1')
    elif day == 2:
        print('day 2')
        buttons[1].click()
    elif day == 3:
        print('day 3')
        buttons[2].click()
    elif day == 4:
        print('day 4')
        buttons[3].click()
    elif day == 5:
        print('day 5')
        buttons[4].click()
    elif day == 6:    
        print('day 6')
        buttons[5].click()
    else:
        print('day 7')
        buttons[6].click()

    time.sleep(5)
    return driver.page_source


def load_game_page (link):
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--disable-extensions')
    options.add_argument('--incognito')
    options.add_argument('--headless')
    driver_location = str(sys.argv[1])
    driver = webdriver.Chrome(executable_path=driver_location, options=options)
    driver.get(link)
    time.sleep(5)
    return driver.page_source

start = timeit.default_timer()
days = [1,2,3,4,5,6,7]
links = []

# Iterate through each day of the weak to scan for matches
for day in days:
    page_source = get_page_source('https://esports-betonline.ultraplay.net/esports/early-markets')
    soup = BeautifulSoup(page_source, 'html.parser')    

    # Collcet the links to each individal game
    newLink = 'True'
    for link in soup.find_all('a', attrs={'href': re.compile("/esports/league-of-legends")}):
        if newLink == 'True':
            newLink = 'False'
            links.append('https://esports-betonline.ultraplay.net' + link.get('href'))
        else:
            newLink = 'True'

    print('Checking day: ' + str(day) + ' Total games this week so far: ' + str(len(links))) 

print(links)

print('Grabbing objectives and odds of each game...')

# Iterate through each match to get the games objectives and odds
for idx, match in enumerate(links):
    page_source = load_game_page(links[idx])
    soup = BeautifulSoup(page_source, 'html.parser')
    content = soup.find("div", { "class" : "qLaRB" })

    print(list(content.strings))

    league = list(content.strings)[0] 
    game = list(content.strings)[1]
    team_one = list(content.strings)[2]
    team_two = list(content.strings)[4]
    game_date = list(content.strings)[7].split(' ')[0].replace("/", ".")
    year = time.strftime('%Y')

    outfile = game_date + "." + year + " " + team_one + " vs " + team_two + ".csv"
    outfile = open(outfile, "w")
    writer = csv.writer(outfile)
    writer.writerow(['Objective', 'Team 1', 'T1 Odds', 'Team 2', 'T2 Odds'])

    # Gives us the bet categories
    objectives = []
    objective_names = soup.findAll("div", { "class" : "_3Zukk" })
    for idx, objective in enumerate(objective_names): 
        objectives.append(objective.text)

    # Gives us the bet odds
    objective_odds = []
    odds = soup.findAll("div", { "class" : "_2rn1X" })
    for idx, odd in enumerate(odds): 
        objective_odds.append(list(odd.strings))

    if len(objectives) == len(objective_odds):
        for idx, x in enumerate(objectives):
            writer.writerow([objectives[idx].strip()] + objective_odds[idx])

stop = timeit.default_timer()
print('Time taken: ', stop - start)


