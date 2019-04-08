import serial
import csv
def getData():
    ser = serial.Serial('COM4',9600)
    print(ser.readline().decode("utf-8").strip('\n').strip('\r'))

getData()

def writeCsv():
    ser = serial.Serial('COM4',9600)
    with open('test.csv', mode='w') as csv_file:
        fieldnames = ['status']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
        writer.writeheader()
        while (1):
            data = ser.readline().decode("utf-8").strip('\n').strip('\r')
            writer.writerow({'status': data})
            
writeCsv()