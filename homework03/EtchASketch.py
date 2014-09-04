# usage: python EtchASketch.py <size of the board> 
# run the led matrix pin C to P9_19 (SCL) and pin D to P9_20 (SDA)
# from Tkinter import *
import Adafruit_BBIO.GPIO as GPIO
from Adafruit_I2C import Adafruit_I2C
import argparse
from time import sleep
import Image
import ImageDraw
from Adafruit_LED_Backpack import BicolorMatrix8x8

# load temperature
temp1 = Adafruit_I2C(0x4a)
# set up LED matrix
display = BicolorMatrix8x8.BicolorMatrix8x8()
display.begin()
display.clear()
display.write_display()

# these are controls
N="P9_12";
S="P9_14";
W="P9_16";
E="P9_18";
C="P9_22";
button_List=[N,S,W,E,C]
 
for i in range(len(button_List)):
    GPIO.setup(button_List[i], GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(button_List[i], GPIO.RISING) 
  
#----------------------------------------------------------------------
# parse the board size argument 
parser = argparse.ArgumentParser()
parser.add_argument("Size", help="display the size of a the board")
args = parser.parse_args()
size=int(args.Size)
x=0
y=0

##### Functions:
# move controls
def move_N():
    global y,color
    y = (y+1)%size
    display.set_pixel(y, x, color)
    display.write_display()

def move_S():
    global y,color
    y=(y-1)%size
    display.set_pixel(y,x, color)
    display.write_display()
 

def move_E():
    global x,color
    x = (x + 1)%size
    display.set_pixel(y,x,  color)
    display.write_display()


def move_W():
    global x,color
    x = (x - 1)%size
    display.set_pixel( y,x, color)
    display.write_display()


def erase_all():
    display.clear()
    display.write_display()


def waitingForSketch():
    if GPIO.event_detected(N):
        move_N()
    if GPIO.event_detected(S):
        move_S()
    if GPIO.event_detected(W):
        move_W()
    if GPIO.event_detected(E):
        move_E() 
    if GPIO.event_detected(C):
        erase_all()
        global x,y
        x=0
        y=0
# call itself every 100 ms
    sleep(0.1)  

while (True):

    color= 2 if temp1.readU8(0)>22 else 1

    print "Current temperature is "+str(temp1.readU8(0))+" degree"

    display.set_pixel(0,0,1) # initial coordinate 
    display.write_display()
    waitingForSketch()



