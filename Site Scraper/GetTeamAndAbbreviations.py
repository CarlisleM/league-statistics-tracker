import re
import time
import pandas as pd
import psycopg2
from unidecode import unidecode
from bs4 import BeautifulSoup
from selenium import webdriver
from team_name_mapper import *

def get_page_source(link):
    driver.get(link)
    return driver.page_source

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--disable-extensions')
driver = webdriver.Chrome(executable_path='/Users/Carlisle/Desktop/Projects/chromedriver.exe', options=options)
#driver_location = str(sys.argv[1])
#driver = webdriver.Chrome(executable_path=driver_location, options=options)
driver.implicitly_wait(10)  # not sure if needed

list_of_leagues_to_scrape = [
    # 2022
    'https://lol.fandom.com/wiki/LCK/2022_Season/Summer_Season', # LCK 1 
    'https://lol.fandom.com/wiki/LEC/2022_Season/Summer_Season', # LEC 2 
    'https://lol.fandom.com/wiki/LVP_SuperLiga/2022_Season/Summer_Season', # LVP 3
    'https://lol.fandom.com/wiki/LCO/2022_Season/Split_2', # LCO (Oceania) 4
    'https://lol.fandom.com/wiki/LFL/2022_Season/Summer_Season', # LFL 5 
    'https://lol.fandom.com/wiki/PCS/2022_Season/Summer_Season', # PCS 6
    'https://lol.fandom.com/wiki/LCS/2022_Season/Summer_Season', # LCS 7 
    'https://lol.fandom.com/wiki/NA_Academy_League/2022_Season/Summer_Season', # NA Academy 8
    'https://lol.fandom.com/wiki/LLA/2022_Season/Closing_Season', # LLA 9 
    'https://lol.fandom.com/wiki/Ultraliga/Season_8', # Ultraliga 10
    'https://lol.fandom.com/wiki/LPL/2022_Season/Summer_Season', # LPL 11 
    'https://lol.fandom.com/wiki/LJL/2022_Season/Summer_Season', # LJL 12
    'https://lol.fandom.com/wiki/TCL/2022_Season/Summer_Season', # TCL 13
    'https://lol.fandom.com/wiki/VCS/2022_Season/Summer_Season', # VCS 14 
    'https://lol.fandom.com/wiki/CBLOL/2022_Season/Split_2', # CBLOL 15
]

team_id = 1
teams = []

for league_url in list_of_leagues_to_scrape:
    league = league_url.split("/")
    league = league[4].replace("_", " ")
    league_id = get_league_id(league)

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

    print('Scraping ' + league_url)

    page_source = get_page_source(league_url)
    soup = BeautifulSoup(page_source, 'html.parser')

    teams_table = soup.find(attrs={"class": ["wikitable2 standings"]})
    rows = teams_table.findChildren(['tr'])

    for row in rows[1:len(rows)]:
        team_info_row = row.find(attrs={"class": ["popup-button-pretty"]})
        if team_info_row != None:
            split = re.split("team=|display=", str(team_info_row))
            team_name = split[1][:-1]
            team_abbreviation = split[2].split(" ")[0]
            teams.append([team_id, unidecode(team_name), unidecode(team_abbreviation), league_id])
            team_id = team_id + 1

print('Finished getting upcoming matches!')

for team in teams:
    print("team:", team)

if len(teams) > 0:
    # Confirm if the user wants to post to the database or not
    print("Would you like to post the new data to the database (y/n)? ")
    post_data = input()

    if post_data == "y" or post_data == "Y":
        print('Posting to the database')

        conn = psycopg2.connect(user="ezcmimgzrrckca", password="f2a321242d195f37a75a5beefc494bd6fa93729059889e554fffdece504d5f00", host="ec2-34-232-191-133.compute-1.amazonaws.com", port="5432", database="ddpnab9lbjao5d", sslmode='require')
        cur = conn.cursor()

        for team in teams:
            print("team_id: " + str(team[0]) + ", team_name: " + str(team[1]) + ", team_abbreviation: " + str(team[2]) + ", league: " + str(team[3]))
            cur.execute("INSERT INTO teams VALUES (%s, %s, %s, %s)", team[:4])

        print("Files were committed to the database")
        conn.commit()

# Close the browser
driver.close()
driver.quit()
