# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 09:48:40 2019

@author: Habib Abdul R
"""

import matplotlib.pyplot as plt

def plot():    
    x = [6,3,5]
    y = [4,8,10]
    x1 = [6,3,5]
    y2 = [4,8,10]
    plt.subplot(221)
    plt.plot(x,y)
    plt.ylabel('Sumbu Y')
    plt.xlabel('Sumbu X')
    plt.subplot(222)
    plt.plot(x1,y2)
    plt.ylabel('Sumbu Y')
    plt.xlabel('Sumbu X')
    plt.show()
    