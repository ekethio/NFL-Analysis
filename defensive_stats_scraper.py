# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 12:18:57 2020

@author: ekshe
"""
import requests
import pandas as pd
from selenium import webdriver

from bs4 import BeautifulSoup as bs
from bs4 import Comment

#res = requests.get('https://www.pro-football-reference.com/boxscores/201909050chi.htm')

teams = ['nwe', 'buf', 'nyj', 'mia', 'rav', 'pit', 'cle', 'cin', 'phi', 'dal', 'nyg', 'was',\
         'gnb', 'min', 'chi', 'det', 'htx', 'jax', 'clt', 'oti', 'nor', 'atl', 'car', 'tam',\
         'kan', 'sdg', 'den', 'rai', 'crd', 'sfo', 'ram', 'sea']

data = pd.DataFrame()
for team in teams: 
    driver = webdriver.Chrome()
    driver.get('https://www.pro-football-reference.com/teams/{}/2019_advanced.htm'.format(team))
    rest = driver.page_source
    driver.quit()
    
    
    p = pd.DataFrame(pd.read_html(rest)[-1])
    p.columns = p.columns.get_level_values(1)
    p['team'] = team
    data = data.append(p)
    

data.to_csv('data/defensive_stats.csv')




