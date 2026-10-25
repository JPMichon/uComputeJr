## [Version Française à ce lien](./README.md)

# uCompute Junior (Bring your own PICO)

The **uComputeJunior** is a streamlined and highly accessible version of the [RP2040 uCompute platform](https://github.com/JPMichon/RP2040_uCompute). Designed specifically for **novice hobbyists and makers**, it features a "Bring your own Pico" framework: it eliminates the need to solder complex surface-mount devices (SMD) by directly hosting a standard, ready-to-use Raspberry Pi Pico module.

This board serves as a hardware entry gateway to seamlessly integrate into the global uCompute environment, while also simplifying the onboarding and access to ecosystem projects like the programmable [uCompute Rover robot](https://github.com/JPMichon/uCompute_Rover).


<img width="558" height="367" alt="image" src="https://github.com/user-attachments/assets/9ae96d46-1b85-4960-8d46-99c5ffb2fcdd" />


---

## 🎓 A Perfect Solution for Education and Fablabs

The **uCompute Junior** stands out as the perfect tool for introducing electronics and embedded systems, whether in school environments (**middle and high schools**) or within **Fablabs**.

* **For the educational sector:** Thanks to its "Bring your own Pico" approach, it greatly simplifies classroom setup by hosting a standard, off-the-shelf **Raspberry Pi Pico** module. By combining the power of the Raspberry Pi Pico community, the clarity of the **MicroPython** language, and the flexibility of the **uCompute ecosystem**, teachers have a turnkey environment to structure engaging practical workshops (ranging from simple LED blinking to driving the _uCompute Rover Robot_).
* **For Fablabs and hands-on workshops:** Although the board requires surface-mount soldering (SMD), the design deliberately uses **0805-sized** components, which are particularly easy to handle and hand-solder. This makes it an excellent educational medium to demystify and teach SMD soldering without requiring complex industrial equipment (such as a reflow oven or a hot plate).


The entire project is driven by Open Hardware values and shared under the **CC BY-NC-SA 4.0** license. Since all manufacturing files (Gerbers, schematics) are freely accessible, schools and Fablabs can order, modify, or locally produce their own boards at a minimal cost, fostering total technological autonomy and frictionless knowledge sharing without budget constraints.

> [!NOTE]
> Si vous débutez et n'avez jamais commandé de circuits imprimés, sachez qu'il existe de nombreuses plateformes en ligne. De mon côté, j'utilise les services de JLCPCB. Si vous voulez tester leur site, vous pouvez utiliser mon lien de parrainage : **[JLCPCB](https://jlcpcb.com/?from=REDLD)**. Cela vous permettra d'obtenir des coupons de réduction pour vos premières impressions, tout en m'offrant des crédits pour soutenir et financer mes futurs projets. Rien ne vous y oblige bien sûr, mais c'est un excellent moyen de donner un coup de pouce à la chaîne !

---

### 📻 Extension Modules & Backward Compatibility (Add-ons)

The main highlight of the **uCompute Junior** lies in the native integration of its add-on extension socket and its I/O pin header (Header H1). Despite being a streamlined version, the board maintains **full backward compatibility with all communication and extension modules from the uCompute ecosystem**.

This allows you to instantly upgrade your Junior (wireless links, robotic telemetry, remote control) by directly plugging in daughterboards from the main project or the Rover Robot.

👉 **[Access the ecosystem modules repository (RP2040_uCompute Modules)](https://github.com/JPMichon/RP2040_uCompute/tree/main/Modules)**

| Location on Junior | Compatible Module | Description & Features | Hardware Render |
| :--- | :--- | :--- | :--- |
| **Add-On module** <br>(Communication) | **Wi-Fi Module** <br>(ESP-12F) | Adapter board embedding an ESP8266 to add full Wi-Fi connectivity. | <img width="100" height="133" alt="Module Wi-Fi ESP-12F" src="https://github.com/user-attachments/assets/f0c80621-1b07-46e6-844b-4594e3d338f9" /> |
| **Add-On module** <br>(Communication) | **Radio Module** <br>(NRF24L01) | Adapter for 2.4 GHz radio links, ideal for bidirectional communication. | <img width="112" height="140" alt="Module Radio NRF24L01" src="https://github.com/user-attachments/assets/a6a0a83b-80ed-4dbc-bc28-06579f64b54c" /> |
| **Add-On module** <br>(Communication) | **LoRa Module** <br>(RFM95W) | Long-range adapter exploiting LoRa radio technology. | <img width="112" height="140" alt="Module LoRa RFM95W" src="https://github.com/user-attachments/assets/729ed810-e456-4e6b-88fb-1f3c61edea25" /> |
| **Header H1** <br>(I/O Connector) | **µCompute Remote** <br>| Extension board integrating an analog joystick and buttons for RC piloting. | <img width="175" height="131" alt="Manette uCompute Remote" src="https://github.com/user-attachments/assets/25dda003-8ab8-48c4-a7d1-1a45fdbca7a4" /> |
| **Header H1** <br>(I/O Connector) | **µCompute Rover** <br> | Controller for DC motors (2+2), servo motor, HC-SR04 sensor, and Neo-6M GPS module. | <img width="220" height="145" alt="Contrôleur uCompute Rover" src="https://github.com/user-attachments/assets/90114819-d70b-4cbb-8cfd-5e95b66cca84" /> |

> ℹ **Technical note regarding network support (W5500 Module):**
> Although the **U7** add-on socket is natively designed to accommodate a **W5500** Ethernet module, using this wired connectivity under MicroPython requires special software attention. Unlike standard scripts, activating the W5500 network features **requires a custom recompilation of the MicroPython firmware** to directly integrate the network stack drivers (C drivers) required by this component.

---

## 🛠️ Manufacturing & Assembly (Do It Yourself)

This project is fully Open Hardware. The **Gerber** file, electrical schematics, and the complete Bill of Materials (BOM) are available in the Hardware/ folder. You are free to export these files to have your printed circuit boards (PCBs) manufactured by the supplier of your choice.

⚠ **Required Technical Level & Tools:**  
Manual assembly of the PCB is a stimulating but **perfectly accessible challenge for most makers**, even if it is your very first transition to surface-mount components (SMD).

To facilitate hand-soldering and avoid frustration, the circuit was designed with smart hardware constraints:
* **Comfortable component size:** The smallest surface chips and resistors use the **0805** format. This is the ideal size for beginners, as the parts remain highly visible and easy to manipulate with tweezers.
* **No complex packages:** The board eliminates micro-components with invisible leads (such as QFN or BGA) that require a hot air station or a heating plate. A simple traditional soldering iron equipped with a fine tip is more than enough.

💡 **To succeed with your assembly, simply equip yourself with:**
* A classic fine-tip soldering iron (adjustable temperature recommended).
* High-quality fine solder wire.
* A jar or pen of **soldering flux** (the indispensable magic ingredient to cleanly align tin on SMD pads).
* High-precision tweezers.
* Good lighting, a dose of patience, and your uCompute Junior will come to life in less than an hour!

---

## 🛠 Hardware Specifications

| Feature | Component / Specification | Main Function |
| :--- | :--- | :--- |
| **Core** | Raspberry Pi Pico Socket (U1) | General computation and control |
| **Power Supply** | USB-C Input (6-pin) + Protective Fuse | General 5V |
| **Add-on** | Communication Module Socket (U7) | Wired network connectivity (SPI) |
| **Storage** | MicroSD Card Reader (TF Card) | Mass storage and file systems |
| **Main Display** | 1.3" IPS ST7789 LCD Screen (240x240) | High-resolution color graphical interface |
| **Optional Display** | SSD1306 OLED Screen Support (I2C) | Optional monochrome display |
| **EEPROM Memory** | CAT24CxxxWI-G (U5) | Non-volatile configuration backup |
| **Audio** | Active/passive piezoelectric buzzer (BUZ) | Sound alerts and audio effects |
| **Inputs** | 3-button resistor ladder (BTN1-BTN3) | User navigation and interaction (ADC reading) |
| **Extension** | UART Connector + NeoPixel Header + Header H1 | Serial connectivity, LED strips, and free GPIOs |

---
## 📋 Bill of Materials, Pinout, and Subsystems

| Quantité | Valeur / Référence | Désignation (Designator) | Nom du composant | Empreinte (Footprint) |
| :---: | :--- | :--- | :--- | :--- |
| **1** | RASPBERRY PI PICO | U1 | RASPBERRY PI PICO | RASPBERRY PI PICO / RASPBERRY PI PICO W |
| **1** | CAT24CxxxWI-G | U5 | CAT24CxxxWI-G | SOIC-8 |
| **1** | SD_CARD_TF | U6 | SD_CARD_TF | MICRO-USB-SMD_MICRO-SD |
| **1** | HX TYPE-C 6P QTWT | USB-C | HX TYPE-C 6P QTWT | TYPE-C-SMD_USB-TYPE-C-007 |
| **3** | 10nf | C1, C2, C3 | Capacitor | C0805 |
| **2** | 100uF | C4, C15 | 100uF | CAP-SMD_BD5.0-L5.3-W5.3-LS6.3-FD |
| **4** | 2kΩ | R13, R1, R5, R6 | 2k | R0805 |
| **3** | 10kΩ | R3, R4, R10 | 10k | R0805 |
| **3** | 1kΩ | R7, R8, R9 | 1k | R0805 |
| **2** | 5.1kΩ | R11, R12 | 5.1k | R0805 |
| **1** | 270Ω | R2 | 270r | R0805 |
| **1** | MBR120LSFT | D1 | MBR120LSFT | DO-214AC_L4.3-W2.7-LS5.3-RD |
| **1** | PPTC FUSE1206 | FUSE | PPTC FUSE1206 | F1206 |
| **2** | XL-1206QPC | 5V, 3V3 | XL-1206QPC | LED0805 |
| **1** | RX | RX | RX | LED0805 |
| **1** | TX | TX | TX | LED0805 |
| **2** | Connecteur femelle 20 pins | Emplacement Pico (U1) | Header femelle 1x20 Pas 2.54mm | CONN-TH_20P-P2.54mm |
| **2** | Connecteur femelle 6 pins | Emplacement Module (U7) | Header femelle 1x6 Pas 2.54mm | CONN-TH_6P-P2.54mm |
| **1** | Connecteur male 14 pins | Connecteur de prototypage (H1) | Header Male 1x14 Pas 2.54mm | HDR-TH_14P-P2.54-V-M|

## 📺 Options d'Affichage au Choix

Le circuit intègre une double empreinte vous laissant la liberté d'installer l'interface visuelle la plus adaptée à vos besoins :

| Écran TFT IPS ST7789 (1.3" - 240x240 px) | Écran OLED SSD1306 (0.96" - 128x64 px) |
| :---: | :---: |
| **Option graphique couleur (Bus SPI)** | **Option économique monochrome (Bus I2C)** |
| <img width="226" height="181" alt="Écran TFT IPS ST7789 couleur" src="https://github.com/user-attachments/assets/8058baaa-8250-4343-b1ee-2f4264cbfdd8" /> | <img width="175" height="164" alt="Écran OLED SSD1306 monochrome" src="https://github.com/user-attachments/assets/af83c2a7-cb08-471e-b7a2-98eef86f3fd2" /> |



---

## 📌 Brochage et Assignation des GPIO (Pinout)

> ⚠ **Note importante concernant les différences de GPIO :**
> Contrairement à la carte uCompute d'origine, la version Junior n'a pas accès aux broches **GP23** et **GP24**. Pour pallier cette limitation matérielle, les modifications et réallocations suivantes ont été appliquées :
> * **Sur le peigne d'E/S (Header H1) :** La broche **GP24** a été remplacée par la broche **GP07**.
> * **Pour le connecteur NeoPixel :** Le signal de contrôle, initialement sur le **GP23**, a été remappé sur la broche **GP06**.
> 
> **Conséquences logicielles et matérielles :**
> 1. Le uCompute Junior ne dispose plus de la broche dédiée à la **détection matérielle de présence de la carte MicroSD**.
> 2. Le contrôle matériel du rétroéclairage (**BLK**) de l'écran LCD ST7789 n'est plus disponible.

---

Toutes les connexions entre le Raspberry Pi Pico et les périphériques de la carte sont regroupées ci-dessous :

| Périphérique | Broche Pico (GPIO) | Fonction SPI / I2C / UART / ADC |
| :--- | :--- | :--- |
| **UART (Console)** | GPIO 0 | TX (LED Rouge d'état) |
| **UART (Console)** | GPIO 1 | RX (LED Verte d'état) |
| **Écran LCD ST7789** | GPIO 2 | SCL (Horloge SPI) |
| **Écran LCD ST7789** | GPIO 3 | SDA (Données SPI / MOSI) |
| **Écran LCD ST7789** | GPIO 4 | RES (Reset) |
| **Écran LCD ST7789** | GPIO 5 | DC |
| **Barrette NeoPixel** | GPIO 6 | Broche Neopixel |
| **Module Communication**| GPIO 8 | INT (Interruption) |
| **Module Communication**| GPIO 9 | CS (Chip Select Ethernet) |
| **Bus SPI Partagé (Réseau/SD)**| GPIO 10 | SCLK (Horloge SPI) |
| **Bus SPI Partagé (Réseau/SD)**| GPIO 11 | MOSI (Master Out Slave In) |
| **Bus SPI Partagé (Réseau/SD)**| GPIO 12 | MISO (Master In Slave Out) |
| **Lecteur MicroSD** | GPIO 13 | CS (Chip Select Carte SD) |
| **Buzzer** | GPIO 16 | Signal Audio (PWM) |
| **Écran OLED / EEPROM** | GPIO 20 | SDA (Bus I2C principal) |
| **Écran OLED / EEPROM** | GPIO 21 | SCL (Bus I2C principal) |
| **Échelle de Boutons** | GPIO 26 | Entrée Analogique ADC0 (BTN1, BTN2, BTN3) |

### Le bornier ( 1x14 pins Header):
Le bornier (pins Header) facilite le prototypage. l'espacement est standard a 2,54 mm ceci permet de l'enficher dans un carte de prototypage (Protoboard) ou des cables de liaison (jumper wires) avec embouts *Dupont* afin de relier vos circuits ou modules.

### Alimentations et signaux:
1. **5V** (Alimentation directe issue de l'USB, idéale pour la puissance)
2. **3.3V** 
3. **GND** (Masse commune)
4. **UART 0** : `GP0` (TX) & `GP1` (RX)
5. **2 Entrées Analogiques (ADC) :** `GP27` (ADC1) & `GP28` (ADC2)
6. **6 Broches Numériques (GPIO) :** `GP16`, `GP17`, `GP18`, `GP19`, `GP22`, `GP07`

<BR>

> [!CAUTION]
> **Le RP2040 n'est pas tolérant au 5V.** 
> Selon la section *Absolute Maximum Ratings* de la [fiche technique officielle du RP2040 (Datasheet)](https://pip-assets.raspberrypi.com/categories/814-rp2040/documents/RP-008371-DS-1-rp2040-datasheet.pdf), la tension maximale absolue sur les broches d'E/S (`IOVDD`) est de **3,63V**. L'application directe de 5V détruira le microcontrôleur.
<BR>

---

## 🔌 Architecture des Sous-Systèmes

### 1. Alimentation et Protection
Le circuit utilise un connecteur USB-C robuste limité aux lignes d'alimentation principales.
* **Sécurité :** Un fusible réarmable (FUSE) protège la carte contre les surintensités.
* **Anti-retour :** Une diode Schottky MBR120LSFT (D1) empêche les conflits d'alimentation lorsque le Pico est branché simultanément en USB natif et sur la carte.

### 2. Gestion des Entrées (Échelle Analogique)
Pour économiser les broches du Pico, les boutons **BTN1, BTN2 et BTN3** partagent une seule broche analogique (**GPIO 26 / ADC0**). 
* Chaque pression de bouton modifie la tension lue par l'ADC grâce à un pont diviseur de tension unique (R7, R8, R9, R10).

### 3. Bus de Communication
* **Bus I2C :** Partagé entre la mémoire EEPROM de stockage de configuration et le connecteur d'écran OLED standard (SSD1306). Des résistances de pull-up de 10k Ω (R3, R4) stabilisent le bus.
* **Bus SPI :** Partagé de manière efficace entre le module de communication et la carte MicroSD grâce à des lignes de sélection de puce (*Chip Select*) distinctes sur les GPIO 9 et 13.

---

## 📜 Licence

Le matériel (fichiers de conception, schémas, typons) et les logiciels de ce projet sont mis à disposition selon les termes de la Licence **Creative Commons Attribution - Pas d'Utilisation Commerciale - Partage dans les Mêmes Conditions 4.0 International (CC BY-NC-SA 4.0)**.

❌ **L'utilisation commerciale de ce projet (revente de PCBs nus, kits ou cartes retroPico assemblées) est strictement interdite sans autorisation préalable de l'auteur.**

Consultez le fichier [LICENSE](LICENSE) pour lire l'intégralité des termes.

---

## ☕ Soutenir le projet

Si vous appréciez mon travail et souhaitez m'offrir un café pour me soutenir bénévolement dans mes futurs projets de soudure et de code, vous pouvez me laisser un [**pourboire sur Ko-fi** ](https://ko-fi.com/jpmichon). C'est entièrement volontaire et grandement apprécié !
