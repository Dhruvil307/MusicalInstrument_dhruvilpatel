from abc import ABC

from MusicalInstrument import MusicalInstrument


class StringFamily(MusicalInstrument, ABC):
    def __init__(self, Harp, Violin, Piano) -> None:
        super().__init__()
        self.Harp = Harp
        self.Violin = Violin
        self.Piano = Piano


class Harp(StringFamily):
    super().__init__(Harp=str)


class Violin(StringFamily):
    super().__init__(Violin=str)


class Piano(StringFamily):
    super().__init__(Piano=str)
