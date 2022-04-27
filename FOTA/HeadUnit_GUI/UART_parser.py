
import serial
import time
#import tkinter.messagebox as MSG


#open FileToFlash.txt  file
toFlashHand = open("FileToFlash.txt" , "r")

#Read FileToFlash.txt (first read is first-line) 
fileName = toFlashHand.readline()
#delet \n from the name
fileName = fileName.replace("\n",'')
#close the file
toFlashHand.close()

#path of file-to-flash  file
path  = "/var/www/html/codenext/uploadfile/files/" + fileName



#file Handing 
fileHand = open(path, "r")

#parsing HEX file
#for iterator in fileHand :
 #   print(iterator)

print (fileName+ '\n')
#MSG.showinfo( "Message", fileName )


ser =serial.Serial()
ser.port = "/dev/serial0"
ser.baudrate = 9600
ser.open()

#reset ARM 
ser.write("RESET\n".encode())
#print (fileName)
time.sleep(2)


#rec = ser.read()
#while rec != b'n': 
#    rec = ser.read()

#print ("hi")

receive=0

for record in fileHand :
    for digit in record :
        #print (digit, end="" )
        ser.write(digit.encode())
        print ( digit )
    #time.sleep()

    receive = ser.read()
    print (receive)
    while receive != b'k': 
        receive = ser.read()
        print (receive)

   # time.sleep(.2)
 #   print (receive) 
   # record = fileHand.readline()
   # record = iterator + '\n'
    #print (record)
   # record = str(record+'\r')
   # record = str(record)
    #print ( record )
    #ser.write(record.encode())
   # ser.write('\r\n'.encode())
    #ser.write(record)
    #time.sleep(.5)
    #receive = ser.read()
    #while receive != b'\xff' :
     #   print (receive)
      #  receive = ser.read()


#Append flashed file to LastFlashex.text
#fname= fileName +'\n'

fname = fileName + '\n' 
file_list=[fname]

#open the file to read
Handler = open("LastFlashed.txt" , "r+")
#parse all the file
for line in Handler :
    file_list.append(line)

#close
Handler.close()

#reopen with write 
writeHandler = open("LastFlashed.txt" , "w+")
#append
for iterator in file_list :
    writeHandler.write(iterator)

writeHandler.close()

#MSG.showinfo( "Message", "finished" )
print ("finished")

