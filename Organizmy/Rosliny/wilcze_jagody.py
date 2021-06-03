from .roslina_trujaca import RoslinaTrujaca
import pygame


class WilczeJagody(RoslinaTrujaca):
    __sila = 99
    __nazwa = "Wilcze Jagody"
    __tekstura = None
    __sciezka_tekstury = "wilczejagody.png"

    def __init__(self, swiat, pozycja):
        if self.__tekstura is None and self.__sciezka_tekstury:
            self.__tekstura = pygame.image.load(self.__sciezka_tekstury)
        super().__init__(swiat, pozycja, self.__nazwa, self.__tekstura, self.__sila)

    def WygenerujKopie(self):
        return WilczeJagody(self._swiat, self.DajPozycje())
