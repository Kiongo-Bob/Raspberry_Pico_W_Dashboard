import time
from machine import Pin
from hcsr04 import HCSR04

trigger_pin = 15
echo_pin = 14

trig_status =  Pin(16, Pin.IN, Pin.PULL_DOWN) # Check the status of the trigger pin

sensor = HCSR04(trigger_pin, echo_pin)

while true:
    try:
        distance = sensor.distance_cm() # reads distance in every iteration
        print(f'{:.2f} cm'.format(distance))
    except OSError as e:
        print("Echo pin input not received: ", e)