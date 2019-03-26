# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 17:27:33 2019

@author: Habib Abdul R
"""

import csv

#jawaban nomor 1 prakter
def modelist():
    with open('1174002.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print(row[0], row[1], row[2])

#jawaban nomor 2 praktek
def modedict():
    with open('1174002.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            print(row['npm'], row['nama'], row['kelas'])
