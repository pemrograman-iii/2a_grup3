# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 08:47:51 2019

@author: dzihan
"""

# In[mod]
print (1174095%3+2)

# In[No 1]
import matplotlib.pyplot as plt
 
def bar():
    plt.subplot(221)
    plt.bar([.25,1.25,2.25,3.25,4.25], [50,40,70,90,55], 
    label="Mobil", color='c',width=.5)
    plt.bar([.75,1.75,2.75,3.75,4.75], [80,90,40,70,30], 
    label="Sepeda", color='m', width=.5)
    plt.title('Bar 1')
    plt.subplot(222)
    plt.bar([.25,1.25,2.25,3.25,4.25], [55,43,72,92,57], 
    label="Motor", color='r',width=.5)
    plt.bar([.75,1.75,2.75,3.75,4.75], [88,30,48,50,15], 
    label="Becak", color='g', width=.5)
    plt.title('Bar 2')
    plt.show()