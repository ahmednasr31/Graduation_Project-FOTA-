import spidev
#in RPi3 only spi0
bus=0
#in RPi3 there are 2 slave select pins
device=0

#create spi object 
SPI_Obj = spidev.SpiDev()

#set speed in HZ (4MHZ)
SPI_Obj.max_speed_hz=5000

#open bus
SPI_Obj.open(bus, device)

#Date to send
to_send = [0x01, 0x02, 0x03]

#Send 
SPI_Obj.xfer2(10)


while True :
	pass
