import mingus.core.chords as chords
import utils
from mingus.core.scales import Major
from mingus.containers import *
from keyboard import Keyboard
from random import choice, randint
from optparse import OptionParser


parser = OptionParser()
parser.add_option("-c", "--chords", help='chords used in training. Example: "triads sevenths augmented"', default='triads')
parser.add_option("-k", "--key", help='major key to select chords from. Example: "C"', default='C')
(options, args) = parser.parse_args()
keyboard = Keyboard()

while True:
    chord = utils.random_chord(options.key, options.chords.split())

    flat_chord = utils.flatten_notes(NoteContainer(chord))
    while True:
        played_notes = keyboard.next_state()
        if played_notes is None:        
            keyboard.play(NoteContainer(chord))
        else:
            flat_played_notes = utils.flatten_notes(played_notes)
            if flat_chord == flat_played_notes:
                chord_name = chords.determine(chord)[0]
                chord_guess = None
                while chord_guess != chord_name:
                    if chord_guess == 'I give up.':
                        print chord_name
                        break

                    chord_guess = raw_input("Enter the chord name: ")
                
                break
            else:
                print 'played: ',
                print played_notes.determine()
                #print ' ({}) /= ({})'.format('-'.join(str(x) for x in flat_chord), '-'.join(str(x) for x in flat_played_notes))



