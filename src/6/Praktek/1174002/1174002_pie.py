# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 09:33:57 2019

@author: Habib Abdul R
"""

# In[Pie]:
import matplotlib.pyplot as plt

def pie():
    hari = [1,2,3,4,5]
    
    tidur = [7,8,6,11,7]
    makan = [2,3,4,3,2]
    working = [7,8,7,2,2]
    main = [8,5,7,8,13]
    slices = [7,2,2,13]
    aktifitas = ['tidur','makan','working','main']
    cols = ['c', 'm', 'r', 'b']
    
    plt.subplot(221)
    plt.pie(slices,
            labels=aktifitas,
            colors=cols,
            startangle=90,
            shadow= True,
            explode=(0,0.1,0,0),
            autopct='%1.1f%%')
    plt.title('Contoh Pie 1')
    
    pubg = [1,2,3,4,5]
    
    mobile = [7,8,6,11,7]
    FF = [2,3,4,3,2]
    tujuhK = [7,8,7,2,2]
    coc = [8,5,7,8,13]
    slices = [7,2,2,13]
    game = ['pubg','free fire','seven knight', 'coc']
    col = ['r', 'g', 'b', 'c']
    
    plt.subplot(222)
    plt.pie(slices,
            labels=game,
            colors=col,
            startangle=90,
            shadow= True,
            explode=(0,0.1,0,0),
            autopct='%1.1f%%')
    plt.title('Contoh Pie 2')
    plt.show()