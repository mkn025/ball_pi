import pygame, os
pygame.init()


# vindu og klokke
x_vin, y_vin = 1280, 720
vindu = pygame.display.set_mode((x_vin,y_vin))

# laster inn bilde

funnet_bilde = True



try:
    info_bilde = pygame.image.load("Underprogram/Info_bilde.jpg")
except:
    funnet_bilde = False
    print("Finner ikke bilde")



# funtion for tekst 
def tekst(tekst, x_kod, y_kod, farge, skrift_størrelse):
    skrift = pygame.font.SysFont("Arial", skrift_størrelse)
    tekst_objekt = skrift.render(tekst, True, farge)
    vindu.blit(tekst_objekt, (x_kod, y_kod))

# gjør det mulig å avslutte program
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        break

    if funnet_bilde == True:
        vindu.blit(info_bilde, (0,0))
    elif funnet_bilde == False:
        vindu.fill((255,255,255))
        tekst("Finner ikke bilde", x_vin/2 - 150, y_vin/2 - 100, (0,0,0), 50)



    pygame.display.update()