from abc import ABC

from MusicalInstrument import MusicalInstrument
from Interfaces import *
import math


class PercussionFamily(Playable, Repairable, MusicalInstrument):

    def __init__(self, value, htp="", htr="", keys=0, name=""):
        super(PercussionFamily, self).__init__(value)
        self.instrument = name
        self.no_of_keys = keys
        self.htp = htp
        self.htr = htr

    def how_to_play(self):
        print("Play method: {}".format(self.htp))

    def how_to_repair(self):
        print("Repair method: {}".format(self.htr))

    def special_features(self):
        print("Key count of {} is: {}".format(self.instrument, self.no_of_keys))