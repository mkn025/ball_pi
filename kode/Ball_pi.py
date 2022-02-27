from tkinter import E
from turtle import circle
import pygame
pygame.init()


# Viktige varibler
x_vin,y_vin = (1280),(720)
fps = 120

# Farger
Bakgrunn = (30,30,30)
farge_ball = (220,244,255)
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



# bevegelses varibler

    # stor ball
radius_stor_ball = 100
stor_ball_pos_x = 700
stor_ball_pos_y = 500 - radius_stor_ball


    # Fysikk variabler stor ball 
masse_stor_ball = 1000000

    # liten ball 
radius_liten_ball = 50
liten_ball_pos_x = 0 + radius_liten_ball
liten_ball_pos_y = stor_ball_pos_y + radius_stor_ball - radius_liten_ball



    # Fysikk variabler liten ball 

dx_stor_ball = 1 # farten stor ball
masse_stor_ball = 1


dx_liten_ball = 0   # farten liten ball
masse_liten_ball= 1


# kolidering
kolisjon = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    vindu.fill(Bakgrunn)
    bakke(blue)

    # Grunnbevegelse 
    stor_ball_pos_x -= dx_stor_ball
    liten_ball_pos_x += dx_liten_ball


    # støt med annen ball 
    if stor_ball_pos_x - radius_stor_ball < liten_ball_pos_x + radius_liten_ball:
        kolisjon = True
    else:
        kolisjon = False
   

  
    

    if kolisjon == True:
        other = "liten"
        this = "stor"
        sum_av_M = masse_stor_ball + masse_liten_ball
        dx_liten_ball = ((masse_stor_ball-masse_liten_ball)/sum_av_M * dx_stor_ball) + (2*masse_liten_ball/sum_av_M) * dx_liten_ball



 # støt med vegg
    if stor_ball_pos_x > x_vin - radius_stor_ball:
        dx_stor_ball = -dx_stor_ball

    elif liten_ball_pos_x < 0 + radius_liten_ball:
        dx_liten_ball = -dx_liten_ball
    # rendre ballene 
    stor_ball(stor_ball_pos_x,stor_ball_pos_y,radius_stor_ball)
    liten_ball(liten_ball_pos_x,liten_ball_pos_y,radius_liten_ball)
    

    pygame.display.update()
