from PercussionFamily import PercussionFamily
from StringFamily import StringFamily


class Piano(StringFamily, PercussionFamily):

    def __init__(self, keys, nstrings):
        super(Piano, self).__init__(
            725.00,
            'By hitting the keys that trigger hammers to hit the strings',
            'Replace the broken strings or keys',
            nstrings
        )
        super(Piano, self).__init__(
            725.00,
            'By hitting the keys that trigger hammers to hit the strings',
            'Replace the broken strings or keys',
            keys
        )

    def make_sound(self):
        return 'Vibrating the soundboard'
