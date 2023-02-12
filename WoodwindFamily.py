from MusicalInstrument import MusicalInstrument
from Interfaces import *


class WoodwindFamily(Playable, MusicalInstrument):
    def __init__(self, value, htp, name):
        super().__init__(value)
        self.instrument = name
        self.made_of = "made of wood"
        self.htp = htp

    def how_to_play(self):
        print("Play method: {}".format(self.htp))

    def special_features(self):
        print("{} is: {}".format(self.instrument, self.made_of))
