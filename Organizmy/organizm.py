from abc import abstractmethod, ABC
import pygame


class Organizm(ABC):
    def __init__(self, swiat, pozycja, nazwa, tekstura, sila, inicjatywa):
        self._swiat = swiat
        self._pozycja = pozycja
        self._sila = sila
        self._inicjatywa = inicjatywa
        self._zywy = True
        self._nazwa = nazwa
        self._tekstura = tekstura

    def __str__(self):
        return self.DajNazwe() + " [" + str(self.DajPozycje().DajX()) + "," + str(self.DajPozycje().DajY()) \
               + "] o sile (" + str(self.DajSile()) + ")"
    
    @abstractmethod
    def Akcja(self):
        pass

    def Renderuj(self, ekran, wymiary_komorki, margines):
        if not self.Zywy():
            return
        x = margines + self._pozycja.DajX() * (wymiary_komorki + margines)
        y = margines + self._pozycja.DajY() * (wymiary_komorki + margines)
        self.RenderujIkone(self, ekran, x, y, wymiary_komorki)

    @staticmethod
    def RenderujIkone(self, ekran, x, y, wymiary_komorki):
        tekstura = self.DajTeksture()
        ekran.blit(tekstura, (x, y))

    def DajPozycje(self):
        return self._pozycja

    def UstawPozycje(self, punkt):
        self._pozycja = punkt

    def DajSile(self):
        return self._sila

    def OffsetSile(self, przesuniecie):
        self._sila += przesuniecie

    def DajInicjatywe(self):
        return self._inicjatywa

    def Zywy(self):
        return self._zywy
    
    @abstractmethod
    def WygenerujKopie(self):
        pass

    def DajNazwe(self):
        return self._nazwa

    def DajTeksture(self):
        return self._tekstura

    def DoZapisu(self):
        return self.DajNazwe() + " " + str(self.DajPozycje().DajX()) + " " \
               + str(self.DajPozycje().DajY()) + " " + str(self.DajSile())

    @abstractmethod
    def _Kolizja(self, organism):
        pass

    def _WykonajRuch(self, pole_docelowe):
        if not self._pozycja.Pusty():
            return False
        self.DajPozycje().UstawPozycje(None)
        self._swiat.DajMape().UstawOrganizm(self.DajPozycje(), None)
        self.UstawPozycje(pole_docelowe)
        self._swiat.DajMape().UstawOrganizm(self.DajPozycje(), self)
        return True

    def _Umrzyj(self, organizm):
        if organizm is None:
            print(self, "umarl.")
        else:
            print(str(self) + " zostal zabity przez " + str(organizm))
        self._zywy = False
        self._pozycja.UstawOrganizm(None)
        self._pozycja = None
        return True