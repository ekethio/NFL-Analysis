# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 22:49:43 2020

@author: ekshe
"""


import pandas as pd
pd.options.display.max_columns = 100
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

import requests


path = 'c:/users/ekshe/nfl/'
file_name = 'nflpbp.csv'

df = pd.read_csv(path + file_name)
df.columns = df.columns.map(lambda x: x.lower())
col_to_keep = ['game_id', 'away_team', 'home_team', 'posteam', 'defteam', 'game_date', 'drive', \
               'quarter_seconds_remaining','down',  'yardline_100', 'ydstogo',\
               'yards_gained', 'shotgun', 'no_huddle' , 'yards_after_catch', 'field_goal_result', \
               'play_type' , 'pass_attempt', 'game_half', 'qb_scramble', 'rush_attempt',\
               'score_differential','pass_touchdown', 'rush_touchdown', 'passer_player_name',\
               'receiver_player_name',  'rusher_player_name','complete_pass', 'interception', \
                'penalty', 'sack', 'third_down_converted', 'fourth_down_converted', 'fumble_lost']

df = df[col_to_keep] 
col_mapper = { 'game_date' : 'date', 'quarter_seconds_remaining': 'time', 'yards_gained': 'yards',\
              
               'yards_after_catch': 'yac', 'pass_attempt': 'ispass', 'rush_attempt': 'isrush', \
               'score_differential' : 'score_diff', 'pass_touchdown': 'passtd', 'rush_touchdown'\
               :'rushtd', 'passer_player_name' : 'passer', 'receiver_player_name': 'receiver',\
               'rusher_player_name': 'rusher', 'interecption': 'int'}
    
df.columns = df.columns.map(lambda x: col_mapper[x] if x in col_mapper else x )
df['season'] = df.date.map(lambda x: x.split('-')[0])

# Fix team names 
team_names = ['posteam', 'defteam', 'away_team', 'home_team']
for name in team_names:
    pos_team_mapper = {'LA' : 'LAR', 'STL' :"LAR", 'SD': 'LAC', 'JAX': "JAC"}
    df[name] = df[name].map(lambda x: pos_team_mapper[x] if x in pos_team_mapper else x)
    
df.to_csv('data/pbp_cleaned.csv')






