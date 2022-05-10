

import pygame 
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



start_bilde = load_image("Presentasjon1.jpg")

def rask_simuering():
    pygame.time.delay(10)


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
    elif keys[pygame.K_1]:
        print("1")
    elif keys[pygame.K_2]:
        print("2")
    elif keys[pygame.K_3]:
        print("3")
    elif keys[pygame.K_4]:
        print("4")
    elif keys[pygame.K_5]:
        print("5")
    elif keys[pygame.K_6]:
        print("6")
    elif keys[pygame.K_7]:
        print("7")
    elif keys[pygame.K_t]:
        print("t")
    elif keys[pygame.K_r]:
        print("r")
    elif keys[pygame.K_f]:
        print("f")
        
    

    pygame.display.update()