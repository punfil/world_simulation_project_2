import pygame
import sys
from pygame.locals import *
from Swiat.swiat import Swiat

szerokosc, wysokosc = 20, 20
wymiary_komorki = 20
margines = 5
kolor_tla = (40, 40, 40)
szerokosc_przycisku = 50
default_title = "184657 Wojciech Panfil Projekt 2 Programowanie Obiektowe"

pygame.init()
pygame.font.init()
ekran = pygame.display.set_mode(((wymiary_komorki + margines) * szerokosc + margines,
                                 (wymiary_komorki + margines) * wysokosc + margines + szerokosc_przycisku))
pygame.display.set_caption(default_title)
ekran.fill(kolor_tla)
pygame.display.update()
swiat = Swiat(szerokosc, wysokosc, ekran, wymiary_komorki, margines, default_title, szerokosc_przycisku)
wyjscie = False
while not wyjscie:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_q):
            wyjscie = True
            break
        swiat.WykonajWydarzenia(event)
    ekran.fill(kolor_tla)
    swiat.RenderujSwiat(ekran, wymiary_komorki, margines)
    pygame.display.update()
    pygame.time.delay(16)
pygame.display.quit()
pygame.quit()
sys.exit()
