import pygame
pygame.init()


# Viktige varibler
x_vin,y_vin = (1280),(720)
fps = 120



# Farger
Bakgrunn = (30,30,30)
farge_ball = (220,244,255)
svart = (0,0,0)

#vindu etc.
vindu = pygame.display.set_mode((x_vin,y_vin))
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


    vindu.fill(Bakgrunn)


    pygame.display.update()
