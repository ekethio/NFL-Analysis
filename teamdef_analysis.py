# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 16:35:57 2020

@author: ekshe
"""


import pandas as pd
import numpy as np
import seaborn as sns


df = pd.read_csv('data/defensive_stats.csv')
df = df.iloc[:, 1:]

teams = df[df.Player == "Team Total"].dropna(axis =1).drop(['Player'], axis =1)
teams.columns = teams.columns.map(lambda x: x.lower())

teams.team = teams.team.map(lambda x: x.upper())
teams.index = teams.team
teams.drop(['team', 'mtkl', 'mtkl%', 'qbkd', 'hrry', 'cmp%', 'rat', \
            'comb', 'dadot'], axis =1, inplace = True)
#teams['cmp%'] = teams['cmp%'].map(lambda x:float(x.split('%')[0]))
#teams['mtkl%'] = teams['mtkl%'].map(lambda x:float(x.split('%')[0]))
teams = teams.applymap(lambda x : float(x))

corr = teams.corr()

sns.heatmap(corr)
#sns.lmplot('prss','yds/tgt', data = teams)
print (teams.sort_values(by = 'cmp', ascending = False))