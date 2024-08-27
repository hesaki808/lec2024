from pyb import ADC
from time import sleep

# in WeACT Blackpill, 
# [A0..3] : PA0, PA1, PA2
adc0 = ADC('PA0')
adc1 = ADC('PA1')
adc2 = ADC('PA2')
adc3 = ADC('PA3')
adc4 = ADC('PA4')
adc5 = ADC('PA5')
adc6 = ADC('PA6')
adc7 = ADC('PA7')

adc8 = ADC('PB0')
adc9 = ADC('PB1')

while True:
    a = adc0.read()
    b = adc1.read()
    c = adc2.read()
    d = adc3.read()
    e = adc4.read()
    f = adc5.read()
    g = adc6.read()
    h = adc7.read()
    i = adc8.read()
    j = adc9.read()

    print("{0},{1},{2},{3},{4},{5},{6},{7},{8},{9}".format(a, b, c, d, e, f, g, h, i, j))
    sleep(0.5)
