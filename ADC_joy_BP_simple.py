from pyb import ADC, Pin
from time import sleep

# [A0..1] : PA0, PA1
adc0 = ADC('PA0')
adc1 = ADC('PA1')

while True:
    a = adc0.read()
    b = adc1.read()

    print("{0},{1}".format(a, b))
    sleep(0.5)

