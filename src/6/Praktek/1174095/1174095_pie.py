# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 09:33:57 2019

@author: dzihan
"""

# In[Pie]:
import matplotlib.pyplot as plt

def pie():
    
    slices = [7,2,2,13]
    aktifitas = ['belajar','solat','ngaji','main']
    cols = ['g', 'y', 'm', 'c']
    
    plt.subplot(221)
    plt.pie(slices,
            labels=aktifitas,
            colors=cols,
            startangle=80,
            shadow= True,
            explode=(0,0.1,0,0),
            autopct='%1.1f%%')
    plt.title('Contoh Pie 1')
    
    slices = [7,2,2,13]
    game = ['motor','mobil','sepeda', 'becak']
    col = ['b', 'g', 'r', 'c']
    
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