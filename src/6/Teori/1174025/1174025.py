# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 21:39:53 2019

@author: dezha
"""
# In[No 2 Teori]:
import matplotlib.pyplot as plt
x = [6,3,5]
y = [4,8,10]
plt.plot(x,y)
plt.ylabel('Sumbu Y')
plt.xlabel('Sumbu X')
plt.show()



# In[No 3 Bar]:
from matplotlib import pyplot as plt

plt.bar([.25,1.25,2.25,3.25,4.25], [50,40,70,90,55], 
label="Ferrari", color='r',width=.5)
plt.bar([.75,1.75,2.75,3.75,4.75], [80,90,40,70,30], 
label="Lamborgini", color='c', width=.5)
plt.title('Contoh Bar')
plt.show()

# In[Histogram]:
from matplotlib import pyplot as plt

populasi = [20,20,33,50,68,79,11,12,23,46,79,]
rakyat = [0,10,20,30,40,50,70,80]
plt.hist(populasi, rakyat, histtype='bar', width=2.8)
plt.title('Contoh Histogram')
plt.show()

# In[Scatter]:
import matplotlib.pyplot as plt

x = [1,1.5,2,2.5,3,3.5,3.7]
y = [7.5,8,8.5,9,9.5,10,10.5]

s = [8,8.5,9,9.5,10,10.5,11]
a = [3,3.5,3.7,4,4.5,5,5.2]

plt.scatter(x,y, label='biru', color='b')
plt.scatter(s,a, label='merah', color='r')
plt.xlabel('saving*100')
plt.ylabel('income*1000')
plt.title('Contoh Scatter')
plt.legend()
plt.show()

# In[Pie Chart]:
import matplotlib.pyplot as plt

hari = [1,2,3,4,5]

tidur = [7,8,6,11,7]
makan = [2,3,4,3,2]
working = [7,8,7,2,2]
main = [8,5,7,8,13]
slices = [7,2,2,13]
aktifitas = ['tidur','makan','working','main']
cols = ['c', 'm', 'r', 'b']

plt.pie(slices,
        labels=aktifitas,
        colors=cols,
        startangle=90,
        shadow= True,
        explode=(0,0.1,0,0),
        autopct='%1.1f%%')
plt.title('Contoh Pie')
plt.show()

# In[No 5 SubPlot]
import numpy as np
import matplotlib.pyplot as plt
 
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)
t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.2)
t3 = np.arange(0.0, 4.0, 0.3)
t4 = np.arange(0.0, 4.0, 0.2)
t5 = np.arange(1.0, 1.0, 0.4)
t6 = np.arange(3.0, 2.0, 0.5)
t7 = np.arange(3.0, 3.0, 0.3)
t8 = np.arange(2.0, 4.0, 0.1)
t9 = np.arange(6.0, 2.0, 0.2)
plt.subplot(331)#tinggi,lebar,urutan
plt.plot(t1, f(t1), 'bo', t2, f(t2))
plt.subplot(332)
plt.plot(t1, f(t1), t2, f(t2))
plt.subplot(333)
plt.plot(t1, f(t1), t2, f(t2), t3, f(t3))
plt.subplot(334)
plt.plot(t1, f(t1), t2, f(t2), t3, f(t3), t4, f(t4))
plt.subplot(335)
plt.plot(t1, f(t1), t2, f(t2), t3, f(t3), t4, f(t4), t5, f(t5))
plt.subplot(336)
plt.plot(t1, f(t1), t2, f(t2), t3, f(t3), t4, f(t4), t5, f(t5), t6, f(t6))
plt.subplot(337)
plt.plot(t1, f(t1), t2, f(t2), t3, f(t3), t4, f(t4), t5, f(t5), t6, f(t6), t7, f(t7))
plt.subplot(338)
plt.plot(t1, f(t1), t2, f(t2), t3, f(t3), t5, f(t5), t6, f(t6), t7, f(t7), t8, f(t8))
plt.subplot(339)
plt.plot(t1, f(t1), t2, f(t2), t3, f(t3), t6, f(t6), t7, f(t7), t8, f(t8), t9, f(t9))
plt.show()