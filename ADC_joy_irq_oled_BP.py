from pyb import ADC, Pin
from machine import I2C
from ssd1306 import SSD1306_I2C
from ubinascii import hexlify as hex
from time import sleep

# I2C1 :WeAct Blackpill :B6(SCL), B7(SDA)
# [A0..1] : PA0, PA1
adc0 = ADC('PA0')
adc1 = ADC('PA1')
button = Pin('PA2', Pin.IN)

# button.irq(lambda p:print(p))
button.irq(trigger=Pin.IRQ_FALLING, handler = lambda p:print('pressed.'))

i2c1 = I2C(1, freq=400000)
adrs_disp1 = 0x3c

address = i2c1.scan() # return address list.
for unit in address:
    print(hex(unit.to_bytes(4, 'big')))

display1 = SSD1306_I2C(128, 64, i2c1, addr=adrs_disp1)

def scale_value(value, in_min, in_max, out_min, out_max):
    scaled_value = (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    return int(scaled_value)

while True:
    a = scale_value(adc0.read(), 0, 4096, 0, 128)
    b = scale_value(adc1.read(), 0, 4096, 0, 64)
    c = button.value()

    display1.fill(0)
    display1.rect(int(a), int(b), 3, 3, 1)
    display1.show()

