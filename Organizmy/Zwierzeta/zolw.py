from .zwierze import Zwierze
import random
import pygame


class Zolw(Zwierze):
    __nazwa = "Zolw"
    __sila = 2
    __inicjatywa = 1
    __szansa_wykonania_ruchu = 0.25
    __zolw_odpiera_ataki_slabsze_niz = 5
    __tekstura = None
    __sciezka_tekstury = "zolw.png"

    def __init__(self, swiat, pozycja):
        if self.__tekstura is None and self.__sciezka_tekstury:
            self.__tekstura = pygame.image.load(self.__sciezka_tekstury)
        super().__init__(swiat, pozycja, self.__nazwa, self.__tekstura, self.__sila, self.__inicjatywa)

    def Akcja(self):
        if self.__szansa_wykonania_ruchu >= random.random():
            super().Akcja()

    def WygenerujKopie(self):
        return Zolw(self._swiat, self.DajPozycje())

    def _CzyTenSamGatunek(self, partner):
        return isinstance(partner, Zolw)

    def _Kolizja(self, organizm):
        if self.__CzyOdpieraAtak(organizm):
            print("Zolw odparl atak", organizm)
            return False
        return super()._Kolizja(organizm)

    def __CzyOdpieraAtak(self, organizm):
        return self.__zolw_odpiera_ataki_slabsze_niz > organizm.DajSile()
