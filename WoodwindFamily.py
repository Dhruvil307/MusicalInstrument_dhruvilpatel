from MusicalInstrument import MusicalInstrument
from Interfaces import *


class WoodwindFamily(Playable, MusicalInstrument):
    def __init__(self, value, htp):
        super().__init__(value)
        self.made_of = "made of wood"
        self.htp = htp

    def how_to_play(self):
        print("Play method: {}".format(self.htp))
