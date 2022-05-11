import pygame
import os

pygame.init()

# vindu og klokke
x_vin, y_vin = 1280, 720
vindu = pygame.display.set_mode((x_vin,y_vin))

# laster inn bilde
start_bilde = pygame.image.load("Bilde_gui.jpg")

# gjør det mulig å avslutte program
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    # viser bilde
    vindu.blit(start_bilde, (0,0))

    # takes keyborad input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        break
    elif keys[pygame.K_e]:
        os.system("python3 kode/Underprogram/kube_pi_treg.py")
    elif keys[pygame.K_r]:
        os.system("python3 kode/Underprogram/kube_pi.py")
    elif keys[pygame.K_t]:
        os.system("python3 kode/Underprogram/Forklaring.py")
    elif keys[pygame.K_k]:
        os.system("python3 kode/Underprogram/kube_pi_forklaring.py")
    
    pygame.display.update()