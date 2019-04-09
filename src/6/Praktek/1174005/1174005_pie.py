# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 16:35:14 2019

@author: user
"""

# In[Pie]:
import matplotlib.pyplot as plt

def pie():
    Kamis = [1,2,3,4,5]
    
    toba = [9,8,6,11,7]
    ha = [2,3,4,3,2]
    futsal = [7,8,7,2,2]
    main = [8,5,7,8,13]
    slices = [7,2,2,13]
    aktifitas = ['toba','ha','futsal','main']
    cols = ['c', 'b', 'm', 'b']
    
    plt.subplot(221)
    plt.pie(slices,
            labels=aktifitas,
            colors=cols,
            startangle=90,
            shadow= True,
            explode=(0,0.1,0,0),
            autopct='%1.1f%%')
    plt.title('Contoh Pie 1')
    
    Hugo = [1,2,3,4,5]
    
    rpg = [7,8,6,11,7]
    ID = [2,3,4,3,2]
    fps = [7,8,7,2,2]
    racing = [8,5,7,8,13]
    slices = [7,2,2,13]
    game = ['rpg','idle game','First Person Shooter', 'racing']
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