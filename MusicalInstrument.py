from abc import ABC, abstractmethod
from Interfaces import Repairable, PriceProvider, Playable


# Abstract Class
class MusicalInstrument(PriceProvider):

    def __init__(self, value):
        self.value = value

    @abstractmethod
    def make_sound(self):
        pass

    def get_price(self):
        print("The price: ${}".format(self.value))
