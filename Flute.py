from WoodwindFamily import WoodwindFamily


class Flute(WoodwindFamily):

    def make_sound(self):
        print('Guiding a stream of air')

    def PriceProvider(self):
        return '$', 74.99

    def how_to_play(self):
        print('By blowing into the flute')
