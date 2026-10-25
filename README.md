## [English version available here](./README.EN.md)

# uCompute Junior (Bring your own PICO)

Le **uComputeJunior** est une carte d'extension et de développement conçue autour du microcontrôleur **Raspberry Pi Pico**. Fidèle à la philosophie *"Bring your own Pico"*, cette plateforme intègre de nombreux composants pour l'affichage, le stockage, le réseau et les interactions, tout en restant accessible et modulaire.

<img width="497" height="314" alt="image" src="https://github.com/user-attachments/assets/13087ef4-5fba-496f-962a-4c9e4731b73f" />


---

## 🛠️ Fabrication & Assemblage (Do It Yourself)

Ce projet est sous licence **CC BY-NC-SA 4.0**. Les fichiers **Gerber** ainsi que la liste des composants (BOM) sont disponibles dans le dossier `Hardware/`. Vous pouvez librement faire fabriquer les PCBs chez le fournisseur de votre choix.

⚠️ **Niveau technique requis :** L'assemblage manuel du PCB reste relativement simple, les plus petites composantes de surface sont de format 0805. Un fer a souder muni d'une pointe fine, du flux et un peu de patience, c'est un défit tout a fait accessible à la majorité de bidouilleur.

---

## 🛠 Spécifications Matérielles

| Caractéristique | Composant / Spécification | Fonction principale |
| :--- | :--- | :--- |
| **Cœur** | Emplacement pour Raspberry Pi Pico (U1) | Calcul et contrôle général |
| **Alimentation** | Entrée USB-C (6 broches) + Fusible de protection | Alimentation générale 5V / 3.3V |
| **Add-on** | Module de communication (U7) | Connectivité réseau filaire (SPI) |
| **Stockage** | Lecteur de carte MicroSD (TF Card) | Stockage de masse et systèmes de fichiers |
| **Affichage 1** | Écran LCD 1.3" IPS ST7789 (240x240) | Interface graphique couleur haute résolution |
| **Affichage alternative** | Support d'écran OLED SSD1306 (I2C) | Affichage optionnel monochrome |
| **Mémoire EEPROM** | CAT24CxxxWI-G (U5) | Sauvegarde de configuration non-volatile |
| **Audio** | Buzzer piézoélectrique actif/passif (BUZ) | Alertes sonores et effets audio |
| **Entrées** | Échelle de 3 boutons poussoirs (BTN1-BTN3) | Navigation et interactions utilisateur (lecture ADC) |
| **Extension** | Connecteur UART + Header Neopixel + Header H1 | Connectivité série, bandeaux LED et GPIO libres |

---

## 📌 Brochage et Assignation des GPIO (Pinout)

Toutes les connexions entre le Raspberry Pi Pico et les périphériques de la carte sont regroupées ci-dessous :

| Périphérique | Broche Pico (GPIO) | Fonction SPI / I2C / UART / ADC |
| :--- | :--- | :--- |
| **UART (Console)** | GPIO 0 | TX (LED Rouge d'état) |
| **UART (Console)** | GPIO 1 | RX (LED Verte d'état) |
| **Écran LCD ST7789** | GPIO 2 | SCL (Horloge SPI) |
| **Écran LCD ST7789** | GPIO 3 | SDA (Données SPI / MOSI) |
| **Écran LCD ST7789** | GPIO 4 | RES (Reset) / DC / BL |
| **Écran LCD ST7789** | GPIO 5 | Contrôle additionnel / Backlight |
| **Barrette NeoPixel** | GPIO 6 | Sortie données LED RGB adressables |
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
			

