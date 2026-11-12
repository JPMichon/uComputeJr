#----------------------------------------------------------------
# Prerequest: SSD1306 as display
# Compatibility: Work with all PICO version
# JPMichon  11/2026
#
# https://github.com/JPMichon/uComputeJr
#----------------------------------------------------------------

from machine import I2C, Pin
from ssd1306 import SSD1306_I2C
from time import sleep


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
    
    
# ---------------------------------------------------------------
#initialisation du port i2c

i2c=I2C(0,sda=Pin(_I2C_SDA), scl=Pin(_I2C_SCL), freq=200000)

# -----------------------------------
# Choisir la résolution du OLED
#
oled = SSD1306_I2C(128, 64, i2c)
#oled = SSD1306_I2C(128, 32, i2c)
#------------------------------------
#
# scan du bus I2C
#
#affichage la page d'accueil
oled.text('Scan i2c bus...', 10,25)
oled.show()
sleep(2) # attend 2sec
#efface l'ecran
oled.fill(0)
oled.show()

devices = i2c.scan()
pointeur=11 # permet d'incrémenter les lignes
if len(devices) == 0:
  oled.text('No i2c device !', 0,0)
  oled.show()  
else:
  oled.text('Device found:' +str(len(devices)), 3,1)
  oled.rect(0,0,128,10,1)
  oled.show()    
  for device in devices:  
    oled.text('Hex addr: '+str(hex(device)),0,pointeur)
    pointeur=pointeur+10
oled.show()   
#-------------------------------------------
# Registre des adresses i2c  
# 0x38  = AHT10/AHT20 temperature+humidity sensor
# 0x3c  = OLED SSD1306
# 0x40  = INA219 Current monitor
# 0x50  = EEPROM
# 0x68  = EEPROM
#
#------------------------------------------

