# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 12:01:39 2019

@author: Nico Sembiring
"""

from matplotlib import pyplot as plt

def soalplot():

    hasil = 1174096 % 3 + 2
    
    x = [2014,2015,2016,2017,2018,2019]
    y = [76,87,105,122,148,170]
    x2 = [2014,2015,2016,2017,2018,2019]
    y2 = [78,97,114,134,146,167]
    
    for i in range(1, hasil+1):
        plt.subplot(2,2,i)
        plt.plot(x,y,'b',label='Tim Sate Padang', linewidth=1)
        plt.plot(x2,y2,'r',label='Tim Sate Madura',linewidth=1)
        plt.title('Penikmat Sate')
        plt.ylabel('Jumlah Penikmat')
        plt.xlabel('Tahun')
        plt.legend()
        plt.grid(True,color='k')
        plt.subplots_adjust(wspace=.4, hspace=.7)
    
    plt.show()