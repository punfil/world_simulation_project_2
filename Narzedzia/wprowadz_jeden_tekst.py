import pygame


def DajTekst(ekran, tytul):
    mala_czcionka = pygame.font.SysFont('Corbel', 20)
    bialy = (255, 255, 255)
    kolor_tla = (40, 40, 40)
    input_active = True
    text = ""
    pygame.display.set_caption(tytul)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and input_active:
                if event.key == pygame.K_RETURN:
                    return text
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
            ekran.fill(kolor_tla)
            text_surf = mala_czcionka.render(text, True, bialy)
            ekran.blit(text_surf, text_surf.get_rect(center=ekran.get_rect().center))
            pygame.display.update()
