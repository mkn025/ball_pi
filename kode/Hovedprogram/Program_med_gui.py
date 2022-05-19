import pygame,os

pygame.init()


# vindu og klokke
x_vin, y_vin = 1280, 720
vindu = pygame.display.set_mode((x_vin,y_vin))

# laster inn bilde

loadet_bilde = True
try:
    start_bilde = pygame.image.load("Bilde_gui.jpg")
except:
    loadet_bilde = False

# plays a sound file
def lyd(lyd_fil):
    pygame.mixer.init()
    try:
        pygame.mixer.music.load(lyd_fil)
        pygame.mixer.music.play()
    except:
        print("Finner ikke lydfil")    
   

musikk_spiller = True
lyd("wii.wav")

# starter programm og stopper musikk
def start_program_og_musikk_stopp(bane):
    pygame.mixer.music.pause()
    os.system(f"python3 {bane}")
    if musikk_spiller == True:
        pygame.mixer.music.unpause()
    
# tekst funksjon
def tekst(tekst, x_kod, y_kod, farge, skrift_størrelse):
    skrift = pygame.font.SysFont("Arial", skrift_størrelse)
    tekst_objekt = skrift.render(tekst, True, farge)
    vindu.blit(tekst_objekt, (x_kod, y_kod))

# varibels for moving ball
x_ball = 0
y_ball = y_vin/2
x_ball_vek = 0.001
y_ball_vek = 0.001



# gjør det mulig å avslutte program
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    # viser bilde
    #fill vinduet med hvit
    if loadet_bilde == True:
        vindu.blit(start_bilde, (0,0))
    elif loadet_bilde == False:
        vindu.fill((255,255,255))
        tekst("Finner ikke bilde", x_vin/2 - 150, y_vin/2 - 100, (0,0,0), 50)
        tekst("trykk e r t eller k og se hva som skjer :)", x_vin/2 - 150, y_vin/2 + 150, (0,0,0), 50)
        pygame.draw.circle(vindu, (0,0,0), (x_ball,y_ball), 50)


        x_ball += x_ball_vek
        y_ball += y_ball_vek
        if x_ball > x_vin or x_ball < 0:
            x_ball_vek = -x_ball_vek
        if y_ball > y_vin or y_ball < 0:
            y_ball_vek = -y_ball_vek
        # prints x_ball and y_ball in game 
        tekst(f"x_ball: {x_ball}", 0 + 150, 0 + 100, (0,0,0), 50)
        tekst(f"y_ball: {y_ball}", 0 + 150, 0 + 50, (0,0,0), 50)
        



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
    elif keys[pygame.K_i]:
        start_program_og_musikk_stopp("kode/Underprogram/info_program.py")
    elif keys[pygame.K_m]:
        musikk_spiller = False
        pygame.mixer.music.pause()
    elif keys[pygame.K_n]:
        musikk_spiller = True
        pygame.mixer.music.unpause()
    pygame.display.update()