# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 16:53:27 2019

@author: user
"""

import csv

def readCsv():
    with open('praktek.csv', mode='r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            print(row['jarak'])
            
readCsv()