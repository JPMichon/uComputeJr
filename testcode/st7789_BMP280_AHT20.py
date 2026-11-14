#----------------------------------------------------------------
# Prerequest: ST7789 as display
#
# Compatibility: Work with all PICO version
# JPMichon  11/2026
#
# https://github.com/JPMichon/uComputeJr
#---------------------------------------------------------------
from machine import I2C, Pin, SPI, PWM, ADC
import st7789 as st7789
import framebuf2
import ahtx0
from bmp280 import *
import utime



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

# Configuration UserInput
BTN_Analogue = ADC(_Boutons)

# set landscape screen
screen_width = 240
screen_height = 240
screen_rotation = 1
# #Creation du frame buffer meme taille que l'écran
buffer = bytearray(screen_width * screen_height * 2)
fbuf = framebuf2.FrameBuffer(buffer, screen_width, screen_height, framebuf2.RGB565)

#Initialisation du LCD
spi0 = machine.SPI(0,24000000,sck=machine.Pin(_ST7789_SCK,machine.Pin.OUT),mosi=machine.Pin(_ST7789_MOSI,machine.Pin.OUT), polarity=1,phase=1)
if IS_Junior == True:
    display = st7789.ST7789(spi0, screen_width, screen_height, reset=Pin(_ST7789_RESET, Pin.OUT), dc=Pin(_ST7789_DC, Pin.OUT), rotation=screen_rotation)
else:
    display = st7789.ST7789(spi0, screen_width, screen_height, reset=Pin(_ST7789_RESET, Pin.OUT), dc=Pin(_ST7789_DC, Pin.OUT), backlight=Pin(_ST7789_BL, Pin.OUT), rotation=screen_rotation)


#Initialisation du I2C
i2c=I2C(0,sda=Pin(_I2C_SDA), scl=Pin(_I2C_SCL), freq=200000)

#initialisation du Capteur de pression
sensorBMP280 = BMP280(i2c,0x77)
sensorAHT20 = ahtx0.AHT10(i2c)


# main
while True:
    pressure=sensorBMP280.pressure
    p_bar=pressure/100000
    p_mmHg=pressure/133.3224
    p_inHg= pressure/3386.39
    Temperature=round(sensorAHT20.temperature,2)
    Humidity=round(sensorAHT20.relative_humidity,2)
    
    fbuf.fill(st7789.BLACK) # Efface l'écran (le framefuffer)
    fbuf.rect(0, 0, 240, 35,st7789.BLUE)
    fbuf.large_text('Monitor', 40, 10, 3, st7789.CYAN)
    fbuf.large_text("Temp.:"+str(Temperature)+" C", 10, 50, 2, st7789.BLUE)
    fbuf.large_text("Hum. :"+str(Humidity)+" %", 10, 70, 2, st7789.BLUE)
    fbuf.large_text("Pression:", 10, 100, 2, st7789.BLUE)
    fbuf.large_text("(kPa)  "+ str(round(pressure/1000,2)), 20, 120, 2, st7789.YELLOW)
    fbuf.large_text("(mmHg) "+ str(round(p_mmHg,2)), 20, 140, 2, st7789.YELLOW)
    fbuf.large_text("(inHg) "+ str(round(p_inHg,2)), 20, 160, 2, st7789.YELLOW)
    fbuf.large_text("(bar) "+ str(round(p_bar,5)), 20, 180, 2, st7789.YELLOW)
    print("\nAHT20")
    print("------")
    print("Temperature: %0.2f C" % Temperature)
    print("Humidity: %0.2f %%" % Humidity)
    print("\nBMP280")
    print("------")
    print("Temperature: %0.2f C" % sensorBMP280.temperature)

    print("Pressure: {} kPa, {} bar, {} mmHg, {} inHg".format(pressure/1000,p_bar,p_mmHg,p_inHg))
    display.blit_buffer(buffer, 0, 0, screen_width, screen_height)
    utime.sleep(5)
    
    