

import pygame, math
pygame.init

# farger
black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
blue = (125, 177, 244)
yellow = (255,255,0)
bakgrunn = (30,30,30)

# vindu og klokke
x_vin, y_vin = 1280, 720
vindu = pygame.display.set_mode((x_vin,y_vin))
clock = pygame.time.Clock()




y0 = float(y_vin/2)
r = float(200)
x0 = float(x_vin/2)


# funskjoner 
def h(x):
    return y0 + (math.sqrt(r**2-((x-x0)**2)))

def g(x):
    return y0 - (math.sqrt(r**2-((x-x0)**2)))

z = -r + x0 
k = -r + x0

treff = True

# bal kodd
dx = 0.9
dy = -0.2

x_kod_ball = x_vin/2 -200
y_kod_ball = y_vin/2
kordinater_liten_ball = (x_kod_ball,y_kod_ball)

# gjør det mulig å avslutte program
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    vindu.fill(bakgrunn)

    pygame.draw.circle(vindu, yellow, (x_vin/2,y_vin/2), 200, width=1)
    

    # kall kræsj

    pygame.draw.circle(vindu, yellow, (x_kod_ball,y_kod_ball), 10, width=0)
    pygame.draw.line(vindu, white,(0,y_vin/2), (x_vin,y_vin/2), width=1)
    
    y_kod_ball += -dy
    x_kod_ball += dx
    
    if y_kod_ball <= g(x_kod_ball):
        dx = -dx
        dy = -dy
        
    if y_kod_ball >= h(x_kod_ball):
        dx = -dx
        dy = -dy

    

    pygame.display.update()  