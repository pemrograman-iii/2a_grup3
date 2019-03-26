# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 10:54:17 2019

@author: dzihan
"""

#no1
import csv

with open('isicsv.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Isi disitu teh {", ".join(row)}')
                line_count += 1
            else:
                print(f'\t{row[0]} bekerja di {row[1]} birthday {row[2]}.')
                line_count += 1
                print(f'Processed {line_count} lines.')

#no2
import csv

with open('isicsv.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'isi disitu teh {", ".join(row)}')
            line_count += 1
        print(f'\t{row["nama"]} bekerja di {row["kerjaan"]} department, dan birthday {row["bulan"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')
    
def bacacsvlist():
    with open('isicsv.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f' {", ".join(row)}')
                line_count += 1
            else:
                print(f'\t Orang Ini {row[0]} \ {row[1]} lahir {row[2]}.')
                line_count += 1    
    
    
def nulis():
    with open('test-tulis.csv', mode='w') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        employee_writer.writerow(['Asep', 'Pekerja', 'Januari'])
        employee_writer.writerow(['Deblo', 'Arsitek', 'Maret'])