# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 10:00:46 2019

@author: dezha
"""

from matplotlib import pyplot as ch6

print(1174025%3+2)
def bar():
    x1 = [3, 6, 9, 12, 15]
    y1 = [5, 10, 15, 20, 25]
    
    x2 = [2, 6, 4, 9, 3]
    y2 = [5, 2, 7, 9, 4]
    
    x3 = [8, 4, 2, 7, 1]
    y3 = [7, 3, 5, 10, 2]
    
    x4 = [11, 5, 15, 17, 8]
    y4 = [4, 4, 8, 15, 7]
    
    ch6.subplot(221)
    ch6.bar(x1, y1)
    
    ch6.subplot(222)
    ch6.bar(x2, y2)
    
    ch6.subplot(223)
    ch6.bar(x3, y3)
    
    ch6.subplot(224)
    ch6.bar(x4, y4)
    
    ch6.show()

bar()