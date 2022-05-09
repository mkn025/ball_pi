#Finne π ved kollisjon
import pygame,time,math
from math import pi as π

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
fps = 60
clock = pygame.time.Clock()

#vindu etc.
vindu = pygame.display.set_mode((x_vin,y_vin))

# elementer:
def bakke(farge):
    pygame.draw.rect(vindu, farge, (0,650,x_vin,y_vin), width=0)

def stor_firkant(x_kod, y_kod, x_lengde,y_lengde):
    pygame.draw.rect(vindu,ball_farge,(x_kod, y_kod,x_lengde,y_lengde))

def liten_firkant(x_kod, y_kod, x_lengde,y_lengde):
    pygame.draw.rect(vindu,ball_farge,(x_kod, y_kod,x_lengde,y_lengde))
    
start_time = time.time()
def runtime():
    print("Tid = " + str(time.time() - start_time) + " sekunder")

#lage lyd
def lyd(lyd_fil):
    pygame.mixer.init()
    pygame.mixer.music.load(lyd_fil)
    pygame.mixer.music.play()
    
# desimaler av pi 
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


# start posisjoner til kube 
def kube_start_på_nytt(siffer):
    global stor_kube_pos_x, stor_kube_pos_y,liten_kube_pos_y, liten_kube_pos_x, Antall_kollisjoner 
    global v1_start, v2_start, m1, m2, antall_siffer,L, ti_potens,ti_potens2,hundre_potens, tegning_linje
    
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
    else:
        tegning_linje = True
    print_ferdig()

    



def print_ferdig():
    print("\n")
    print("Antall kollisjoner =",Antall_kollisjoner)
    print("π =",round(π,7))
    runtime()
    print("Antall siffer =",antall_siffer)
    print("\n")

# Fysikk variabler kuber  
v2_start = -0.9/(ti_potens) # farten stor kube
m2 = 1 * (hundre_potens)

v1_start = 0   # farten liten kube
m1 = 1

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

def alle_tegning():
    #Vindu 
    vindu.fill(Bakgrunn)
    pygame.draw.line(vindu, white,(0,y_vin/2), (x_vin,y_vin/2), width=1)
    pygame.draw.line(vindu, white,(x_vin/2,0), (x_vin/2,y_vin), width=1)
    bakke(blue)
    
    # rendre Kuben 
    stor_firkant(stor_kube_pos_x,stor_kube_pos_y,lengde_stor_kube,lengde_stor_kube)
    liten_firkant(liten_kube_pos_x,liten_kube_pos_y,lengde_liten_kube,lengde_liten_kube)

    #tekst som vises i bilde
    tekst(1000,100,Antall_kollisjoner, "Antall treff")
    tekst(1000,150,round(π,7),"")

    #Stor kube
    tekst2(1000-64,y_vin - 64,"m2 =")
    tekst(1000,y_vin - 64 ,100,"Kg")
    tekst_liten(1000+42,y_vin - 68,round(antall_siffer),"")
    tekst2(1000-64,y_vin - 32,"v2 =")
    tekst(1000,y_vin - 32,round(v2_start,int(antall_siffer+6)),"m/s")
    
    #Liten kube
    tekst2(200-64,y_vin - 64,"m1 =")
    tekst(200,y_vin - 64 ,m1,"Kg")
    tekst2(200-64,y_vin - 32,"v1 =")
    tekst(200,y_vin - 32,round(v1_start,int(antall_siffer+6)),"m/s")
    
    #tekst som viser antall siffer
    tekst2(x_vin/2-96, y_vin- 48,"Antall Siffer =")
    tekst(x_vin/2 + 64, y_vin - 48,antall_siffer,"")

# telling av kollisjon
Antall_kollisjoner = 0  
antall_treff_skal_bli = round(π*ti_potens2)

# kollidering
kollisjon = False
kollisjon_med_vegg = False

"""
* Forkalring *
"""
#Tegning av sirkel
v2_start_konstant = 0.9/ti_potens
større = 20 #Hvor mye større sirkel skal være
stor_sirkel_radius = math.sqrt(m2)*(v2_start_konstant)*større
liten_sirkel_radius = 5

#Ting til funskjonene
y0 = float(y_vin/2)
r = float(stor_sirkel_radius)
x0 = float(x_vin/2)

#Funskjonene til store sirkelen 
def h(x):# Bunn 
    return y0 + (math.sqrt(r**2-((x-x0)**2)))

def g(x): # Topp 
    return y0 - (math.sqrt(r**2-((x-x0)**2)))


# kod til ball i sirkel 
x_kod_ball = ((x_vin/2)+(math.sqrt(m2)*(større*v2_start)))
y_kod_ball = ((y_vin/2)+(math.sqrt(m1)*(større*v1_start))) 

def sirkel_tegning():
    #Stor sirkel
    pygame.draw.circle(vindu, rød, (x_vin/2,y_vin/2), stor_sirkel_radius, width=2)
    
    #Liten sirkel og linjer gjennom gjennom 

    pygame.draw.circle(vindu, green, (x_kod_ball,y_kod_ball), liten_sirkel_radius, width=0)
    
    #Aksenavn
    tekst2(x_vin-(192+96),y_vin/2-40,"v2 = math.sqrt(m2)*v2") #X-akse
    tekst2(x_vin/2+5,10,"v1 = math.sqrt(m1)*v1") #Y-akse          #Høyeste v1 altså lik v2 ^
    

L = []

"""
* Programmet *
"""
program_kjører = False
tegning_linje = True

# oppdaterer siffer 

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
        print_ferdig()
        

    elif key[pygame.K_ESCAPE]:
        break 


    alle_tegning()
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
                        pygame.draw.lines(vindu,green,False,L,width=1)
                
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

                    lyd("CodingChallenges_CC_139_Pi_Collisions_P5_clack.wav")
                    kollisjon = False

                # Endring av fart uten fysikk
                elif kollisjon_med_vegg == True:
                    Antall_kollisjoner += 1 
                    lyd("CodingChallenges_CC_139_Pi_Collisions_P5_clack.wav")
                    kollisjon_med_vegg = False

                # støt med veg
                if liten_kube_pos_x <= 0:
                    v1_start *= -1 #Farten går andre veien fordi veggen er "uendlig" masse

                    #Siden liten ball skifter fortegn
                    y_kod_ball = g(x_kod_ball) #Ballen går rett opp på sirkel
                    L.append(kordinater_ball)
                    kollisjon_med_vegg = True

        if stor_kube_pos_x > x_vin:
            program_kjører = False
            pygame.draw.lines(vindu,green,False,L,width=1)
            

        pygame.display.update() 