# usage: python EtchASketch.py <size of the board>
from Tkinter import *
import Adafruit_BBIO.GPIO as GPIO
import argparse
# these are controls
N="P9_12";
S="P9_14";
W="P9_16";
E="P9_18";
C="P9_22";
button_List=[N,S,W,E,C]
LED_list=["P9_11","P9_13","P9_15","P9_17"]
# set up input and output pins
for i in range(len(button_List)):
    GPIO.setup(button_List[i], GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(button_List[i], GPIO.BOTH) 
for i in range(len(LED_list)):
     GPIO.setup(LED_list[i], GPIO.OUT)    
#----------------------------------------------------------------------
# parse the board size argument 
parser = argparse.ArgumentParser()
parser.add_argument("Size", help="display the size of a the board")
args = parser.parse_args()
##### Set variables:
canvas_height = int(args.Size)
canvas_width = int(args.Size)
canvas_color = "white"
x=canvas_width/2
y=canvas_height/2
color="black"
line_width=10
line_length=10

##### Functions:
# move controls
def move_N():
    global y
    canvas.create_line(x, y, x, (y-line_length), width=line_width, fill=color)
    y = y - line_length

def move_S():
    global y
    canvas.create_line(x, y, x, y+line_length, width=line_width, fill=color)
    y = y + line_length

def move_E():
    global x
    canvas.create_line(x, y, x + line_length, y, width=line_width, fill=color)
    x = x + line_length

def move_W():
    global x
    canvas.create_line(x, y, x - line_length, y, width=line_width, fill=color)
    x = x - line_length

def erase_all():
    canvas.delete(ALL)

def waitingForSketch():
    if GPIO.event_detected(N):
        global toggle0
        GPIO.output(LED_list[0],toggle0)
        toggle0 ^= 1 
        move_N()
        
    if GPIO.event_detected(S):
        global toggle1
        GPIO.output(LED_list[1],toggle1)
        toggle1 ^= 1 
        move_S()
        
    if GPIO.event_detected(W):
        global toggle2
        GPIO.output(LED_list[2],toggle2)
        toggle2 ^= 1 
        move_W()
        
    if GPIO.event_detected(E):
        global toggle3
        GPIO.output(LED_list[3],toggle3)
        toggle3 ^= 1 
        move_E() 
        
    if GPIO.event_detected(C):
        erase_all()
        global x,y
        x=canvas_width/2
        y=canvas_height/2
# call itself every 10 ms
    window.after(10, waitingForSketch)    

window = Tk()
window.title("Etch A Sketch")
canvas = Canvas(bg=canvas_color, height=canvas_height, width=canvas_width, highlightthickness=0)
canvas.pack()
toggle0,toggle1,toggle2,toggle3=1,1,1,1;
waitingForSketch()
# loop forever...                    
window.mainloop()




