## [English version available here](./README.EN.md)

# uCompute Junior (Bring your own PICO)

Le **uComputeJunior** est une version allégée et beaucoup plus accessible de la plateforme [RP2040 uCompute](https://github.com/JPMichon/RP2040_uCompute). Pensée spécifiquement pour les **bricoleurs novices et les makers**, elle adopte un format *"Bring your own Pico"* : elle élimine le besoin de souder des composants de surface complexes (CMS) en accueillant directement un module Raspberry Pi Pico standard prêt à l'emploi. 

Cette carte sert de passerelle d'initiation matérielle pour s'intégrer facilement dans l'environnement global uCompute et facilite, par la même occasion, la prise en main et l'accès aux projets de l'écosystème comme le robot programmable [uCompute Rover](https://github.com/JPMichon/uCompute_Rover).


<img width="558" height="367" alt="image" src="https://github.com/user-attachments/assets/9ae96d46-1b85-4960-8d46-99c5ffb2fcdd" />


---

## 🎓 Une solution idéale pour l'enseignement et les Fablabs

Le **uCompute Junior** s'impose comme l'outil parfait pour l'initiation à l'électronique et aux systèmes embarqués, que ce soit en milieu scolaire (**écoles et collèges**) ou au sein des **Fablabs**. 

* **Pour le milieu éducatif :** Grâce à son approche *"Bring your own Pico"*, il simplifiera grandement la mise en œuvre en classe en accueillant un module Raspberry Pi Pico standard prêt à l'emploi. En combinant la puissance de la communauté **Raspberry Pi Pico**, la clarté du langage **MicroPython** et la flexibilité de l'écosystème **uCompute**, les enseignants disposent d'un environnement clé en main pour structurer des ateliers pratiques captivants (du simple clignotement de LED au pilotage du *uCompute Rover*).
* **Pour les Fablabs et ateliers pratiques :** Bien que la carte nécessite de la soudure de surface (CMS), le choix s'est délibérément porté sur des composants de taille **0805**, particulièrement faciles à manipuler et à souder à la main. Cela en fait un excellent support pédagogique pour dédramatiser et enseigner la soudure CMS sans nécessiter d'équipement industriel complexe (comme un four ou une plaque chauffante).

L'intégralité du projet est propulsée par les valeurs de l'Open Hardware et partagée sous licence **CC BY-NC-SA 4.0**. L'ensemble des fichiers de fabrication (Gerber, schémas) étant librement accessible, les établissements scolaires tout comme les Fablabs peuvent commander, modifier ou produire localement leurs propres cartes à moindre coût, favorisant une autonomie technologique totale et un partage des connaissances sans friction budgétaire.

💵 **Un budget maîtrisé :** Avec un coût de revient estimé à **20$ CAD (~13€)** par carte (incluant le PCB, le Pi Pico et l'écran), c'est la solution idéale pour équiper une classe entière ou un Fablab à moindre coût.

> [!NOTE]
> Si vous débutez et n'avez jamais commandé de circuits imprimés, sachez qu'il existe de nombreuses plateformes en ligne. De mon côté, j'utilise les services de JLCPCB. Si vous voulez tester leur site, vous pouvez utiliser mon lien de parrainage : **[JLCPCB](https://jlcpcb.com/?from=REDLD)**. Cela vous permettra d'obtenir des coupons de réduction pour vos premières impressions, tout en m'offrant des crédits pour soutenir et financer mes futurs projets. Rien ne vous y oblige bien sûr, mais c'est un excellent moyen de donner un coup de pouce à la chaîne !

---

### 📻 Modules d'extension & Rétrocompatibilité (Add-ons)

Le grand point fort du **uCompute Junior** réside dans l'intégration native de son connecteur d’extension d'add-on et de son peigne d'E/S (Header H1). Bien qu'il s'agisse d'une version allégée, la carte conserve une **compatibilité totale et descendante avec l'ensemble des modules de communication et d'extension de l'écosystème uCompute**. 

Cela vous permet de faire évoluer instantanément votre Junior (liaisons sans fil, télémétrie robotique, pilotage à distance) en y clipsant directement les cartes filles matérielles issues du projet principal ou du Rover.

👉 **[Accéder au répertoire des modules de l'écosystème (RP2040_uCompute Modules)](https://github.com/JPMichon/RP2040_uCompute/tree/main/Modules)**

| Emplacement sur le Junior | Module compatible | Description & Fonctionnalités | Rendu Matériel |
| :--- | :--- | :--- | :--- |
| **Add-On module** <br>(Communication) | **Module Wi-Fi** <br>(ESP-12F) | Carte d'adaptation embarquant un ESP8266 pour ajouter une connectivité Wi-Fi complète. | <img width="100" height="133" alt="Module Wi-Fi ESP-12F" src="https://github.com/user-attachments/assets/f0c80621-1b07-46e6-844b-4594e3d338f9" /> |
| **Add-On module** <br>(Communication) | **Module Radio** <br>(NRF24L01) | Adaptateur pour liaisons radio 2,4 GHz, idéal pour la communication bidirectionnelle. | <img width="112" height="140" alt="Module Radio NRF24L01" src="https://github.com/user-attachments/assets/a6a0a83b-80ed-4dbc-bc28-06579f64b54c" /> |
| **Add-On module** <br>(Communication) | **Module LoRa** <br>(RFM95W) | Adaptateur longue portée exploitant la technologie radio LoRa. | <img width="112" height="140" alt="Module LoRa RFM95W" src="https://github.com/user-attachments/assets/729ed810-e456-4e6b-88fb-1f3c61edea25" /> |
| **Header H1** <br>(Connecteur E/S) | **µCompute Remote** <br>| Carte d'extension intégrant un joystick analogique et des boutons pour le pilotage RC. | <img width="175" height="131" alt="Manette uCompute Remote" src="https://github.com/user-attachments/assets/25dda003-8ab8-48c4-a7d1-1a45fdbca7a4" /> |
| **Header H1** <br>(Connecteur E/S) | **µCompute Rover** <br> | Contrôleur pour moteurs CC (2+2), servomoteur, capteur HC-SR04 et module GPS Neo-6M. | <img width="220" height="145" alt="Contrôleur uCompute Rover" src="https://github.com/user-attachments/assets/90114819-d70b-4cbb-8cfd-5e95b66cca84" /> |

> ℹ **Note technique concernant le support réseau (Module W5500) :**
> Bien que le connecteur d'add-on **U7** soit nativement conçu pour accueillir un module Ethernet **W5500**, l'utilisation de cette connectivité filaire sous MicroPython requiert une attention logicielle particulière. Contrairement aux scripts standards, l'activation des fonctionnalités réseau du W5500 **nécessite une recompilation personnalisée du firmware MicroPython** afin d'y intégrer directement les pilotes de pile réseau (*drivers C*) requis par ce composant.

---

## 🛠️ Fabrication & Assemblage (Do It Yourself)

Ce projet est entièrement Open Hardware. Les fichiers **Gerber**, les schémas électriques ainsi que la liste complète des composants (BOM) sont disponibles dans le dossier `Hardware/`. Vous pouvez librement exporter ces fichiers pour faire fabriquer vos circuits imprimés (PCBs) chez le fournisseur de votre choix.

⚠ **Niveau technique requis & Matériel :**  
L'assemblage manuel du PCB est un défi stimulant mais **parfaitement accessible à la majorité des bidouilleurs**, même s'il s'agit de votre première transition vers les composants montés en surface (CMS). 

Afin de faciliter le travail à la main et d'éviter la frustration, le circuit a été conçu avec des contraintes matérielles intelligentes :
* **Taille de composants confortable :** Les plus petites puces et résistances de surface utilisent le format **0805**. C'est la taille idéale pour s'initier, car les pièces restent bien visibles et faciles à manipuler à la pince.
* **Pas de boîtiers complexes :** La carte élimine les micro-composants aux broches invisibles (comme les QFN ou BGA) qui exigent une station à air chaud ou une plaque chauffante. Un simple fer à souder traditionnel équipé d'une panne fine suffit amplement.

💡 **Pour réussir votre montage, munissez-vous simplement de :**
* Un fer à souder classique à pointe fine (température réglable recommandée).
* De la soudure fine de bonne qualité.
* Un pot ou un stylo de **flux de soudure** (l'ingrédient magique indispensable pour aligner proprement l'étain sur les pastilles CMS).
* Une pince de précision brucelle (tweezers).
* Un bon éclairage, une dose de patience, et votre uCompute Junior prendra vie en moins d'une heure !

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
## 📋 Liste des Composants (BOM - Bill of Materials)

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
			

