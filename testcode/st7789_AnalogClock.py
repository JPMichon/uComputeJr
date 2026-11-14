#----------------------------------------------------------------
# Prerequest: ST7789 as display
#
# Compatibility: Work with all PICO version
# JPMichon  11/2026
#
# https://github.com/JPMichon/uComputeJr
#----------------------------------------------------------------
from machine import UART, Pin, SPI, ADC
import time
import math
import struct
import st7789
import framebuf2

IS_Junior = True
# ---------------------------------------------------------------
# uCompute standard pins
_SSD1306_ADDR = 0x3C
_Buzzer = 11 # définition du  buzzer (GP11)
_MicroSD_Select = 13 # définition de la pin Select du SDCARD (GP13)
_SPI1_SCK = 14 # SPI1_shared Clock
_SPI1_MOSI = 15 # SPI1_shared MOSI
_SPI1_MISO = 12 # SPI1_shared MISO
_Led_System = 25 # définition du port  del systeme (GP25)
_I2C_SDA = 20 # définition de Data du I2C(0) (GP20)
_I2C_SCL = 21 # définition de SCL du I2C(0) (GP21)
_Boutons = 26 # définition du port analogue des boutons (GP26)
_ST7789_SCK = 2 # définition de la pin Clock du ST7789 (GP2) SPI0
_ST7789_MOSI = 3 # définition de la pin MOSI du ST7789 (GP3) SPI0
_ST7789_RESET = 4 # définition de la pin Reset du ST7789 (GP4)
_ST7789_DC = 5 # définition de la pinSelect du ST7789 (GP5)
# Definition des Pins pour le module ESP12f du addon-on modile
_Comm_TX = 8 # definition de la pin TX du add-on module
_Comm_RX = 9 # definition de la pin RX du add-on module
_Comm_EN = 12 # definition de la pin ENABLE du add-on module
_Comm_RST = 10 # definition de la pin RESET du add-on module

# --- CONFIGURATION MATÉRIELLE ---
if IS_Junior == True:
    _Neopixel = 6 # Gpio pour le connecteur neopixel
else:
    _ST7789_BL = 6 # définition de la pinBacklit du ST7789 (GP6)
    _MicroSD_Detect = 7 # détection de la présence d'une carte MicroSD (GP7)
    _Neopixel = 23 # Gpio pour le connecteur neopixel
    
# ---------------------------------------------------------------   
# Configuration de l'écran ST7789 (SPI)
screen_width = 240
screen_height = 240
screen_rotation = 1

# Configuration UserInput
BTN_Analogue = ADC(_Boutons)

# Configuration de l'horloge
Clock_Radius = 110

# Couleurs de l'affichage
Background_Color = st7789.BLACK
DIAL_Color = st7789.WHITE
HOUR_Color = st7789.WHITE
DateBox_Color = 0x45b0 #STEELBLUE
DateBox_border_Color = 0xff1f #LIGHTYELLOW
MIN_Color = 0x7BEF # Gris clair
SEC_Color = 0xF800 # Rouge
TXT_Color = st7789.WHITE  

# Initialisation de l'affichage
spi0 = SPI(0, 20000000, sck=Pin(_ST7789_SCK, Pin.OUT), mosi=Pin(_ST7789_MOSI, Pin.OUT), polarity=1, phase=1)

if IS_Junior == True:
    display = st7789.ST7789(spi0, screen_width, screen_height, reset=Pin(_ST7789_RESET, Pin.OUT), dc=Pin(_ST7789_DC, Pin.OUT), rotation=screen_rotation)
else:
    display = st7789.ST7789(spi0, screen_width, screen_height, reset=Pin(_ST7789_RESET, Pin.OUT), dc=Pin(_ST7789_DC, Pin.OUT), backlight=Pin(_ST7789_BL, Pin.OUT), rotation=screen_rotation)

# Initialisation du FrameBuffer
buffer_width = screen_width
buffer_height = screen_height
buffer = bytearray(buffer_width * buffer_height * 2)
fbuf = framebuf2.FrameBuffer(buffer, buffer_width, buffer_height, framebuf2.RGB565)

import machine
import time
# Assure-toi que st7789, fbuf, tft (ou ton objet écran) et BTN_Analogue sont bien initialisés avant.

def Read_Keys():
    _read = BTN_Analogue.read_u16()
    if _read < 7000:
        return 'Droite'
    elif _read < 12000:
        return 'select'
    elif _read < 16000:
        return 'Gauche'
    return 'null'

