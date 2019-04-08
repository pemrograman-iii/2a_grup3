# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 14:20:40 2019

@author: user
"""

# In[3 graph]

from matplotlib import pyplot as plt
 
x = [5,2,7]
y = [2,16,4]
plt.plot(x,y)
plt.title('Membuat x dan y')
plt.ylabel('Ini Sumbu Y')
plt.xlabel('Ini Sumbu X')
plt.show()


# In[3 bar]
from matplotlib import pyplot as plt
 
plt.bar([0.25,1.25,2.25,3.25,4.25],[50,40,70,80,20],
label="BMW",color='y',width=.5)
plt.bar([.75,1.75,2.75,3.75,4.75],[80,20,20,50,60],
label="Audi", color='r',width=.5)
plt.legend()
plt.xlabel('Days')
plt.ylabel('Distance (kms)')
plt.title('Contoh Bar')
plt.show()

# In[3 histogram]
import matplotlib.pyplot as plt
population_age = [11,22,16,9,10,15,22,55,62,45,21,22,34,42,42,4,2,102,95,85,55,110,120,70,65,55,111,115,80,75,65,54,44,43,42,48]
bins = [0,10,20,30,40,50,60,70,80,90,100]
plt.hist(population_age, bins, histtype='bar', rwidth=0.8)
plt.xlabel('age groups')
plt.ylabel('Number of people')
plt.title('Contoh Histogram')
plt.show()

# In[3 Scatter]
import matplotlib.pyplot as plt
x = [1,1.5,2,2.5,3,3.5,3.6]
y = [7.5,8,8.5,9,9.5,10,10.5]
 
x1=[8,8.5,9,9.5,10,10.5,11]
y1=[3,3.5,3.7,4,4.5,5,5.2]
 
plt.scatter(x,y, label='high income low saving',color='r')
plt.scatter(x1,y1,label='low income high savings',color='b')
plt.xlabel('simpanan dalam ratusan')
plt.ylabel('pendapatan dalam ribuan')
plt.title('Scatter Plot')
plt.legend()
plt.show()

# In[3 area plot]
import matplotlib.pyplot as plt
days = [1,2,3,4,5]
  
sleeping =[7,8,6,11,7]
eating = [2,3,4,3,2]
working =[7,8,7,2,2]
playing = [8,5,7,8,13]
  
plt.plot([],[],color='m', label='Sleeping', linewidth=5)
plt.plot([],[],color='c', label='Eating', linewidth=5)
plt.plot([],[],color='r', label='Working', linewidth=5)
plt.plot([],[],color='k', label='Playing', linewidth=5)
  
plt.stackplot(days, sleeping,eating,working,playing, colors=['m','c','r','k'])
  
plt.xlabel('x')
plt.ylabel('y')
plt.title('Area Plot')
plt.legend()
plt.show()

# In[3 Pie]
import matplotlib.pyplot as plt
 
days = [1,2,3,4,5]
 
sleeping =[7,8,6,11,7]
eating = [2,3,4,3,2]
working =[7,8,7,2,2]
playing = [8,5,7,8,13]
slices = [7,2,2,13]
activities = ['sleeping','eating','working','playing']
cols = ['c','m','r','b']
 
plt.pie(slices,
  labels=activities,
  colors=cols,
  startangle=70,
  shadow= True,
  explode=(0.1,0,0,0),
  autopct='%1.1f%%')
 
plt.title('contoh Pie')
plt.show()

# In[subplot]

import matplotlib.pyplot as plt
 
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)
t1 = np.arange(0.5, 5.0, 0.2)
t2 = np.arange(0.0, 5.0, 0.02)
t3 = np.arange(0.0, 4.0, 0.5)
t4 = np.arange(1.0, 4.2, 0.3)
plt.subplot(331)
plt.plot(t1, f(t1), t1, f(t1))
plt.subplot(332)
plt.plot(t2, f(t2), t2, f(t2))
plt.subplot(333)
plt.plot(t3, f(t3), t3, f(t3))
plt.subplot(334)
plt.plot(t2, f(t2), t3, f(t3))
plt.subplot(335)
plt.plot(t4, f(t4), t1, f(t1))
plt.subplot(336)
plt.plot(t1, f(t1), t2, f(t2))
plt.subplot(337)
plt.plot(t4, f(t4), t4, f(t4))
plt.subplot(338)
plt.plot(t3, f(t3), t4, f(t4))
plt.subplot(339)
plt.plot(t4, f(t4), t2, f(t2))
plt.show()

# In[histogram 2]
import matplotlib.pyplot as plt
kategori = [21,55,26,45,21,22,34,42,4,99,102,110,120,122,123,125,130,111,116,117,80,75,65,54,44,43,42,48]
bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]
plt.hist(kategori, bins, histtype='bar', rwidth=0.8)
plt.xlabel('Kategori')
plt.ylabel('Jumlah anak')
plt.title('Nomor7')
plt.show()

