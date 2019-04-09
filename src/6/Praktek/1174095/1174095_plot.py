# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 09:48:40 2019

@author: dzihan
"""

import matplotlib.pyplot as plt

def plot():    
    x = [3,6,5]
    y = [5,7,9]
    x1 = [3,6,5]
    y2 = [5,7,9]
    plt.subplot(221)
    plt.plot(x,y)
    plt.ylabel('Sumbu Y')
    plt.xlabel('Sumbu X')
    plt.subplot(222)
    plt.plot(x1,y2)
    plt.ylabel('Sumbu Y')
    plt.xlabel('Sumbu X')
    plt.show()
    