from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time

# I2C1 :WeAct Blackpill :B6(SCL), B7(SDA)
# class machine.I2C(id, scl, sda, ferq=400000, timeout=50000)
# I2C.init(scl, sda, *, freq=400000)
i2c1 = I2C(1, freq=400000)

address = i2c1.scan() # return address list.
for unit in address:
    print(hex(unit))

display1 = SSD1306_I2C(128, 64, i2c1, addr=0x3c)


display1.fill(1)

display1.show()

time.sleep(1)
display1.fill(0)

display1.show()


display1.text("connecting..", 0, 0)
display1.show()


