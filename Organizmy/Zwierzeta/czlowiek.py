import random

from .zwierze import Zwierze
import pygame
import copy
from Nawigacja.kierunki import Kierunek


class Czlowiek(Zwierze):
    __nazwa = "Czlowiek"
    __sila = 5
    __inicjatywa = 4
    __tekstura = None
    __sciezka_tekstury = "czlowiek.png"
    __czas_odnowy_umiejetnosci_specjalnej = 5
    __czas_umiejetnosc_specjalna = 5
    __szansa_umiejetnosci_po_trzech = 0.5

    def __init__(self, swiat, pozycja):
        if self.__tekstura is None and self.__sciezka_tekstury:
            self.__tekstura = pygame.image.load(self.__sciezka_tekstury)
        super().__init__(swiat, pozycja, self.__nazwa, self.__tekstura, self.__sila, self.__inicjatywa)
        self._cooldown = 0
        self._pozostaly_czas = 0
        self._kierunek_ruchu = Kierunek.POLNOC

    def WygenerujKopie(self):
        return None

    def UstawKierunek(self, kierunek):
        self._kierunek_ruchu = kierunek

    def Akcja(self):
        self.__ObsluzUmiejetnoscSpecjalna()
        if self.Zywy():
            x_cel, y_cel = self._DajPoleDocelowe()
            super()._WykonajRuch(self._swiat.DajMape().DajPole(x_cel, y_cel))

    def AktywujUmiejetnoscSpecjalna(self):
        if self._cooldown == 0:
            print("Czlowiek uzyl swojej swojej umiejetnosci specjalnej! Bedzie aktywna przez ",
                  self.__czas_umiejetnosc_specjalna, "tur!")
            self.UstawCooldown(self.__czas_odnowy_umiejetnosci_specjalnej)
            self.UstawPozostalyCzasUmiejetnosc(self.__czas_umiejetnosc_specjalna)

    def UstawCooldown(self, cooldown):
        self._cooldown = cooldown

    def UstawPozostalyCzasUmiejetnosc(self, czas):
        self._pozostaly_czas = czas

    def DajUmiejetnoscPozostalyCzas(self):
        return self._pozostaly_czas

    def DoZapisu(self):
        return super().DoZapisu() + " " + str(self._pozostaly_czas) + " " + str(self._cooldown)

    def _DajPoleDocelowe(self):
        poledocelowe = copy.copy(self.DajPozycje())
        if self.__CzyUmiejetnoscAktywna():
            for i in range(2):
                poledocelowe.OffsetPunkt(self._kierunek_ruchu)
        else:
            poledocelowe.OffsetPunkt(self._kierunek_ruchu)
        self._swiat.ZapetlijPunkt(poledocelowe)
        return poledocelowe.DajX(), poledocelowe.DajY()

    def _CzyTenSamGatunek(self, partner):
        return False

    def __CzyUmiejetnoscAktywna(self):
        i = self.DajUmiejetnoscPozostalyCzas()
        if i > 2 or (i < 3 and i > 0 and random.random() < self.__szansa_umiejetnosci_po_trzech):
            return True
        return False

    def __ObsluzUmiejetnoscSpecjalna(self):
        if self._pozostaly_czas > 0:
            self._pozostaly_czas -= 1
            if self._pozostaly_czas == 0:
                print("Umiejetnosc specjalna czlowieka zakonczyla sie")
            return
        if self._cooldown == 0 and self._pozostaly_czas > 0:
            self._pozostaly_czas -= 1
            if self._pozostaly_czas == 0:
                print("Umiejetnosc specjalna czlowieka znow jest gotowa do dzialania!")
