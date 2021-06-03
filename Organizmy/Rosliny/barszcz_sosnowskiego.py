from .roslina_trujaca import RoslinaTrujaca
from ..Zwierzeta.zwierze import Zwierze
import Organizmy.Zwierzeta.cyber_owca as co
from Nawigacja.pole import Pole
import pygame


class BarszczSosnowskiego(RoslinaTrujaca):
    __sila = 10
    __nazwa = "Barszcz Sosnowskiego"
    __tekstura = None
    __sciezka_tekstury = "barszczsosnowskiego.png"

    def __init__(self, swiat, pozycja):
        if self.__tekstura is None and self.__sciezka_tekstury:
            self.__tekstura = pygame.image.load(self.__sciezka_tekstury)
        super().__init__(swiat, pozycja, self.__nazwa, self.__tekstura, self.__sila)
        
    def WygenerujKopie(self):
        return BarszczSosnowskiego(self._swiat, self.DajPozycje())

    def Akcja(self):
        if not self.Zywy():
            return
        kierunki = self.DajPozycje().DajWektoryJednostkowe()
        for kierunek in kierunki:
            temp_pole = Pole(self.DajPozycje().DajX() + kierunek.DajX(), self.DajPozycje().DajY() + kierunek.DajY(),
                             None)
            self._swiat.ZapetlijPunkt(temp_pole)
            organizm = self._swiat.DajMape().DajOrganizm(temp_pole.DajX(), temp_pole.DajY())
            if isinstance(organizm, Zwierze):
                organizm._Umrzyj(self)

    def _Kolizja(self, organizm):
        if isinstance(organizm, co.CyberOwca):
            self._Umrzyj(organizm)
            return True
        else:
            return super()._Kolizja(organizm)
