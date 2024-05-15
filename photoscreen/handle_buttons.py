#!/usr/bin/env python3

from gpiozero import Button
import signal
import os
from appstate import appstate

print("""handle_buttons.py - Detect which button has been pressed

Press Ctrl+C to exit!

""")

# Gpio pins for each button (from top to bottom)
#BUTTONS = [5, 6, 16, 24]

# These correspond to buttons A, B, C and D respectively
#LABELS = ['A', 'B', 'C', 'D']

hold_time = 2
long_press_A = False
long_press_B = False
long_press_C = False
long_press_D = False

def handle_A():
    global long_press_A
    if not long_press_A:
        print('Button A: Next')
        appstate.appstate_next()
    long_press_A = False

def handle_long_press_A():
    global long_press_A
    long_press_A = True
    print('Button A: Long Press')

def handle_B():
    print('Button B: Prev')
    appstate.appstate_prev()

def handle_C():
    print('Button C')

def handle_D():
    print("switch wlan power management off")
    os.system('sudo iw wlan0 set power_save off')
    os.system('sudo ifconfig wlan0 up') 
def handle_long_press_D():
    print("shutdown now.")
    os.system('sudo shutdown now') 


button_A = Button(5, hold_time = hold_time)
button_A.when_released = handle_A
button_A.when_held = handle_long_press_A

buttonB = Button(6)
buttonB.when_pressed = handle_B

buttonC = Button(16)
buttonC.when_pressed = handle_C

buttonD = Button(24, hold_time = hold_time)
buttonD.when_pressed = handle_D
buttonD.when_held = handle_long_press_D

# Finally, since button handlers don't require a "while True" loop,
# we pause the script to prevent it exiting immediately.
signal.pause()
