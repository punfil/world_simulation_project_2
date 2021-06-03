from .zwierze import Zwierze
from Nawigacja.pole import Pole
import pygame
import random


class Antylopa(Zwierze):
    __nazwa = "Antylopa"
    __sila = 4
    __inicjatywa = 4
    __zasieg_ruchu = 2
    __szansa_ucieczki = 0.5
    __tekstura = None
    __sciezka_tekstury = "antylopa.png"

    def __init__(self, swiat, pozycja):
        if self.__tekstura is None and self.__sciezka_tekstury:
            self.__tekstura = pygame.image.load(self.__sciezka_tekstury)
        super().__init__(swiat, pozycja, self.__nazwa, self.__tekstura, self.__sila, self.__inicjatywa)

    def WygenerujKopie(self):
        return Antylopa(self._swiat, self.DajPozycje())

    def Akcja(self):
        for i in range(self.__zasieg_ruchu):
            super().Akcja()

    def _CzyTenSamGatunek(self, partner):
        return isinstance(partner, Antylopa)

    def _DajPoledoUcieczki(self):
        kierunki = self.DajPozycje().DajWektoryJednostkowe()
        for kierunek in kierunki:
            temp_pole = Pole(self.DajPozycje().DajX() + kierunek.DajX(), self.DajPozycje().DajY() + kierunek.DajY(),
                             None)
            self._swiat.ZapetlijPunkt(temp_pole)
            pole = self._swiat.DajMape().DajPole(temp_pole.DajX(), temp_pole.DajY())
            if pole.DajOrganizm() is None:
                return pole
        return None

    def _WykonajUnik(self, atakujacy):
        if not isinstance(atakujacy, Zwierze):
            return False
        pole = self._DajPoledoUcieczki()
        if pole is None:
            return False
        else:
            print(self, "uciekla przed okrutnym napastnikiem", atakujacy)
            return self._WykonajRuch(pole)

    def _Kolizja(self, organizm):
        if random.random() <= self.__szansa_ucieczki and self._WykonajUnik(organizm):
            return True
        else:
            return super()._Kolizja(organizm)
