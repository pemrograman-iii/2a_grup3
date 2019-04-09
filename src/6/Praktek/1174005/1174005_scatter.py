# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 16:51:49 2019

@author: user
"""

# In[Sactter]:
import matplotlib.pyplot as plt
 
 
def scatter():
    x = [1,1.5,2,2.5,3,3.5,3.7]
    y = [7.5,8,8.5,9,9.5,10,10.5]
    
    s = [8,8.5,9,9.5,10,10.5,11]
    a = [3,3.5,3.7,4,4.5,5,5.2]
    
    x1 = [1,1.5,2,2.5,3,3.5,3.7]
    y1 = [7.5,8,8.5,9,9.5,10,10.5]
    
    s1 = [8,8.5,9,9.5,10,10.5,11]
    a1 = [3,3.5,3.7,4,4.5,5,5.2]
    
    plt.subplot(221)
    plt.scatter(x,y, label='high income', color='m')
    plt.scatter(s,a, label='low income', color='b')
    plt.title('Contoh Scatter')
    plt.legend()
    plt.subplot(222)
    plt.scatter(x1,y1, label='high income', color='m')
    plt.scatter(s1,a1, label='low income', color='b')
    plt.title('Contoh Scatter')
    plt.legend()
    plt.show()