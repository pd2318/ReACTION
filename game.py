#!/bin/python3

# Import Python required modules for Frankenstein.

import RPi.GPIO as GPIO
import time
import random
import sys

# Setup the GPIO Pin numbers.

GPIO.setmode(GPIO.BCM)
TOUCH = 4
REED = 16
REDLED = 13
GRELED = 21
BUZZ = 19
GPIO.setup(TOUCH, GPIO.IN)
GPIO.setup(REED, GPIO.IN)
GPIO.setup(REDLED, GPIO.OUT)
GPIO.setup(GRELED, GPIO.OUT)
GPIO.setup(BUZZ, GPIO.OUT)

# Print an introduction message of the game.

print()
print("ReACTION - How fast can you be?")
print("[Press ctrl+c to end the game]")
print()

# Define the Start function which waits
# for a magnet to be detected before beginning
# the reaction game, followed by instructions.

def start():
    try:
        print("Start New Game with Magnet")
        print()
        while 1:
            RawValue = GPIO.input(REED)
            if (RawValue == 0):
                print("Magnet Detected, Game Starting")
                print("------------------------------")
                print("Touch the Sensor when Buzzer")
                print("Sounds and the Red Light Shows!")
                print()
                game()
            else:
                time.sleep(0.1)
# The Except clause of Start to exit the loop upon pressing Ctrl-C.
    except KeyboardInterrupt:
        pass
        print()
        print("Exiting ReACTION")
        print("---Thank you!---")
        GPIO.output(GRELED, GPIO.LOW)
        GPIO.output(REDLED, GPIO.LOW)
        GPIO.output(BUZZ, GPIO.LOW)
        GPIO.cleanup()
        sys.exit()

# Defines the Game function where a random
# number from a defined list is selected as
# the amount of time for the reaction game.

def game():
    sequence=[3,4,5,6,7,8,9]
    TIMLIM = random.choice(sequence)
    GPIO.output(GRELED, GPIO.HIGH)
    time.sleep(TIMLIM)
    REASTA = time.perf_counter()
    try:
# Waits for the player to touch the sensor after
# lighting the Red LED and sounding buzzer.
        print("Touch Now!")
        print()
        while 1:
            GameValue = GPIO.input(TOUCH)
            if (GameValue == 0):
                GPIO.output(REDLED, GPIO.HIGH)
                GPIO.output(BUZZ, GPIO.HIGH)
# After player touches the sensor, turn off the
# LEDs and buzzer, and print their reaction time.
            else:
                REAEND = time.perf_counter()
                GPIO.output(REDLED, GPIO.LOW)
                GPIO.output(GRELED, GPIO.LOW)
                GPIO.output(BUZZ, GPIO.LOW)
                REATIM = REAEND - REASTA
                print("Your reaction time is")
                print(REATIM,"seconds.")
                print()
                start()
# The Except clause of Game to exit the loop upon pressing Ctrl-C.
    except KeyboardInterrupt:
        print()
        print("Exiting ReACTION")
        print("---Thank you!---")
        GPIO.output(GRELED, GPIO.LOW)
        GPIO.output(REDLED, GPIO.LOW)
        GPIO.output(BUZZ, GPIO.LOW)
        GPIO.cleanup()
        sys.exit()

start()
