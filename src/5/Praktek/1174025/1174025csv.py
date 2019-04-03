import csv

def readCsv():
    with open('test.csv', mode='r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            print(row['status'])
            
readCsv()
