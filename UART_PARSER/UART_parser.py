
import serial
import time

#file Handing 
fileHand = open("/var/www/html/codenext/uploadfile/files/project_1.hex", "r")

#parsing HEX file
#for iterator in fileHand :
 #   print(iterator)


ser =serial.Serial()
ser.port = "/dev/serial0"
ser.baudrate = 9600
ser.open()





for iterator in fileHand :
    record = fileHand.readline()
    print (record + '\n\r')
   # record = str(record+'\r')
  #  record = str(record)
    ser.write(record.encode())
    ser.write('\r\n'.encode())
    #ser.write(record)
   # time.sleep(1)
    #receive = ser.read()
    #while receive != b'\xff' :
     #   print (receive)
      #  receive = ser.read()
