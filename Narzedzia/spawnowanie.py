import pygame
from Organizmy import *
from pygame.locals import *
from Nawigacja.pole import Pole
from Organizmy.Rosliny.wilcze_jagody import WilczeJagody
from Organizmy.Rosliny.barszcz_sosnowskiego import BarszczSosnowskiego
from Organizmy.Rosliny.mlecz import Mlecz
from Organizmy.Rosliny.guarana import Guarana
from Organizmy.Rosliny.trawa import Trawa


class SpawnMenu:
    __rzedy = 3
    __kolumny = 3
    __kolor_tla = (30, 30, 30)
    __kolor_ramki = (110, 110, 110)

    def __init__(self, swiat, wymiary_komorki, margines, ekran):
        self._swiat = swiat
        self._wymiary_komorki = wymiary_komorki
        self._margines = margines
        self._ekran = ekran
        pozycja = Pole(-1, -1, None)
        self._ikony = [
            [Antylopa(swiat, pozycja), CyberOwca(swiat, pozycja), Lis(swiat, pozycja)],
            [Owca(swiat, pozycja), Zolw(swiat, pozycja), Wilk(swiat, pozycja)],
            [WilczeJagody(swiat, pozycja), BarszczSosnowskiego(swiat, pozycja), Trawa(swiat, pozycja)],
            [Guarana(swiat, pozycja), Mlecz(swiat, pozycja)]
        ]
        self._ostatni_x = 0
        self._ostatni_y = 0
        self._pole = None

    def WykonajWydarzenia(self, mysz, klikniete_pole):
        self._ostatni_x, self._ostatni_y = self.__MenuMiesciSieNaEkranie(mysz)
        self._pole = klikniete_pole
        self.__Renderuj()
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    nowa_mysz = pygame.mouse.get_pos()
                    done = True
                    break
        x = (nowa_mysz[0] - self._ostatni_x) // (self._wymiary_komorki + self._margines)
        y = (nowa_mysz[1] - self._ostatni_y) // (self._wymiary_komorki + self._margines)
        if y in range(0, len(self._ikony)) and x in range(0, len(self._ikony[y])):
            pole_docelowe = self._pole
            if pole_docelowe is not None and pole_docelowe.Pusty():
                pole_ostateczne = self._swiat.DajMape().DajPole(pole_docelowe.DajX(), pole_docelowe.DajY())
                organizm = self._ikony[y][x].WygenerujKopie()
                organizm.UstawPozycje(pole_ostateczne)
                pole_ostateczne.UstawOrganizm(organizm)
                print("Spawnowanie na " + str(pole_ostateczne))
                self._swiat.DodajOrganizmNatychmiast(organizm)
        pygame.display.update()

    def __MenuMiesciSieNaEkranie(self, pozycja):
        (x, y) = pozycja[0], pozycja[1]
        cell = self._wymiary_komorki + self._margines
        menu_w = cell * len(self._ikony) + self._margines + 4
        menu_s = cell * len(self._ikony[0]) + self._margines + 4
        fit_x = self._ekran.get_width() - menu_s - x
        fit_y = self._ekran.get_height() - menu_w - y
        if fit_x < 0:
            x += fit_x
        if fit_y < 0:
            y += fit_y
        return x, y

    def __Renderuj(self):
        wysokosc = (self._wymiary_komorki + self._margines) * len(self._ikony) + self._margines
        szerokosc = (self._wymiary_komorki + self._margines) * len(self._ikony[0]) + self._margines
        pygame.draw.rect(self._ekran, self.__kolor_ramki,
                         (self._ostatni_x - 1, self._ostatni_y - 1, szerokosc + 2, wysokosc + 2), 6)
        pygame.draw.rect(self._ekran, self.__kolor_tla, (self._ostatni_x, self._ostatni_y, szerokosc, wysokosc))
        for y in range(len(self._ikony)):
            for x in range(len(self._ikony[y])):
                x_pozycja = self._ostatni_x + x * (self._wymiary_komorki + self._margines) + self._margines
                y_pozycja = self._ostatni_y + y * (self._wymiary_komorki + self._margines) + self._margines
                Organizm.RenderujIkone(self._ikony[y][x], self._ekran, x_pozycja, y_pozycja, self._wymiary_komorki)
        pygame.display.update()
