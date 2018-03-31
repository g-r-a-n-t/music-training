#!/usr/bin/python
from random import randint

import mido


interval_names = ['unison', 'minor 2nd', 'major 2nd', 'minor 3rd', 'major 3rd', 'perfect 4th', 'tritone', 'perfect 5th', 'minor 6th', 'major 6th', 'minor 7th', 'major 7th', 'octave']

def play_note(value):
	outport = mido.open_output()
	message = mido.Message('note_on', note=value)
	outport.send(message)

def hear_note():
	inport = mido.open_input()
	while True:
		message = inport.receive()
		if message.type is 'note_on' and message.velocity is not 0:
			return message.note
		elif message.type is 'control_change' and message.value is not 0:
			return None

def random_note(last):
	num_intervals = len(interval_names) - 1
	if last < 50:
		return last + randint(0, num_intervals)
	elif 70 < last:
		return last - randint(0, num_intervals)
	else:
		return last + randint(num_intervals * -1, num_intervals)

last_note = 60
while True:
	curr_note = random_note(last_note)
	while True:	
		played_note = hear_note()
		if played_note is curr_note:
			break
		elif played_note is None:
			play_note(curr_note)
		
	print interval_names[abs(last_note - curr_note)]
	last_note = curr_note




