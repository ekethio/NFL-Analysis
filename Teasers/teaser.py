# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 23:25:31 2020

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

#Select variables and choose relevant data subset
cols_include = ['score_home', 'score_away', 'home_favorite', 'schedule_season',\
                'spread_favorite', 'schedule_week','over_under_line', 'point_total',\
                'over_under_result','score_difference', 'favorite_covered', 'home_wins']
df = df[cols_include]
df = df[df.over_under_line.notna()]

df['spread_result'] = df.apply(lambda row: row.score_home - row.score_away if not row.home_favorite \
                               else row.score_away - row.score_home , axis =1)
df['spread_home'] = df.apply(lambda row: row.spread_favorite if row.home_favorite \
                             else -row.spread_favorite, axis =1 )

df['total_range' ] =pd.qcut(df.over_under_line, 2, labels = ['low',  'high'])
reg_df = df[(df.schedule_season > 2000) & (df.schedule_week < 18)]
reg_df.drop(['schedule_season', 'schedule_week'], axis =1 , inplace = True )

reg_df['favorite_teaser'] = reg_df.spread_favorite + 6
reg_df['underdog_teaser'] = -reg_df.spread_favorite + 6

# Assign value 1 if teaser covers,  0 if it doesn't cover and -1 if it is a push 
reg_df['favorite_teaser_cover'] = reg_df.apply(lambda row: 1 if ( row.spread_result < row.favorite_teaser) \
                                             else 0, axis =1) 
reg_df['underdog_teaser_cover'] = reg_df.apply(lambda row: 1 if (-row.spread_result < row.underdog_teaser) \
                                             else 0, axis =1)
reg_df.loc[reg_df.spread_result == reg_df.underdog_teaser, 'underdog_teaser_cover'] = -1
reg_df.loc[reg_df.spread_result == reg_df.favorite_teaser, 'favorite_teaser_cover'] = -1
 
   
# Function to calculate the ROI of teased lines (assuming -110 american odds for two teaser legs)
def ROI(scores):
    ev = []
    for i in range (5000):
        outcomes = np.random.choice(scores, 2)    
        if outcomes[0] == 1 and outcomes[1] ==1:
            ev.append(1)
        if outcomes[0] ==0  or outcomes[1] ==0:
            ev.append(-1.1)          
    return np.mean(ev)/1.1
            

# Create teaser tables with teased lines as index and their respective ROI and sample size as columns
favorite_teaser = reg_df.pivot_table(values = 'favorite_teaser_cover', index = ['favorite_teaser'], columns= 
                                                                                'total_range', aggfunc =[ ROI, len])  
underdog_teaser =reg_df.pivot_table(values = 'underdog_teaser_cover', index = ['underdog_teaser'],  columns = 'total_range',\
                                                                               aggfunc =[ ROI, len])   
#favorite_teaser.columns = favorite_teaser.columns.get_level_values(0)
#underdog_teaser.columns = underdog_teaser.columns.get_level_values(0)
 

for teaser in [favorite_teaser, underdog_teaser]: 

    teaser.drop(teaser[(teaser.ROI.low <= -0.2) | (teaser.ROI.high <= -0.2) |(teaser.len.low <= 30)\
                       | teaser.ROI.low.isna() | teaser.ROI.high.isna()].index, inplace = True)
    low = teaser.ROI.low.apply(lambda x:  str(np.round(x *100, 2)) + '%' )
    high = teaser.ROI.high.apply(lambda x: str(np.round(x *100, 2)) + '%' )
    teaser.rename(columns= {'len': 'sample'}, inplace= True)
    teaser['ROI'] = np.transpose(np.array([low, high]))


print (favorite_teaser)
print (underdog_teaser)

ax.set_title('favorite_Teasers ROI')
ax.set_ylim (-30, 20)
ax.set_ylabel('ROI in %')
ax.sexlabel('Teased up to')

