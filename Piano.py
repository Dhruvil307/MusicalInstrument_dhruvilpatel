from StringFamily import StringFamily


class Piano(StringFamily):
    def make_sound(self):
        return 'Vibrating the soundboard'

    def how_to_repair(self):
        return 'Replace the broken strings or keys'

    def PriceProvider(self):
        return '$ 725.00'

    def how_to_play(self):
        return 'By hitting the keys that trigger hammers to hit the strings'
