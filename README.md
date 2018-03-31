# Music Training

This repository contains exercises in music theory and ear training. Best used with a midi keyboard and pedal.

example usage:
```sh
python chords.py --key C --chords "triads sevenths" # play triads and sevenths in the key of C major
# pedal is struck to play a chord through audio output. In this case it's A minor
played:  ['G'] # a single key is pressed
played:  ['A'] # a sing key is pressed
# corrected chord is played and user is prompted to enter its name
Enter the chord name: D minor triad # incorrect answer given
Enter the chord name: A minor triad # correct answer is given
# next chord is played
```
