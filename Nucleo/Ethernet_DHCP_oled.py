from machine import I2C, Pin
from ssd1306 import SSD1306_I2C
from ubinascii import hexlify as hex
import time
# import urequests
# import ujson

import network
lan = network.LAN()
lan.active(1)
time.sleep(5)
print(lan)

# I2C1 :NUCLEO 144 F429ZI :B8(SCL), B9(SDA)
# -> pin 2(B8), Pin 4(B9) on CN7.
# USER button: PC13
button = Pin('PC13', Pin.IN)
button.irq(trigger=Pin.IRQ_FALLING, handler = lambda p:print('pressed.'))

i2c1 = I2C(1, freq=400000)
adrs_disp1 = 0x3d

address = i2c1.scan() # return address list.
for unit in address:
    print(hex(unit.to_bytes(2, 'big')))

display1 = SSD1306_I2C(128, 64, i2c1, addr=adrs_disp1)

while True:
    ipstring = str(lan)
    display1.fill(0)
    display1.rect(0, 0, 128, 11, 1)
    display1.text(ipstring[7:-1], 1, 2)
    display1.show()
    