from machine import Pin
import utime

IN1 = Pin('PA0', Pin.OUT)
IN2 = Pin('PA1', Pin.OUT)
IN3 = Pin('PA2', Pin.OUT)
IN4 = Pin('PA3', Pin.OUT)
pins = [IN1,IN2,IN3,IN4]

setup = [0,0,0,0]
step1 =[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
step1_reverse =[[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]]

wait_ms = 2
step2 = [[1,0,0,1],[1,1,0,0],[0,1,1,0],[0,0,1,1]]

step3 = [[1,0,0,1],[1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],[0,0,1,0],[0,0,1,1],[0,0,0,1]]

for i in range(4):
    pins[i].value(setup[i])
utime.sleep_ms(wait_ms)    
print("")
print("Rotate.")
while True:
    for step in reversed(step3):
        for i in range(4):
            pins[i].value(step[i])
        utime.sleep_ms(wait_ms)