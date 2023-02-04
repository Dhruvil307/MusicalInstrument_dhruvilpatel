from StringFamily import StringFamily


class Harp(StringFamily):
    def make_sound(self):
        print('Vibrating strings')

    def how_to_repair(self):
        print('Replace the broken strings')

    def PriceProvider(self):
        return '$', 255.00

    def how_to_play(self):
        print('By strumming the strings and peddling to adjust the string lengths'
              )
