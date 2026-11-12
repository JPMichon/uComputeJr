#----------------------------------------------------------------
# Prerequest: ST7789 as display, ESP12F module
#
# Compatibility: Work with all PICO version
# JPMichon  11/2026
#
# https://github.com/JPMichon/uComputeJr
#----------------------------------------------------------------
from machine import UART, Pin, SPI
import time
import math
import struct
import st7789
import framebuf2
from SECRET import _SSID, _WifiPWD

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

# Configuration de l'horloge
Clock_Radius = 110
ntp_server = "pool.ntp.org"
gmt_offset = -4 * 3600

# Couleurs de l'affichage
Background_Color = st7789.BLACK
DIAL_Color = st7789.WHITE
HOUR_Color = st7789.WHITE
DateBox_Color = 0x45b0 #STEELBLUE
DateBox_border_Color = 0xff1f #LIGHTYELLOW
MIN_Color = 0x7BEF # Gris clair
SEC_Color = 0xF800 # Rouge
NTP_Color = 0x7BEF # Gris clair
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

# Initialisation du port serie
esp_en = Pin(_Comm_EN, Pin.OUT)
esp_rst = Pin(_Comm_RST, Pin.OUT)
uart = UART(1, baudrate=115200, tx=Pin(_Comm_TX), rx=Pin(_Comm_RX))

# ---Initialisation du ESP12f ---
def esp_boot():
    esp_rst.value(0)
    time.sleep(0.5)
    esp_rst.value(1)
    esp_en.value(1)
    time.sleep(2)
    
def send_at(cmd, timeout=3000, expected="OK"):
    uart.write(cmd + "\r\n")
    start = time.ticks_ms()
    resp = b""
    while (time.ticks_ms() - start) < timeout:
        if uart.any():
            resp += uart.read()
            try:
                if expected in resp.decode('utf-8', 'ignore'):
                    return True
            except:
                pass
    return False

def get_ntp_time(server):
    send_at(f'AT+CIPSTART="UDP","{server}",123')
    if send_at("AT+CIPSEND=48"):
        uart.write(b'\x1b' + 47 * b'\0')
        time.sleep(1)
        raw = uart.read()
        if raw:
            try:
                idx = raw.find(b':') + 1
                return struct.unpack(">I", raw[idx:][40:44])[0] - 2208988800
            except:
                pass
    return None

def connect_wifi(ssid, pwd):
    send_at("AT+CWMODE=1")
    return send_at(f'AT+CWJAP="{ssid}","{pwd}"', timeout=10000)

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
    fbuf.large_text(ntp_server, cx-45, cy+40, 1, NTP_Color)
    
    display.blit_buffer(buffer, 0, 0, buffer_width, buffer_height)
    
# -------------------------------------------------------------------------
#  Boucle principale
# 

fbuf.fill(st7789.BLACK)
fbuf.large_text("SYNCING", 60, 70, 2, st7789.WHITE)
fbuf.large_text("Please WAIT...", 20, 140, 2, st7789.WHITE)
# Rafraîchissement complet de l'affichage via le buffer
display.blit_buffer(buffer, 0, 0, buffer_width, buffer_height)

esp_boot()

if connect_wifi(_SSID, _WifiPWD):
    ntp_sec = get_ntp_time(ntp_server)
    if ntp_sec:
        offset = (ntp_sec + gmt_offset) - time.time()
        while True:
            t = time.localtime(time.time() + int(offset))
            #print(t) # debug to see if i can get info from NTP
            draw_analog_clock(t)
            time.sleep(1)