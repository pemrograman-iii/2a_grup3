# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 10:44:00 2019

@author: Nico Sembiring
"""
# In[]

print(1174096%3+2)

# In[]
import matplotlib.pyplot as plt

def soalscatter():
    plt.subplot(331)
    x = [1,3,5,7,9,11,13,15,17.5]
    y = [2,4,6,8,10,12,14,16,17.5]

    plt.scatter(x,y, label='Mei',color='r')
    
    plt.xlabel('Hari')
    plt.ylabel('Penjualan')
    plt.title('Data Penjualan')
    plt.legend()
    
    plt.subplot(332)
    x = [1,3,5,7,9,11,13,15,17.5]
    y = [14,12,6,7.4,9,15,13.5,11,5]

    plt.scatter(x,y, label='Juni',color='g')
    
    plt.xlabel('Hari')
    plt.ylabel('Penjualan')
    plt.title('Data Penjualan')
    plt.legend()
    
    plt.subplot(333)
    x = [1,3,5,7,9,11,13,15,17.5]
    y = [5,4,3,4,5,6,7,8,5]

    plt.scatter(x,y, label='Juli',color='b')
    
    plt.xlabel('Hari')
    plt.ylabel('Penjualan')
    plt.title('Data Penjualan')
    plt.legend()

    plt.show()