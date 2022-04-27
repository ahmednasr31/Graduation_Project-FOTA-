#import UART_parser
import time
import RPi.GPIO as GPIO
import multiprocessing
import tkinter.messagebox as MSG


#UART
import serial
#create and open UART
myser =serial.Serial()
myser.port = "/dev/serial0"
myser.baudrate = 9600
myser.open()




TRIG=21
ECHO=20
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
distance=0
pulse_start=0
pulse_duration=0
pulse_end=0
receive=0
'''
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
'''






'''


while True:
    print"distance measurement in progress"
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
    GPIO.output(TRIG,False)
    print"waiting for sensor to settle"
    time.sleep(0.2)
    GPIO.output(TRIG,True)
    time.sleep(0.00001)
    GPIO.output(TRIG,False)
    while GPIO.input(ECHO)==0:
        pulse_start=time.time()
    while GPIO.input(ECHO)==1:
        pulse_end=time.time()
    pulse_duration=pulse_end-pulse_start
    distance=pulse_duration*17150
    distance=round(distance,2)
    print"distance:",distance,"cm"
    time.sleep(2)    
'''
def getDistance():
    global   TRIG , ECHO , distance , pulse_start ,pulse_duration ,pulse_end,receive
#    GPIO.setmode(GPIO.BCM)


#    print ("distance measurement in progress")
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
    GPIO.output(TRIG,False)
#   print ("waiting for sensor to settle")
    time.sleep(0.2)
    GPIO.output(TRIG,True)
    time.sleep(0.00001)
    GPIO.output(TRIG,False)
    while GPIO.input(ECHO)==0:
        pulse_start=time.time()
    while GPIO.input(ECHO)==1:
        pulse_end=time.time()
    pulse_duration=pulse_end-pulse_start
    distance=pulse_duration*17150
    distance=round(distance,2)
   # print ("distance:",distance,"cm")
#    time.sleep(2)
 #  GPIO.cleanup()


def measure():
    global distance
#    GPIO.setmode(GPIO.BCM)
    while True:
        getDistance()
        msg = int( distance )

        if   (msg > 15 ) :
            myser.write("go\n".encode())
#                print ("go")

        elif (msg <= 15) :  
            myser.write("stop\n".encode())
#                print ("stop")

        else: print("else not greater nor lower than 10 cm")

            #receive= myser.read()
            #while receive != b'k' :
            #    receive= myser.read()
            #counter+=1
            #timeout
            #if counter == 20 :
             #  pass 
        print (msg)
        #sleep for 0.2 sec
#        time.sleep(.2)
            #GPIO.cleanup()

'''

status=0

try :

    status ^= 1
    if status == 1 :
        dis = multiprocessing.Process( target=measure )
        dis.start()
#        MSG.showinfo( "Message", "CRUISE CONTROL ON")

#       print  ("on")
    elif status == 0 :
        dis = multiprocessing.Process( target=measure )
        dis.terminate()
#        MSG.showinfo( "Message", "CRUISE CONTROL OFF")
#       print  ("off")

except:
    pass
#    GPIO.cleanup()

#finally:
#    GPIO.cleanup() 

'''
