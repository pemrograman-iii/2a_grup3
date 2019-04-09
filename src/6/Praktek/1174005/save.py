# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 16:55:54 2019

@author: user
"""

import serial

def getDataLoop():
    ser = serial.Serial('COM5',9600)
    while (1):
        print(ser.readline().decode("utf-8").strip('\n').strip('\r'))
        
getDataLoop()