#!/usr/bin/python

import mido
from mingus.containers import *

class Keyboard:
	def __init__(self):
		self.state = NoteContainer()
		self.outport = mido.open_output()
		self.inport = mido.open_input()

	def next_state(self):
		for message in self.inport:
			if message.type is 'control_change' and message.value is 127:
				self.state = NoteContainer()
                                return None

			elif message.type is 'note_on':
				note = Note(message.note)
				if message.velocity is not 0:
					self.state.add_note(note)
					self.gaining = True

				elif self.gaining:
					old_state = NoteContainer(self.state)
					self.gaining = False
					self.state.remove_note(note)
					return old_state

				elif not self.gaining:
					self.state.remove_note(note)
		
	def play(self, notes):
		for note in notes:
			message = mido.Message('note_on', note=int(note), velocity=64)
			self.outport.send(message)
			self.inport.receive()
"""
keyboard = Keyboard()
while True:
	print keyboard.next_state()
"""
