import pygame,time,math
from math import pi as π

"""
* Forkalring *
"""
pygame.init()
pygame.font.init()

# Viktige varibler
x_vin,y_vin = (1280),(720)

# Farger
Bakgrunn = (30,30,30)
svart = (0,0,0)
blue = (125, 177, 244)
ball_farge  = (95, 137, 140)
white = (255,255,255)
rød = (255,0,0)
green = (0,255,0)
cyan = (0,252,194)
lilla = (85,8,217)
fps = 60
clock = pygame.time.Clock()

#vindu etc.
vindu = pygame.display.set_mode((x_vin,y_vin))

def kube_start_på_nytt(siffer):
    global stor_kube_pos_x, stor_kube_pos_y,liten_kube_pos_y, liten_kube_pos_x, Antall_kollisjoner, v1_start, v2_start, m1, m2, antall_siffer,L, ti_potens,ti_potens2,hundre_potens, tegning_linje
    stor_kube_pos_x = 220 + 400
    stor_kube_pos_y = 650 - lengde_stor_kube
    liten_kube_pos_x = 70
    liten_kube_pos_y = 650 - lengde_liten_kube
    
    Antall_kollisjoner = 0
    
    antall_siffer = siffer
    
    hundre_potens = math.pow(100, antall_siffer-1)
    ti_potens = math.pow(10,antall_siffer-2)
    ti_potens2 = math.pow(10,antall_siffer-1)
    
    v2_start = -0.9/(ti_potens) 
    m2 = 1 * (hundre_potens)
    v1_start = 0   
    m1 = 1
    L = []
    if siffer >= 4:
        tegning_linje = False

    



print("\n")
antall_siffer = 0
hundre_potens = math.pow(100, antall_siffer-1)
ti_potens = math.pow(10,antall_siffer-2)
ti_potens2 = math.pow(10,antall_siffer-1)


# stor kube
lengde_stor_kube = 100
stor_kube_pos_x = 220 + 400
stor_kube_pos_y = 650 - lengde_stor_kube

# liten kube 
lengde_liten_kube = lengde_stor_kube/5
liten_kube_pos_x = 70
liten_kube_pos_y = 650 - lengde_liten_kube

# Fysikk variabler kuber  
v2_start = -0.9/(ti_potens) # farten stor kube
m2 = 1 * (hundre_potens)

v1_start = 0   # farten liten kube
m1 = 1


# telling av kollisjon
Antall_kollisjoner = 0  
antall_treff_skal_bli = round(π*ti_potens2)

# kollidering
kollisjon = False
kollisjon_med_vegg = False

#Tegning av sirkel
v2_start_konstant = 0.9/ti_potens
større = 40 #Hvor mye større sirkel skal være
stor_sirkel_radius = math.sqrt(m2)*(v2_start_konstant)*større
liten_sirkel_radius = 5

#Ting til funskjonene
y0 = float(y_vin/2)
r = float(stor_sirkel_radius)
x0 = float(x_vin/2)

#Funskjonene til store sirkelen 
def h(x):#Bunn 
    return y0 + (math.sqrt(r**2-((x-x0)**2)))

def g(x): #Topp
    return y0 - (math.sqrt(r**2-((x-x0)**2)))

x_kod_ball = ((x_vin/2)+(math.sqrt(m2)*(større*v2_start)))
y_kod_ball = ((y_vin/2)+(math.sqrt(m1)*(større*v1_start))) 

# tekst
font = pygame.font.SysFont('arial', 32)
font2 = pygame.font.SysFont('arial', 16)
def tekst(x,y,varibler, tekst):
    tekst_som_vises = font.render(f"{varibler} {tekst} ",True,white)
    vindu.blit(tekst_som_vises,(x, y))

def tekst2(x,y,tekst):
    tekst_som_vises = font.render(tekst,True,white)
    vindu.blit(tekst_som_vises,(x, y))

def tekst_liten(x,y,varibler, tekst):
    tekst_som_vises = font2.render(f"{varibler} {tekst} ",True,white)
    vindu.blit(tekst_som_vises,(x, y))

start_time = time.time()
def runtime():
    print("Tid = " + str(time.time() - start_time) + " sekunder")

#lage lyd
def lyd(lyd_fil):
    pygame.mixer.init()
    pygame.mixer.music.load(lyd_fil)
    pygame.mixer.music.play()
    

