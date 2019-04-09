# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 09:31:53 2019

@author: Nico Sembiring
"""
# In[]

print(1174096%3+2)
# In[]
import matplotlib.pyplot as plt
 
def soalbar():
    plt.subplot(331)
    plt.bar([0.25,1.25,2.25,3.25,4.25],[50,40,70,80,20],
            label="Nasi",color='y',width=.5)
    plt.bar([.75,1.75,2.75,3.75,4.75],[80,20,20,50,60],
            label="Sate", color='b',width=.5)
    plt.title('Makanan Favorit')
    plt.legend()
   
    plt.subplot(332)
    plt.bar([0.25,1.25,2.25,3.25,4.25],[50,40,70,80,20],
            label="Bihun",color='c',width=.5)
    plt.bar([.75,1.75,2.75,3.75,4.75],[80,20,20,50,60],
            label="Kwetiaw", color='g',width=.5)
    plt.title('Makanan Favorit')
    plt.legend()
   
    plt.subplot(333)
    plt.bar([0.25,1.25,2.25,3.25,4.25],[50,40,70,80,20],
            label="Sop",color='m',width=.5)
    plt.bar([.75,1.75,2.75,3.75,4.75],[80,20,20,50,60],
            label="Gulai", color='k',width=.5)
    plt.title('Makanan Favorit')
    plt.legend()

    plt.show()


