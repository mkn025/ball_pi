

from pickle import TRUE
import pygame, math, time
pygame.init

#Farger
black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
blue = (125, 177, 244)
yellow = (255,255,0)
bakgrunn = (30,30,30)

#Vindu og klokke
x_vin, y_vin = 1280, 720
vindu = pygame.display.set_mode((x_vin,y_vin))
clock = pygame.time.Clock()

font = pygame.font.SysFont('arial', 32)
def tekst(x,y,varibler, tektst):
    tekts_som_vises = font.render(f"{varibler} {tektst} ",True,white)
    vindu.blit(tekts_som_vises,(x, y))

#Ting til funskjonene
y0 = float(y_vin/2)
r = float(200)
x0 = float(x_vin/2)

#Funskjonene til store sirkelen 
def h(x):
    return y0 + (math.sqrt(r**2-((x-x0)**2)))

def g(x):
    return y0 - (math.sqrt(r**2-((x-x0)**2)))

#Radius stor sirkel
stor_sikrel_radius = 200
liten_sirkel_radius = 10

#Liten sirkel kordinater og fart
start_dx = 1   #Må finne formel til disse to
dy = 1

dx = start_dx
treff_dx = 0
dx_t_f = True #Dx true/false

x_kod_ball = ((x_vin/2)-stor_sikrel_radius)
y_kod_ball = (y_vin/2)
kordinater_liten_ball = (x_kod_ball,y_kod_ball)
#Ande ting 
Treff = 0

#PROGRAMMET:
while True:
    # gjør det mulig å avslutte program
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    vindu.fill(bakgrunn)

    #Stor sirkel
    pygame.draw.circle(vindu, yellow, (x_vin/2,y_vin/2), stor_sikrel_radius, width=1)
    
    #Liten sirkel og linjer gjennom gjennom 
    pygame.draw.circle(vindu, yellow, (x_kod_ball,y_kod_ball), liten_sirkel_radius, width=0)
    pygame.draw.line(vindu, white,(0,y_vin/2), (x_vin,y_vin/2), width=1)
    
    #Bevegelse liten sirkel
    y_kod_ball += dy
    x_kod_ball += dx
    
    #Definere når dx skal være 0 eller noe annet
    if dx_t_f == True:
        dx = start_dx
    elif dx_t_f == False:
        dx = treff_dx

    #Når den treffer øverste halvdel av sirkel
    if y_kod_ball <= g(x_kod_ball) and y_kod_ball < y_vin/2:
        dx = -dx
        dy = -dy
        dx_t_f = True
        Treff+=1

    #Når den treffer nederste halvdel av sirkel
    if y_kod_ball >= h(x_kod_ball) and y_kod_ball > y_vin/2:
        dy = -dy
        dx_t_f = False
        Treff += 1
        
    #Liten ball stopper når den når enden av sirkelen på andre siden av start pos
    if y_kod_ball == (y_vin/2) and x_kod_ball == (x_vin/2 + stor_sikrel_radius):
        dx = 0
        dy = 0
        Ny_Treff = Treff+1
        
    print("Antall treff er",Ny_Treff)
    tekst(1000,100,Ny_Treff, "Antall treff")

    pygame.display.update()  