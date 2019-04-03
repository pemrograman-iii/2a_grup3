# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 15:45:40 2019

@author: Nico Sembiring
"""

import serial

def getDataLoop():
    ser = serial.Serial('COM5',9600)
    while (1):
        print(ser.readline().decode("utf-8").strip('\n').strip('\r'))
        
getDataLoop()