# 🧪 Programmes de Test et Exemples / Test Code & Examples

[Français](#-français) | [English](#-english)

---

## Français

Ce répertoire contient des scripts de diagnostic et des exemples pratiques en **MicroPython** pour valider le bon fonctionnement matériel de votre **uCompute Junior** après l'assemblage, ainsi que pour tester ses différents ports d'extension (I2C, UART, NeoPixel, écran ST7789 et modules Wi-Fi).

### 🔍 Liste des scripts de test

* **[Scan_I2C_OLED.py](Scan_I2C_OLED.py)** — Analyse le bus I2C (`GPIO 20` / `GPIO 21`) pour détecter les périphériques connectés (comme la mémoire EEPROM à l'adresse `0x50`) et affiche le résultat sur un écran alternatif **OLED SSD1306**.
* **[Song_Mario_Piezo.py](Song_Mario_Piezo.py)** — Teste le buzzer piézoélectrique intégré (`GPIO 11`) en jouant le célèbre thème musical de *Super Mario Bros.* via modulation PWM.
* **[Test_NeoPixel.py](Test_NeoPixel.py)** — Valide le connecteur **NeoPixel** (`GPIO 6`) en animant un ruban ou un anneau de DEL adressables WS2812B. *(Pensez à alimenter la carte via le port USB-C du Junior pour fournir le 5V).*
* **[st7789_PicoW_NTP_AnalogClock.py](st7789_PicoW_NTP_AnalogClock.py)** — Affiche une horloge analogique sur l'écran couleur **ST7789** en synchronisant l'heure automatiquement via Internet (protocole NTP) à l'aide du Wi-Fi intégré d'un **Raspberry Pi Pico W** ou **Pico 2 W**.
* **[st7789_ESP12F_NTP_AnalogClock.py](st7789_ESP12F_NTP_AnalogClock.py)** — Variante de l'horloge analogique NTP conçue pour un **Pico standard** couplé au module d'extension **Wi-Fi ESP-12F** branché sur le port *Add-on Module* (`U7`).
* **[st7789_MotionRadar_HLK-LD2420.py](st7789_MotionRadar_HLK-LD2420.py)** — Exemple d'utilisation du port série **UART** (`GPIO 0` / `GPIO 1`) pour lire et afficher les données d'un capteur radar de présence/mouvement **HLK-LD2420** sur l'écran couleur ST7789.

### ⚙️ Conseils d'utilisation

1. **Bibliothèques requises :** Copiez au préalable les pilotes correspondants depuis le dossier [`lib/`](../lib/) sur votre Raspberry Pi Pico.
2. **Configuration réseau :** Pour les exemples d'horloge NTP, ouvrez le script dans **Thonny** et renseignez le nom de votre réseau Wi-Fi (`SSID`) ainsi que votre mot de passe avant de lancer l'exécution.

---

## English

This directory contains diagnostic scripts and practical **MicroPython** examples to verify the hardware functionality of your **uCompute Junior** after assembly, as well as to test its expansion ports (I2C, UART, NeoPixel, ST7789 display, and Wi-Fi add-on modules).

### 🔍 Available Test Scripts

* **[Scan_I2C_OLED.py](Scan_I2C_OLED.py)** — Scans the I2C bus (`GPIO 20` / `GPIO 21`) to detect connected devices (such as the onboard EEPROM at address `0x50`) and displays the results on an alternative **SSD1306 OLED** screen.
* **[Song_Mario_Piezo.py](Song_Mario_Piezo.py)** — Tests the onboard piezoelectric buzzer (`GPIO 11`) by playing the classic *Super Mario Bros.* theme melody using PWM signals.
* **[Test_NeoPixel.py](Test_NeoPixel.py)** — Tests the **NeoPixel** header (`GPIO 6`) by driving a WS2812B addressable LED strip or ring. *(Remember to power the board via the Junior's USB-C port to supply 5V).*
* **[st7789_PicoW_NTP_AnalogClock.py](st7789_PicoW_NTP_AnalogClock.py)** — Displays an analog clock on the **ST7789** color screen while automatically syncing the time over the Internet (NTP) using the built-in Wi-Fi of a **Raspberry Pi Pico W** or **Pico 2 W**.
* **[st7789_ESP12F_NTP_AnalogClock.py](st7789_ESP12F_NTP_AnalogClock.py)** — A variant of the NTP analog clock built for a **standard Pico** paired with the **ESP-12F Wi-Fi** daughterboard plugged into the *Add-on Module* socket (`U7`).
* **[st7789_MotionRadar_HLK-LD2420.py](st7789_MotionRadar_HLK-LD2420.py)** — Demonstrates how to use the **UART** serial port (`GPIO 0` / `GPIO 1`) to read and display presence/motion data from an **HLK-LD2420** radar sensor on the ST7789 color display.

### ⚙️ Usage Tips

1. **Required libraries:** Make sure to copy the matching driver files from the [`lib/`](../lib/) folder onto your Raspberry Pi Pico first.
2. **Wi-Fi credentials:** For the NTP clock examples, open the script in **Thonny** and enter your Wi-Fi network name (`SSID`) and password before running it.

---

⬅️ [Retour à l'accueil du projet / Back to Project Home](../README.md)
