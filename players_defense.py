# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 18:32:02 2020

@author: ekshe
"""


import pandas as pd
pd.options.display.max_rows = 100
import numpy as np
import seaborn as sns


df = pd.read_csv('data/defensive_stats.csv')
df = df.iloc[:, 1:]

df.columns = df.columns.map(lambda col : col.lower())
df = df.applymap(lambda x: x.lower() if str(x) == x else x)

df = df[(df.player != 'team total')& (df.player != 'player' ) & (df.air != 'pass coverage')]


strings = ['player', 'team', 'pos', 'cmp%', 'mtkl%']

df = df.apply(lambda x: x.apply(lambda y: float(y)) if x.name not in strings \
              else x.map(lambda k: str(k).upper()))
df.index = df.player
df.drop(['player' ], axis =1, inplace = True )
df['prss/g'] = df.prss/df.g
print (df.sort_values(by ='prss/g', ascending = False).iloc[:90, :])