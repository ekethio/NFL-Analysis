# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 17:12:25 2020

@author: ekshe
"""

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
#import plotly.plotly as py
#import plotly.graphobjs as go 



data = pd.read_csv("nfl_betting_df.csv")
data = data[data.schedule_season > 1978]
data['total_ppg'] = data.h_ppg + data.a_ppg
data['total_papg'] = data.h_papg + data.a_papg 
data['score_diff'] = data.score_home - data.score_away

reg_data = data[(data.schedule_week > 1) & (data.schedule_week < 18)& (data.schedule_season > 2000)]
week5_data = data[(data.schedule_week > 5) & (data.schedule_week < 18) & (data.schedule_season > 2000)]


"""                                       
def n_samples(arr,sample_size,n_samples):
    size = sample_size
    sample_means=[]
    
    for n in range(n_samples):
        sample_means.append(np.random.choice(arr,size).mean())
    
    return sample_means
 
x = n_samples(week5_data.spread_favorite,1000,50)
"""
#sns.distplot(x)
#sns.distplot(data.score_diff)

unique = np.round(data.score_diff.value_counts()[:10]/(len(data)) *100, 1) 
#sns.barplot(unique.index, unique)
    
print (reg_data.favorite_covered)

#Create a pivot table with indexes being lines and columns being outcomes
reg_pivot = reg_data.pivot_table(index = 'over_under_line', \
                              columns = 'over_under_result', aggfunc = {'over_under_result' : len}, fill_value = 0)
reg_pivot_spr = reg_data.pivot_table(index = 'spread_favorite', columns = 'favorite_covered',\
                                       aggfunc= {'favorite_covered' : len}, fill_value = 0)
    
#Remove heirarchy from the columns 
reg_pivot.columns = reg_pivot.columns.get_level_values(1)
reg_pivot_spr.columns = reg_pivot_spr.columns.get_level_values(1)
reg_pivot_spr.columns = ['Yes', 'No', 'Push']

#Create a column for percent of total that goes over
reg_pivot['total_results'] = reg_pivot.over + reg_pivot.under + reg_pivot.push
reg_pivot['percent_of_total'] = reg_pivot.total_results *100/len(reg_data) 
reg_pivot['over_ratio'] = reg_pivot.over/(reg_pivot.over + reg_pivot.under)


#plot regression line of OU line on going over
'''sns.regplot(reg_pivot.index, reg_pivot.over_ratio)
ax.set_title('Effect of line on going over')
ax.set_xlim(35, 55)
ax.set_xlabel('Over Under Line')
ax.set_ylabel('Share of over outcomes')


'''
spr_three = reg_data[reg_data.spread_favorite == -3].score_diff 
ax = sns.distplot(spr_three)
ax.set_xlim(-20, 20)
#sns.countplot(reg_data[(reg_data.spread_favorite > -8)].spread_favorite)
#print(reg_data[(reg_data.home_favorite == 1) & (reg_data.spread_favorite > -8)].groupby(by = 'spread_favorite').median()['score_diff'])
#print(reg_data[(reg_data.home_favorite == 0) & (reg_data.spread_favorite > -8)].groupby(by = 'spread_favorite').median()['score_diff'])
#print (reg_pivot_spr.sort_index(ascending = False))

reg_data['favorite'] = reg_data.home_favorite.apply(lambda x : 'Home' if x else 'Away')
reg_data['won'] = reg_data.apply(lambda row: -1.1 if (((row.score_diff > -row.spread_favorite) and row.home_favorite) or\
                                 (row.score_diff < row.spread_favorite) and not row.home_favorite)  else 1, axis =1)
reg_data.loc[((reg_data['score_diff'] == reg_data['spread_favorite']) & (~ reg_data['home_favorite'])) | \
                                 ((reg_data['score_diff'] == -reg_data['spread_favorite']) & (reg_data['home_favorite'])), 'won']  = 0
                                     
print (reg_data.won)
teaser = reg_data.pivot_table(values = 'won', index = ['spread_favorite', 'favorite'], aggfunc = [np.mean, np.median, len, sum])
teaser.columns = teaser.columns.get_level_values(0)
teaser['mean'] = teaser['mean'].apply(lambda x: np.round(x/1.1, 3))

print (teaser['mean'].mean())

print (teaser.sort_index(ascending = False).iloc[:40, :])
