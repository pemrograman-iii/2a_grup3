# -*- coding: utf-8 -*-
"""

Created on Mon Mar 25 17:27:54 2019
@author: Nico Sembiring
"""
import pandas
import csv

def bacacsv():
    with open('1174096.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                print(f'\t NPM : {row[0]} Nama : {row[1]} Kelas : {row[2]}.')
                line_count += 1
                print(f'Processed {line_count} lines.')

def bacadictionary():
    with open('1174096.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            print(f'\t NPM : {row["name"]} Nama : {row["department"]} Kelas :  {row["birthday month"]}.')
            line_count += 1
        print(f'Processed {line_count} lines.')

def nulis():
    with open('test-tulis.csv', mode='w') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        employee_writer.writerow(['Ucok', 'Tukang', 'November'])
        employee_writer.writerow(['Udin', 'Mandor', 'April'])

#Fungsi Try Except 
def bacaCsvPandas():
    try:
        df = pandas.read_csv('teori.csv')
        print(dt)
    except SyntaxError:
        print("Kesalahan penulisan syntax")
    except NameError:
        print("Variable tersebut tidak ada")
    except TypeError:
        print("Tipe data salah")
    except:
        print("Terjadi sebuah kesalahan")

bacaCsvPandas()
