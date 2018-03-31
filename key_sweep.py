#!/usr/bin/python

from random import randint
import sys
import mido

interval_names = ['unison', 'minor 2nd', 'major 2nd', 'minor 3rd', 'major 3rd', 'perfect 4th', 'tritone', 'perfect 5th', 'minor 6th', 'major 6th', 'minor 7th', 'major 7th', 'octave']

major_intervals = [2, 2, 1, 2, 2, 2, 1]

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

def build_scale(key_center, intervals, num_octaves):
	key_root = key_center - 12 * num_octaves
	
	scale = [key_root]
	for i in range(num_octaves * 2):
		for interval in intervals:
			scale.append(scale[-1] + interval)

	return scale



key_center = int(sys.argv[1])
num_octaves = int(sys.argv[2])
scale = build_scale(key_center, major_intervals, num_octaves)

last_index = num_octaves * 8 - 1
last_note = scale[last_index] 
while True:
	current_index = randint(max(0, last_index - 8), min(len(scale) - 1, last_index + 8) - 1)
	current_note = scale[current_index]
	while True:
		played_note = hear_note()
		if played_note is None:
			play_note(current_note)
		elif played_note is current_note:
			break

	print interval_names[abs(current_note - last_note)]

	last_index = current_index
	last_note = scale[last_index]







