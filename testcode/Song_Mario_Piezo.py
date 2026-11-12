#----------------------------------------------------------------
# uCompute Test piezo
#----------------------------------------------------------------
# Prerequest: None
# Compatibility: Work with all PICO version
# JPMichon  11/2026
#
# https://github.com/JPMichon/uComputeJr
#----------------------------------------------------------------
from machine import Pin, PWM
import utime 

IS_Junior = True
# ---------------------------------------------------------------
# uCompute standard pins
_SSD1306_ADDR = 0x3C
_Buzzer = 11 # définition du buzzer (GP11)
_MicroSD_Select = 13 # définition de la pin Select du SDCARD (GP13)
_SPI1_SCK = 14 # SPI1_shared Clock
_SPI1_MOSI = 15 # SPI1_shared MOSI
_SPI1_MISO = 12 # SPI1_shared MISO
_Led_System = 25 # définition du port del systeme (GP25)
_I2C_SDA = 20 # définition de Data du I2C(0) (GP20)
_I2C_SCL = 21 # définition de SCL du I2C(0) (GP21)
_Boutons = 26 # définition du port analogue des boutons (GP26)
_ST7789_SCK = 2 # définition de la pin Clock du ST7789 (GP2) SPI0
_ST7789_MOSI = 3 # définition de la pin MOSI du ST7789 (GP3) SPI0
_ST7789_RESET = 4 # définition de la pin Reset du ST7789 (GP4)
_ST7789_DC = 5 # définition de la pin Select du ST7789 (GP5)
#UART
_UART_RX = 1
_UART_TX = 0


# --- CONFIGURATION MATÉRIELLE ---
if IS_Junior == True:
    _Neopixel = 6 # Gpio pour le connecteur neopixel
else:
    _ST7789_BL = 6 # définition de la pin Backlit du ST7789 (GP6)
    _MicroSD_Detect = 7 # détection de la présence d'une carte MicroSD (GP7)
    _Neopixel = 23 # Gpio pour le connecteur neopixel

# Dictionnaire des fréquences des notes
NOTES = {
    'DO4': 262, 'RE4': 294, 'MI4': 330, 'FA4': 349, 'SOL4': 392, 'LA4': 440, 'SI4': 494,
    'DO5': 523, 'RE5': 587, 'MI5': 659, 'FA5': 698, 'SOL5': 784, 'LA5': 880, 'SI5': 988,
    'SILENCE': 0
}

def play_mario():
    Buzzer = PWM(Pin(_Buzzer))
    
    # Partition du thème principal de Mario
    partition = [
        'MI5', 'MI5', 'SILENCE', 'MI5', 'SILENCE', 'DO5', 'MI5', 'SILENCE',
        'SOL5', 'SILENCE', 'SOL4', 'SILENCE',
        'DO5', 'SILENCE', 'SOL4', 'SILENCE', 'MI4', 'SILENCE',
        'LA4', 'SILENCE', 'SI4', 'SILENCE', 'SIB4', 'LA4', 'SILENCE',
        'SOL4', 'MI5', 'SOL5', 'LA5', 'SILENCE', 'FA5', 'SOL5',
        'SILENCE', 'MI5', 'SILENCE', 'DO5', 'RE5', 'SI4'
    ]
    
    # Durées correspondantes (en secondes)
    tempos = [
        0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12,
        0.12, 0.36, 0.12, 0.36,
        0.18, 0.18, 0.18, 0.18, 0.18, 0.18,
        0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12,
        0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12,
        0.12, 0.12, 0.12, 0.12, 0.12, 0.24
    ]
    
    # Note intermédiaire manquante (le La bémol / Si bémol) ajoutée dynamiquement
    NOTES['SIB4'] = 466
    
    for note, duree in zip(partition, tempos):
        frequence = NOTES[note]
        
        if frequence == 0:
            Buzzer.duty_u16(0)
            utime.sleep(duree)
        else:
            Buzzer.freq(frequence)
            Buzzer.duty_u16(1500)  # Volume légèrement réduit pour les notes aiguës
            utime.sleep(duree)
            
        # Micro-pause obligatoire pour détacher les notes identiques qui se suivent
        Buzzer.duty_u16(0)
        utime.sleep(0.03)
        
    Buzzer.duty_u16(0)

# Joue le thème en boucle toutes les 6 secondes
while True:
    play_mario()
    utime.sleep(6)