def sirkel_tegning():
    vindu.fill(Bakgrunn)
    #Stor sirkel
    pygame.draw.circle(vindu, lilla, (x_vin/2,y_vin/2), stor_sirkel_radius, width=2)
    
    #Liten sirkel og linjer gjennom gjennom 
    pygame.draw.line(vindu, white,(0,y_vin/2), (x_vin,y_vin/2), width=1)
    pygame.draw.line(vindu, white,(x_vin/2,0), (x_vin/2,y_vin), width=1)
    pygame.draw.circle(vindu, rød, (x_kod_ball,y_kod_ball), liten_sirkel_radius, width=0)
    
    #Aksenavn
    tekst2(x_vin-(192+96),y_vin/2-40,"v2 = math.sqrt(m2)*v2") #X-akse
    tekst2(x_vin/2,10,"v1 = math.sqrt(m1)*v1") #Y-akse          #Høyeste v1 altså lik v2 ^
    

L = []

"""
* Programmet *
"""
program_kjører = False
tegning_linje = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    # Definere key
    key = pygame.key.get_pressed()

    if antall_siffer == 0:
        v2_start = 0
        program_kjører = True
  
    # Test for tast
    if key[pygame.K_1]:         
        program_kjører = True
        siffer_update = 1
        kube_start_på_nytt(siffer_update)
    elif key[pygame.K_2]:
        program_kjører = True
        siffer_update = 2
        kube_start_på_nytt(siffer_update)
    elif key[pygame.K_3]:
        program_kjører = True
        siffer_update = 3
        kube_start_på_nytt(siffer_update)
    elif key[pygame.K_4]:
        program_kjører = True
        siffer_update = 4
        kube_start_på_nytt(siffer_update)
    elif key[pygame.K_5]:
        program_kjører = True
        siffer_update = 5
        kube_start_på_nytt(siffer_update)
    elif key[pygame.K_6]:
        program_kjører = True
        siffer_update = 6
        kube_start_på_nytt(siffer_update)
    elif key[pygame.K_7]:
        program_kjører = True
        siffer_update = 7
        kube_start_på_nytt(siffer_update)

        

    elif key[pygame.K_ESCAPE]:
        break 


    sirkel_tegning()
    clock.tick(fps)

    if program_kjører == True:
        for i in range(int(ti_potens2)):
                
                # Grunnbevegelse 
                stor_kube_pos_x += v2_start
                liten_kube_pos_x += v1_start

                #Kordinater liten ball
                x_kod_ball = ((x_vin/2)+(math.sqrt(m2)*(større*v2_start)))
                y_kod_ball = ((y_vin/2)-(math.sqrt(m1)*(større*v1_start)))
                kordinater_ball = (x_kod_ball,y_kod_ball)
                L.append(kordinater_ball)

                #lager linje i sirkel
                if Antall_kollisjoner >= 1:
                    if tegning_linje == True:
                        pygame.draw.lines(vindu,cyan,False,L,width=2)
                
                # støt mellom kubene
                if (liten_kube_pos_x+lengde_liten_kube) < (stor_kube_pos_x) or (liten_kube_pos_x) > (stor_kube_pos_x+lengde_stor_kube): 
                    kollisjon = False
                else:
                    Antall_kollisjoner += 1
                    kollisjon = True

                if kollisjon == True:
                    # utregninger for elastisk kollisjon
                    sum_av_M = m2 + m1        
                    v2 = ((((m2-m1)*v2_start)+(2*m1*v1_start))/(sum_av_M))
                    v1 = ((((m1-m2)*v1_start)+(2*m2*v2_start))/(sum_av_M))
                    v1_start = v1 
                    v2_start = v2

                    #Sirkel kordinater liste
                    L.append(kordinater_ball)

                    lyd("klikkelyd.wav")
                    kollisjon = False

                # Endring av fart uten fysikk
                elif kollisjon_med_vegg == True:
                    Antall_kollisjoner += 1 
                    lyd("klikkelyd.wav")
                    kollisjon_med_vegg = False

                # støt med veg
                if liten_kube_pos_x <= 0:
                    v1_start *= -1 #Farten går andre veien fordi veggen er "uendlig" masse

                    #Siden liten ball skifter fortegn
                    y_kod_ball = g(x_kod_ball) #Ballen går rett opp på sirkel
                    L.append(kordinater_ball)
                    kollisjon_med_vegg = True

        if stor_kube_pos_x > x_vin:
            print("Antall kollisjoner =",Antall_kollisjoner)
            print("π =",round(π,7))
            runtime()
            print("Antall siffer =",antall_siffer)
            program_kjører = False
            pygame.draw.lines(vindu,cyan,False,L,width=2)

        pygame.display.update()