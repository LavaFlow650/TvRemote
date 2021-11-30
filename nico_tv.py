from adafruit_circuitplayground import cp
from remote import r
import time
import math

r = r()

TRIP  = 4
RESET = 2

ERROR = 30

def accToSend(x,y):
    angle = 360*math.atan2(y,x)/(2*math.pi)
    if(0-ERROR<=angle and angle<=0+ERROR):
        r.send('right')
    elif(90-ERROR<=angle and angle<=90+ERROR):
        r.send('up')
    elif(-90-ERROR<=angle and angle<=-90+ERROR):
        r.send('down')
    elif(180-ERROR<=angle or angle<=-180+ERROR):
        r.send('left')

def reset():
    mag=RESET+1
    while(RESET<=mag):
        acc = cp.acceleration
        mag = math.sqrt(acc.x**2+acc.y**2)
        #print(RESET,mag)
        time.sleep(.1)

while True:
    if cp.button_b:
        r.send('ok')
        while cp.button_b:
            pass
    acc = cp.acceleration
    mag = math.sqrt(acc.x**2+acc.y**2)
    if(mag>=TRIP):
        accToSend(acc.x,acc.y)
        reset()
    #time.sleep(.1)
