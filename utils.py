import mingus.core.chords as chords
import mingus.core.progressions as progressions
from mingus.core.scales import Major
from mingus.containers import *
from keyboard import Keyboard
from random import choice, randint
from optparse import OptionParser

notes = ['C', 'C#', 'Db', 'D', 'D#', 'Eb', 'E', 'E#', 'F', 'F#', 'Gb', 'G', 'G#', 'Ab', 'A', 'A#', 'Bb', 'B#']

suffixes = {}
suffixes['triads'] = ['m', 'M', 'dim']
suffixes['sevenths'] = ['m7', 'M7', '7', 'm7b5', 'dim7', 'm/M7']
suffixes['augmented'] = ['aug', 'M7+5', 'M7+', 'm7+', '7+']
suffixes['suspended'] = ['sus4', 'sus2', 'sus47', 'sus', '11', 'sus4b9']
suffixes['sixths'] = ['6', 'm6', 'M6', '6/7', '6/9']
suffixes['ninths'] = ['9', 'M9', 'm9', '7b9', '7#9']
suffixes['elevenths'] = ['11', '7#11', 'm11']
suffixes['thirteenths'] = ['13', 'M13', 'm13']
suffixes['altered'] = ['7b5', '7b9', '7#9', '67']
suffixes['special'] = ['5', 'NC', 'hendrix']

def chord_in_key(chord, key):
    for note in chord:
        if note not in Major(key).ascending():
            return False

    return True

def random_chord(key, suffix_types):
    root = choice(notes)
    suffix_type = choice(suffix_types)
    suffix = choice(suffixes[suffix_type])
    chord = chords.from_shorthand(root + suffix)
    if chord_in_key(chord, key):    
        return chord
    else:
        return random_chord(key, suffix_types)

def flatten_notes(notes):
   return map(lambda note: int(note) % 12, notes)

def progression_map(key, values):
    chords = progressions.to_chords(values, key)
    pairs = zip(values,chords)
    #TODO: use higher order function
    chord_map = {}
    for pair in pairs:
        chord_map[pair[0]] = pair[1]

    return chord_map

