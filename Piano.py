from PercussionFamily import PercussionFamily
from StringFamily import StringFamily


class Piano(StringFamily, PercussionFamily):

    def __init__(self, keys, nstrings):
        StringFamily.__init__(
            self,
            725.00,
            'By hitting the keys that trigger hammers to hit the strings',
            'Replace the broken strings or keys',
            nstrings,
            "Piano"
        )
        PercussionFamily.__init__(
            self,
            725.00,
            'By hitting the keys that trigger hammers to hit the strings',
            'Replace the broken strings or keys',
            keys,
            "Piano"
        )

    def make_sound(self):
        return 'Vibrating the soundboard'

    def special_features(self):
        super().special_features()
        PercussionFamily.special_features(self)
