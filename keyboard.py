import mido
from musthe import *

class Keyboard:
    def __init__(self):
        self.state = set()
        self.outport = mido.open_output()
        self.inport = mido.open_input()

    def next_state(self):
        for message in self.inport:
            # pedal down
            if message.type is 'control_change' and message.value is 127:
                return None

            elif message.type is 'note_on':
                note = message.note
                if message.velocity is not 0:
                    self.state.add(note)
                    self.gaining = True

            elif self.gaining:
                old_state = set(self.state)
                self.gaining = False
                if note in self.state:
                    self.state.remove(note)
                return old_state

            elif not self.gaining and note in self.state:
                self.state.remove(note)

    def play(self, notes):
        for note in notes:
            message = mido.Message('note_on', note=note, velocity=50)
            self.outport.send(message)
            self.inport.receive()
