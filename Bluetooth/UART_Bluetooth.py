import serial
import time

#data = "ahmed"
data = str(input("write Data To Send"))

ser =serial.Serial()
ser.port = "/dev/serial1"
ser.baudrate = 9600
ser.open()
ser.write(data.encode())
#ser.write(data)

while True :
    data = str(input("Write Data To Send "))
    ser.write(data.encode())
    recieve = ser.read()
    while recieve == 'OK\r\n' :
        data = str(input("Enter Next Record"))
        ser.write(data.encode())
        recieve = ser.read()


