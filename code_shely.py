from adafruit_circuitplayground import cp
from remote import r
import time

r = r()

LEFT = "LEFT"
RIGHT = "RIGHT"
NEUTRAL = "NEUTRAL"

LAST_DIRECTION = "NEUTRAL"



while True:
    accx = cp.acceleration.x
    print(accx)


    if accx <= -5.0 and accx >= -9.8:
        if LAST_DIRECTION != LEFT:
            r.send("left")
            print("left")
            LAST_DIRECTION = LEFT
            time.sleep(0.5)


    elif accx <= 9.8 and accx >= 5.0:
        if LAST_DIRECTION != RIGHT:
            r.send("right")
            print("right")
            LAST_DIRECTION = RIGHT
            time.sleep(0.5)

    else:
        LAST_DIRECTION = NEUTRAL
