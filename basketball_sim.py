# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 20:14:19 2020

@author: ekshe
"""
import numpy as np
import pandas as pd
import seaborn as sns


iterations = 500

def calculate_odds(itera, accuracy):
    att = []
    for i in range( itera):
        trial = 1
        while True:
           
            score = 0
            for attempt in range(100):
                if np.random.randint(0, 100) < accuracy : 
                    score = score +1 
           
            if score > 89:
                 att.append(trial)
  
                 break 
            trial = trial + 1
    return np.mean(att)


shooting_percentage = [79, 80,81,82,83, 84, 85, 86 ]



attempts = []
for accuracy in shooting_percentage:
    attempts.append(calculate_odds(iterations, accuracy))


ser = pd.DataFrame({"Accuracy": shooting_percentage, "Average Attempts Needed" :attempts})
                    
ser["Accuracy"] = ser.Accuracy.apply(lambda x: str(x) + "%")

sns.barplot(ser.Accuracy, ser.iloc[:, 1])
print (ser)
    
    





