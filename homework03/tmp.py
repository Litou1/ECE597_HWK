import Adafruit_BBIO.GPIO as GPIO
from Adafruit_I2C import Adafruit_I2C
import time 

temp1 = Adafruit_I2C(0x4a)

Alert="P9_11"

GPIO.setup(Alert, GPIO.IN)
GPIO.add_event_detect(Alert, GPIO.BOTH)

temp1.write8(1,0x04) # POL=1
temp1.write8(2,0x14) # low
temp1.write8(3,0x1a) # high

while (True):
	if GPIO.event_detected(Alert):
		print("HIGH")
	# print hex(temp1.readU8(1))
	print "Current temperature is "+str(temp1.readU8(0))+" degree"
	time.sleep(0.5)	

GPIO.cleanup()  		

