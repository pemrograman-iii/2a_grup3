# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 11:03:32 2019

@author: dzihan
"""

import pandas
#no3
df = pandas.read_csv('isicsv.csv')
print(df)

#no4
df = pandas.read_csv('isicsv.csv')
uji = pandas.DataFrame.from_dict(df)
print(uji)

#no5
df = pandas.read_csv('isipandas.csv', parse_dates=['Birthday'])
print(df)

#no6
df = pandas.read_csv('isipandas.csv', index_col='Name')
print(df)

#no7
df = pandas.read_csv('isipandas.csv',
        header=0, 
        names=['Nama', 'tgl lahir','Gaji', 'Jatah Cuti'])
print(df)

def bacalistpandas():
    df = pandas.read_csv('isipandas.csv')
    print(df)

def write():
    df = pandas.read_csv('isipandas.csv', 
            index_col='Employee', 
            parse_dates=['Hired'],
            header=0, 
            names=['Employee', 'Hired', 'Salary', 'Sick Days'])
    df.to_csv('d1174095_pandas_baru.csv')