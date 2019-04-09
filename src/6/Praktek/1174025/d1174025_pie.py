# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 10:03:31 2019

@author: dezha
"""

from matplotlib import pyplot as ch6

print(1174025%3+2)
def pie():    
    slices = [10,4,7,10]
    slices2 = [9,8,2,2]
    slices3 = [8,10,5,5]
    slices4 = [6,9,4,2]
    aktifitas = ['lolok','makan','kojo','main']
    cols = ['c', 'm', 'r', 'b']
    
    ch6.subplot(221)
    ch6.pie(slices,
            labels=aktifitas,
            colors=cols,
            startangle=90,
            shadow= True,
            explode=(0,0.1,0,0),
            autopct='%1.1f%%')
    ch6.title('Pie 1')
    
    ch6.subplot(222)
    ch6.pie(slices2,
            labels=aktifitas,
            colors=cols,
            startangle=90,
            shadow= True,
            explode=(0,0.1,0,0),
            autopct='%1.1f%%')
    ch6.title('Pie 2')
    
    ch6.subplot(223)
    ch6.pie(slices3,
            labels=aktifitas,
            colors=cols,
            startangle=90,
            shadow= True,
            explode=(0,0.1,0,0),
            autopct='%1.1f%%')
    ch6.title('Pie 3')
    
    ch6.subplot(224)
    ch6.pie(slices4,
            labels=aktifitas,
            colors=cols,
            startangle=90
            ,
            shadow= True,
            explode=(0,0.1,0,0),
            autopct='%1.1f%%')
    ch6.title('Pie 4')
    ch6.show()

pie()