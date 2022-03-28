# Ball_pi med Rami sine forberinger
import pygame
from math import pi as π
pygame.init()
pygame.font.init()

# Viktige varibler
x_vin,y_vin = (1280),(720)
fps = 120

# Farger
background = (30,30,30)
color_ball = (220,244,255)
black = (0,0,0)
blue = (125, 177, 244)
ball_color  = (95, 137, 140)

#vindu etc.
window = pygame.display.set_mode((x_vin,y_vin))
clock = pygame.time.Clock()


# elementer:
def ground(color):
    pygame.draw.rect(window, color, (0,500,x_vin,y_vin), width=0)

def stor_ball(x_kod, y_kod, radius):
    pygame.draw.circle(window, ball_color, (x_kod,y_kod), radius, width=0)

def liten_ball(x_kod, y_kod, radius):
    pygame.draw.circle(window, ball_color, (x_kod,y_kod), radius, width=0)


    

# desimaler av pi 
pi = float(input("Hvor mange siffer av π? : "))
hundre_potens = pi-2
potens_radius = hundre_potens*2


# bevegelses varibler

    # Big ball
radius_big_ball = 100 * (potens_radius)
big_ball_pos_x = 700
big_ball_pos_y = 500 - radius_big_ball


    # small ball 
radius_small_ball = 50
small_ball_pos_x = 0 + radius_small_ball + 100
small_ball_pos_y = big_ball_pos_y + radius_big_ball - radius_small_ball





# Fysikk variabler baller  

v2_start = -2 # farten stor ball
m2 = 100 * (10**(potens_radius))

v1_start = 0   # farten liten ball
m1 = 1



# tekst
font = pygame.font.SysFont('arial', 32)
def tekst(x,y,varibler, tektst):
    tekts_som_vises = font.render(f"{varibler} {tektst} ",True,(255,255,255))
    window.blit(tekts_som_vises,(x, y))






# telling av kolisjon
sum_collision = 0  

# kolidering
collision = False
collision_with_wall = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    window.fill(background)
    ground(blue)

    # Grunnbevegelse 
    big_ball_pos_x += v2_start
    small_ball_pos_x += v1_start

    # støt med annen ball 
    if (big_ball_pos_x - radius_big_ball) <= (small_ball_pos_x + radius_small_ball): 
        collision = True
        sum_collision += 1
    else:
        collision = False

    # tekst som vises i bilde
   
    print(v2_start,v1_start)


    if collision == True:
        # endring av fart og retning
        
    
        # utregninger for elastisk kolisjon
        sum_of_M = m2 + m1        
        v2 = ((((m2-m1)*v2_start)+(2*m1*v1_start))/(sum_of_M))
        v1 = ((((m1-m2)*v1_start)+(2*m2*v2_start))/(sum_of_M))

        v1_start = v1 
        v2_start = v2
        collision = False
        # Endring av fart uten fysikk

    elif collision_with_wall == True:
        sum_collision += 1 
        collision_with_wall = False



    # støt med veg
    if small_ball_pos_x < 0 + radius_small_ball:
        v1_start = -v1_start
        collision_with_wall = True


    

    # stopping av simulasjonen 
    if big_ball_pos_x > 13000:
       pygame.quit()
       print(sum_collision) 

    # rendre ballene 
    stor_ball(big_ball_pos_x,big_ball_pos_y,radius_big_ball)
    liten_ball(small_ball_pos_x,small_ball_pos_y,radius_small_ball)



    # tekst som vises i bilde
    tekst(1000,100,sum_collision, "Antall treff")
    tekst(1000,150,round(π,7),"")


    pygame.display.update()
