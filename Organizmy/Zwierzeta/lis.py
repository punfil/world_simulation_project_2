from .zwierze import Zwierze
import copy
import pygame


class Lis(Zwierze):
    __nazwa = "Lis"
    __sila = 3
    __inicjatywa = 7
    __tekstura = None
    __sciezka_tekstury = "lis.png"

    def __init__(self, swiat, pozycja):
        if self.__tekstura is None and self.__sciezka_tekstury:
            self.__tekstura = pygame.image.load(self.__sciezka_tekstury)
        super().__init__(swiat, pozycja, self.__nazwa, self.__tekstura, self.__sila, self.__inicjatywa)

    def _DajPoleDocelowe(self):
        ##Korzystam z metody, ktora da mi pola dookola biezacej lokalizacji
        pola_docelowe = self._DajPolaDlaDzieci(self)
        bezpieczne_pole = self.DajPozycje()
        for i in pola_docelowe:
            if self._swiat.DajMape().DajOrganizm(i.DajX(), i.DajY()) is None or self._swiat.DajMape().DajOrganizm(
                    i.DajX(), i.DajY()).DajSile() <= self.__sila:
                bezpieczne_pole = i
                break
        return self._swiat.DajMape().DajPole(bezpieczne_pole.DajX(), bezpieczne_pole.DajY())

    def WygenerujKopie(self):
        return Lis(self._swiat, self.DajPozycje())

    def _CzyTenSamGatunek(self, partner):
        return isinstance(partner, Lis)
