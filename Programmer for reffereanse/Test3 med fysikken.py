import pygame, math, time

pygame.init
pygame.font.init()

#Ganger fart med 10 fordi vi har gjort radiusen 10 ganger større

#Farger
black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
blue = (125, 177, 244)
yellow = (255,255,0)
bakgrunn = (30,30,30)
rød = (255,0,0)

#Vindu og klokke
x_vin, y_vin = 1280, 720
vindu = pygame.display.set_mode((x_vin,y_vin))
clock = pygame.time.Clock()
FPS = 120

#Tekst
font = pygame.font.SysFont("arial", 32)
def tekst(x,y,varibler, tekst):
    tekts_som_vises = font.render(f"{varibler} {tekst} ",True,white)
    vindu.blit(tekts_som_vises,(x, y))

#Radius
stor_sirkel_radius = 90 #(math.sqrt(m2)*(10*v2_start) 
liten_sirkel_radius = 5

#Ting til funskjonene
y0 = float(y_vin/2)
r = float(stor_sirkel_radius)
x0 = float(x_vin/2)

#Funskjonene til store sirkelen 
def h(x):
    return y0 + (math.sqrt(r**2-((x-x0)**2)))

def g(x):
    return y0 - (math.sqrt(r**2-((x-x0)**2)))


x_kod_ball = ((x_vin/2)+(math.sqrt(m2)*(10*v2_start))) #math.sqrt(m2)*(10*v2_start)
y_kod_ball = (y_vin/2+(math.sqrt(m1)*(10*v1_start))) #math.sqrt(m1)*(10*v1_start)
kordinater_liten_ball = (x_kod_ball,y_kod_ball) 

def tegning():
    vindu.fill(bakgrunn)

    #Stor sirkel
    pygame.draw.circle(vindu, rød, (x_vin/2,y_vin/2), stor_sirkel_radius, width=2)
    
    #Liten sirkel og linjer gjennom gjennom 
    pygame.draw.circle(vindu, green, (x_kod_ball,y_kod_ball), liten_sirkel_radius, width=0)
    pygame.draw.line(vindu, white,(0,y_vin/2), (x_vin,y_vin/2), width=2)
    pygame.draw.line(vindu, white,(x_vin/2,0), (x_vin/2,y_vin), width=2)


#PROGRAMMET:
while True:
    # gjør det mulig å avslutte program
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    for i in range(int(ti_potens2)):
            sum_av_M = m2 + m1        
            v2 = ((((m2-m1)*v2_start)+(2*m1*v1_start))/(sum_av_M))
            v1 = ((((m1-m2)*v1_start)+(2*m2*v2_start))/(sum_av_M))

            v1_start = v1 
            v2_start = v2

    #Hvor rask programm går
    clock.tick(FPS)
    tegning()
    pygame.display.update()