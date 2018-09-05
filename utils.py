def progression_notation(chord, scale):
    if not chord_in_scale(chord, scale):
        return None

    numerals = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']
    string = numerals[scale_index(chord.notes[0], scale)]
    if '7' in str(chord):
        string += '7'

    return string

def scale_index(note, scale):
    return notes_as_numbers(scale.notes).index(note.number % 12 + 12)

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
