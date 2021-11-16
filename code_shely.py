from adafruit_circuitplayground import cp
from remote import r
import time

r = r()

while True:
    accx = cp.acceleration.x
    print(accx)

    if accx <= -5.0 and accx >= -9.8:
        r.send("left")
        print("left")

    if accx <= 9.8 and accx >= 5.0:
        r.send("right")
        print("right")
