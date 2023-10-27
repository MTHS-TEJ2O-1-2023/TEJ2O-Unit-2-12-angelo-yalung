"""
Created by: Angelo Yalung
Created on: Oct 2023
This module is a Micro:bit MicroPython program
"""

from microbit import *
from hcsr04 import HCSR04
import machine
import neopixel


# variables
sensor = HCSR04(trigger_pin=1, echo_pin=2)
np = neopixel.NeoPixel(machine.Pin(4), 4)
distance = sensor.distance_cm()


# start up
display.show(Image.HAPPY)


# if distance is greater than or equal to 10
while True:
    if button_a.is_pressed():
        if distance >= 10:
            np[0] = (0, 255, 0)
            np[1] = (0, 255, 0)
            np[2] = (0, 255, 0)
            np[3] = (0, 255, 0)
            print("Distance:", distance, "cm")
        else:
            np[0] = (255, 0, 0)
            np[1] = (255, 0, 0)
            np[2] = (255, 0, 0)
            np[3] = (255, 0, 0)
            print("Distance:", distance, "cm")
