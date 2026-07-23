import machine, time
from machine import Pin
from hcsr04 import HCSR04

trigger_pin = 15
echo_pin = 0

sensor = HCSR04(trigger_pin, echo_pin)

distance = sensor.distance_cm()

while distance:
    # Implement a PIR sensor since it draws very little current to wake the trigger Pin
    pass