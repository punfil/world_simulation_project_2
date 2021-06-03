from .roslina import Roslina
import pygame


class Trawa(Roslina):
    __sila = 0
    __nazwa = "Trawa"
    __tekstura = None
    __sciezka_tekstury = "trawa.png"

    def __init__(self, swiat, pozycja):
        if self.__tekstura is None and self.__sciezka_tekstury:
            self.__tekstura = pygame.image.load(self.__sciezka_tekstury)
        super().__init__(swiat, pozycja, self.__nazwa, self.__tekstura, self.__sila)

    def WygenerujKopie(self):
        return Trawa(self._swiat, self.DajPozycje())
