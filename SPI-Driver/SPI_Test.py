import binascii
import spidev
import time 

#create spi object
spi_ob = spidev.SpiDev()

#open Spi port 0  slave 0
spi_ob.open(0,0)

#spi mode 
#spi_ob.mode = 2
spi_ob.mode = 0b01

#slave select True
spi_ob.cshigh=True

#spi set speed 
spi_ob.max_speed_hz=5000


to_send = [0x01, 0x02, 0x03]

spi_ob.xfer2(to_send)

while True :
	pass
