from abc import ABC

from MusicalInstrument import MusicalInstrument
from Interfaces import *


class StringFamily(Playable, Repairable, MusicalInstrument):
    def __init__(self, value, htp="", htr="", nstrings=0):
        super(StringFamily, self).__init__(value)
        self.no_of_strings = nstrings
        self.htp = htp
        self.htr = htr

    def how_to_play(self):
        print("Play method: {}".format(self.htp))

    def how_to_repair(self):
        print("Repair method: {}".format(self.htr))
