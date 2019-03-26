# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 17:27:33 2019

@author: Habib Abdul R
"""
import pandas

#Jawaban nomor 3 praktek
def ListPandas():
    df = pandas.read_csv('1174002.csv')
    dt = pandas.DataFrame(df)
    print(dt['npm'])

#Jawaban nomor 4 praktek
def DictPandas():
    df = pandas.read_csv('1174002.csv')
    dt = pandas.DataFrame(df)
    print(dt['npm'])

#Jawaban nomor 5 praktek
def ubahFormatTanggal():
    df = pandas.read_csv('1174002.csv', parse_dates=['ttl'])
    print(df)

#Jawaban nomor 6 praktek
def ubahIndexKolom():
    df = pandas.read_csv('1174002.csv')
    df.index = ['Row_1', 'Row_2']
    print(df)

#Jawaban nomor 7 praktek
def ubahNamaKolom():
    df = pandas.read_csv('1174002.csv')
    df.columns =['Col_1', 'Col_2', 'Col_3', 'Col_4'] 
    print(df)
    

def tulisCsvPandas():
    df = pandas.read_csv('1174002.csv', 
            index_col='NPM', 
            parse_dates=['Tanggal Lahir'],
            header=0, 
            names=['NPM', 'Nama', 'Kelas', 'Tanggal Lahir'])
    df.to_csv('no5.csv')
    