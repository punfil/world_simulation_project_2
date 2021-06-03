import copy
from abc import abstractmethod
from ..organizm import Organizm


class Zwierze(Organizm):

    def __init__(self, swiat, pozycja, nazwa, tekstura, sila, inicjatywa):
        super().__init__(swiat, pozycja, nazwa, tekstura, sila, inicjatywa)

    def Akcja(self):
        if self.Zywy():
            self._WykonajRuch(self._DajPoleDocelowe())

    def _Kolizja(self, organizm):
        if not self.Zywy():
            return
        if self.DajSile() >= organizm.DajSile():
            organizm._Umrzyj(self)
            return False
        else:
            self._Umrzyj(organizm)
            return True

    @abstractmethod
    def _CzyTenSamGatunek(self, partner):
        pass

    def _WykonajRuch(self, pole_docelowe):
        if pole_docelowe == self.DajPozycje():
            return False
        organizm = pole_docelowe.DajOrganizm()
        if organizm is None:
            self.DajPozycje().UstawOrganizm(None)
            self.UstawPozycje(pole_docelowe)
            pole_docelowe.UstawOrganizm(self)
            self._pozycja = pole_docelowe
            return True
        elif self._CzyTenSamGatunek(organizm):
            self._RozmnozSie(organizm)
            return False
        elif organizm._Kolizja(self):
            self.DajPozycje().UstawOrganizm(None)
            self.UstawPozycje(pole_docelowe)
            pole_docelowe.UstawOrganizm(self)
            return False
        return False

    def _DajPolaDlaDzieci(self, partner):
        ##Dziecko stawiamy obok partnera, matka nie nosi dziecka, aby sprobowac postawic je kolo siebie
        kierunki = partner.DajPozycje().DajWektoryJednostkowe()
        pole = copy.copy(partner.DajPozycje())
        pola_dla_dzieci = list()
        for kierunek in kierunki:
            pole.OffsetWspolrzedne(kierunek.DajX(), kierunek.DajY())
            self._swiat.ZapetlijPunkt(pole)
            pola_dla_dzieci.append(copy.copy(pole))
            pole.OffsetWspolrzedne(-kierunek.DajX(), -kierunek.DajY())
            self._swiat.ZapetlijPunkt(pole)
        return pola_dla_dzieci

    def _RozmnozSie(self, partner):
        poladladzieci = self._DajPolaDlaDzieci(partner)
        for i in poladladzieci:
            if self._swiat.DajMape().DajOrganizm(i.DajX(), i.DajY()) is None:
                dziecko = self.WygenerujKopie()
                self._swiat.DajMape().DajPole(i.DajX(), i.DajY()).UstawOrganizm(dziecko)
                dziecko.UstawPozycje(self._swiat.DajMape().DajPole(i.DajX(), i.DajY()))
                self._swiat.DodajOrganizm(dziecko)
                if self is partner:
                    print(self, " rozmnozyl sie")
                else:
                    print(self, " rozmnozyl sie z ", partner)
                return True
        return False

    def _DajPoleDocelowe(self):
        poledocelowe = copy.copy(self.DajPozycje())
        kierunek = poledocelowe.DajLosowyWektorJednostkowy()
        poledocelowe.OffsetPunkt(kierunek)
        self._swiat.ZapetlijPunkt(poledocelowe)
        return self._swiat.DajMape().DajPole(poledocelowe.DajX(), poledocelowe.DajY())
