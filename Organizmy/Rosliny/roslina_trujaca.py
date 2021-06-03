from .roslina import Roslina


class RoslinaTrujaca(Roslina):
    def __init__(self, swiat, pozycja, nazwa, tekstura, sila):
        super().__init__(swiat, pozycja, nazwa, tekstura, sila)

    def _Kolizja(self, organizm):
        ##Wersja 1. Organizm zatruwa się rośliną -> zjada ją, ginie on, ginie też roślina
        organizm._Umrzyj(self)
        self._Umrzyj(None)
        return False
        ##Wersja 2. Organizm zjada "owoc rosliny", wiec on ginie, ona niekoniecznie. Jezeli jest wystarczajaco silny, nie zatruje sie
        '''if self.DajSile() > organizm.DajSile():
            organizm._Umrzyj(self)
            return False
        else:
            self._Umrzyj(organizm)
            return True'''
