from .roslina import Roslina
import pygame


class Guarana(Roslina):
    __sila = 0
    __nazwa = "Guarana"
    __tekstura = None
    __sciezka_tekstury = "guarana.png"
    __bonus_do_sily = 3

    def __init__(self, swiat, pozycja):
        if self.__tekstura is None and self.__sciezka_tekstury:
            self.__tekstura = pygame.image.load(self.__sciezka_tekstury)
        super().__init__(swiat, pozycja, self.__nazwa, self.__tekstura, self.__sila)

    def WygenerujKopie(self):
        return Guarana(self._swiat, self.DajPozycje())

    def _Kolizja(self, organizm):
        organizm.OffsetSile(self.__bonus_do_sily)
        self._Umrzyj(organizm)
        return True
