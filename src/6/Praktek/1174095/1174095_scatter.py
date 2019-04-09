# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 09:20:40 2019

@author: dzihan
"""

# In[Sactter]:
import matplotlib.pyplot as plt
 
 
def scatter():
    x = [1,1.3,2,2,3,3.7,3.9]
    y = [5,8,8,9.5,9.5,10,10]
    
    s = [8,8,9,7.5,11,10.5,11]
    a = [4,3.5,3.7,8,4.5,5,6]
    
    x1 = [1,1.3,2,2,3,3.7,3.9]
    y1 = [5,8,8,9.5,9.5,10,10]
    
    s1 = [8,8,9,7.5,11,10.5,11]
    a1 = [4,3.5,3.7,8,4.5,5,6]
    
    plt.subplot(221)
    plt.scatter(x,y, label='high income', color='b')
    plt.scatter(s,a, label='low income', color='r')
    plt.title('Contoh Scatter')
    plt.legend()
    plt.subplot(222)
    plt.scatter(x1,y1, label='high income', color='b')
    plt.scatter(s1,a1, label='low income', color='r')
    plt.title('Contoh Scatter')
    plt.legend()
    plt.show()