from .zwierze import Zwierze
import pygame


class Owca(Zwierze):
    __nazwa = "Owca"
    __sila = 4
    __inicjatywa = 4
    __tekstura = None
    __sciezka_tekstury = "owca.png"

    def __init__(self, swiat, pozycja):
        if self.__tekstura is None and self.__sciezka_tekstury:
            self.__tekstura = pygame.image.load(self.__sciezka_tekstury)
        super().__init__(swiat, pozycja, self.__nazwa, self.__tekstura, self.__sila, self.__inicjatywa)

    def WygenerujKopie(self):
        return Owca(self._swiat, self.DajPozycje())

    def _CzyTenSamGatunek(self, partner):
        return isinstance(partner, Owca)
