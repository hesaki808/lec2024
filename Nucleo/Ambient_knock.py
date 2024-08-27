# https://github.com/AmbientDataInc/ambient-python-lib/blob/master/ambient.py
from pyb import ADC
import network
import time
import gc

import ambient

adc0 = ADC('PA3')

lan = network.LAN()
lan.active(1)
time.sleep(5)
print(lan)

am = ambient.Ambient(81385, "8f443355ef302a67")

while True:
    a = adc0.read()
    r = am.send({'d1': a})
    gc.collect()
    print(a)
    time.sleep(30)