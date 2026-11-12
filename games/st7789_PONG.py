#----------------------------------------------------------------
#  Pong game 240x240 ST7789 SPI LCD
#----------------------------------------------------------------
# Prerequest: ST7789 as display
# Compatibility: Work with all PICO version
# JPMichon  11/2026
#
# https://github.com/JPMichon/uComputeJr
#----------------------------------------------------------------
from machine import I2C, Pin, SPI, PWM
import st7789 as st7789
import framebuf2
import utime

# Variables pour le jeux
BALL_SIZE = 6 # 2X2 pixels
BALL_SPEED_init = 4 # permet d'accelerer la balle
PAD_WIDTH = 25 # largeur de la palette
PAD_HEIGHT = 2
PAD_STEP =10
HALF_PAD_WIDTH = int(PAD_WIDTH / 2)
HALF_PAD_HEIGHT = int(PAD_HEIGHT / 2)
PAD_HEIGHT = 6
BG_TEXT_COLOR = st7789.color565(35, 35, 50) # Gris-bleu discret pour le fond
BORDER_COLOR = st7789.BLUE
# Couleurs de la balle selon le niveau de vitesse
BALL_COLORS = [st7789.WHITE, st7789.YELLOW, st7789.ORANGE, st7789.RED]

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

# --- CONFIGURATION MATÉRIELLE ---
if IS_Junior == True:
    _Neopixel = 6 # Gpio pour le connecteur neopixel
else:
    _ST7789_BL = 6 # définition de la pinBacklit du ST7789 (GP6)
    _MicroSD_Detect = 7 # détection de la présence d'une carte MicroSD (GP7)
    _Neopixel = 23 # Gpio pour le connecteur neopixel
    
    
BTN_Analogue = machine.ADC(_Boutons) #Diviseur de tension des boutons

# set landscape screen
screen_width = 240
screen_height = 240
screen_rotation = 1
# #Creation du frame buffer meme taille que l'écran
buffer = bytearray(screen_width * screen_height * 2)
fbuf = framebuf2.FrameBuffer(buffer, screen_width, screen_height, framebuf2.RGB565)

spi0 = machine.SPI(0,20000000,sck=machine.Pin(_ST7789_SCK,machine.Pin.OUT),mosi=machine.Pin(_ST7789_MOSI,machine.Pin.OUT), polarity=1,phase=1)
if IS_Junior == True:
    display = st7789.ST7789(spi0, screen_width, screen_height, reset=Pin(_ST7789_RESET, Pin.OUT), dc=Pin(_ST7789_DC, Pin.OUT), rotation=screen_rotation)
else:
    display = st7789.ST7789(spi0, screen_width, screen_height, reset=Pin(_ST7789_RESET, Pin.OUT), dc=Pin(_ST7789_DC, Pin.OUT), backlight=Pin(_ST7789_BL, Pin.OUT), rotation=screen_rotation)


NOTES = {
    'DO4': 262, 'RE4': 294, 'MI4': 330, 'FA4': 349, 'SOL4': 392, 'LA4': 440, 'SI4': 494,
    'DO5': 523, 'RE5': 587, 'MI5': 659, 'FA5': 698, 'SOL5': 784, 'LA5': 880, 'SI5': 988,
    'DO6': 1047, 'RE6': 1175, 'MI6': 1319, 'SILENCE': 0}
   
def play_game_start():
    buzzer = PWM(Pin(_Buzzer))
    partition = ['DO5', 'MI5', 'SOL5', 'DO5', 'PAUSE', 'DO6']
    tempos = [0.10, 0.10, 0.10, 0.15, 0.05, 0.35]
    for note, duree in zip(partition, tempos):
        frequence = 0 if note == 'PAUSE' else NOTES[note]
        if frequence == 0:
            buzzer.duty_u16(0)
            utime.sleep(duree)
        else:
            buzzer.freq(frequence)
            buzzer.duty_u16(32768)
            utime.sleep(duree)
        buzzer.duty_u16(0)
        utime.sleep(0.01)
    buzzer.deinit()
    
def play_game_over():
    buzzer = PWM(Pin(_Buzzer))
    partition = ['MI5', 'RE5', 'DO5', 'SI4', 'PAUSE', 'LA4']
    tempos = [0.15, 0.15, 0.15, 0.25, 0.10, 0.60]
    for note, duree in zip(partition, tempos):
        frequence = 0 if note == 'PAUSE' else NOTES[note]
        if frequence == 0:
            buzzer.duty_u16(0)
            utime.sleep(duree)
        else:
            buzzer.freq(frequence)
            buzzer.duty_u16(32768)
            utime.sleep(duree)
        buzzer.duty_u16(0)
        utime.sleep(0.02)
    buzzer.deinit()

def play_Collision_hit():
    buzzer = PWM(Pin(_Buzzer))
    buzzer.freq(NOTES['SOL5'])
    buzzer.duty_u16(16384)
    utime.sleep(0.05)
    buzzer.deinit()


def Read_Keys():
    _read = BTN_Analogue.read_u16()
    _KeyPress='null'
    if _read < 7000: #Droite
        _KeyPress='Droite'
    elif _read < 12000: #Select
        _KeyPress='select'
    elif _read < 16000: # Gauche
        _KeyPress='Gauche'          
    #print(str(_read)) #pour le debuggage affiche la lecture de la clé dans la console    
    return _KeyPress #+str(_read) 

