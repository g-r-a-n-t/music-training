import utils

from keyboard import Keyboard
from musthe import *
from random import choice, randint
from optparse import OptionParser


parser = OptionParser()
parser.add_option("-c", "--chords", help='chords used in training. Example: "maj min dim"', default='maj')
parser.add_option("-r", "--scale-root", help='root to base scale off of. Example: "C"', default='C')
parser.add_option("-s", "--scale-name", help='chords are restricted to this scale. Example: "major"', default='major')
(options, args) = parser.parse_args()

keyboard = Keyboard()
chord_names = options.chords.split();
scale = Scale(Note(options.scale_root), options.scale_name)

while True:
    # generate a chord
    chord = None
    while not utils.chord_in_scale(chord, scale):
        root = choice(scale.notes)
        chord_name = choice(chord_names)
        chord = Chord(root, chord_name)

    print(str(chord))
    # wait till user plays chord
    flattened_chord = utils.flatten_notes(chord.notes)
    while True:
        played_notes = keyboard.next_state()
        if played_notes is None:
            print('wrong')
            #keyboard.play(NoteContainer(chord))
        else:
            flattened_played_notes = utils.flatten_numbers(played_notes)
            if flattened_chord == flattened_played_notes:
                break
