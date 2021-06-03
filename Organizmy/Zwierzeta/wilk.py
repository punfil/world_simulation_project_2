from .zwierze import Zwierze
import pygame


class Wilk(Zwierze):
    __nazwa = "Wilk"
    __sila = 9
    __inicjatywa = 5
    __tekstura = None
    __sciezka_tekstury = "wilk.png"

    def __init__(self, swiat, pozycja):
        if self.__tekstura is None and self.__sciezka_tekstury:
            self.__tekstura = pygame.image.load(self.__sciezka_tekstury)
        super().__init__(swiat, pozycja, self.__nazwa, self.__tekstura, self.__sila, self.__inicjatywa)

    def WygenerujKopie(self):
        return Wilk(self._swiat, self.DajPozycje())

    def _CzyTenSamGatunek(self, partner):
        return isinstance(partner, Wilk)
