#Finne pi ved kollisjon

import random
import time
import pygame
from math import pi as pi

pygame.init()
pygame.font.init()



# desimaler av pi 


antall_siffer = 4 #float(input("Hvor mange siffer av pi? : "))

# Viktige varibler
x_vin,y_vin = (1280),(720)

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

# runtime
start_time = time.time()
def runtime():
    print("Runtime: " + str(time.time() - start_time) + " seconds")

# fuctions that plays a sound file

# legger til noe i en fil
def add_to_file(file_name, var_name, var_value):
    with open(file_name, 'a') as f:
        f.write(f"{var_name} = {var_value}" + '\n')



def play_sound(sound_file):
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()
    


# stor ball
radius_stor_ball = 150
stor_ball_pos_x = 551
stor_ball_pos_y = 500 - radius_stor_ball

# liten ball 
radius_liten_ball = 150
liten_ball_pos_x = 0 + radius_liten_ball + 100
liten_ball_pos_y = stor_ball_pos_y + radius_stor_ball - radius_liten_ball


# Fysikk variabler baller  

v2_start = -300/(10**(antall_siffer-1)) # farten stor ball
m2 = 0.01 * (100**(antall_siffer))

v1_start = 0   # farten liten ball
m1 = 0.01 * 100

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


play_sound("/Users/martinknutsen/Documents/GitHub/ball_pi/CodingChallenges_CC_139_Pi_Collisions_P5_clack.wav")


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
   
    print(v1_start, v2_start)

    if kolisjon == True:
        # utregninger for elastisk kolisjon
        sum_av_M = m2 + m1        
        v2 = ((((m2-m1)*v2_start)+(2*m1*v1_start))/(sum_av_M))
        v1 = ((((m1-m2)*v1_start)+(2*m2*v2_start))/(sum_av_M))

        v1_start = v1 
        v2_start = v2
        kolisjon = False
        play_sound("/Users/martinknutsen/Documents/GitHub/ball_pi/CodingChallenges_CC_139_Pi_Collisions_P5_clack.wav")

        # Endring av fart uten fysikk

    elif kolisjon_med_vegg == True:
        Antall_kolisjoner += 1 
        kolisjon_med_vegg = False

    # støt med veg
    if liten_ball_pos_x - radius_liten_ball <= 0:
        v1_start *= -1
        kolisjon_med_vegg = True
        play_sound("CodingChallenges_CC_139_Pi_Collisions_P5_clack.wav")


    # stopping av simulasjonen 
    if stor_ball_pos_x > x_vin - radius_stor_ball:
       pygame.quit()
       runtime() 
       print(Antall_kolisjoner)
       # adds runtime to test.txt file
       add_to_file("test.txt",antall_siffer,(time.time() - start_time))




    # rendre ballene 
    
    stor_ball(stor_ball_pos_x,stor_ball_pos_y,radius_stor_ball)
    liten_ball(liten_ball_pos_x,liten_ball_pos_y,radius_liten_ball)

    # tekst som vises i bilde
    tekst(1000,100,Antall_kolisjoner, "Antall treff")
    tekst(1000,150,round(pi,7),"")

    
    pygame.display.update()
        