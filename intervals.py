#!/usr/bin/python

import utils
import time

from keyboard import Keyboard
from musthe import *
from random import choice, randint
from optparse import OptionParser


parser = OptionParser()
parser.add_option("-c", "--intervals", help='intervals used in training. Example: "M2 P5"', default='M2 P5')
parser.add_option("-r", "--interval-root", help='root to base intervals off of. Example: "C"', default='C')
parser.add_option("-w", "--written-hint", help='prints the name of the interval you are tasked with playing', action='store_true', default=False)
parser.add_option("-a", "--audible-hint", help='audibly plays the interval you are tasked with playing', action='store_true', default=False)
parser.add_option("-t", "--two-hands", help='checks if the interval was played in both hands', action='store_true', default=False)
(options, args) = parser.parse_args()

keyboard = Keyboard()
intervals = options.intervals.split();
interval_root = Note(options.interval_root)

def hint(interval):
    if options.written_hint:
        print(str(interval))
    if options.audible_hint:
        keyboard.play(utils.notes_as_numbers([interval_root, interval_root + interval]))

def check(played_notes, interval):
    played_counts = utils.numbers_as_counts(played_notes)
    expected_set = set(utils.notes_as_counts([interval_root, interval_root + interval]))

    if set(played_counts) != expected_set:
        return False

    if options.two_hands and not all(count == 2 for count in played_counts.values()):
        return False

    return True


while True:
    # pick an interval
    interval = Interval(choice(intervals))

    # wait till user plays chord
    print('new interval (press pedal for hint)')
    start_time = 0 # track time it took to play
    while True:
        played_notes = keyboard.next_state()
        if played_notes is None: # pedal
            if start_time == 0:
                start_time = time.time()
            hint(interval)
        else: # keys played
            if check(played_notes, interval):
                print("time: {}s".format(time.time() - start_time))
                break
