#!/usr/bin/env python
"""
Info about our project comes here
"""

__author__ = "Timo Verbist"
__email__ = "timo.verbist@student.kdg.be"
__status__ = "Development"

import time
from gpiozero import Button
from gpiozero.pins.pigpio import PiGPIOFactory

IP = PiGPIOFactory('192.168.0.204')
start_button = Button(pin=14, pin_factory=IP)
stop_button = Button(pin=15, pin_factory=IP)
reset_button = Button(pin=18, pin_factory=IP)


def main():
    print("0")
    start = 0
    chrono = 0
    while True:
        while start_button.value == 1:
            if start_button.value == 0:
                start = time.time() - chrono
            elif reset_button.value == 0:
                start = time.time()
        while stop_button.value == 1:
            chrono = time.time() - start
            print(chrono)
            if stop_button.value == 0:
                print("pauze")


if __name__ == '__main__':  # code to execute if called from command-line
    main()
