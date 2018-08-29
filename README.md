# Music Training

This repository contains practical exercises in music theory and ear training. You will need a [midi keyboard](http://m-audio.com/products/view/keystation-49) and [pedal](http://m-audio.com/products/view/sp-2) configured with your system along with an inter-application audio routing service, like [Jack Audio Connection Kit](http://jackaudio.org/). The python libraries [mido](https://github.com/olemb/mido), [python-rtmidi](https://pypi.org/project/python-rtmidi/), and [musthe](https://github.com/gciruelos/musthe) must be installed to run these scripts. This is developed for Python 3.

## Chords
The chords script will challenge you to play a randomly generated chord
within a given key. When you have played the chord correctly, it will generate another. Chord types are limited to what is passed in under the "chords" option.
To receive a hint for the chord you are trying to play, press the pedal. Depending on your options, this will either print the shorthand representation or play the chord through your configured audio output, or both. You don't need to play the chord in any specific way, it can be inverted or in a different octave. If you would like, you can set the "two hands" flag, which will require you two play each chord in both hands.
```sh
$ ./chords.py -h
Usage: chords.py [options]

Options:
  -h, --help            show this help message and exit
  -c CHORDS, --chords=CHORDS
                        chords used in training. Example: "maj min dim"
  -s SCALE_NAME, --scale-name=SCALE_NAME
                        scale to base chord selection off of. Example: "major"
  -r SCALE_ROOT, --scale-root=SCALE_ROOT
                        root to base scale off of. Example: "C"
  -w, --written-hint    prints the name of the chord you are tasked with
                        playing
  -a, --audible-hint    audibly plays the chord you are tasked with playing
  -t, --two-hands       checks if the chord was played in both hands
```

### Available parameters:
- chords: *maj, min, aug, dim, dom7, min7, maj7, aug7, m7dim5*
- scales: *major, natural_minor, harmonic_minor, melodic_minor, major_pentatonic, minor_pentatonic*
- roots: *any note*

### Example usage:
```sh
$ ./chords.py --scale-name major --scale-root E --written-hint --audible-hint --two-hands --chords "maj min"
new chord (press pedal for hint)
Bmaj
time: 4.741794109344482s
new chord (press pedal for hint)
Amaj
time: 3.338390588760376s
new chord (press pedal for hint)
F#min
time: 5.929013013839722s
new chord (press pedal for hint)
...
```
## Intervals
The intervals script will challenge you to play a randomly generated interval. When you have played the interval correctly, it will generate another. Intervals are limited to what is passed in under the "intervals" option. To receive a hint for the interval you are trying to play, press the pedal. Depending on your options, this will either print the shorthand representation or play the interval through your configured audio output. If you would like, you can set the "two hands" flag, which will require you two play each interval in both hands.
```sh
$ ./intervals.py -h
Usage: intervals.py [options]

Options:
  -h, --help            show this help message and exit
  -c INTERVALS, --intervals=INTERVALS
                        intervals used in training. Example: "M2 P5"
  -r INTERVAL_ROOT, --interval-root=INTERVAL_ROOT
                        root to base intervals off of. Example: "C"
  -w, --written-hint    prints the name of the interval you are tasked with
                        playing
  -a, --audible-hint    audibly plays the interval you are tasked with playing
  -t, --two-hands       checks if the interval was played in both hands

```
### Available parameters:
- intervals: *P1, m2, M2, m3, M3, P4, A4, P5, m6, M6, m7, M7, P8*
- roots: *any note*

### Example usage:
add this
