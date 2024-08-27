import pyb, micropython

micropython.alloc_emergency_exception_buf(100)

class Foo(object):
    def __init__(self, timer, led):
        self.led = led
        timer.callback(self.cb)
    def cb(self, tim):
        self.led.toggle()

# LED(1) is PC13.
blue = Foo(pyb.Timer(1, freq=8), pyb.LED(1))