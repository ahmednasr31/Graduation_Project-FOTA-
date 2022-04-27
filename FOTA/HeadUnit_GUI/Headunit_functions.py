import os 
import RPi.GPIO as GPIO
import tkinter as Tkinter
import tkinter.messagebox as MSG
#import UART_parser
#from  Headunit import canvas1
import time
#from sensor_threaded  import*
#import RPi.GPI as GPIO
import threading
import multiprocessing
from   cruise_control  import*


counter=0


def none ():
    #Glob_print="Unfortunately, This Service Not Supported Currently."

#    helloCallBack()
    MSG.showwarning( "Warning", "Unfortunately,This Service Not Supported Currently.")
   # return "Unfortunately, This Service Not Supported Currently."
    print ("Unfortunately, This Service Not Supported Currently.")




def cruiseControl():
#    pass
    global counter , dis 
    #os.popen("python3 cruise_control.py").read()
    #os.system("python3 cruise_control.py")

    counter ^= 1
    if counter == 0 :
        dis.terminate()
#        GPIO.cleanup()
        MSG.showinfo( "Message", "CRUISE CONTROL OFF")
        print  ("off")

    elif counter == 1 :

        dis = multiprocessing.Process( target=measure )
        dis.start()
        #sreturn = os.popen("python3 sensor_threaded.py ").read()
        MSG.showinfo( "Message", "CRUISE CONTROL ON")
        print  ("on")

def UpdateVersion ():

    #global Global_Print
    #Run SearchScript.sh (to update lastupdate file)
    os.system("./SearchScript.sh ")

    #Run FileToFlashUpdater.py with lastUpdate  parameter
    scriptReturn = os.popen("python3 FileToFlashUpdater.py lastUpdate ").read() 

    #Read the return of if okupdate Run UART_parser.py
    if scriptReturn == "oklastupdate" :
        MSG.showinfo( "Message", "UPDATING")
        os.system("python3 UART_parser.py ")
        print  ("updating")


    #If noupdate return ("YOU ARE UP TO DATE")
    elif scriptReturn == 'noupdate' :
        MSG.showinfo( "Message", "YOU ARE UP TO DATE")
        print  ("YOU ARE UP TO DATE")

    else :
        print ("else is_"+scriptReturn+"_")




def BackLastVersion():
    #just read script
    scriptReturn = os.popen("python3 FileToFlashUpdater.py lastFlashed ").read() 
    #print (scriptReturn)

    #Read the return of if ..........
    if scriptReturn == "oklastflashed" :
        print  ("Backing To The Old")
        MSG.showinfo( "Message", "BACKING TO THE  OLD VESION")

        os.system("python3 UART_parser.py")

    #If return ("YO")
    elif scriptReturn == "alreadyold" :
        MSG.showinfo( "Message", "YOU ARE ALREADY ON THE OLD VERSION")
        print  ("You are on the old")

    else :
        print ("else is_"+scriptReturn+"_")



