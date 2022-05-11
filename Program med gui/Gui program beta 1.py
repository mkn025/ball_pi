
import math, time, pygame
from math import pi as π
from Funksjoner_for_gui import *

pygame.init()
pygame.font.init()

# Viktige varibler
x_vin,y_vin = (1280),(720)

# Farger
Bakgrunn = (30,30,30)
svart = (0,0,0)
blue = (125, 177, 244)
ball_farge  = (95, 137, 140)
white = (255,255,255)
fps = 60
clock = pygame.time.Clock()
#vindu etc.
vindu = pygame.display.set_mode((x_vin,y_vin))

# elementer:
def bakke(farge):
    pygame.draw.rect(vindu, farge, (0,500,x_vin,y_vin), width=0)

def stor_firkant(x_kod, y_kod, x_lengde,y_lengde):
    pygame.draw.rect(vindu,ball_farge,(x_kod, y_kod,x_lengde,y_lengde))

def liten_firkant(x_kod, y_kod, x_lengde,y_lengde):
    pygame.draw.rect(vindu,ball_farge,(x_kod, y_kod,x_lengde,y_lengde))
    
start_time = time.time()
def runtime():
    print("Tid = " + str(time.time() - start_time) + " sekunder")

#lage lyd
def lyd(lyd_fil):
    pygame.mixer.init()
    pygame.mixer.music.load(lyd_fil)
    pygame.mixer.music.play()
    
# desimaler av pi 
print("\n")
antall_siffer = 0
hundre_potens = math.pow(100, antall_siffer-1)
ti_potens = math.pow(10,antall_siffer-2)
ti_potens2 = math.pow(10,antall_siffer-1)


# stor kube
lengde_stor_kube = 200
stor_kube_pos_x = 220
stor_kube_pos_y = 500 - lengde_stor_kube

# liten kube 
lengde_liten_kube = lengde_stor_kube/5
liten_kube_pos_x = 70
liten_kube_pos_y = 500 - lengde_liten_kube

# Fysikk variabler kuber  
v2_start = -0.9/(ti_potens) # farten stor kube
m2 = 1 * (hundre_potens)

v1_start = 0   # farten liten kube
m1 = 1

# tekst
font = pygame.font.SysFont('arial', 32)
font2 = pygame.font.SysFont('arial', 16)
def tekst(x,y,varibler, tekst):
    tekst_som_vises = font.render(f"{varibler} {tekst} ",True,white)
    vindu.blit(tekst_som_vises,(x, y))

def tekst2(x,y,tekst):
    tekst_som_vises = font.render(tekst,True,white)
    vindu.blit(tekst_som_vises,(x, y))

def tekst_liten(x,y,varibler, tekst):
    tekst_som_vises = font2.render(f"{varibler} {tekst} ",True,white)
    vindu.blit(tekst_som_vises,(x, y))

def alle_tegning():
    #Vindu 
    vindu.fill(Bakgrunn)
    bakke(blue)
    
    # rendre Kuben 
    stor_firkant(stor_kube_pos_x,stor_kube_pos_y,lengde_stor_kube,lengde_stor_kube)
    liten_firkant(liten_kube_pos_x,liten_kube_pos_y,lengde_liten_kube,lengde_liten_kube)

    #tekst som vises i bilde
    tekst(1000,100,Antall_kollisjoner, "Antall treff")
    tekst(1000,150,round(π,7),"")
    tekst(stor_kube_pos_x + lengde_stor_kube/4,stor_kube_pos_y + lengde_stor_kube/2-16 ,100,"Kg") #Tekst stor kube
            
    #liten tekst til liten kube og potensen
    tekst_liten(liten_kube_pos_x + lengde_liten_kube/4,liten_kube_pos_y + lengde_liten_kube/2-8 ,m1,"Kg")
    tekst_liten(stor_kube_pos_x + lengde_stor_kube/2-7,stor_kube_pos_y + lengde_stor_kube/2-20 ,round(antall_siffer),"")
            
    #Fart tekst
    tekst2(200-64,500 + 32,"v1 =")
    tekst(200,500 + 32,int(round(v1_start,7)),"m/s")

    tekst2(1000-64,500 + 32,"v2 =")
    tekst(1000,500 + 32,int(round(v2_start,7)),"m/s")

def kube_start_på_nytt(siffer):
    global stor_kube_pos_x, stor_kube_pos_y,liten_kube_pos_y, liten_kube_pos_x, Antall_kollisjoner
    global v1_start, v2_start, m1, m2, antall_siffer,Liste_kordinater, ti_potens,ti_potens2,hundre_potens, tegning_linje
    global program_kjører
    
    stor_kube_pos_x = 220
    stor_kube_pos_y = 500 - lengde_stor_kube
    liten_kube_pos_x = 70
    liten_kube_pos_y = 500 - lengde_liten_kube
    
    Antall_kollisjoner = 0
    
    antall_siffer = siffer
    
    hundre_potens = math.pow(100, antall_siffer-1)
    ti_potens = math.pow(10,antall_siffer-2)
    ti_potens2 = math.pow(10,antall_siffer-1)
    
    v2_start = -0.9/(ti_potens) 
    m2 = 1 * (hundre_potens)
    v1_start = 0   
    m1 = 1
    Liste_kordinater = []

    if siffer >= 4:
        tegning_linje = False
    else:
        tegning_linje = True


    if siffer == 0:
        v2_start = 0
    program_kjører = True

# telling av kollisjon
Antall_kollisjoner = 0  

# kollidering
kollisjon = False
kollisjon_med_vegg = False
program_kjører = False




# laster inn bilde
start_bilde = pygame.image.load("Bilde_gui.jpg")


# for å toggle de av 
treg_kjør = False
kube_pi = False
forkalring = False 
kube_pi_forklaring = False





# gjør det mulig å avslutte program
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()


    

    # show image
    if treg_kjør == False and kube_pi == False and forkalring == False and kube_pi_forklaring == False:
        vindu.blit(start_bilde, (0,0))

    
    # input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        treg_kjør = False
        kube_pi = False
        forkalring = False
        kube_pi_forklaring = False


    elif keys[pygame.K_e]:
        treg_kjør = True
        # setter de andre til false
        kube_pi = False
        forkalring = False
        kube_pi_forklaring = False
    elif keys[pygame.K_r]:
        kube_pi = True
        # setter de andre til false
        treg_kjør = False
        forkalring = False
        kube_pi_forklaring = False
    elif keys[pygame.K_t]:
        forkalring = True
        # setter de andre til false
        treg_kjør = False
        kube_pi = False
        kube_pi_forklaring = False
    elif keys[pygame.K_k]:
        kube_pi_forklaring = True
        # setter de andre til false
        treg_kjør = False
        kube_pi = False
        forkalring = False


    if treg_kjør == True:
        treg_kjør_program()

    if kube_pi == True:
        kube_pi_program1()
    
    if forkalring == True:
        forkalring_program()
    
    if kube_pi_forklaring == True:
        kube_pi_forklaring_program()


    pygame.display.update()

