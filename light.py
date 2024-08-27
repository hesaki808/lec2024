
from pyb import Timer, Pin, LED, ADC
from time import sleep

adc0 = ADC('PA3')

while True:
    a = adc0.read()
    
    print("{0}".format(a))
    sleep(0.05)