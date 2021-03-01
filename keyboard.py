import mido
from musthe import *

class Keyboard:
    def __init__(self):
        self.state = set()
        self.outport = mido.open_output()
        self.inport = mido.open_input()
        self.gaining = True

    def next_state(self):
        for message in self.inport:
            # pedal down
            if message.type is 'control_change' and message.value is 127:
                return None
            elif message.type is 'note_on' or message.type is 'note_off':
                note = message.note
                if message.type is 'note_on':
                    self.state.add(note)
                    self.gaining = True

                elif message.type is 'note_off':
                    old_state = set(self.state)
                    self.gaining = False
                    if note in self.state:
                        self.state.remove(note)
                    return old_state

                elif not self.gaining and note in self.state:
                    self.state.remove(note)

    def play(self, notes):
        for note in notes:
            message = mido.Message('note_on', note=note, velocity=80)
            self.outport.send(message)
            self.inport.receive()
