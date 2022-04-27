#!/usr/bin/python3

from signal import signal, SIGTERM, SIGHUP, pause
from time import sleep
from threading import Thread
from gpiozero import DistanceSensor
#import sys
#import os

#UART
import serial

#create and open UART
ser =serial.Serial()
ser.port = "/dev/serial0"
ser.baudrate = 9600
ser.open()


receive=0
counter=0

#Ultra-Sonic
reading = True
sensor = DistanceSensor(echo=20, trigger=21)

def safe_exit(signum, frame):
    exit(1)

def read_distance():
    global message

    while reading:
        msg = int(sensor.value * 100)

        if      (msg >  10) :
            ser.write("go\n".encode())
            print ("go")

        elif    (msg <= 10) :
            ser.write("stop\n".encode())
            print ("stop")


        else :
            print("else not greater non lower than 10 cm")



        receive= ser.read()
        while receive != b'k' :
            receive=ser.read()
            counter+=1
            if counter == 20 :
               pass

        #print distance any way
        print(msg)
        sleep(0.6)

try:
    signal(SIGTERM, safe_exit)
    signal(SIGHUP, safe_exit)

    reader = Thread(target=read_distance, daemon=True)
#    reader.start()

    pause()

except KeyboardInterrupt:
    pass


finally:
    reading = False
    reader.join()
    sensor.close()
