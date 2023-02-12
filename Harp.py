from StringFamily import StringFamily


class Harp(StringFamily):

    def __init__(self, nstrings):
        super().__init__(
            255.00,
            'By strumming the strings and peddling to adjust the string lengths',
            'Replace the broken strings',
            nstrings
        )

    def make_sound(self):
        return 'Vibrating strings'
