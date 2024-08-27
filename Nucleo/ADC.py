from pyb import ADC
from time import sleep

# [A0..3] : PA3, PC0, PC3
adc0 = ADC('PA3')
adc1 = ADC('PC0')
adc2 = ADC('PC3')

while True:
    a = adc0.read()
    b = adc1.read()
    c = adc2.read()

    print("{0},{1},{2}".format(a, b, c))
    sleep(0.5)
