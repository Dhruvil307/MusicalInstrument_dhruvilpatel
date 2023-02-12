from Drum import Drum
from Flute import Flute
from Harp import Harp
from PercussionFamily import PercussionFamily
from StringFamily import StringFamily
from Violin import Violin
from Xylophone import Xylophone
from Piano import Piano
from Order import Order
from MusicalInstrument import Repairable, PriceProvider, Playable, MusicalInstrument

if __name__ == '__main__':

    drum = Drum(0, 20)  # this drum has 0 keys and the size of its diameter is 20. (Assume drum does not have any key.)
    flute = Flute()  # this flute does not have any specific attribute, except the inherited ones.
    harp = Harp(40)  # this harp has 40 strings
    piano = Piano(88, 230)  # this piano has 88 keys and 230 strings
    violin = Violin(4)  # this violin has 4 strings
    xylophone = Xylophone(25)  # this xylophone has 25 keys

    instrument_list = [drum, flute, harp, violin, xylophone, piano]

    for indx, i in enumerate(instrument_list):
        print("------------------------------------OUTPUT {}------------------------------------".format(indx+1))
        print("Details of ", i.__class__.__name__)
        print("Makes sound:", i.make_sound())
        i.how_to_play()
        if isinstance(i, Repairable):
            i.how_to_repair()
        i.get_price()

    print("------------------------------------OUTPUT 7------------------------------------")
    print("SPECIAL FEATURES")
    for i in instrument_list:
        i.special_features()

    print("------------------------------------OUTPUT 8------------------------------------")
    print("All instruments in price ascending order:")
    instrument_list.sort()
    for i in instrument_list:
        print("{} price: {}".format(i.__class__.__name__, i.value))

    order_Bob = Order(111, "Bob")  # id of the order = 111 and customer name = Bob
    order_Alice = Order(222, "Alice")  # id of the order = 222 and customer name = Alice

    for i in instrument_list:
        if isinstance(i, PercussionFamily):
            order_Bob.add_instrument(i)
        if isinstance(i, StringFamily):
            order_Alice.add_instrument(i)

    print("------------------------------------OUTPUT 9------------------------------------")
    print("Order total for Bob ({}): {}".format(order_Bob.o_id, order_Bob.get_total()))
    print("Order total for Alice ({}): {}".format(order_Alice.o_id, order_Alice.get_total()))

    print("------------------------------------CUSTOM ORDER------------------------------------")