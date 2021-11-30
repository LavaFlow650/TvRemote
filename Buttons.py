from adafruit_circuitplayground import cp
from remote import r
import time

r = r()

while True:
    while cp.switch == True:
        time.sleep(0.15)
        cp.pixels.fill((0, 0, 0))
        if cp.button_a and cp.button_b:
            cp.pixels.fill((0, 100, 0))
            r.send("ok")
#            print("ok")

        elif cp.button_a and not cp.button_b:
            cp.pixels[0] = (0, 100, 0)
            cp.pixels[1] = (0, 100, 0)
            cp.pixels[2] = (0, 100, 0)
            cp.pixels[7] = (0, 100, 0)
            cp.pixels[8] = (0, 100, 0)
            cp.pixels[9] = (0, 100, 0)
            r.send("up")
#            print("up")

        elif cp.button_b and not cp.button_a:
            cp.pixels[5] = (0, 100, 0)
            cp.pixels[6] = (0, 100, 0)
            cp.pixels[7] = (0, 100, 0)
            cp.pixels[4] = (0, 100, 0)
            cp.pixels[3] = (0, 100, 0)
            cp.pixels[2] = (0, 100, 0)
            r.send("down")
#            print("down")

        pass
    while cp.switch == False:
        time.sleep(0.15)
        cp.pixels.fill((0, 0, 0))
        if cp.button_a and cp.button_b:
            cp.pixels.fill((0, 100, 0))
            r.send("ok")
#            print("ok")

        if cp.button_a:
            cp.pixels[0] = (0, 100, 0)
            cp.pixels[1] = (0, 100, 0)
            cp.pixels[2] = (0, 100, 0)
            cp.pixels[3] = (0, 100, 0)
            cp.pixels[4] = (0, 100, 0)
            r.send("left")
#            print("left")

        if cp.button_b:
            cp.pixels[5] = (0, 100, 0)
            cp.pixels[6] = (0, 100, 0)
            cp.pixels[7] = (0, 100, 0)
            cp.pixels[8] = (0, 100, 0)
            cp.pixels[9] = (0, 100, 0)
            r.send("right")
#            print("right")

        pass
