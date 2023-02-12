from PercussionFamily import PercussionFamily


class Xylophone(PercussionFamily):

    def __init__(self, keys):
        super().__init__(
            49.00,
            'By hitting bars with two mallets',
            'Replace the broken keys',
            keys,
            "Xylophone"
        )

    def make_sound(self):
        return 'Through resonators'

