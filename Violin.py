from StringFamily import StringFamily


class Violin(StringFamily):
    def make_sound(self):
        print('Vibrating strings')

    def how_to_repair(self):
        print('Replace the broken bridge')

    def PriceProvider(self):
        return '$', 350.00

    def how_to_play(self):
        print('By resting the violin on shoulder, plucking the strings bow and picking notes with fingers')
