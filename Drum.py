from PercussionFamily import PercussionFamily

import math


class Drum(PercussionFamily):

    def __init__(self, keys, diameter):
        super().__init__(
            349.50,
            'By hitting the membrane with sticks',
            'Replace the membrane',
            keys,
            "Drum"
        )
        self.diameter = diameter
        self.diameter_in_inch = diameter / 2.54

    def make_sound(self):
        return 'Vibrating stretched membrane'

