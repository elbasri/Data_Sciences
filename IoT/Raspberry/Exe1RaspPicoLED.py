from machine import Pin
import time

#Waiting until the Pi Pico starts
time.sleep(0.1)
t = 0
print("Hello, Pi Pico! {}".format(t))
led = Pin(5, Pin.OUT)
status = 0
while True:
    if status == 0:
        led.toggle()
        time.sleep(1)
        status = 1
    else:
        led.off()
        time.sleep(1)
        status = 0

#Full project: https://wokwi.com/projects/382085804170382337