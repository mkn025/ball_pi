#Finne π ved kollisjon
import pygame
import time
import math
from math import pi as π

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
rød = (255,0,0)
green = (0,255,0)
fps = 60
clock = pygame.time.Clock()

#vindu etc.
vindu = pygame.display.set_mode((x_vin,y_vin))

# elementer:
def bakke(farge):
    pygame.draw.rect(vindu, farge, (0,650,x_vin,y_vin), width=0)

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
antall_siffer = float(input("Hvor mange siffer av π? : "))
hundre_potens = math.pow(100, antall_siffer-1)
ti_potens = math.pow(10,antall_siffer-2)
ti_potens2 = math.pow(10,antall_siffer-1)


# stor kube
lengde_stor_kube = 200
stor_kube_pos_x = 220
stor_kube_pos_y = 650 - lengde_stor_kube

# liten kube 
lengde_liten_kube = lengde_stor_kube/5
liten_kube_pos_x = 70
liten_kube_pos_y = 650 - lengde_liten_kube

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
    tekst2(200-64,650 + 32,"v1 =")
    tekst(200,650 + 32,round_v1,"m/s")

    tekst2(1000-64,650 + 32,"v2 =")
    tekst(1000,650 + 32,round_v2,"m/s")

# telling av kollisjon
Antall_kollisjoner = 0  

# kollidering
kollisjon = False
kollisjon_med_vegg = False

"""
* Forkalring *
"""
#Tegning av sirkel
stor_sirkel_radius = 90 #(math.sqrt(m2)*(10*v2_start) 
liten_sirkel_radius = 5

#Ting til funskjonene
y0 = float(y_vin/2)
r = float(stor_sirkel_radius)
x0 = float(x_vin/2)

#Funskjonene til store sirkelen 
def h(x):#Bunn 
    return y0 + (math.sqrt(r**2-((x-x0)**2)))

def g(x): #Topp
    return y0 - (math.sqrt(r**2-((x-x0)**2)))

x_kod_ball = ((x_vin/2)+(math.sqrt(m2)*(10*v2_start)))
y_kod_ball = ((y_vin/2)+(math.sqrt(m1)*(10*v1_start))) 

def sikrel_tegning():
    #Stor sirkel
    pygame.draw.circle(vindu, rød, (x_vin/2,y_vin/2), stor_sirkel_radius, width=2)
    
    #Liten sirkel og linjer gjennom gjennom 
    pygame.draw.circle(vindu, green, (x_kod_ball,y_kod_ball), liten_sirkel_radius, width=0)
    pygame.draw.line(vindu, white,(0,y_vin/2), (x_vin,y_vin/2), width=2)
    pygame.draw.line(vindu, white,(x_vin/2,0), (x_vin/2,y_vin), width=2)



"""
* Programmet *
"""

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    for i in range(int(ti_potens2)):
            round_v1 = round(v1_start,int(antall_siffer+6))
            round_v2 = round(v2_start,int(antall_siffer+6))

            # Grunnbevegelse 
            stor_kube_pos_x += v2_start
            liten_kube_pos_x += v1_start

            # støt mellom kubene
            if (liten_kube_pos_x+lengde_liten_kube) < (stor_kube_pos_x) or (liten_kube_pos_x) > (stor_kube_pos_x+lengde_stor_kube): 
                kollisjon = False
            else:
                Antall_kollisjoner += 1
                kollisjon = True

            if kollisjon == True:
                # utregninger for elastisk kollisjon
                sum_av_M = m2 + m1        
                v2 = ((((m2-m1)*v2_start)+(2*m1*v1_start))/(sum_av_M))
                v1 = ((((m1-m2)*v1_start)+(2*m2*v2_start))/(sum_av_M))

                v1_start = v1 
                v2_start = v2

                #Sirkel kordinater
                x_kod_ball = ((x_vin/2)+(math.sqrt(m2)*(10*v2)))
                y_kod_ball = ((y_vin/2)-(math.sqrt(m1)*(10*v1)))

                lyd("CodingChallenges_CC_139_Pi_Collisions_P5_clack.wav")
                kollisjon = False
            # Endring av fart uten fysikk
            elif kollisjon_med_vegg == True:
                Antall_kollisjoner += 1 
                lyd("CodingChallenges_CC_139_Pi_Collisions_P5_clack.wav")
                kollisjon_med_vegg = False
            # støt med veg
            if liten_kube_pos_x <= 0:
                v1_start *= -1
                y_kod_ball = g(x_kod_ball)
                kollisjon_med_vegg = True

    if stor_kube_pos_x > x_vin:
        print("Antall kollisjoner =",Antall_kollisjoner)
        print("π =",round(π,7))
        runtime()
        print("\n")
        break

    alle_tegning()
    sikrel_tegning()
    clock.tick(fps)
    pygame.display.update() 