#!/usr/bin/python

import mido

inport = mido.open_input()

while True:
    print(inport.receive())
