from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def consumption(self):
        pass


class Coat (Clothes):
    type = 'Пальто'

    def __init__(self, v):
        self.v = v

    @property
    def consumption(self):
        return round(self.v / 6.5 + 0.5, 2)


class Costume (Clothes):
    type = 'Костюм'

    def __init__(self, h):
        self.h = h

    @property
    def consumption(self):
        return round(2 * self.h + 0.3, 2)


coat = Coat(43)
print(coat.consumption)

costume = Costume(1.8)
print(costume.consumption)
