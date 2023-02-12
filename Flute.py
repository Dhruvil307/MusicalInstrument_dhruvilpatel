from WoodwindFamily import WoodwindFamily


class Flute(WoodwindFamily):

    def __init__(self):
        super().__init__(
            74.99,
            'By blowing into the flute'
        )

    def make_sound(self):
        return 'Guiding a stream of air'
