#!/bin/python3

# Import Python required modules for Frankenstein.

import os
import random
import RPi.GPIO as GPIO
import sys
import time

# Setup the GPIO Pin numbers.

GPIO.setmode(GPIO.BCM)
BUTTON = 22
BUZZ = 19
TOUCH = 4
REED = 16
GRELED = 21
REDLED = 13
GPIO.setup(BUTTON, GPIO.IN)
GPIO.setup(BUZZ, GPIO.OUT)
GPIO.setup(REED, GPIO.IN)
GPIO.setup(TOUCH, GPIO.IN)
GPIO.setup(GRELED, GPIO.OUT)
GPIO.setup(REDLED, GPIO.OUT)

# Print an introduction message of the game.

os.system('clear')
print()
print("ReACTION - How fast can you be?")
print()
print("[Single Player Mode]")
print()

# Define the Start function which waits
# for a magnet to be detected before beginning
# the reaction game, followed by instructions.

def start():
    try:
        PLAYERS = 1
        print("Start a new Single Player game with magnet.")
        print("Click the button to select Two Player Versus.")
        print()
        print("*Press ctrl+c to end the game*")
        print()
        while 1:
            REEDVAL = GPIO.input(REED)
            BUTTONV = GPIO.input(BUTTON)
            if (BUTTONV == 0) and (PLAYERS == 1):
                os.system('clear')
                print()
                print("ReACTION - How fast can you be?")
                print("*Press ctrl+c to end the game*")
                print()
                print("---> Two Player Versus <---")
                print()
                print("Click the button to change player mode.")
                print()
                print("Start New Game with Magnet")
                print()
                PLAYERS = 2
                time.sleep(1)
            elif (BUTTONV == 0) and (PLAYERS == 2):
                os.system('clear')
                print()
                print("ReACTION - How fast can you be?")
                print("*Press ctrl+c to end the game*")
                print()
                print("---> Single Player <---")
                print()
                print("Click the button to change player mode.")
                print()
                print("Start New Game with Magnet")
                print()
                PLAYERS = 1
                time.sleep(1)
            elif (REEDVAL == 0):
                print("Magnet Detected, Game Starting")
                print("------------------------------")
                print("Touch the Sensor when Buzzer")
                print("Sounds and the Red Light Shows!")
                print()
                game(PLAYERS)
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

def game(player_number):
    os.system('clear')
    print("The number of Players Selected:",player_number)
    print()
    print("Get ready, Player 1!")
    sequence=[3,4,5,6,7,8,9]
    TIMLIM = random.choice(sequence)
    GPIO.output(GRELED, GPIO.HIGH)
    time.sleep(TIMLIM)
    if (player_number == 1):
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
    elif (player_number == 2):
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
                    PLAY1VAL = REAEND - REASTA
                    print("Player 1, your reaction time is")
                    print(PLAY1VAL,"seconds.")
                    print()
                    TIMLIM = random.choice(sequence)
                    time.sleep(3)
                    GPIO.output(GRELED, GPIO.HIGH)
                    print("Get ready, Player 2!")
                    print()
                    time.sleep(TIMLIM)
                    break
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
                    PLAY2VAL = REAEND - REASTA
                    print("Player 2, your reaction time is")
                    print(PLAY2VAL,"seconds.")
                    print()
                    time.sleep(2)
                    if (PLAY1VAL < PLAY2VAL):
                        os.system('clear')
                        print()
                        print("Player 1 ReACTION time:",PLAY1VAL)
                        print("Player 2 ReACTION time:",PLAY2VAL)
                        print()
                        print("----> Player 1 Has a Faster ReACTION! <----")
                        print()
                        start()
                    elif (PLAY2VAL < PLAY1VAL):
                        os.system('clear')
                        print()
                        print("Player 1 ReACTION time:",PLAY1VAL)
                        print("Player 2 ReACTION time:",PLAY2VAL)
                        print()
                        print("----> Player 2 Has a Faster ReACTION! <----")
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
