from ..organizm import Organizm
import copy
import random


class Roslina(Organizm):
    __inicjatywa_rosliny = 0
    __szansa_rozmnazania = 0.15

    def __init__(self, swiat, pozycja, nazwa, tekstura, sila):
        super().__init__(swiat, pozycja, nazwa, tekstura, sila, self.__inicjatywa_rosliny)

    def Akcja(self):
        if not self.Zywy():
            return
        self._PodejmijProbeRozmnozeniaSie()

    def _Kolizja(self, organizm):
        self._Umrzyj(organizm)
        return True

    def _PodejmijProbeRozmnozeniaSie(self):
        szansa = random.random()
        if szansa >= self.__szansa_rozmnazania:
            return False
        pole = copy.copy(self.DajPozycje())
        kierunek = pole.DajLosowyWektorJednostkowy()
        pole.OffsetWspolrzedne(kierunek.DajX(), kierunek.DajY())
        self._swiat.ZapetlijPunkt(pole)
        poledocelowe = self._swiat.DajMape().DajPole(pole.DajX(), pole.DajY())
        if poledocelowe is None or poledocelowe.DajOrganizm() is not None:
            return False
        klon = self.WygenerujKopie()
        klon.UstawPozycje(poledocelowe)
        poledocelowe.UstawOrganizm(klon)
        self._swiat.DodajOrganizm(klon)
        print(self, "rozmnozyl sie")
        return True
