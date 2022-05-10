import pygame
import os


pygame.init
pygame.font.init()

# farger
black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
blue = (125, 177, 244)
yellow = (255,255,0)
bakgrunn = (30,30,30)

# vindu og klokke
x_vin, y_vin = 1280, 720
vindu = pygame.display.set_mode((x_vin,y_vin))
clock = pygame.time.Clock()


# loads image
def load_image(filename):
    image = pygame.image.load(filename)
    return image



start_bilde = load_image("Presentasjon2.jpg")




# gjør det mulig å avslutte program
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    


    # show image
    vindu.blit(start_bilde, (0,0))

    # takes keyborad input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        break
    elif keys[pygame.K_t]:
        os.system("python3 kode/kube_pi_tref.py")
    elif keys[pygame.K_r]:
       os.system("python3 kode/kube_pi.py")
    elif keys[pygame.K_f]:
       os.system("python3 kode/kube_pi_forklaring.py")
        
    

    pygame.display.update()