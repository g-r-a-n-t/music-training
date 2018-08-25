import utils

from keyboard import Keyboard
from musthe import *
from random import choice, randint
from optparse import OptionParser


parser = OptionParser()
parser.add_option("-c", "--chords", help='chords used in training. Example: "maj min dim"', default='maj')
parser.add_option("-s", "--scale-name", help='scale to base chord selection off of. Example: "major"', default='major')
parser.add_option("-r", "--scale-root", help='root to base scale off of. Example: "C"', default='C')
parser.add_option("-w", "--written-hint", help='prints the name of the chord you are tasked with playing', action='store_true', default=False)
parser.add_option("-a", "--audible-hint", help='audibly plays the chord you are tasked with guessing', action='store_true', default=False)
parser.add_option("-t", "--two-hands", help='checks if the chord was played in both hands', action='store_true', default=False)
(options, args) = parser.parse_args()

keyboard = Keyboard()
chord_names = options.chords.split();
scale = Scale(Note(options.scale_root), options.scale_name)

def hint(chord):
    if options.written_hint:
        print(str(chord))
    if options.audible_hint:
        keyboard.play(utils.notes_as_numbers(chord.notes))

def check(played_notes, expected_chord):
    played_counts = utils.numbers_as_counts(played_notes)
    expected_set = set(utils.notes_as_counts(expected_chord.notes))

    if set(played_counts) != expected_set:
        return False

    if options.two_hands and not all(count == 2 for count in played_counts.values()):
        return False

    return True


while True:
    # generate a chord
    chord = None
    while not utils.chord_in_scale(chord, scale):
        chord_root = choice(scale)
        chord_name = choice(chord_names)
        chord = Chord(chord_root, chord_name)

    # wait till user plays chord
    print('new chord (press pedal for hint)')
    while True:
        played_notes = keyboard.next_state()
        if played_notes is None:
            hint(chord)
        else:
            if check(played_notes, chord):
                break
