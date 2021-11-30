from adafruit_circuitplayground import cp
from remote import r
import time

r = r()

while True:

    def color(direction):
        cp.pixels.fill((0, 0, 0))
        if direction == "ok":
            cp.pixels.fill((0, 100, 0))
        if direction == "up":
            x = [0, 1, 2, 7, 8, 9]
            for i in x:
                cp.pixels[i] = (0, 100, 0)
        if direction == "down":
            x = [2, 3, 4, 5, 6, 7]
            for i in x:
                cp.pixels[i] = (0, 100, 0)
        if direction == "left":
            x = [0, 1, 2, 3, 4]
            for i in x:
                cp.pixels[i] = (0, 100, 0)
        if direction == "right":
            x = [5, 6, 7, 8, 9]
            for i in x:
                cp.pixels[i] = (0, 100, 0)

    while cp.switch == True:
        time.sleep(0.15)
        cp.pixels.fill((0, 0, 0))
        if cp.button_a and cp.button_b:

            color("ok")
            r.send("ok")

        elif cp.button_a and not cp.button_b:
            color("up")
            r.send("up")

        elif cp.button_b and not cp.button_a:
            color("down")
            r.send("down")

        pass
    while cp.switch == False:
        time.sleep(0.15)
        cp.pixels.fill((0, 0, 0))
        if cp.button_a and cp.button_b:

            color("ok")
            r.send("ok")

        if cp.button_a:
            color("left")
            r.send("left")

        if cp.button_b:
            color("right")
            r.send("right")

        pass
