# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 12:15:14 2019

@author: Nico Sembiring
"""
import pandas

def bacalistpandas():
    df = pandas.read_csv('1174096.csv')
    print(df)

def bacadictpandas():
    df = pandas.read_csv('1174096.csv')
    uji = pandas.DataFrame.from_dict(df)
    print(uji)
    
def standartanggal():
    df = pandas.read_csv('1174096.csv', parse_dates=['ttl'])
    print(df)

def changeindexcol():
    df = pandas.read_csv('1174096.csv', index_col='npm')
    print(df)

def renameatt():
    df = pandas.read_csv('1174096.csv',
            header=0, 
            names=['Nomor Induk Mahasiswa', 'Name','Class', 'Tanggal Lahir'])
    print(df)

def write():
    df = pandas.read_csv('hrdata.csv', 
            index_col='Employee', 
            parse_dates=['Hired'],
            header=0, 
            names=['Employee', 'Hired', 'Salary', 'Sick Days'])
    df.to_csv('1174096pandas.csv')    