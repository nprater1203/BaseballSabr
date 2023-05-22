import pandas as pd
import re
import requests 
from bs4 import BeautifulSoup
import math

url = 'http://www.espn.com/mlb/history/leaders/_/breakdown/season/year/2022/start/1'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

header = soup.find('tr', attrs = {'class': 'colhead'})
# for h in header.find_all('td'):
#     print(h.get_text(), end="   ")
# print("")

numOfStats = 0
headerList = header.find_all('td')

#Scrapes the header and Freedie Freeman's stats from 2022
firstRow = soup.find('tr', attrs = {'class': 'evenrow player-10-30193'})
r1LList = firstRow.find_all('td')

numOfStats = len(headerList)

# Initializes the stat map
statMap = {headerList[numOfStats-1].get_text(): float(r1LList[numOfStats-1].get_text())}

# Adds all the stats that were scraped to the map 
for x in range(numOfStats):
    # Check to see if the value is a string, if so add it, otherwise convert it to a float
    if headerList[x].get_text() == 'PLAYER':
        statMap['PLAYER'] = r1LList[x].get_text()
    else:
        statMap[headerList[x].get_text()] = float(r1LList[x].get_text())

print(statMap)

# Calculate necessities for advanced stats
totBasesDoubles = 2 * statMap['2B']
totBasesTriples = 3 * statMap['3B']
totBasesHR = 4 * statMap['HR']
totBasesSingles = statMap['H'] - (statMap['2B'] + statMap['3B'] + statMap['HR'])

# Calculate Freedie Freemans's Runs Created 
freemanRC = (totBasesSingles+totBasesDoubles+totBasesTriples+totBasesHR) * ((statMap['H'] + statMap['BB']) / (statMap['AB'] + statMap['BB']))

print(statMap['PLAYER'], "RC in 2022 = ", round(freemanRC,1))




# firstRow = soup.find('tr', attrs = {'class': 'evenrow player-10-30193'})
# for r1 in firstRow.find_all('td'):
    
#     print(r1.get_text(), end="  ")

# print("")

# header= soup.find('tr', attr={'class': 'colhead'})
# columns = [col.get_text() for col in header.find_all('td')]

# print(columns)