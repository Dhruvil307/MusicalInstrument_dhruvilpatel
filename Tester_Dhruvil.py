from Drum import Drum
from Flute import Flute
from Harp import Harp
from Piano import Piano
from Violin import Violin
from Xylophone import Xylophone

from MusicalInstrument import Repairable, PriceProvider, Playable, MusicalInstrument

if __name__ == '__main__':

    drum = Drum(0, 20)  # this drum has 0 keys and the size of its diameter is 20. (Assume drum does not have any key.)
    flute = Flute()  # this flute does not have any specific attribute, except the inherited ones.
    harp = Harp(40)  # this harp has 40 strings
    piano = Piano(88, 230)  # this piano has 88 keys and 230 strings
    violin = Violin(4)  # this violin has 4 strings
    xylophone = Xylophone(25)  # this xylophone has 25 keys

    instrument_list = [drum, flute, harp, piano, violin, xylophone]

    for i in instrument_list:

        if isinstance(i, MusicalInstrument):
            i.make_sound()
        if isinstance(i, Playable):
            i.how_to_play()
        if isinstance(i, Repairable):
            i.how_to_repair()
        if isinstance(i, PriceProvider):
            i.get_price()

        print(f'Details of {i}')
        print(f'Make Sound: {i.make_sound}')
        print(f'Play Method: {i.how_to_play}')
        print(f'Repair Method: {i.how_to_repair}')
        print(f'The price: {i.get_price}')
