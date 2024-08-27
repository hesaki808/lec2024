from pyb import ADC, Pin
from time import sleep

# [A0..1] : PA0, PA1
adc0 = ADC('PA0')
adc1 = ADC('PA1')

button = Pin('PA2', Pin.IN)

# button.irq(lambda p:print(p))
button.irq(trigger=Pin.IRQ_FALLING, handler = lambda p:print('pressed.'))

def scale_value(value, in_min, in_max, out_min, out_max):
    scaled_value = (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    return scaled_value

while True:
    a = scale_value(adc0.read(), 0, 4096, 0, 128)
    b = scale_value(adc1.read(), 0, 4096, 0, 64)
    c = button.value()

    print("{0},{1},{2}".format(a, b, c))
    if b > 3000:
        print('up')
    elif b < 1000:
        print('down')
    if a > 3000:
        print('right')
    elif a < 1000:
        print('left')
        
    if (1500 < a < 2500) and (1500 < b < 2500):
        print('nt')

    sleep(0.5)

