from abc import ABC, abstractmethod
from Interfaces import Repairable, PriceProvider, Playable


# Abstract Class
class MusicalInstrument(Repairable, PriceProvider, Playable, ABC):
    @abstractmethod
    def make_sound(self):
        pass

    def how_to_repair(self):
        pass

    def get_price(self):
        pass

    def how_to_play(self):
        pass
