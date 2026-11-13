#----------------------------------------------------------------
# uCompute test Neopixel
#----------------------------------------------------------------
# Prerequest: USB-C should be connected to get 5V for Neopixel
# Compatibility: Work with all PICO version
# JPMichon  11/2026
#
# https://github.com/JPMichon/uComputeJr
#----------------------------------------------------------------
import machine, neopixel
import time
import utime

# #Dans le cas d'un RP2350 dans certains cas les timing doivent etre ajusté
RP2350 = False
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
# ---------------------------------------------------------------
#Nombre de neopixel
NBR_NeoPixel = 8

# --- initialisation ---
np = neopixel.NeoPixel(machine.Pin(_Neopixel), NBR_NeoPixel)
if RP2350:
    np.timing = (350, 900, 800, 450)


def demo(np):
    n = np.n

    # cycle
    for i in range(6 * n):
        for j in range(n):
            np[j] = (0, 0, 0)
        np[i % n] = (0, 255, 0)
        np.write()
        time.sleep_ms(25)

    # bounce
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 128)
        if (i // n) % 2 == 0:
            np[i % n] = (0, 0, 0)
        else:
            np[n - 1 - (i % n)] = (0, 0, 0)
        np.write()
        time.sleep_ms(60)

    # fade in/out
    for i in range(0, 4 * 256, 8):
        for j in range(n):
            if (i // 256) % 2 == 0:
                val = i & 0xff
            else:
                val = 255 - (i & 0xff)
            np[j] = (val, 0, 0)
        np.write()

    # clear
    for i in range(n):
        np[i] = (0, 0, 0)
    np.write()
   
while True:
    demo(np)
    utime.sleep(1)