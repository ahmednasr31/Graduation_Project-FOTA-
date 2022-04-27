
import serial 


UART_Obj = serial.Serial( baudrate=9600)# , parity=serial.PARITY_NONE , stopbits = serial.STOPBITS_ONE , bytesize= serial.EIGHTBITS )

UART_Obj.write ("HELLO AHEMD NASR ")


while True :
	pass 
	
	
