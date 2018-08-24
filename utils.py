from keyboard import Keyboard
from musthe import *
from random import choice, randint
from optparse import OptionParser

def chord_in_scale(chord, scale):
    if chord is None:
        return False

    return flatten_notes(chord.notes).issubset(flatten_notes(scale.notes))

def flatten_notes(notes):
    return set(map(lambda note: note.number % 12, notes))


def flatten_numbers(numbers):
    return set(map(lambda number: number % 12, numbers))
