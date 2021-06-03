from enum import Enum


class Kierunek(Enum):
    POLNOC = (0, -1)
    WSCHOD = (1, 0)
    POLUDNIE = (0, 1)
    ZACHOD = (-1, 0)
    BRAK = (0, 0)

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def DajX(self):
        return self._x

    def DajY(self):
        return self._y
