import pygame, math, time

pygame.init
pygame.font.init()

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
stor_sirkel_radius = 200
liten_sirkel_radius = 10

#Ting til funskjonene
y0 = float(y_vin/2)
r = float(stor_sirkel_radius)
x0 = float(x_vin/2)

#Funskjonene til store sirkelen 
def h(x):
    return y0 + (math.sqrt(r**2-((x-x0)**2)))

def g(x):
    return y0 - (math.sqrt(r**2-((x-x0)**2)))

#Liten sirkel kordinater og fart
start_dx = 1   #Må finne formel til disse to
start_dy = 1

dx = start_dx
dy = start_dy

treff_dx = 0
treff_dy = 1

x_kod_ball = ((x_vin/2)-stor_sirkel_radius)
y_kod_ball = (y_vin/2)
kordinater_liten_ball = (x_kod_ball,y_kod_ball)

#Ande ting 
treff = 0
ny_treff = 0

#PROGRAMMET:
while True:
    # gjør det mulig å avslutte program
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    vindu.fill(bakgrunn)

    #Stor sirkel
    pygame.draw.circle(vindu, rød, (x_vin/2,y_vin/2), stor_sirkel_radius, width=2)
    
    #Liten sirkel og linjer gjennom gjennom 
    pygame.draw.circle(vindu, green, (x_kod_ball,y_kod_ball), liten_sirkel_radius, width=0)
    pygame.draw.line(vindu, white,(0,y_vin/2), (x_vin,y_vin/2), width=2)
    pygame.draw.line(vindu, white,(x_vin/2,0), (x_vin/2,y_vin), width=2)

   #Bevegelse liten sirkel
    y_kod_ball += dy
    x_kod_ball += dx

    #Når den treffer øverste halvdel av sirkel
    if y_kod_ball <= g(x_kod_ball) and y_kod_ball < y_vin/2:
        dx = start_dx
        dy = start_dy
        treff += 1

    #Når den treffer nederste halvdel av sirkel
    if y_kod_ball >= h(x_kod_ball) and y_kod_ball > y_vin/2:
        dx = treff_dx
        dy = -treff_dy
        treff += 1
        
    #Liten ball stopper når den når enden av sirkelen på andre siden av start pos
    if y_kod_ball == (y_vin/2) and x_kod_ball >= (x_vin/2 + stor_sirkel_radius):
        ny_treff = treff+1
        dx = 0
        dy = 0
        tekst(1000,100,ny_treff, "Antall treff")
    else:
        tekst(1000,100,treff, "Antall treff")
    
    #Hvor rask programm går
    clock.tick(FPS)

    pygame.display.update()