

import tkinter as GUI 
import tkinter.font as font
from PIL import Image, ImageTk
import os
from  Headunit_functions import*
import time
import threading
import multiprocessing
import RPi.GPIO as GPIO




#os.system("xdotool key ctrl+shift+n")
#os.system("cd /home/pi/Desktop/Gradution-Project/HeadUnit_GUI")


#Fuction Calls
FunctionCall=[ cruiseControl , UpdateVersion , BackLastVersion , none ]



def init():
    global     main_window , FunctionCall
    #font-style
    myFont = font.Font(family='Helvetica'  ,size=17  ,weight="bold")
    #list-of-buttons-text
    left_side_buttons = ["Imergancy Call" , "Music" , "Gallery" , "Messages"]
    right_side_buttons= ["Cruise control" , "Update Version" , "Back To LastVerion","Report Error" ]
    #List-of-Buttons
    left_button=[]
    right_button=[]


    for iterator in range( 0 , 4 ) : 
        #
        left_button.append(GUI.Button(main_window,width=16,height=2,fg="#dfe3e7",bg="#3a424b",
        activeforeground="black", activebackground="#596673" ,font=myFont, bd=0,
        text=left_side_buttons[iterator] ,command=FunctionCall[3])  )
        #place
        left_button[iterator].place( x=50 , y=1*((iterator+1)*85) )

    #Right_side label buttons (..+..+..+..)
    for iterator in range( 0 , 4 ) :
        #Button
        right_button.append(GUI.Button(main_window,width=16,height=2,fg="#dfe3e7",bg="#3a424b",
        activeforeground="black", activebackground="#596673", font=myFont, bd=0,
        text=right_side_buttons[iterator],command=FunctionCall[iterator])  )
        #place
        right_button[iterator].place( x=500 ,  y=1*((iterator+1)*85) )


#create main_window 
main_window=GUI.Tk()

#disable resizability 
main_window.resizable(False , False)

#Set title 
main_window.title("FOTA")

#Set Geometry of main_window
main_window.geometry("800x480-4-12")

#myImage = ImageTk.PhotoImage( file = "./HeadUnit_Images/image_4.jpg")  
#open image
#myImage = Image.open("./HeadUnit_Images/image_4.jpg")  
myImage = Image.open("./HeadUnit_Images/img2.png") 

#resize image after open 
bg_image = myImage.resize((800,480))
#convert as image
img = ImageTk.PhotoImage(bg_image)  

#create Canvas
canvas1 = GUI.Canvas( main_window, width=1600 ,height=960 )
canvas1.pack(fill ="both" , expand=True)
#Display-image 
canvas1.create_image(0,0, image=img , anchor="nw")

#canvas2 = GUI.Canvas( main_window, width=200 ,height=200 )


#Display Text
#canvas1.create_text( 600,750,text=Global_Print, font=("Havanica",30) , fill="#DC143C" )
#initialize

init()
#GPIO.cleanup()

#main window loop
main_window.mainloop()
