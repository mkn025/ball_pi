from pickle import FALSE
from re import I
import pygame

x_vin,y_vin = 1280,720

# farger
Bakgrunn = (30,30,30)
svart = (0,0,0) 
blue = (125, 177, 244)
green = (0,255,0)
ball_farge  = (95, 137, 140)
white = (255,255,255)
rød = (255,0,0)


vindu = pygame.display.set_mode((x_vin,y_vin))

# elementer 
def bakke(farge):
    pygame.draw.rect(vindu, farge, (0,500,x_vin,y_vin), width=0)

# parametere for stor sikel
radius_stor_sirkel = 200

# paramentre for liten ball 
radius_liten_ball = 10
x_pos_liten_ball, y_pos_liten_ball = x_vin/2-radius_stor_sirkel, y_vin/2

bevegelses_x = True
bevegelses_y = True

dx = 1
dy = 1

#Definisjon av ting
def bakgrunn():
    vindu.fill(Bakgrunn) 

def linjer(farge,start_pos, end_pos,width):
    pygame.draw.line(vindu, farge, (start_pos), (end_pos), width=width)

def sirkel(Kordinater,radius,width):
    pygame.draw.circle(vindu,blue, (Kordinater),radius,width=width)

treff_1 = False
treff_2 = 1
treff_3 = 1

#program    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    

    #Bevegelse
    if bevegelses_x:
        x_pos_liten_ball += dx
    if bevegelses_y:
        y_pos_liten_ball += dy
    



    if x_pos_liten_ball == (x_vin/2) and y_pos_liten_ball == (y_vin/2 + radius_stor_sirkel):
        bevegelses_x = False
        dy = -dy
        treff_1 = True
        treff_2 = 2 




    if x_pos_liten_ball == (x_vin/2) and y_pos_liten_ball == (y_vin/2 - radius_stor_sirkel):
        dy = -dy
        bevegelses_x = True
        treff_2 = 3
        treff_3 = 2

        




    #Vindu farge
    bakgrunn()

    #Stor sikel
    sirkel((x_vin/2,y_vin/2),radius_stor_sirkel,1)
    
    # liten ball som skal kolidere
    sirkel((x_pos_liten_ball,y_pos_liten_ball),radius_liten_ball,0)
    
    # vannrett linje
    linjer(white,(0,y_vin/2),(x_vin,y_vin/2),1)
    
    # loddrett linje
    linjer(white,(x_vin/2,0),(x_vin/2,y_vin),1)
    
    #linje som følger sirkel
    if treff_1 == False:
        linjer(rød,(x_vin/2-radius_stor_sirkel,y_vin/2),(x_pos_liten_ball,y_pos_liten_ball),3)

    if treff_1 == True:
        linjer(rød,(x_vin/2-radius_stor_sirkel,y_vin/2),(x_vin/2,y_vin/2+radius_stor_sirkel),3)

    if treff_2 == 2:
        linjer(rød,(x_vin/2,y_vin/2+radius_stor_sirkel),(x_pos_liten_ball,y_pos_liten_ball),3)

    if treff_2 == 3:
        linjer(rød,(x_vin/2,y_vin/2+radius_stor_sirkel),(x_vin/2,y_vin/2 - radius_stor_sirkel),3)

    if treff_3 == 2:
        linjer(rød,(x_vin/2,y_vin/2 - radius_stor_sirkel),(x_pos_liten_ball,y_pos_liten_ball),3)


    pygame.display.update()
