#----------------------------------------------------------------
# uCompute HLK-LD2420 Distance Graph + Directional Sound (ST7789)
#----------------------------------------------------------------
# Prerequest: ST7789 as display
# Compatibility: Work with all PICO version
# JPMichon  11/2026
#
# https://github.com/JPMichon/uComputeJr
#----------------------------------------------------------------
from machine import Pin, SPI, UART, PWM
import st7789 as st7789
import framebuf2
import time
import struct

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
# Configuration de l'écran ST7789 (SPI)
screen_width = 240
screen_height = 240
screen_rotation = 1

spi0 = SPI(0, 20000000, sck=Pin(_ST7789_SCK, Pin.OUT), mosi=Pin(_ST7789_MOSI, Pin.OUT), polarity=1, phase=1)

if IS_Junior:
    display = st7789.ST7789(spi0, screen_width, screen_height, reset=Pin(_ST7789_RESET, Pin.OUT), dc=Pin(_ST7789_DC, Pin.OUT), rotation=screen_rotation)
else:
    display = st7789.ST7789(spi0, screen_width, screen_height, reset=Pin(_ST7789_RESET, Pin.OUT), dc=Pin(_ST7789_DC, Pin.OUT), backlight=Pin(_ST7789_BL, Pin.OUT), rotation=screen_rotation)

# Initialisation du Buzzer
buzzer = PWM(Pin(_Buzzer))
buzzer.duty_u16(0)

# Couleurs RGB565
BLACK     = 0x0000
WHITE     = 0xFFFF
GREEN     = 0x07E0
CYAN      = 0x07FF
RED       = 0xF800
YELLOW    = 0xFFE0
GRAY_GRID = 0x2104
DARK_BLUE = 0x0010

# Initialisation du FrameBuffer
buffer_width = screen_width
buffer_height = screen_height
buffer = bytearray(buffer_width * buffer_height * 2)
fbuf = framebuf2.FrameBuffer(buffer, buffer_width, buffer_height, framebuf2.RGB565)

# Initialisation UART0 (auto-détection 115200 / 256000 bauds)
baudrates = (115200, 256000)
baud_idx = 0
uart = UART(0, baudrate=baudrates[baud_idx], bits=8, parity=None, stop=1, tx=Pin(_UART_TX), rx=Pin(_UART_RX), rxbuf=1024)

# Paramètres du graphique
GRAPH_X = 32
GRAPH_Y = 44
GRAPH_W = 202
GRAPH_H = 165
MAX_DIST_CM = 600   # Échelle verticale maximale (600 cm = 6 m)

# Historique des échantillons : tuples (distance_cm, mouvement_detecte)
samples = [None] * GRAPH_W
rx_stream = bytearray()

current_dist_cm = None
prev_dist_cm = None
presence = False
motion_flag = False
motion_dir = 0          # -1 = rapprochement, +1 = éloignement, 0 = immobile
motion_speed_cm = 0     # Amplitude du déplacement en cm
last_motion_time = 0
last_beep_time = 0

last_raw_str = "En attente..."
last_rx_time = 0
last_baud_switch = time.ticks_ms()

def evaluate_motion(new_dist):
    global prev_dist_cm, motion_flag, motion_dir, motion_speed_cm, last_motion_time
    if prev_dist_cm is not None:
        diff = new_dist - prev_dist_cm
        if abs(diff) >= 3:
            motion_flag = True
            motion_dir = -1 if diff < 0 else 1
            motion_speed_cm = abs(diff)
            last_motion_time = time.ticks_ms()
    prev_dist_cm = new_dist

