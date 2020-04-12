# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 19:38:35 2020

@author: ekshe
"""
import pandas as pd
pd.options.display.max_columns = 100
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

path ="data/pbp_cleaned.csv"
df = pd.read_csv(path)

play_types = ['pass', 'run']
df = df[df.play_type.isin(play_types)]

qb_stats=  df[df.ispass ==1].groupby(by = 'passer').sum()\
          [['interception', 'passtd', 'yards', 'play', 'sack']]
qb = qb_stats[qb_stats.play > 4000]
qb = qb.assign(ypp = lambda qb : qb.yards/qb.play, \
               spp = lambda qb : qb.sack/qb.play,
               intpp = lambda qb : qb.interception/qb.play,\
               td_int_ratio = lambda qb: qb.passtd/qb.interception)

qb.columns = qb.columns.map(lambda x: x.upper())


print (qb.sort_values (by = 'YPP', ascending = False))

