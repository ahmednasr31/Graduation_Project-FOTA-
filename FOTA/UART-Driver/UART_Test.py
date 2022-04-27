import serial

#serialport = serial.Serial("serial0", baudrate=9600, timeout=3.0)
serialport = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=3.0)


while True:
    serialport.write("rnSay something:")
    rcv = port.read(10)
    #serialport.write("rnYou sent:" + repr(rcv))
