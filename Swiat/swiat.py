from Nawigacja.mapa import Mapa
from pygame.locals import *
import random
from Organizmy.Rosliny import *
from Organizmy.Rosliny.wilcze_jagody import WilczeJagody
from Organizmy.Rosliny.barszcz_sosnowskiego import BarszczSosnowskiego
from Organizmy.Rosliny.mlecz import Mlecz
from Organizmy.Rosliny.guarana import Guarana
from Organizmy.Rosliny.trawa import Trawa
from Nawigacja.kierunki import Kierunek
from Narzedzia.wprowadz_jeden_tekst import *
from Narzedzia.spawnowanie import SpawnMenu

pygame.init()


class Swiat:
    __rozszerzenie_pliku_zapisu = ".zapisgry"
    __katalog_zapisow = "zapis/"
    __kolor_pustego_pola = (70, 70, 70)
    __mala_czcionka = pygame.font.SysFont('Corbel', 20)
    __bialy = (255, 255, 255)
    __przyciski = list()
    __przyciski.append(__mala_czcionka.render("Kolejna tura!", True, __bialy))
    __przyciski.append(__mala_czcionka.render("Nowa Gra", True, __bialy))
    __przyciski.append(__mala_czcionka.render("Wczytaj Gre", True, __bialy))
    __przyciski.append(__mala_czcionka.render("Zapisz Gre", True, __bialy))
    __liczba_przyciskow = 4
    __stala_rozmieszczenia_przyciskow = 180

    def __init__(self, x, y, ekran, rozmiar_komorki, margines, tytul, rozmiar_przycisku):
        self._mapa = Mapa(x, y)
        self._kolejka_organizmow = list()
        self._nowe_organizmy = list()
        self._tura = 1
        self._czlowiek = None
        self._wymiary_komorki = rozmiar_komorki
        self._margines_komorki = margines
        self._ekran = ekran
        self._domyslny_tytul = tytul
        self._obecny_tytul = tytul
        self._wielkosc_przycisku = rozmiar_przycisku
        self.__init()
        self.__menu_spawnowania = SpawnMenu(self, rozmiar_komorki, margines, ekran)

    def DajMape(self):
        return self._mapa

    def WykonajTure(self):
        print("Runda " + str(self._tura) + " zaczyna sie")
        for organizm in self._kolejka_organizmow:
            organizm.Akcja()
        self.__InicjujNoweOrganizmy()
        self.__UsunMartweOrganizmy()
        self.__SortujOrganizmy()
        print("Runda " + str(self._tura) + " zakonczyla sie")
        self._tura += 1

    def RenderujSwiat(self, ekran, wymiary_komorki, margines):
        self._wymiary_komorki = wymiary_komorki
        self._margines_komorki = margines
        self.__RysujSiatke(ekran, wymiary_komorki, margines)
        for organizm in self._kolejka_organizmow:
            organizm.Renderuj(ekran, wymiary_komorki, margines)
        self.__RenderujPrzyciski(ekran, wymiary_komorki, margines)

    def DodajOrganizm(self, organizm):
        self._nowe_organizmy.append(organizm)

    def DodajOrganizmNatychmiast(self, organizm):
        self._nowe_organizmy.append(organizm)
        self.__InicjujNoweOrganizmy()
        self.RenderujSwiat(self._ekran, self._wymiary_komorki, self._margines_komorki)
        return

    def DajSzerokosc(self):
        return self._mapa.DajSzerokosc()

    def DajWysokosc(self):
        return self._mapa.DajWysokosc()

    def ZapetlijPunkt(self, pole):
        if pole.DajX() < 0:
            pole.OffsetX(self.DajSzerokosc())
        if pole.DajX() >= self.DajSzerokosc():
            pole.OffsetX(-self.DajSzerokosc())
        if pole.DajY() < 0:
            pole.OffsetY(self.DajWysokosc())
        if pole.DajY() >= self.DajWysokosc():
            pole.OffsetY(-self.DajWysokosc())

    def WykonajWydarzenia(self, event):
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                self.WykonajTure()
            elif event.key == K_UP:
                self._czlowiek.UstawKierunek(Kierunek.POLNOC)
                self.WykonajTure()
            elif event.key == K_RIGHT:
                self._czlowiek.UstawKierunek(Kierunek.WSCHOD)
                self.WykonajTure()
            elif event.key == K_DOWN:
                self._czlowiek.UstawKierunek(Kierunek.POLUDNIE)
                self.WykonajTure()
            elif event.key == K_LEFT:
                self._czlowiek.UstawKierunek(Kierunek.ZACHOD)
                self.WykonajTure()
            elif event.key == K_f:
                self._czlowiek.AktywujUmiejetnoscSpecjalna()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mysz = pygame.mouse.get_pos()
            if event.button == 3:
                pole = self.__PixelNaPole(mysz)
                self.__menu_spawnowania.WykonajWydarzenia(mysz, pole)
                return
            komendy = {0: lambda: self.WykonajTure(), \
                       1: lambda: self.__NowySwiat(int(DajTekst(self._ekran, "Wprowadz szerokosc swiata")),
                                                   int(DajTekst(self._ekran, "Wprowadz wysokosc swiata"))), \
                       2: lambda: self.__WczytajSwiat(DajTekst(self._ekran, "Podaj nazwe pliku odczytu")), \
                       3: lambda: self.__ZapiszSwiat(DajTekst(self._ekran, "Podaj nazwe pliku zapisu"))}
            stala = (self._wymiary_komorki + self._margines_komorki) * self.DajSzerokosc()
            y1 = (self._wymiary_komorki + self._margines_komorki) * self.DajWysokosc() + self._margines_komorki
            y2 = (
                         self._wymiary_komorki + self._margines_komorki) * self.DajWysokosc() + self._margines_komorki + self._wielkosc_przycisku
            for i in range(self.__liczba_przyciskow):
                current_x1 = i * (stala / self.__stala_rozmieszczenia_przyciskow * self._wielkosc_przycisku)
                current_x2 = (i + 1) * (stala / self.__stala_rozmieszczenia_przyciskow * self._wielkosc_przycisku)
                if mysz[0] <= current_x2 and mysz[0] >= current_x1 and mysz[1] <= y2 and mysz[1] >= y1:
                    komendy[i]()
                    self.__AktualizujTytul()
                    return

    def __AktualizujTytul(self):
        pygame.display.set_caption(self._obecny_tytul)

    def __PixelNaPole(self, mysz):
        x = mysz[0] // (self._margines_komorki + self._wymiary_komorki)
        y = mysz[1] // (self._margines_komorki + self._wymiary_komorki)
        return self._mapa.DajPole(x, y)

    def __InicjujNoweOrganizmy(self):
        for organizm in self._nowe_organizmy:
            self._kolejka_organizmow.append(organizm)
        self._nowe_organizmy.clear()
        self.__SortujOrganizmy()

    def __NowySwiat(self, szerokosc, wysokosc):
        if szerokosc <= 0 or wysokosc <= 0:
            return False
        self.__Wyczysc(szerokosc, wysokosc)
        self.__init()
        return True

    def __Wyczysc(self, szerokosc, wysokosc, tura=1):
        self._mapa.UstawRozmiar(szerokosc, wysokosc)
        self._tura = tura
        self._kolejka_organizmow.clear()
        self._nowe_organizmy.clear()

    def __ZapiszSwiat(self, nazwa_zapis):
        plik = open(self.__katalog_zapisow + nazwa_zapis + self.__rozszerzenie_pliku_zapisu, "w")
        plik.write("& " + str(self.DajSzerokosc()) + " " + str(self.DajWysokosc()) + " " + str(self._tura) + "\n")
        for organizm in self._kolejka_organizmow:
            plik.write(organizm.DoZapisu() + "\n")
        plik.close()

    def __WczytajSwiat(self, nazwa_zapis):
        try:
            plik = open(self.__katalog_zapisow + nazwa_zapis + self.__rozszerzenie_pliku_zapisu, "r")
        except FileNotFoundError:
            print("Plik jest uszkodzony lub nie istnieje")
            return
        with plik:
            for linia in plik:
                zawartosc = linia.split()
                if zawartosc[0] == "&":
                    szerokosc = int(zawartosc[1])
                    wysokosc = int(zawartosc[2])
                    tura = int(zawartosc[3])
                    self.__Wyczysc(szerokosc, wysokosc, tura)
                elif zawartosc[0] in ["Antylopa", "Lis", "Czlowiek", "Owca", "CyberOwca", "Zolw", "Wilk",
                                      "WilczeJagody", "BarszczSosnowskiego", "Trawa", "Guarana", "Mlecz"]:
                    x = int(zawartosc[1])
                    y = int(zawartosc[2])
                    sila = int(zawartosc[3])
                    pole = self._mapa.DajPole(x, y)
                    organizm = None
                    if zawartosc[0] == "Czlowiek":
                        organizm = Czlowiek(self, pole)
                        pozostaly_czas = int(zawartosc[4])
                        cool_down = int(zawartosc[5])
                        organizm.UstawPozostalyCzasUmiejetnosc(pozostaly_czas)
                        organizm.UstawCooldown(cool_down)
                        self._czlowiek = organizm
                    elif zawartosc[0] == "Antylopa":
                        organizm = Antylopa(self, pole)
                    elif zawartosc[0] == "Lis":
                        organizm = Lis(self, pole)
                    elif zawartosc[0] == "Owca":
                        organizm = Owca(self, pole)
                    elif zawartosc[0] == "Zolw":
                        organizm = Zolw(self, pole)
                    elif zawartosc[0] == "Wilk":
                        organizm = Wilk(self, pole)
                    elif zawartosc[0] == "CyberOwca":
                        organizm = CyberOwca(self, pole)
                    elif zawartosc[0] == "WilczeJagody":
                        organizm = WilczeJagody(self, pole)
                    elif zawartosc[0] == "BarszczSosnowskiego":
                        organizm = BarszczSosnowskiego(self, pole)
                    elif zawartosc[0] == "Trawa":
                        organizm = Trawa(self, pole)
                    elif zawartosc[0] == "Guarana":
                        organizm = Guarana(self, pole)
                    elif zawartosc[0] == "Mlecz":
                        organizm = Mlecz(self, pole)
                    pole.UstawOrganizm(organizm)
                    organizm.OffsetSile(sila - organizm.DajSile())
                    self._kolejka_organizmow.append(organizm)
        self.__ZmienWielkoscWyswietlacza()

    def __UsunMartweOrganizmy(self):
        for i in range(len(self._kolejka_organizmow) - 1, -1, -1):
            if not self._kolejka_organizmow[i].Zywy():
                del self._kolejka_organizmow[i]

    def __SortujOrganizmy(self):
        self._kolejka_organizmow.sort(key=lambda organizm: organizm.DajInicjatywe(), reverse=True)

    def __RenderujPrzyciski(self, ekran, wymiary_komorki, margines):
        stala = (wymiary_komorki + margines) * self.DajSzerokosc()
        for i in range(self.__liczba_przyciskow):
            ekran.blit(self.__przyciski[i], (
                i * (stala / self.__stala_rozmieszczenia_przyciskow * self._wielkosc_przycisku),
                (wymiary_komorki + margines) * self.DajWysokosc() + margines))

    def __RysujSiatke(self, ekran, wymiary_komorki, margines):
        prostokat = Rect(-wymiary_komorki, -wymiary_komorki, wymiary_komorki, wymiary_komorki)
        for y in range(self.DajWysokosc()):
            prostokat.y += wymiary_komorki + margines
            prostokat.x = -wymiary_komorki
            for x in range(self.DajSzerokosc()):
                prostokat.x += wymiary_komorki + margines
                pygame.draw.rect(ekran, self.__kolor_pustego_pola, prostokat)

    def __init(self):
        self.__ZmienWielkoscWyswietlacza()
        for x in range(self.DajSzerokosc()):
            for y in range(self.DajWysokosc()):
                i = random.randint(0, 60)
                if i <= 10:
                    pole = self._mapa.DajPole(x, y)
                    organizm = None
                    if i == 0:
                        organizm = Lis(self, pole)
                    elif i == 1:
                        organizm = Trawa(self, pole)
                    elif i == 2:
                        organizm = Mlecz(self, pole)
                    elif i == 3:
                        organizm = Guarana(self, pole)
                    elif i == 4:
                        organizm = WilczeJagody(self, pole)
                    elif i == 5:
                        organizm = Wilk(self, pole)
                    elif i == 6:
                        organizm = Zolw(self, pole)
                    elif i == 7:
                        organizm = Owca(self, pole)
                    elif i == 8:
                        organizm = BarszczSosnowskiego(self, pole)
                    elif i == 9:
                        organizm = Antylopa(self, pole)
                    elif i == 10:
                        organizm = CyberOwca(self, pole)
                    pole.UstawOrganizm(organizm)
                    self._kolejka_organizmow.append(organizm)
        while True:
            x = random.randint(0, self._mapa.DajSzerokosc() - 1)
            y = random.randint(0, self._mapa.DajWysokosc() - 1)
            pole = self._mapa.DajPole(x, y)
            if pole.Pusty():
                self._czlowiek = Czlowiek(self, pole)
                pole.UstawOrganizm(self._czlowiek)
                self._kolejka_organizmow.append(self._czlowiek)
                break
        self.__SortujOrganizmy()

    def __ZmienWielkoscWyswietlacza(self):
        komorka = self._wymiary_komorki + self._margines_komorki
        pygame.display.set_mode((komorka * self.DajSzerokosc() + self._margines_komorki,
                                 komorka * self.DajWysokosc() + self._margines_komorki + self._wielkosc_przycisku))
