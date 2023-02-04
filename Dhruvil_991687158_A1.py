# Name: DHRUVIL PATEL
# Username: PATE4456
# Student Id: 991687158
# Course: PROG23199
# Assignment: Assignment #1
# Date: January 26, 2023
# Program: assignment1_dhruvil_patel.py
# Instructor’s name: Syed Tanbeer


from dataclasses import dataclass
from abc import ABC, abstractmethod
import math


class MusicalInstrument(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Repairable(ABC):
    def how_to_repair(self):
        pass


class PriceProvider(ABC):
    def get_price(self):
        pass


class Playable(ABC):
    def how_to_play(self):
        pass


class StringFamily(MusicalInstrument):
    super().__init__(ABC)

    def __init__(self, Harp, Violin, Piano) -> None:
        super().__init__()
        self.Harp = Harp
        self.Violin = Violin
        self.Piano = Piano


class Harp(StringFamily):
    super().__init__(Harp=str)


class Violin(StringFamily):
    super().__init__(Violin=str)


class Piano(StringFamily):
    super().__init__(Piano=str)


class PercussionFamily(MusicalInstrument):
    super().__init__(Piano)

    def __init__(self, Xylophone, Drum) -> None:
        self.Xylophone = Xylophone
        self.Drum = Drum


class Xylophone(PercussionFamily):
    super().__init__(Xylophone=str)


class Drum(PercussionFamily):
    super().__init__(Drum=str)

    def diameter_in_inch(self, radius, diameter):
        self.radius = radius
        self.diameter = diameter
        return self.diameter == 2 * math.pi * self.radius


class WoodwindFamily(MusicalInstrument):

    def __init__(self, Flute):
        self.Flute = Flute


class Order:

    def __init__(self, o_id, customer_name, orders) -> None:
        self.o_id = o_id
        self.customer_name = customer_name
        self.orders = orders

    def add_instrument(self, instrument):
        self.instrument = instrument


order_Bob = Order(111, "Bob")  # id of the order = 111 and customer name = Bob
order_Alice = Order(222, "Alice")  # id of the order = 222 and customer name = Alice

# abstract class containing abstract method @abstractmethod
# def make_sound():subclass all instruments from all the classes
