from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from bme680 import *
import time

# I2C1 :WeAct Blackpill :B6(SCL), B7(SDA)
# class machine.I2C(id, scl, sda, ferq=400000, timeout=50000)
# I2C.init(scl, sda, *, freq=400000)
i2c1 = I2C(1, freq=400000)

adrs_disp1 = 0x3c
adrs_disp2 = 0x3d

address = i2c1.scan() # return address list.
for unit in address:
    print(hex(unit.to_bytes(4, 'big')))

print([hex(unit.to_bytes(4, 'little')) for unit in address])

bme = BME680_I2C(i2c1)
display1 = SSD1306_I2C(128, 64, i2c1, addr=adrs_disp1)
display2 = SSD1306_I2C(128, 64, i2c1, addr=adrs_disp2)

while True:
    print([bme.temperature, bme.humidity, bme.pressure, bme.gas])
    display1.fill(0)
    display1.text("temp : ", 0, 0)
    display1.text(str(bme.temperature), 56, 0)
    display1.text("humid: ", 0, 8)
    display1.text(str(bme.humidity), 56, 8)
    
    display2.fill(0)
    display2.text("pres: ", 0, 0)
    display2.text(str(bme.temperature), 48, 0)
    display2.text("gas : ", 0, 8)
    display2.text(str(bme.humidity), 48, 8)

    display1.show()
    display2.show()
    time.sleep(1)