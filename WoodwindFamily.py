from abc import ABC

from MusicalInstrument import MusicalInstrument


class WoodwindFamily(MusicalInstrument, ABC):

    def __init__(self, Flute):
        self.Flute = Flute
