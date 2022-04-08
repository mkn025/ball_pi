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

def linjer(start_pos, end_pos,width,farge):
    pygame.draw.line(vindu, farge, (start_pos), (end_pos), width=width)

def sirkel(Kordinater,radius,width):
    pygame.draw.circle(vindu,blue, (Kordinater),radius,width=width)

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
    if x_pos_liten_ball == (x_vin/2) and y_pos_liten_ball == (y_vin/2 - radius_stor_sirkel):
        dy = -dy
        bevegelses_x = True




    #Vindu farge
    bakgrunn()

    linjer((x_vin/2-radius_stor_sirkel, y_vin/2),(x_pos_liten_ball, y_pos_liten_ball),3,rød)

    #Stor sikel
    sirkel((x_vin/2,y_vin/2),radius_stor_sirkel,1)
    
    # liten ball som skal kolidere
    sirkel((x_pos_liten_ball,y_pos_liten_ball),radius_liten_ball,0)
    
    # vannrett linje
    linjer((0,y_vin/2),(x_vin,y_vin/2),1,white)
    
    # loddrett linje
    linjer((x_vin/2,0),(x_vin/2,y_vin),1,white)
    

    pygame.display.update()
