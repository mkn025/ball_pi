#Finne π ved kollisjon

import pygame
import math
from math import pi as π
pygame.init()
pygame.font.init()

# Viktige varibler
x_vin,y_vin = (1280),(720)

clock = pygame.time.Clock()
# Farger
Bakgrunn = (30,30,30)
svart = (0,0,0)
blue = (125, 177, 244)
ball_farge  = (95, 137, 140)

#vindu etc.
vindu = pygame.display.set_mode((x_vin,y_vin))
clock = pygame.time.Clock()


# elementer:
def bakke(farge):
    pygame.draw.rect(vindu, farge, (0,500,x_vin,y_vin), width=0)

def stor_ball(x_kod, y_kod, radius):
    pygame.draw.circle(vindu, ball_farge, (x_kod,y_kod), radius, width=0)

def liten_ball(x_kod, y_kod, radius):
    pygame.draw.circle(vindu, ball_farge, (x_kod,y_kod), radius, width=0)

#lage lyd
def lyd(lyd_fil):
    pygame.mixer.init()
    pygame.mixer.music.load(lyd_fil)
    pygame.mixer.music.play()
    


# desimaler av pi 
antall_siffer = float(input("Hvor mange siffer av π? : "))
hundre_potens = math.pow(100, antall_siffer-1)
FPS = 200 *hundre_potens

# bevegelses varibler

    # stor ball
radius_stor_ball = 100
stor_ball_pos_x = 400
stor_ball_pos_y = 500 - radius_stor_ball

    # liten ball 
radius_liten_ball = 50
liten_ball_pos_x = 0 + radius_liten_ball + 100
liten_ball_pos_y = stor_ball_pos_y + radius_stor_ball - radius_liten_ball


# Fysikk variabler baller  

v2_start = -300 / (10**antall_siffer-1) # farten stor ball
m2 = 1 * (hundre_potens)

v1_start = 0   # farten liten ball
m1 = 1

# tekst
font = pygame.font.SysFont('arial', 32)
def tekst(x,y,varibler, tektst):
    tekts_som_vises = font.render(f"{varibler} {tektst} ",True,(255,255,255))
    vindu.blit(tekts_som_vises,(x, y))

# telling av kolisjon
Antall_kolisjoner = 0  

# kolidering
kolisjon = False
kolisjon_med_vegg = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    vindu.fill(Bakgrunn)
    bakke(blue)

    # Grunnbevegelse 
    stor_ball_pos_x += v2_start
    liten_ball_pos_x += v1_start

    # støt med annen ball 
    if (liten_ball_pos_x + radius_liten_ball) < (stor_ball_pos_x - radius_stor_ball) or (liten_ball_pos_x - radius_liten_ball) > (stor_ball_pos_x + radius_stor_ball): 
        kolisjon = False
    else:
        Antall_kolisjoner += 1
        kolisjon = True
    # tekst som vises i bilde
   
    #print(v2_start,v1_start)

    if kolisjon == True:
        # endring av fart og retning

    

        # utregninger for elastisk kolisjon
        sum_av_M = m2 + m1        
        v2 = ((((m2-m1)*v2_start)+(2*m1*v1_start))/(sum_av_M))
        v1 = ((((m1-m2)*v1_start)+(2*m2*v2_start))/(sum_av_M))

        v1_start = v1 
        v2_start = v2
        lyd("CodingChallenges_CC_139_Pi_Collisions_P5_clack.wav")
        kolisjon = False
        # Endring av fart uten fysikk

    elif kolisjon_med_vegg == True:
        Antall_kolisjoner += 1 
        lyd("CodingChallenges_CC_139_Pi_Collisions_P5_clack.wav")
        kolisjon_med_vegg = False

    # støt med veg
    if liten_ball_pos_x < 0 + radius_liten_ball:
        v1_start *= -1
        kolisjon_med_vegg = True

    # stopping av simulasjonen 
    if stor_ball_pos_x > 6000:
       pygame.quit()
       print(Antall_kolisjoner) 

    # rendre ballene 
    stor_ball(stor_ball_pos_x,stor_ball_pos_y,radius_stor_ball)
    liten_ball(liten_ball_pos_x,liten_ball_pos_y,radius_liten_ball)

    # tekst som vises i bilde
    tekst(1000,100,Antall_kolisjoner, "Antall treff")
    tekst(1000,150,round(π,7),"")
    tekst(stor_ball_pos_x,stor_ball_pos_y,antall_siffer,"Kg")
    clock.tick(FPS)
    pygame.display.update()
