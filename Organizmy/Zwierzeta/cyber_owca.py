from .zwierze import Zwierze
from Nawigacja.szukanie_cyberowca import *
import pygame


class CyberOwca(Zwierze):
    __nazwa = "CyberOwca"
    __sila = 11
    __inicjatywa = 4
    __tekstura = None
    __sciezka_tekstury = "cyberowca.png"

    def __init__(self, swiat, pozycja):
        if self.__tekstura is None and self.__sciezka_tekstury:
            self.__tekstura = pygame.image.load(self.__sciezka_tekstury)
        super().__init__(swiat, pozycja, self.__nazwa, self.__tekstura, self.__sila, self.__inicjatywa)

    def WygenerujKopie(self):
        return CyberOwca(self._swiat, self.DajPozycje())

    def _DajPoleDocelowe(self):
        poledocelowe = ZnajdzSciezke(self._swiat.DajMape(), self.DajPozycje())
        if poledocelowe is None:
            return super()._DajPoleDocelowe()
        else:
            return poledocelowe

    def _CzyTenSamGatunek(self, partner):
        return isinstance(partner, CyberOwca)

    def _Umrzyj(self, organizm):
        from ..Rosliny.barszcz_sosnowskiego import BarszczSosnowskiego
        if isinstance(organizm, BarszczSosnowskiego):
            return False
        else:
            return super()._Umrzyj(organizm)
