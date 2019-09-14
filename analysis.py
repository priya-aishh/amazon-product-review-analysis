# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 19:01:31 2019

@author: LENOVO
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

rev = pd.read_csv("C:\\Users\\LENOVO\\Documents\\Python Scripts\\amazonreviews\\amazonreviews\\spiders\\reviews.csv")
d = rev.iloc[:,2]

dup=0
fake=0
worst=0
poor=0
good=0
excel=0
original=0

for i in d:
    if i.count('duplicate') or i.count('fake') or i.count('worst') or i.count('poor') or i.count('good') or i.count('excel') or i.count('original')> 0:
        dup += i.count('duplicate')
        fake += i.count('fake')
        poor += i.count('poor')
        good += i.count('good')
        excel += i.count('excel')
        original += i.count('original')
        
a = {'duplicate':dup,
     'fake':fake,
     'poor':poor,
     'good':good,
     'excellent':excel,
     'original':original
     }

d = pd.DataFrame({'Words': list(a.keys()),
                  'Count': list(a.values())})
plt.figure(figsize=(16,5))
ax = sns.barplot(data=d, x= "Words", y = "Count")
ax.set(xlabel = 'Words',ylabel = 'Count')
plt.show()
