#Finne π ved kollisjon
import pygame,time,math


pygame.init()
pygame.font.init()

# størrelser på vindu 
x_vin,y_vin = (1280),(720)

# Farger og noen varibler
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

# elementer:
def bakke(farge):
    pygame.draw.rect(vindu, farge, (0,650,x_vin,y_vin), width=0)

def stor_firkant(x_kod, y_kod, x_lengde,y_lengde):
    pygame.draw.rect(vindu,ball_farge,(x_kod, y_kod,x_lengde,y_lengde))

def liten_firkant(x_kod, y_kod, x_lengde,y_lengde):
    pygame.draw.rect(vindu,ball_farge,(x_kod, y_kod,x_lengde,y_lengde))


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
    global v1_start, v2_start, m1, m2, antall_siffer,Liste_kordinater, ti_potens,ti_potens2,hundre_potens
    global program_kjører, tegning_linje
    
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
    Liste_kordinater = []

    if siffer >= 4:
        tegning_linje = False
    else:
        tegning_linje = True


    if siffer == 0:
        v2_start = 0
    program_kjører = True


# Fysikk variabler kuber  
v2_start = -0.9/(ti_potens) # farten stor kube
m2 = 1 * (hundre_potens)

v1_start = 0   # farten liten kube
m1 = 1




# funksjoner for tekst
def tekst_vanlig(x,y,tekst, font_størrelse):
    tekst_som_vises = pygame.font.SysFont('arial', font_størrelse).render(tekst,True,white)  # 32
    vindu.blit(tekst_som_vises,(x, y))


def tekst(x,y,varibler, tekst, font_størrelse):
    tekst_som_vises = pygame.font.SysFont('arial', font_størrelse).render(f"{varibler} {tekst} ",True,white)
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
    tekst(1000,100,Antall_kollisjoner, "Antall treff",32)
    tekst(1000,150,round(math.pi,7),"",32)

    #Stor kube
    tekst_vanlig(1000-64,y_vin - 64,"m2 =",32)
    tekst(1000,y_vin - 64 ,100,"Kg",32)
    tekst(1000+42,y_vin - 68,round(antall_siffer-1),"",16)
    tekst_vanlig(1000-64,y_vin - 32,"v2 =",32)
    tekst(1000,y_vin - 32,round(v2_start,int(antall_siffer+6)),"m/s",32)
    
    #Liten kube
    tekst_vanlig(200-64,y_vin - 64,"m1 =",32)
    tekst(200,y_vin - 64 ,m1,"Kg",32)
    tekst_vanlig(200-64,y_vin - 32,"v1 =",32)
    tekst(200,y_vin - 32,round(v1_start,int(antall_siffer+6)),"m/s",32)
    
    #tekst som viser antall siffer
    tekst_vanlig(x_vin/2-96, y_vin- 48,"Antall Siffer =",32)
    tekst(x_vin/2 + 64, y_vin - 48,antall_siffer,"",32)

# telling av kollisjon
Antall_kollisjoner = 0  
antall_treff_skal_bli = round(math.pi*ti_potens2)


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

# Funskjonen til sirkel
def h(x): # Bunn 
    return y0 + (math.sqrt(r**2-((x-x0)**2))) 

def g(x): # Topp 
    return y0 - (math.sqrt(r**2-((x-x0)**2)))


# kod til ball i sirkel 
x_kod_ball = ((x_vin/2)-(math.sqrt(m2)*(større*v2_start_konstant)))
y_kod_ball = ((y_vin/2)-(math.sqrt(m1)*(større*v1_start))) 

def sirkel_tegning():
    #Stor sirkel
    pygame.draw.circle(vindu, lilla, (x_vin/2,y_vin/2), stor_sirkel_radius, width=2)
    
    #Liten sirkel og linjer gjennom gjennom 

    pygame.draw.circle(vindu, rød, (x_kod_ball,y_kod_ball), liten_sirkel_radius, width=0)
    
    #Aksenavn
    tekst_vanlig(x_vin-(192+96),y_vin/2-40,"v2 = math.sqrt(m2)*v2",32) #X-akse
    tekst_vanlig(x_vin/2+5,10,"v1 = math.sqrt(m1)*v1",32) #Y-akse          #Høyeste v1 altså lik v2 ^
    
# liste av kordinatene til punktene som linjen trekkes igjennom
Liste_kordinater = []


"""
* Programmet *
"""
program_kjører = True
tegning_linje = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    # Definere key
    key = pygame.key.get_pressed()

    if key[pygame.K_0]:         
        kube_start_på_nytt(0)
    elif key[pygame.K_1]:         
        kube_start_på_nytt(1)
    elif key[pygame.K_2]:
        kube_start_på_nytt(2)
    elif key[pygame.K_3]:
        kube_start_på_nytt(3)
    elif key[pygame.K_4]:
        kube_start_på_nytt(4)
    elif key[pygame.K_5]:
        kube_start_på_nytt(5)
    elif key[pygame.K_6]:
        kube_start_på_nytt(6)     
    elif key[pygame.K_7]:
        kube_start_på_nytt(7)
    elif key[pygame.K_ESCAPE]:
        break 
    

    # kaller på funksjonene som tegner i programmet
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
                Liste_kordinater.append(kordinater_ball)
                
                #lager linje i sirkel
                if Antall_kollisjoner >= 1:
                    if tegning_linje == True:
                        pygame.draw.lines(vindu,cyan,False,Liste_kordinater,width=2)
                
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
                    Liste_kordinater.append(kordinater_ball)

                    try:
                        lyd("klikkelyd.wav")
                    except:
                        print("lyd_fil ikke funnet")
                    
                    kollisjon = False

                # Endring av fart uten fysikk
                elif kollisjon_med_vegg == True:
                    Antall_kollisjoner += 1 
                    try:
                        lyd("klikkelyd.wav")
                    except:
                        print("lyd_fil ikke funnet")
                        
                    kollisjon_med_vegg = False

                # støt med veg
                if liten_kube_pos_x <= 0:
                    v1_start *= -1 #Farten går andre veien fordi veggen er "uendlig" masse

                    #Siden liten ball skifter fortegn
                    y_kod_ball = g(x_kod_ball) #Ballen går rett opp på sirkel
                    Liste_kordinater.append(kordinater_ball)
                    kollisjon_med_vegg = True

        if stor_kube_pos_x > x_vin:
            program_kjører = False
            pygame.draw.lines(vindu,cyan,False,Liste_kordinater,width=2)
        
        pygame.display.update() 