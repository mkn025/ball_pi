import pygame,os,math

pygame.init()


# vindu og klokke
x_vin, y_vin = 1280, 720
vindu = pygame.display.set_mode((x_vin,y_vin))

# laster inn bilde
start_bilde = pygame.image.load("Bilde_gui.jpg")


# plays a sound file
def lyd(lyd_fil):
    pygame.mixer.init()
    pygame.mixer.music.load(lyd_fil)
    pygame.mixer.music.play()

lyd("wii.wav")



def start_program_og_musikk_stopp(bane):
    # pause the music
    pygame.mixer.music.pause()
    os.system(f"python3 {bane}")
    pygame.mixer.music.play()



# gjør det mulig å avslutte program
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    # viser bilde
    #fill vinduet med hvit
    
    vindu.blit(start_bilde, (0,0))

    # takes keyborad input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        break
    elif keys[pygame.K_e]:
        start_program_og_musikk_stopp("kode/Underprogram/kube_pi_treg.py")
    elif keys[pygame.K_r]:
        start_program_og_musikk_stopp("kode/Underprogram/kube_pi.py")
    elif keys[pygame.K_t]:
        start_program_og_musikk_stopp("kode/Underprogram/Forklaring.py")
    elif keys[pygame.K_k]:
        start_program_og_musikk_stopp("kode/Underprogram/kube_pi_forklaring.py")
    elif keys[pygame.K_]:
        pygame.mixer.music.stop()
    pygame.display.update()