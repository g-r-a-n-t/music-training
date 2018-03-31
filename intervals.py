#!/usr/bin/python

from random import randint
from random import choice
import sys
import mido

interval_names = ['unison', 'minor 2nd', 'major 2nd', 'minor 3rd', 'major 3rd', 'perfect 4th', 'tritone', 'perfect 5th', 'minor 6th', 'major 6th', 'minor 7th', 'major 7th', 'octave']

major_intervals = [2, 2, 1, 2, 2, 2, 1]

def play_notes(note1, note2):
    outport = mido.open_output()
    message1 = mido.Message('note_on', note=note1)
    message2 = mido.Message('note_on', note=note2)
    outport.send(message1)
    outport.send(message2)

def hear_notes(note1, note2):
    inport = mido.open_input()
    
    current_note = None
    while True:
        message = inport.receive()
        if message.type is 'note_on': 
            if message.velocity is 0:
                current_note = None
            elif current_note is None:
                current_note = message.note
            elif set([note1, note2]) == set([current_note, message.note]):
                return
        elif message.type is 'control_change' and message.value is not 0:
            play_notes(note1, note2)
            inport.receive()
            inport.receive()

def build_scale(key_center, intervals, num_octaves):
    key_root = key_center - 12 * num_octaves

    scale = [key_root]
    for i in range(num_octaves * 2):
        for interval in intervals:
            scale.append(scale[-1] + interval)

    return scale

key_center = int(sys.argv[1])
num_octaves = int(sys.argv[2])
scale = build_scale(key_center, major_intervals, num_octaves)

while True:
    note1 = None
    note2 = None
    while True:
        note1 = choice(scale)
        note2 = choice(scale)
        if abs(note1 - note2) <= 12 and note1 - note2 is not 0:
            break
    
    hear_notes(note1, note2)

    while True:
        half_steps = int(raw_input('half steps: '))
        if abs(note1 - note2) is half_steps:
            print 'correct'
            break


    print interval_names[abs(note1 - note2)]





