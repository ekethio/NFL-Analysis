# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 00:00:06 2020

@author: ekshe
"""


import pandas as pd
pd.options.display.max_columns = 100
import numpy as np
import warnings
warnings.simplefilter('ignore')
import seaborn as sns
import matplotlib.pyplot as plt
import datetime



#Import the data
path = 'c:/users/ekshe/nfl/nfl-analysis/'
df = pd.read_csv(path + 'nfl_betting_df.csv')
df['spread_result'] = df.apply(lambda row: row.score_home - row.score_away if not row.home_favorite \
                               else row.score_away - row.score_home , axis =1)
df['total_score'] = df.score_away + df.score_home
df = df[df.over_under_line.notna()][['spread_favorite', 'spread_result', 'total_score', 'over_under_line', 'schedule_season']]


df = df[df.schedule_season > 2001]

seasonal_ou = df.pivot_table(values = ['over_under_line', 'total_score'], index = 'schedule_season', aggfunc = [np.mean, np.median, max, min])

#seasonal_ou.columns = seasonal_ou.columns.get_level_values(0)

print (seasonal_ou)

print (df.over_under_line.value_counts().iloc[:30])

#sns.regplot(df.total_score, df.spread_favorite)
sns.distplot(df.total_score)

