import copy
from Organizmy.Rosliny.barszcz_sosnowskiego import BarszczSosnowskiego
import math

nie_znaleziono = -1


def ZnajdzNajblizszyBarszcz(mapa, moj_x, moj_y):
    odleglosc = copy.copy(nie_znaleziono)
    barszcz_x, barszcz_y = copy.copy(nie_znaleziono), copy.copy(nie_znaleziono)
    for x in range(mapa.DajSzerokosc()):
        for y in range(mapa.DajWysokosc()):
            if isinstance(mapa.DajOrganizm(x, y), BarszczSosnowskiego):
                inna_odleglosc = ObliczOdleglosc(x, moj_x, y, moj_y)
                if inna_odleglosc < odleglosc or odleglosc == nie_znaleziono:
                    odleglosc = inna_odleglosc
                    barszcz_x = x
                    barszcz_y = y
    return barszcz_x, barszcz_y


def ObliczOdleglosc(x1, x2, y1, y2):
    return math.hypot(x2 - x1, y2 - y1)


def ZnajdzSciezke(mapa, pole_startowe):
    barszcz_x, barszcz_y = ZnajdzNajblizszyBarszcz(mapa, pole_startowe.DajX(), pole_startowe.DajY())
    if barszcz_x == nie_znaleziono and barszcz_y == nie_znaleziono:
        return None
    if barszcz_y > pole_startowe.DajY():
        return mapa.DajPole(pole_startowe.DajX(), pole_startowe.DajY() + 1)
    elif barszcz_y < pole_startowe.DajY():
        return mapa.DajPole(pole_startowe.DajX(), pole_startowe.DajY() - 1)
    elif barszcz_x > pole_startowe.DajX():
        return mapa.DajPole(pole_startowe.DajX() + 1, pole_startowe.DajY())
    elif barszcz_x < pole_startowe.DajX():
        return mapa.DajPole(pole_startowe.DajX() - 1, pole_startowe.DajY())