def WaitInputKey():
    # Boucle TANT QUE la valeur est inférieure au seuil
    while BTN_Analogue.read_u16() > 40000:
        utime.sleep(0.01)
        
#Splash Screen
fbuf.fill(st7789.BLACK) # efface l'écran
fbuf.rect(0, 0, screen_width, screen_height, st7789.BLUE)
fbuf.fill_rect(10, 10, screen_width-20, 100, st7789.BLUE)
fbuf.fill_rect(15, 15, screen_width-30, 90, st7789.GREEN)
fbuf.large_text("uCompute", 60, 30, 2, st7789.BLUE)
fbuf.large_text("-PONG-", 70, 70,2,  st7789.WHITE)
fbuf.large_text("[ANY KEY]", 50, 200,2,  st7789.GREEN)
display.blit_buffer(buffer, 0, 0, screen_width, screen_height)

WaitInputKey() # boucle en attendant que la touche START soit enfoncer
play_game_start()    
fbuf.fill(st7789.BLACK) # efface l'écran
display.blit_buffer(buffer, 0, 0, screen_width, screen_height)
utime.sleep(.2)

x=120 # set la valeur initial de la position du curseur
# Lance la balle a partir du centre
ball_x = int(screen_width / 2)
ball_y = int(screen_height / 2)
# Initialise le mouvement de la balle
ball_x_dir = 1
ball_y_dir = 1
score=0
GameOver=False
BALL_SPEED=2
while not GameOver:
    tempokey = Read_Keys()
    if tempokey == 'Droite':
        x = min(screen_width - PAD_WIDTH - 2, x + PAD_STEP)
    if tempokey == 'Gauche':
        x = max(2, x - PAD_STEP)

    # Effacer et dessiner le décor (Arène + Score en filigrane)
    fbuf.fill(st7789.BLACK)
    # Bordures gauche, haut et droite
    fbuf.vline(0, 0, screen_height, BORDER_COLOR)
    fbuf.vline(screen_width - 1, 0, screen_height, BORDER_COLOR)
    fbuf.hline(0, 0, screen_width, BORDER_COLOR)
    
    # Ligne médiane pointillée
    for i in range(10, screen_width - 10, 15):
        fbuf.hline(i, 120, 8, BG_TEXT_COLOR)
        
    # Score géant au centre en arrière-plan
    fbuf.large_text(str(score), 100, 95, 3, BG_TEXT_COLOR)

    # Dessiner la palette avec un effet de relief
    fbuf.fill_rect(x, 230, PAD_WIDTH, PAD_HEIGHT, st7789.CYAN)
    fbuf.hline(x, 230, PAD_WIDTH, st7789.WHITE) # Reflet supérieur

    # Choisir la couleur de la balle selon la vitesse et la dessiner
    niveau = min(score // 10, len(BALL_COLORS) - 1)
    ball_color = BALL_COLORS[niveau]
    fbuf.fill_rect(int(ball_x), int(ball_y), BALL_SIZE, BALL_SIZE, ball_color)

    # Afficher le tout à l'écran
    display.blit_buffer(buffer, 0, 0, screen_width, screen_height)

    # Calculer les déplacements et collisions (identique à votre logique)
    ball_x += ball_x_dir * BALL_SPEED
    ball_y += ball_y_dir * BALL_SPEED

    if ball_y <= 2:
        play_Collision_hit()
        ball_y_dir = 1
    if ball_x >= screen_width - BALL_SIZE - 2:
        play_Collision_hit()
        ball_x_dir = -1
    if ball_x <= 2:
        play_Collision_hit()
        ball_x_dir = 1

    # Collision avec la palette (ajustée à y = 230)
    if ball_y + BALL_SIZE >= 230: # 230 est la position Y de la palette (ou 235 dans votre code original)
        if x - BALL_SIZE <= ball_x <= x + PAD_WIDTH:
            play_Collision_hit()
            
            # Calculer le centre de la balle et le centre de la palette
            ball_center = ball_x + (BALL_SIZE / 2)
            pad_center = x + (PAD_WIDTH / 2)
            
            # Calculer le décalage relatif (valeur entre -1.0 et 1.0)
            offset = (ball_center - pad_center) / (PAD_WIDTH / 2)
            
            # Appliquer la nouvelle direction horizontale (1.5 règle l'angle maximum)
            ball_x_dir = offset * 1.5
            
            # Inverser la direction verticale et replacer la balle au-dessus de la palette
            ball_y_dir = -1
            ball_y = 230 - BALL_SIZE
            
            score += 1
        elif ball_y > screen_height:
            GameOver = True

    BALL_SPEED = (score // 10) + BALL_SPEED_init       
    
    
# si j'arrive ici c'est que la partie est fini
fbuf.fill(st7789.BLACK) # efface l'écran
display.blit_buffer(buffer, 0, 0, screen_width, screen_height)
fbuf.large_text("Game Over", 60, 70, 2, st7789.BLUE, st7789.BLACK)
fbuf.large_text("Score: " +str(score),70,120, 2, st7789.YELLOW, st7789.BLACK)
display.blit_buffer(buffer, 0, 0, screen_width, screen_height)
play_game_over()