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
    for i in range (10000):
        outcomes = np.random.choice(scores, 2)    
        if outcomes[0] == 1 and outcomes[1] ==1:
            ev.append(1)
        if outcomes[0] ==0  or outcomes[1] ==0:
            ev.append(-1.1)          
    return np.mean(ev)/1.1
            

# Create teaser tables with teased lines as index and their respective ROI and sample size as columns
favorite_teaser = reg_df.pivot_table(values = 'favorite_teaser_cover', index = 'favorite_teaser', aggfunc =[ ROI, len])  
underdog_teaser =reg_df.pivot_table(values = 'underdog_teaser_cover', index = 'underdog_teaser', aggfunc =[ ROI, len])   
favorite_teaser.columns = favorite_teaser.columns.get_level_values(0)
underdog_teaser.columns = underdog_teaser.columns.get_level_values(0)
 
# Keep only the relevant teased it lines 
favorite_teaser = favorite_teaser[(favorite_teaser.index < 5) & (favorite_teaser.index > -4)]
underdog_teaser = underdog_teaser[(underdog_teaser.index < 12)]
underdog_teaser['ROI'] = underdog_teaser.ROI.apply(lambda x: str(np.round(x *100, 2)) + '%' )
favorite_teaser['ROI'] = favorite_teaser.ROI.apply(lambda x: str(np.round(x*100, 2)) + '%')

print (favorite_teaser)
print (underdog_teaser)

ax =sns.barplot(underdog_teaser.index, underdog_teaser.ROI.apply(lambda x: float(x.split('%')[0])))
ax.set_title('Underdog Teasers ROI')
ax.set_ylim (-30, 20)
ax.set_ylabel('ROI in %')
ax.set_xlabel('Teased up to')

