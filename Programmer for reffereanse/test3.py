import pygame
white = (255,255,255)
pygame.init()
vindu = pygame.display.set_mode((800,600))




def tekst(x,y,varibler, tekst, font_størrelse):
    font = pygame.font.SysFont('arial', font_størrelse)
    tekst_som_vises = font.render(f"{varibler} {tekst} ",True,white)
    vindu.blit(tekst_som_vises,(x, y))
