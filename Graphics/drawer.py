# importing image object from PIL
import math
from PIL import Image, ImageDraw

WITH = 2000
HIGHT = 120
INTERVAL = 25
DUTYCYCLE = 1/4
xPos = 10

ONTIME   =   600
ZEROTIME =   600
ONETIME  =   1650


# creating new Image object
img = Image.new("RGB", (WITH, HIGHT))

# create rectangle image
img1 = ImageDraw.Draw(img)

def pwm(cycles):
    global xPos
    for i in range(cycles):
        img1.line((xPos, HIGHT-10, xPos, 10))
        img1.line((xPos, 10, xPos+INTERVAL*DUTYCYCLE, 10))
        xPos += INTERVAL*DUTYCYCLE
        img1.line((xPos, HIGHT-10, xPos, 10))
        img1.line((xPos, HIGHT-10, xPos+INTERVAL*(1-DUTYCYCLE), HIGHT-10))
        xPos += INTERVAL*(1-DUTYCYCLE)

def one():
    global xPos
    pwm(24)
    img1.line((xPos,HIGHT-10,xPos+ONETIME,HIGHT-10))
one()
img.show()