def parse_ld2420():
    global rx_stream, current_dist_cm, prev_dist_cm, presence, motion_flag, motion_dir, last_raw_str, last_rx_time

    if uart.any():
        data = uart.read()
        if data:
            last_rx_time = time.ticks_ms()
            rx_stream.extend(data)
            if len(rx_stream) > 256:
                rx_stream = rx_stream[-128:]

            # 1. Mode Binaire (F4 F3 F2 F1 ... F8 F7 F6 F5)
            bin_hdr = b'\xF4\xF3\xF2\xF1'
            bin_tail = b'\xF8\xF7\xF6\xF5'
            idx_b = rx_stream.rfind(bin_hdr)
            if idx_b != -1:
                idx_end = rx_stream.find(bin_tail, idx_b)
                if idx_end != -1:
                    frame = rx_stream[idx_b:idx_end+4]
                    rx_stream = rx_stream[idx_end+4:]
                    if len(frame) >= 13:
                        presence = (frame[6] > 0)
                        dist = struct.unpack('<H', frame[7:9])[0]
                        if presence and dist > 0:
                            current_dist_cm = dist
                            evaluate_motion(dist)
                        else:
                            current_dist_cm = None
                            prev_dist_cm = None
                            motion_dir = 0
                        last_raw_str = "BIN: " + " ".join("{:02X}".format(b) for b in frame[:8])

            # 2. Mode Texte ASCII (ON / OFF / Range xxx)
            if b'\n' in rx_stream:
                lines = rx_stream.split(b'\n')
                rx_stream = lines[-1]
                for raw_line in lines[:-1]:
                    clean = raw_line.strip()
                    if not clean:
                        continue
                    try:
                        txt = clean.decode('utf-8')
                        last_raw_str = "TXT: " + txt[:24]
                        if txt == "OFF":
                            presence = False
                            current_dist_cm = None
                            prev_dist_cm = None
                            motion_dir = 0
                        elif txt == "ON":
                            presence = True
                        elif txt.startswith("Range "):
                            val = int(txt[6:].strip())
                            if val > 0:
                                presence = True
                                current_dist_cm = val
                                evaluate_motion(val)
                            else:
                                presence = False
                                current_dist_cm = None
                                prev_dist_cm = None
                                motion_dir = 0
                    except Exception:
                        last_raw_str = "HEX: " + " ".join("{:02X}".format(b) for b in clean[:8])

def handle_sound(now):
    global last_beep_time, motion_dir

    # Si aucun mouvement n'a été détecté depuis plus de 300 ms -> silence complet
    if not presence or current_dist_cm is None or time.ticks_diff(now, last_motion_time) > 300 or motion_dir == 0:
        buzzer.duty_u16(0)
        motion_dir = 0
        return

    # Calcul de la cadence et de la fréquence selon le sens du mouvement
    if motion_dir == -1:
        # Rapprochement : bips rapides (100 à 350 ms) et tonalité aiguë (2600 Hz)
        freq = 2600
        interval_ms = max(100, 350 - (motion_speed_cm * 8))
    else:
        # Éloignement : bips lents (450 à 950 ms) et tonalité grave (1600 Hz)
        freq = 1600
        interval_ms = min(950, 450 + (motion_speed_cm * 10))

    elapsed = time.ticks_diff(now, last_beep_time)
    if elapsed >= interval_ms:
        buzzer.freq(freq)
        buzzer.duty_u16(18000)
        last_beep_time = now
    elif elapsed >= 30:
        # Durée du bip fixée à 30 ms
        buzzer.duty_u16(0)

