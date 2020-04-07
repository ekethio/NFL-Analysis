# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 23:25:31 2020

@author: ekshe
"""


import pandas as pd
import numpy as np
import seaborn as sns


#Import the data
path = 'c:/users/ekshe/nfl/nfl-analysis/'
df = pd.read_csv(path + 'nfl_betting_df.csv')

#Select variables and choose relevant data subset
cols_include = ['score_home', 'score_away', 'home_favorite', 'schedule_season',\
                'spread_favorite', 'schedule_week','over_under_line', 'point_total',\
                'over_under_result','score_difference', 'favorite_covered', 'home_wins']
df = df[cols_include]
df = df[df.over_under_line.notna()]

df['spread_home'] = df.apply(lambda row: row.spread_favorite if row.home_favorite \
                             else -row.spread_favorite, axis =1 )
    
reg_df = df[(df.schedule_season > 2001) & (df.schedule_week < 18)]
reg_df.drop(['schedule_season', 'schedule_week'], axis =1 , inplace = True )

prob_needed = np.sqrt(11/21)

reg_df['favorite_teaser'] = reg_df.spread_favorite + 6
reg_df['underdog_teaser'] = -reg_df.spread_favorite + 6

#reg_df['favorite_teaser_cov'] = reg_df.apply(lambda row: 1 if (row.home_favorite and \
 #                                            row.score_difference > -row.favorite_teaser) \
#                                             or (not row.home_favorite and row.score_difference <\
 #                                           row.favorite_teaser) else 0, axis =1) 
#
reg_df['underdog_teaser_cov'] = reg_df.apply(lambda row: 1 if (row.home_favorite and \
                                             row.score_difference < row.underdog_teaser) \
                                             or (not row.home_favorite and row.score_difference >\
                                            -row.underdog_teaser) else 0, axis = 1) 


print ( len(reg_df[reg_df.spread_favorite == -8.5]))
def teaser_ev(scores):
    ev = []
    for i in range (10000):
        outcomes = np.random.choice(scores, 2)
    
        if outcomes[0] == 1 and outcomes[1] ==1:
            ev.append(1)
        if not outcomes[0]  or not outcomes[1]:
            ev.append(-1.1)
            
    return np.mean(ev)/1.1
            

#fav_teaser_table = reg_df.pivot_table(values = 'favorite_teaser_cov', index = 'favorite_teaser', aggfunc =[ teaser_ev, len])  
under_teaser_table =reg_df.pivot_table(values = 'underdog_teaser_cov', index = 'underdog_teaser', aggfunc =[ teaser_ev, len])   
#fav_teaser_table.columns = fav_teaser_table.columns.get_level_values(0)
under_teaser_table.columns = under_teaser_table.columns.get_level_values(0)
 
print (under_teaser_table)

under = under_teaser_table.iloc[:10, :]
under.index = under.index.map(lambda x: '+' + str(x))
under.rename(columns = {'teaser_ev':  'ROI'}, inplace = True)
under['ROI'] = under.ROI.apply(lambda x: str(np.round(x *100, 2)) + '%' )


ax =sns.barplot(under.index, under.ROI.apply(lambda x: float(x.split('%')[0])))
ax.set_ylim (-30, 20)
ax.set_ylabel('ROI in %')
