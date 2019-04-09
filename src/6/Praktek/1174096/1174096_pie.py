# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 11:03:28 2019

@author: Nico Sembiring
"""
# In[]

print(1174096%3+2)
# In[]
import matplotlib.pyplot as plt
def soalpie():
    plt.subplot(331)

    
    slice = [7,2,2,13]
    activities = ['Tidur','Makan','Bekerja','Bermain']
    cols = ['c','m','r','b']
    
    plt.pie(slice,
            labels=activities,
            colors=cols,
            startangle=90,
            shadow= True,
            explode=(0.1,0,0,0),
            autopct='%1.0f%%')
    
    plt.subplots_adjust(hspace=0.3, wspace=0.3)
    plt.title('Senin')

    plt.subplot(332)
    
    slice = [6,3,9,17]
    activities = ['Tidur','Makan','Bekerja','Bermain']
    cols = ['c','m','r','b']
        
    plt.pie(slice,
            labels=activities,
            colors=cols,
            startangle=90,
            shadow= True,
            explode=(0.1,0,0,0),
            autopct='%1.0f%%')
    plt.subplots_adjust(hspace=0.3, wspace=0.3)
    plt.title('Selasa')
    
    plt.subplot(333)
    
    
    slice = [9,5,10,13]
    activities = ['Tidur','Makan','Bekerja','Bermain']
    cols = ['c','m','r','b']
        
    plt.pie(slice,
            labels=activities,
            colors=cols,
            startangle=90,
            shadow= True,
            explode=(0.1,0,0,0),
            autopct='%1.0f%%')
    plt.subplots_adjust(hspace=0.3, wspace=0.3)
    plt.title('Rabu')
        
    plt.show()