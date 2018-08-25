from keyboard import Keyboard
from musthe import *
from random import choice, randint
from optparse import OptionParser

def chord_in_scale(chord, scale):
    if chord is None:
        return False

    chord_set = set(notes_as_counts(chord.notes))
    scale_set = set(notes_as_counts(scale.notes))
    return chord_set.issubset(scale_set)

def notes_as_numbers(notes):
    numbers = []
    for note in notes:
        numbers.append(note.midi_note())

    return numbers

def numbers_as_counts(numbers):
    counts = {}
    for number in numbers:
        octave_number = number % 12
        if octave_number in counts:
            counts[octave_number] += 1
        else:
            counts[octave_number] = 1

    return counts

def notes_as_counts(notes):
    return numbers_as_counts(notes_as_numbers(notes))
