from abc import ABC, abstractmethod


# Interface Repairable
class Repairable(ABC):
    @abstractmethod
    def how_to_repair(self):
        pass


# Interface PriceProvider
class PriceProvider(ABC):
    @abstractmethod
    def get_price(self):
        pass


# Interface Playable
class Playable(ABC):
    @abstractmethod
    def how_to_play(self):
        pass
