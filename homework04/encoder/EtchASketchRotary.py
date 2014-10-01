# usage: python EtchASketch.py <size of the board> 
# run the led matrix pin C to P9_19 (SCL) and pin D to P9_20 (SDA)
# wire eQEP1A to P8_35 and eQEP1B to P8_33
# wire eQEP2A to P8_12 and eQEP1B to P8_11
# from Tkinter import *
import argparse
from time import sleep
import Image
import ImageDraw

import Adafruit_BBIO.GPIO as GPIO
from Adafruit_I2C import Adafruit_I2C
from Adafruit_LED_Backpack import BicolorMatrix8x8
from eqep import eQEP

# set up LED matrix
display = BicolorMatrix8x8.BicolorMatrix8x8()
display.begin()
display.clear()
display.write_display()
color=2
#----------------------------------------------------------------------
# Create an encoder instance for eQEP1 in Absolute mode
encoderX = eQEP("/sys/devices/ocp.3/48302000.epwmss/48302180.eqep", eQEP.MODE_ABSOLUTE)
# Create an encoder instance for eQEP2 in Absolute mode
encoderY = eQEP("/sys/devices/ocp.3/48304000.epwmss/48304180.eqep", eQEP.MODE_ABSOLUTE)
# Set the period to 0.1 seconds, or 100,000,000 nanoseconds
encoderX.set_period(100000000)
encoderY.set_period(100000000)

#----------------------------------------------------------------------
# parse the board size argument 
parser = argparse.ArgumentParser()
parser.add_argument("Size", help="display the size of a the board")
args = parser.parse_args()
size=int(args.Size)
x=0
y=0

prePosX=0
prePosY=0
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

def waitingForSketch():
    global prePosX,prePosY
    currentPosX=encoderX.poll_position()
    currentPosY=encoderY.poll_position()

    if currentPosY>prePosY:
        move_N()
        prePosY=currentPosY
        print "N"
    if currentPosY<prePosY:
        move_S()
        prePosY=currentPosY
        print "S"

    if currentPosX<prePosX:
        move_W()
        prePosX=currentPosX
        print "W"

    if currentPosX>prePosX:
        move_E()
        prePosX=currentPosX
        print "E"
 

while (True):
    display.set_pixel(0,0,2) # initial coordinate 
    display.write_display()
    waitingForSketch()



