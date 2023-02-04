from PercussionFamily import PercussionFamily

import math


class Drum(PercussionFamily):

    def __init__(self, radius, diameter):
        super().__init__(Drum)
        self.diameter = diameter
        self.radius = radius

    def make_sound(self):
        print('Vibrating stretched membrane')

    def how_to_repair(self):
        print('Replace the membrane')

    def get_price(self):
        return '$', 349.50

    def how_to_play(self):
        print('By hitting the membrane with sticks')

    def diameter_in_inch(self):
        return self.diameter / 2.54
