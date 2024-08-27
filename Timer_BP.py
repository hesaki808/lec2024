# LED 1..3 : Green, Blue, Red : B0, B7, B14
from pyb import Timer, Pin, LED
from math import sin, cos, pi
from time import sleep

tim1 = Timer(4, freq = 24)
tim1.callback(lambda t:LED(1).toggle())

while True:
    for i in range(0,360):
        x = sin(pi * 2 * i / 120)
        y = cos(pi * 2 * i / 120)
        print("{0},{1}".format(x, y))
        sleep(0.05)
