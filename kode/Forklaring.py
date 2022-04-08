import pygame

x_vin,y_vin = 1280,720

# farger
Bakgrunn = (30,30,30)
svart = (0,0,0) 
blue = (125, 177, 244)
green = (0,255,0)
ball_farge  = (95, 137, 140)
white = (255,255,255)


vindu = pygame.display.set_mode((x_vin,y_vin))

# elementer 
def bakke(farge):
    pygame.draw.rect(vindu, farge, (0,500,x_vin,y_vin), width=0)


# parametere for sikel
radius_stor_sirkel = 200


# paramentre for liten ball 
radius_liten_ball = 10

def linjer(start_pos, end_pos,width):
    pygame.draw.line(vindu, white, (start_pos), (end_pos), width=width)

x_pos_liten_ball, y_pos_liten_ball = x_vin/2-radius_stor_sirkel, y_vin/2

    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    

    vindu.fill(Bakgrunn)
    # hele sikel
    pygame.draw.circle(vindu, blue, (x_vin/2,y_vin/2), radius_stor_sirkel, width=1)
    pygame.draw.circle(vindu, blue, (x_vin/2-radius_stor_sirkel,y_vin/2), radius_liten_ball, width=0)
    

    # liten ball som skal kolidere
    pygame.draw.circle(vindu, blue, (x_pos_liten_ball,y_pos_liten_ball), radius_liten_ball, width=0)

  
    

    pygame.display.update()