def draw_interface():
    fbuf.fill(BLACK)

    # 1. Barre de titre fixe (Haut)
    fbuf.fill_rect(0, 0, 240, 18, DARK_BLUE)
    connected = (last_rx_time != 0) and (time.ticks_diff(time.ticks_ms(), last_rx_time) < 1500)
    status_txt = "RX OK" if connected else "NO RX"
    status_col = GREEN if connected else RED
    fbuf.text(status_txt, 4, 5, status_col)
    fbuf.text("{}k".format(baudrates[baud_idx] // 1000), 54, 5, CYAN)

    if current_dist_cm is not None:
        fbuf.text("DIST: {:3d} cm".format(current_dist_cm), 108, 5, YELLOW)
    else:
        fbuf.text("DIST: --- cm", 108, 5, WHITE)

    # 2. Sous-barre d'état fixe (indique le sens du mouvement)
    fbuf.text("MVT:", 4, 24, WHITE)
    if motion_dir == -1:
        fbuf.text("APPROCHE", 40, 24, RED)
    elif motion_dir == 1:
        fbuf.text("ELOIGNE", 40, 24, YELLOW)
    else:
        fbuf.text("AUCUN", 40, 24, CYAN)

    fbuf.text("MAX: 600cm", 152, 24, CYAN)

    # 3. Cadre et grille du graphique (Fixe)
    fbuf.rect(GRAPH_X, GRAPH_Y, GRAPH_W, GRAPH_H, WHITE)

    for step in range(5):
        dist_label = int((MAX_DIST_CM / 4) * step)
        y_pos = GRAPH_Y + GRAPH_H - 1 - int((step / 4) * (GRAPH_H - 2))
        fbuf.text("{:3d}".format(dist_label), 2, y_pos - 4, CYAN)
        if 0 < step < 4:
            for gx in range(GRAPH_X + 2, GRAPH_X + GRAPH_W - 2, 6):
                fbuf.pixel(gx, y_pos, GRAY_GRID)

    for gx in range(GRAPH_X + 40, GRAPH_X + GRAPH_W, 40):
        for gy in range(GRAPH_Y + 2, GRAPH_Y + GRAPH_H - 2, 6):
            fbuf.pixel(gx, gy, GRAY_GRID)

    # 4. Tracé de la courbe de distance (Cyan)
    prev_px = None
    prev_py = None

    for i in range(GRAPH_W):
        item = samples[i]
        if item is not None:
            val, has_motion = item
            clamped = min(MAX_DIST_CM, max(0, val))
            px = GRAPH_X + i
            py = GRAPH_Y + GRAPH_H - 2 - int((clamped / MAX_DIST_CM) * (GRAPH_H - 4))
            
            if prev_px is not None and prev_py is not None:
                fbuf.line(prev_px, prev_py, px, py, CYAN)
            else:
                fbuf.pixel(px, py, CYAN)
                
            prev_px = px
            prev_py = py
        else:
            prev_px = None
            prev_py = None

    # Points verts sur les détections de mouvement
    for i in range(GRAPH_W):
        item = samples[i]
        if item is not None:
            val, has_motion = item
            if has_motion:
                clamped = min(MAX_DIST_CM, max(0, val))
                px = GRAPH_X + i
                py = GRAPH_Y + GRAPH_H - 2 - int((clamped / MAX_DIST_CM) * (GRAPH_H - 4))
                fbuf.fill_rect(px - 1, py - 1, 3, 3, GREEN)

    # 5. Ligne fixe en bas : dernière donnée brute reçue
    fbuf.fill_rect(0, 218, 240, 22, DARK_BLUE)
    fbuf.text(last_raw_str, 4, 225, WHITE)

# ---------------------------------------------------------------
# Boucle principale
while True:
    now = time.ticks_ms()

    parse_ld2420()

    # Auto-bascule 115200 <-> 256000 bauds si aucune donnée reçue depuis 3s
    if time.ticks_diff(now, last_rx_time) > 3000 and time.ticks_diff(now, last_baud_switch) > 3000:
        baud_idx = (baud_idx + 1) % len(baudrates)
        uart.init(baudrate=baudrates[baud_idx], bits=8, parity=None, stop=1, tx=Pin(_RADAR_TX), rx=Pin(_RADAR_RX))
        last_baud_switch = now
        last_raw_str = "Scan {} bps...".format(baudrates[baud_idx])

    # Si aucune donnée depuis 1s, considère la zone vide
    if time.ticks_diff(now, last_rx_time) > 1000:
        current_dist_cm = None
        prev_dist_cm = None
        presence = False
        motion_flag = False
        motion_dir = 0

    # Gestion du bip directionnel
    handle_sound(now)

    # Ajoute l'échantillon à droite et décale à gauche
    samples.pop(0)
    if current_dist_cm is not None:
        samples.append((current_dist_cm, motion_flag))
    else:
        samples.append(None)

    motion_flag = False

    draw_interface()
    display.blit_buffer(buffer, 0, 0, screen_width, screen_height)
    time.sleep_ms(30)
