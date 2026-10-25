## [English version available here](./README.EN.md)

# uCompute Junior (Bring your own PICO)

Ce projet est sous licence **CC BY-NC-SA 4.0**. Les fichiers **Gerber** ainsi que la liste des composants (BOM) sont disponibles dans le dossier `Hardware/`. Vous pouvez librement faire fabriquer les PCBs chez le fournisseur de votre choix.

Le **uComputeJunior** est une version allégée et beaucoup plus accessible de la plateforme [RP2040 uCompute](https://github.com/JPMichon/RP2040_uCompute). Pensée spécifiquement pour les **bricoleurs novices et les makers**, elle adopte un format *"Bring your own Pico"* : elle élimine le besoin de souder des composants de surface complexes (CMS) en accueillant directement un module Raspberry Pi Pico standard prêt à l'emploi. 

Cette carte sert de passerelle d'initiation matérielle pour s'intégrer facilement dans l'environnement global uCompute et facilite, par la même occasion, la prise en main et l'accès aux projets de l'écosystème comme le robot programmable [uCompute Rover](https://github.com/JPMichon/uCompute_Rover).


<img width="497" height="314" alt="image" src="https://github.com/user-attachments/assets/13087ef4-5fba-496f-962a-4c9e4731b73f" /><br>

---

## 🎓 Une solution idéale pour l'enseignement et les Fablabs

Le **uCompute Junior** s'impose comme l'outil parfait pour l'initiation à l'électronique et aux systèmes embarqués, que ce soit en milieu scolaire (**écoles et collèges**) ou au sein des **Fablabs**. 

* **Pour le milieu éducatif :** Grâce à son approche *"Bring your own Pico"*, il minimise la complexité et la frustration liées à la soudure de composants de surface CMS, offrant aux élèves une introduction fluide, sécurisante et gratifiante. En combinant la puissance de la communauté **Raspberry Pi Pico**, la clarté du langage **MicroPython** et la flexibilité de l'écosystème **uCompute**, les enseignants disposent d'un environnement clé en main pour structurer des ateliers pratiques captivants (du simple clignotement de LED au pilotage du *uCompute Rover*).
* **Pour les Fablabs et Makerspaces :** Cette carte représente le projet communautaire idéal. Sa conception entièrement basée sur des composants traversants (THT) en fait un excellent support d'apprentissage pour les ateliers d'initiation à la soudure traditionnelle. Elle permet aux membres de s'approprier un matériel polyvalent sans dépendre de machines de pose CMS complexes.

L'intégralité du projet est propulsée par les valeurs de l'Open Hardware et partagée sous licence **CC BY-NC-SA 4.0**. L'ensemble des fichiers de fabrication (Gerber, schémas) étant librement accessible, les établissements scolaires tout comme les Fablabs peuvent commander, modifier ou produire localement leurs propres cartes à moindre coût, favorisant une autonomie technologique totale et un partage des connaissances sans friction budgétaire.


---

## 🛠️ Fabrication & Assemblage (Do It Yourself)

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
			

