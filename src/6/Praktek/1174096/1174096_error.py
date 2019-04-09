# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 12:27:31 2019

@author: Nico Sembiring
"""

from matplotlib import pyplot as plt

def tryExceptError():
    try:
        a=[1,2,3]
        y=[5,2,4]        
        plt.plot(x,y)        
        plt.show()        
    except SyntaxError:
        print("Kesalahan penulisan syntax")
    except NameError:
        print("Variable tersebut tidak ada")
    except TypeError:
        print("Tipe data salah")
    except:
        print("Terjadi sebuah kesalahan")
        
tryExceptError()