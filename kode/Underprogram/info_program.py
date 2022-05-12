import pygame, os
pygame.init()


# vindu og klokke
x_vin, y_vin = 1280, 720
vindu = pygame.display.set_mode((x_vin,y_vin))

# laster inn bilde
info_bilde = pygame.image.load("Info_bilde.jpg")

# gjør det mulig å avslutte program
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    vindu.blit(info_bilde, (0,0))
    pygame.display.update()