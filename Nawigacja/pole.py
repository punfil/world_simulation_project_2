import random


class Pole:
    def __init__(self, x, y, organizm):
        self._organizm = organizm
        self.__x = x
        self.__y = y

    def Pusty(self):
        return self._organizm is None

    def UstawOrganizm(self, organizm):
        self._organizm = organizm

    def DajOrganizm(self):
        return self._organizm

    def UstawPunkt(self, punkt):
        self._punkt = punkt

    def DajPunkt(self):
        return self._punkt

    def DajX(self):
        return self.__x

    def DajY(self):
        return self.__y

    def __str__(self):
        return "Pole (" + str(self.DajX()) + ", " + str(self.DajY()) + ") " + str(self._organizm)

    def OffsetPunkt(self, inny_punkt):
        self.__x += inny_punkt.DajX()
        self.__y += inny_punkt.DajY()

    def OffsetWspolrzedne(self, inny_x, inny_y):
        self.__x += inny_x
        self.__y += inny_y

    def OffsetX(self, inny_x):
        self.__x += inny_x

    def OffsetY(self, inny_y):
        self.__y += inny_y

    def DajLosowyWektorJednostkowy(self):
        x, y = 0, 0
        i = random.randint(0, 3)
        if i == 0:
            y = -1
        elif i == 1:
            y = 1
        elif i == 2:
            x = 1
        else:
            x = -1
        p = Pole(x, y, None)
        return p

    def DajWektoryJednostkowe(self):
        wektory = []
        wektory.append(Pole(0, 1, None))
        wektory.append(Pole(0, -1, None))
        wektory.append(Pole(1, 0, None))
        wektory.append(Pole(-1, 0, None))
        return wektory
