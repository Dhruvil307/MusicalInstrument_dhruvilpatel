from abc import ABC

from MusicalInstrument import MusicalInstrument
from Interfaces import *


class StringFamily(Playable, Repairable, MusicalInstrument):
    def __init__(self, value, htp="", htr="", nstrings=0, name=""):
        super(StringFamily, self).__init__(value)
        self.no_of_strings = nstrings
        self.instrument = name
        self.htp = htp
        self.htr = htr

    def how_to_play(self):
        print("Play method: {}".format(self.htp))

    def how_to_repair(self):
        print("Repair method: {}".format(self.htr))

    def special_features(self):
        print("String count of {} is: {}".format(self.instrument, self.no_of_strings))
