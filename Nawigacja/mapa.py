from Nawigacja.pole import Pole


class Mapa:
    def __init__(self, szerokosc, wysokosc):
        self._szerokosc = szerokosc
        self._wysokosc = wysokosc
        self._mapa = []
        self._init()

    def _init(self):
        self._mapa = [[None for x in range(self._wysokosc)] for y in range(self._szerokosc)]
        for x in range(self._szerokosc):
            for y in range(self._wysokosc):
                self._mapa[x][y] = Pole(x, y, None)

    def DajOrganizm(self, x, y):
        if self.DajPole(x, y):
            return self._mapa[x][y].DajOrganizm()
        return None

    def DajSzerokosc(self):
        return self._szerokosc

    def DajWysokosc(self):
        return self._wysokosc

    def DajPole(self, x, y):
        if x < 0 or y < 0 or x >= self._szerokosc or y >= self._wysokosc:
            return None
        return self._mapa[x][y]

    def UstawPole(self, nowe_pole, organizm):
        self._mapa[nowe_pole.DajX()][nowe_pole.DajY()] = organizm
        
    def UstawRozmiar(self, szerokosc, wysokosc):
        self._szerokosc = szerokosc
        self._wysokosc = wysokosc
        self._init()
