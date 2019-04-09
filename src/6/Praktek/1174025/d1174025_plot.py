# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 10:00:46 2019

@author: dezha
"""

from matplotlib import pyplot as ch6

print(1174025%3+2)
def plot():
    x1 = [3, 6, 9, 12, 15]
    y1 = [5, 10, 15, 20, 25]
    
    x2 = [2, 6, 7, 9, 13]
    y2 = [3, 5, 7, 5, 10]
    
    x3 = [1, 2, 5, 7, 10]
    y3 = [3, 3, 5, 8, 4]
    
    x4 = [1, 5, 10, 15, 18]
    y4 = [4, 4, 8, 15, 7]
    
    ch6.subplot(221)
    ch6.plot(x1, y1)
    
    ch6.subplot(222)
    ch6.plot(x2, y2)
    
    ch6.subplot(223)
    ch6.plot(x3, y3)
    
    ch6.subplot(224)
    ch6.plot(x4, y4)
    
    ch6.show()

plot()