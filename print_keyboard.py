#!/usr/bin/python

from keyboard import Keyboard

keyboard = Keyboard()
while True:
    print(keyboard.next_state())
