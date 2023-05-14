import pandas as pd
import re
import requests 
from bs4 import BeautifulSoup

url = 'http://www.espn.com/mlb/history/leaders/_/breakdown/season/year/2022/start/1'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

row = soup.find('tr', attrs = {'class': 'evenrow player-10-30193'})
for data in row.find_all('td'):
    print(data.get_text())