def SetDateTime():
    rtc = machine.RTC()
    # Récupère la date actuelle du Pico : (année, mois, jour, jour_semaine, heure, minute, seconde, sous-seconde)
    t = rtc.datetime()
    
    # Valeurs par défaut si le Pico vient de démarrer (ex: année 2021)
    annee = t[0] if t[0] >= 2024 else 2024
    mois = t[1]
    jour = t[2]
    heure = t[4]
    minute = t[5]
    
    # Liste des valeurs modifiables : [Jour, Mois, Année (2 chiffres), Heure, Minute]
    valeurs = [jour, mois, annee % 100, heure, minute]
    # Limites (min, max) pour chaque champ
    limites = [(1, 31), (1, 12), (24, 99), (0, 23), (0, 59)]
    
    index = 0 # 0=Jour, 1=Mois, 2=Année, 3=Heure, 4=Minute
    
    # Coordonnées X ajustées pour un écran 240px de large (texte démarrant à X=8)
    pos_x = [8, 56, 104, 152, 200] 
    
    # Attendre que l'utilisateur relâche le bouton 'select' s'il vient d'entrer dans le menu
    while Read_Keys() != 'null':
        time.sleep(0.05)

    while index < 5:
        fbuf.fill(st7789.BLACK)
        
        # Titre centré
        fbuf.large_text("SET Date/Time", 16, 30, 2, st7789.GREEN)
        
        # Formatage de la chaîne de caractères : DD/MM/YY HH:MM
        texte_date = "{:02d}/{:02d}/{:02d} {:02d}:{:02d}".format(
            valeurs[0], valeurs[1], valeurs[2], valeurs[3], valeurs[4]
        )
        
        # Affichage de la date/heure centré sur 240px
        fbuf.large_text(texte_date, 8, 100, 2, st7789.WHITE)
        
        # Dessiner un curseur (barre jaune) sous le champ en cours de modification
        fbuf.fill_rect(pos_x[index], 125, 32, 4, st7789.YELLOW)
        
        # Instructions en bas d'écran centrées
        fbuf.large_text("-     OK     +", 10, 220,2, st7789.GREEN)
        
        # Rafraîchissement de l'écran
        display.blit_buffer(buffer, 0, 0, buffer_width, buffer_height)
        
        # Lecture des boutons
        touche = Read_Keys()
        
        if touche == 'Droite': # Augmenter la valeur
            valeurs[index] += 1
            if valeurs[index] > limites[index][1]:
                valeurs[index] = limites[index][0] # Boucle au minimum
            time.sleep(0.18) # Anti-rebond (debounce)
            
        elif touche == 'Gauche': # Diminuer la valeur
            valeurs[index] -= 1
            if valeurs[index] < limites[index][0]:
                valeurs[index] = limites[index][1] # Boucle au maximum
            time.sleep(0.18) # Anti-rebond
            
        elif touche == 'select': # Passer au champ suivant
            index += 1
            # Attendre le relâchement du bouton pour ne pas sauter plusieurs champs d'un coup
            while Read_Keys() == 'select':
                time.sleep(0.05)
                
        time.sleep(0.02)

    # Une fois les 5 champs validés, on met à jour le RTC du Pico
    nouvelle_annee = 2000 + valeurs[2]
    rtc.datetime((nouvelle_annee, valeurs[1], valeurs[0], 0, valeurs[3], valeurs[4], 0, 0))
    
    # Message de confirmation centré
    fbuf.fill(st7789.BLACK)
    fbuf.large_text("Heure OK!", 48, 100, 2, st7789.GREEN)
    display.blit_buffer(buffer, 0, 0, buffer_width, buffer_height)
    time.sleep(1.5)



def draw_analog_clock(t):
    
    cx = int(screen_width/2) # je m'assure que cx est un entier
    cy = int(screen_height/2) # je m'assure que cy est un entier
   
    fbuf.fill(Background_Color)

    # Cadran (graduations)
    for i in range(12):
        angle = math.radians(i * 30)
        x1 = int(cx + (Clock_Radius - 10) * math.sin(angle))
        y1 = int(cy - (Clock_Radius - 10) * math.cos(angle))
        x2 = int(cx + Clock_Radius * math.sin(angle))
        y2 = int(cy - Clock_Radius * math.cos(angle))
        fbuf.line(x1, y1, x2, y2, DIAL_Color)

    hh, mm, ss = t[3], t[4], t[5]
    
    # Boîte de date
    fbuf.fill_rect(cx+40, cy-9, 50, 16, DateBox_Color)
    fbuf.rect(cx+40, cy-9, 50, 16, DateBox_border_Color)
    date_str = "{:02d}/{:02d}".format(t[2], t[1])
    fbuf.large_text(date_str, cx+45, cy-5, 1, TXT_Color)
    
    # Aiguille des Heures
    h_angle = math.radians((hh % 12) * 30 + mm * 0.5)
    hx = int(cx + (Clock_Radius * 0.5) * math.sin(h_angle))
    hy = int(cy - (Clock_Radius * 0.5) * math.cos(h_angle))
    fbuf.line(cx, cy, hx, hy, HOUR_Color)
    fbuf.line(cx+1, cy, hx+1, hy, HOUR_Color)

    # Aiguille des Minutes
    m_angle = math.radians(mm * 6)
    mx = int(cx + (Clock_Radius * 0.8) * math.sin(m_angle))
    my = int(cy - (Clock_Radius * 0.8) * math.cos(m_angle))
    fbuf.line(cx, cy, mx, my, MIN_Color)

    # Aiguille des Secondes
    s_angle = math.radians(ss * 6)
    sx = int(cx + (Clock_Radius * 0.9) * math.sin(s_angle))
    sy = int(cy - (Clock_Radius * 0.9) * math.cos(s_angle))
    fbuf.line(cx, cy, sx, sy, SEC_Color)

    # Moyeu central et serveur NTP
    fbuf.fill_rect(cx-2, cy-2, 4, 4, DIAL_Color)
        
    display.blit_buffer(buffer, 0, 0, buffer_width, buffer_height)
    
# -------------------------------------------------------------------------
#  Boucle principale
# 

SetDateTime()
# Rafraîchissement complet de l'affichage via le buffer
display.blit_buffer(buffer, 0, 0, buffer_width, buffer_height)


while True:
    t = time.localtime(time.time())
    #print(t) # debug to see if i can get info from NTP
    draw_analog_clock(t)
    time.sleep(1)