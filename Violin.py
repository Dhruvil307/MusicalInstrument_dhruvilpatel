from StringFamily import StringFamily


class Violin(StringFamily):

    def __init__(self, nstrings):
        super().__init__(
            350.00,
            'By resting the violin on shoulder, plucking the strings bow and picking notes with fingers',
            'Replace the broken bridge',
            nstrings
        )

    def make_sound(self):
        return 'Vibrating strings'
