#!/usr/bin/python

import utils
import time

from keyboard import Keyboard
from musthe import *
from random import choice, randint
from optparse import OptionParser


parser = OptionParser()
parser.add_option("-t", "--two-hands", help='checks if the chord was played in both hands', action='store_true', default=False)
(options, args) = parser.parse_args()

keyboard = Keyboard()
curr_key = None
curr_three = []
play_history = []

def hint():
    print(curr_key, end=" | ")
    for chord in curr_three:
        print(utils.progression_notation(chord, curr_key), end = "-")
        
    print("")

def check():
    if len(play_history) < 3:
        return False

    for i, played_notes in enumerate(play_history[-3:]):
        played_counts = utils.numbers_as_counts(played_notes)
        expected_set = set(utils.notes_as_counts(curr_three[i].notes))

        if set(played_counts) != expected_set:
            return False

        if options.two_hands and not all(count == 2 for count in played_counts.values()):
            return False

    return True


while True:
    # set key
    notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
    key_type = ["major", "natural_minor"]
    curr_key = Scale(Note(choice(notes)), choice(key_type))

    # generate a chords
    curr_three = []
    while not len(curr_three) is 3:
        chord_root = choice(curr_key) - Interval('P8')
        chord_names = ["maj", "min", "aug", "dim", "dom7", "min7", "maj7", "aug7", "m7dim5"]
        chord = Chord(chord_root, choice(chord_names))
        if utils.chord_in_scale(chord, curr_key):
            curr_three.append(chord)

    # wait till user plays all three chords
    print('new progression (press pedal for hint)')
    start_time = 0 # track time it took to play
    while True:
        played_notes = keyboard.next_state()
        if played_notes is None: # pedal
            if start_time == 0:
                start_time = time.time()
            hint()
        else: # keys played
            play_history.append(played_notes)
            if check():
                print("time: {}s".format(time.time() - start_time))
                break

