# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 18:07:57 2019

@author: Nico Sembiring
"""

import serial

def baca():
    ser = serial.Serial("COM6",115200)
    baca = ser.readline()
    print(baca)

baca()