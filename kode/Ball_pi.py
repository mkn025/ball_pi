
import pygame
pygame.init()
pygame.font.init()

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


    # liten ball 
radius_liten_ball = 50
liten_ball_pos_x = 0 + radius_liten_ball + 100
liten_ball_pos_y = stor_ball_pos_y + radius_stor_ball - radius_liten_ball



    # Fysikk variabler liten ball 

dx_stor_ball = 1 # farten stor ball
masse_stor_ball = 1


dx_liten_ball = 0   # farten liten ball
masse_liten_ball= 1


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
    stor_ball_pos_x -= dx_stor_ball
    liten_ball_pos_x += dx_liten_ball


    # støt med annen ball 
    if stor_ball_pos_x - radius_stor_ball < liten_ball_pos_x + radius_liten_ball:
        kolisjon = True

    else:
        kolisjon = False

    # tekst som vises i bilde
    tekst(1000,100,Antall_kolisjoner, "Antall treff")
    
    print(dx_stor_ball,dx_liten_ball)
    if kolisjon == True:
        # endring av fart og retning

        Antall_kolisjoner += 1

            
        
        # utregninger for elastisk kolisjon
       
        stor_b = "m1"
        liten_b = "m2"
        dx_liten_ball = "u1"
        dx_stor_ball = "u2"

        sum_av_M = masse_stor_ball + masse_liten_ball
        dx_liten_ball = (((masse_stor_ball-masse_liten_ball)/(sum_av_M)) * dx_liten_ball) + ((2*masse_liten_ball/sum_av_M) * dx_stor_ball)
        dx_liten_ball = (((masse_stor_ball-masse_liten_ball)/(sum_av_M))* dx_stor_ball) + ((2*masse_stor_ball/sum_av_M)*dx_liten_ball)
        
        
        #dx_liten_ball = -dx_liten_ball

        # Endring av fart uten fysikk
        #dx_liten_ball = -dx_liten_ball
        #dx_stor_ball = -dx_stor_ball


    elif kolisjon_med_vegg == True:
        Antall_kolisjoner += 1 
        kolisjon_med_vegg = False


 # støt med vegg
    if stor_ball_pos_x > x_vin - radius_stor_ball:
        dx_stor_ball = -dx_stor_ball
        

    elif liten_ball_pos_x < 0 + radius_liten_ball:
        dx_liten_ball = -dx_liten_ball
        kolisjon_med_vegg = True
    


    # rendre ballene 
    stor_ball(stor_ball_pos_x,stor_ball_pos_y,radius_stor_ball)
    liten_ball(liten_ball_pos_x,liten_ball_pos_y,radius_liten_ball)
    

    pygame.display.update()
