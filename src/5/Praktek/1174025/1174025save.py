import serial

def getDataLoop():
    ser = serial.Serial('COM4',9600)
    while (1):
        print(ser.readline().decode("utf-8").strip('\n').strip('\r'))
        
getDataLoop()
