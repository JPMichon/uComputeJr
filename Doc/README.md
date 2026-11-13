# 👋 Tour du propriétaire : uCompute Junior (Rev 1.0)

Super, vous avez maintenant votre **uCompute Junior** (version 1.0 sur la photo) en main ! Il est temps de faire un tour du propriétaire pour bien comprendre ses fonctionnalités, en commençant par la section en haut à gauche consacrée à l'alimentation.

<img width="1050" height="724" alt="Plain_junior_V1" src="https://github.com/user-attachments/assets/48943b12-aabe-4664-ba01-e11337469098" />

## 🔌 Le port USB-C (Alimentation uniquement)

Situé sur le bord supérieur gauche, ce connecteur USB-C est dédié exclusivement à l'alimentation et ne transfère aucune donnée. Il remplit trois rôles principaux :

1. **Fonctionnement autonome :** Alimenter le Junior sans avoir à le relier à un ordinateur via le port USB du Raspberry Pi Pico.
2. **Alimentation des NeoPixels :** Fournir le 5V nécessaire aux DEL adressables branchées sur le connecteur à 3 broches situé juste en dessous.
3. **Distribution sur le bornier H1 :** Alimenter la broche 1 (**5V**) du connecteur principal **H1** au bas de la carte.

## ⚡ Options d'alimentation et sécurité

* **Sources alternatives :** En plus du port USB-C, vous pouvez alimenter la carte directement en injectant du 5V sur la **broche 1 (5V) du connecteur H1**. *Petite astuce :* la broche **5V** du connecteur **NEOPIXEL** est reliée au même rail et peut également servir d'entrée d'alimentation.
* **Une seule source externe à la fois :** Ne branchez jamais simultanément une source sur le port USB-C de la carte et une autre sur la broche 5V de H1 (ou du connecteur NeoPixel).
* **Protection anti-retour intégrée :** Grâce à sa diode de protection (D1), le Junior est conçu pour accepter une alimentation externe (via son port USB-C) en même temps que le câble USB reliant votre ordinateur au Raspberry Pi Pico, sans risque de conflit électrique.

## 💡 Les témoins lumineux (DEL d'état)

Juste au-dessus du connecteur USB-C se trouvent deux DEL très pratiques pour diagnostiquer l'état de votre carte d'un coup d'œil :

* **DEL 3V3 (Verte) :** Indique que le Raspberry Pi Pico est actif et que son régulateur interne génère bien la tension de 3,3V.
* **DEL 5V (Orange) :** Confirme qu'une tension de 5V est présente sur la carte (fournie soit par le port USB-C du Junior, soit par la broche 5V du bornier H1).

> 💡 **Recommandation pour le mode autonome :** Pour alimenter votre Junior via son port USB-C, l'utilisation d'une batterie externe (*powerbank*) est idéale. Comme la carte ne consomme que quelques milliampères, un modèle compact d'une capacité inférieure à **5 000 mAh** est amplement suffisant.

## 🔗 Le bus I2C et la mémoire EEPROM

En poursuivant vers la droite sur le bord supérieur, on retrouve le connecteur principal du **bus I2C**. Ce protocole à deux fils permet de relier facilement une multitude de capteurs externes ou d'écrans supplémentaires.

* **Brochage :** Le connecteur offre les 4 signaux standards : **3V3**, **GND**, **SCL** (GPIO 21) et **SDA** (GPIO 20).
* **Résistances intégrées :** Des résistances de rappel (*pull-up*) de 10 kΩ (R3 et R4) sont déjà soudées sur la carte. Vous n'avez pas besoin d'en ajouter sur vos modules externes.
* **Mémoire non-volatile intégrée :** Juste à droite de ce connecteur se trouve une puce mémoire EEPROM (**AT24Cxx**, accessible à l'adresse `0x50`). Elle est connectée sur ce même bus I2C et permet à vos programmes de sauvegarder des paramètres ou des scores de jeu même lorsque la carte est débranchée.

## 📡 Le port série UART et les témoins TX / RX

À côté de l'EEPROM se situe le connecteur **UART** (communication série), idéal pour le débogage ou pour dialoguer avec d'autres microcontrôleurs et modules (GPS, Bluetooth, etc.).

* **Brochage :** Il donne accès aux lignes **3V3**, **RX** (GPIO 1), **TX** (GPIO 0) et **GND**.
* **Témoins lumineux d'activité :** À gauche de ce connecteur, deux DEL vous permettent de visualiser le trafic de données en temps réel :
  * **DEL RX (Verte) :** Clignote lorsque le Junior reçoit des données sur la broche GPIO 1.
  * **DEL TX (Rouge) :** Clignote lorsque le Junior transmet des données via la broche GPIO 0.

> ℹ️ **Pourquoi les DEL TX et RX brillent-elles faiblement au démarrage ?**
> Si vous remarquez que les DEL TX et RX restent partiellement allumées (avec une faible intensité) lorsque vous mettez la carte sous tension, **c'est tout à fait normal**. Tant que le port UART n'est pas explicitement initialisé dans votre code MicroPython, les broches GPIO 0 et GPIO 1 du Raspberry Pi Pico demeurent à l'état flottant (haute impédance), ce qui laisse passer un léger courant résiduel à travers les DEL. Elles s'éteindront complètement dès que le périphérique UART sera configuré par logiciel.

## 🔊 Le buzzer piézoélectrique (Sortie audio)

Dans la partie supérieure de la carte, entre le connecteur UART et l'emplacement des modules de communication, trône un **buzzer piézoélectrique**.

* **Contrôle PWM :** Il est piloté par la broche **GPIO 11**. En faisant varier la fréquence du signal PWM (*Pulse Width Modulation*) dans votre code, vous pouvez générer aussi bien de simples bips d'alerte que des mélodies rétro ou des effets sonores pour vos jeux.
  
## 📻 Le port d'extension *Add-on Module* (Communications)

Tout en haut à droite de la carte se trouve un double connecteur femelle à 6 broches (désigné **U7**). Cet emplacement est spécialement conçu pour accueillir les modules de communication sans fil et filaires de l'écosystème uCompute.

**Rétrocompatibilité totale :** Vous pouvez y clipser directement les cartes d'adaptation conçues pour le uCompute original, notamment :
  * **Wi-Fi :** Module ESP-12F (ESP8266) pour connecter vos projets à Internet.
  * **Radio courte portée :** Module NRF24L01+ (2,4 GHz) pour la télémétrie ou le pilotage à distance (ex. avec la manette *uCompute Remote*).
  * **Longue portée :** Module LoRa (RFM95W) pour les liaisons radio longue distance.
  * **Réseau filaire :** Module Ethernet W5500 *(nécessite un firmware MicroPython compilé avec les pilotes C correspondants)*.

> ⚠️ **Attention au sens d'insertion :** Avant de mettre la carte sous tension, assurez-vous toujours de bien aligner les broches d'alimentation (**GND** et **3V3**) de votre carte fille avec celles indiquées sur la sérigraphie du Junior. Un branchement inversé pourrait endommager le module radio ou le régulateur du Pico.

## 🧠 L'emplacement du Raspberry Pi Pico (Le cerveau)

Au centre gauche de la carte se trouvent deux longues rangées de connecteurs femelles à 20 broches. C'est ici que vient s'insérer le microcontrôleur qui donnera vie à votre uCompute Junior, selon l'approche *"Bring your own Pico"* (apportez votre propre Pico).

* **Compatibilité étendue :** Comme l'indique la sérigraphie au centre de l'emplacement, le Junior est conçu pour accueillir toute la famille des cartes Pico (architecture RP2040 et RP2350) :
  * **Raspberry Pi Pico** (modèle standard)
  * **Raspberry Pi Pico W** (avec Wi-Fi et Bluetooth intégrés)
  * **Raspberry Pi Pico 2** (nouvelle génération plus performante)
  * **Raspberry Pi Pico 2 W** (nouvelle génération avec connectivité sans fil)
* **Un assemblage sans contrainte :** L'utilisation de connecteurs femelles permet de retirer ou de remplacer le Pico à tout moment, sans aucune soudure supplémentaire. C'est idéal pour réutiliser un même Pico sur plusieurs projets ou pour le remplacer facilement en cas d'erreur de manipulation en classe.
* **Connexion directe au PC :** Une fois en place, le port micro-USB (ou USB-C selon les variantes) du Pico reste parfaitement accessible sur le bord gauche de la carte pour programmer votre code en MicroPython via Thonny ou VS Code.

> ⚠️ **Sens d'insertion obligatoire :** Veillez toujours à insérer votre Raspberry Pi Pico avec son **connecteur USB orienté vers la gauche** (du même côté que le port USB-C d'alimentation du Junior et en alignement avec l'icône de framboise dessinée sur le circuit). Une insertion à l'envers inverserait les broches d'alimentation et risquerait d'endommager définitivement le microcontrôleur.

## 📺 Les options d'affichage (Écran couleur ou monochrome)

Pour rendre vos projets interactifs, le uCompute Junior intègre une double empreinte vous permettant de choisir entre un écran graphique couleur haute résolution ou un petit écran monochrome économique.

### 1. L'écran principal : TFT IPS 1,3" ST7789 (Couleur)
Juste à droite de l'emplacement du Raspberry Pi Pico se trouve une rangée verticale de 7 broches dédiée à un module d'écran LCD couleur de **1,3 pouce** (résolution de **240 × 240 pixels**) piloté par la puce **ST7789** via le bus SPI.

* **Installation en superposition :** Une fois soudé (ou monté sur un connecteur femelle), cet écran vient se positionner directement **au-dessus du Raspberry Pi Pico**, offrant un format compact type console portable.
* **Brochage (de haut en bas) :**
  * **BLK :** Rétroéclairage *(non connecté sur la version Junior ; le rétroéclairage reste actif en permanence)*
  * **DC :** Sélection Données/Commande (**GPIO 5**)
  * **RES :** Réinitialisation / Reset (**GPIO 4**)
  * **SDA :** Données SPI / MOSI (**GPIO 3**)
  * **SCL :** Horloge SPI (**GPIO 2**)
  * **3V3 :** Alimentation 3,3V
  * **GND :** Masse commune

### 2. L'écran alternatif : OLED SSD1306 (Monochrome)
Juste au-dessus de l'emplacement de la carte MicroSD, un connecteur horizontal à 4 broches (identifié *Alt Display*) permet d'utiliser un écran **OLED 0,96 pouce** (**128 × 64 pixels**) basé sur le contrôleur **SSD1306**.

* **Simplicité I2C :** Ce module utilise le bus I2C principal (**GPIO 20** pour SDA et **GPIO 21** pour SCL) avec l'ordre de broches standard **GND - 3V3 - SCL - SDA**.
* **Idéal pour les budgets serrés :** C'est une excellente alternative économique pour afficher des menus, des valeurs de capteurs ou des messages de débogage tout en libérant les broches SPI utilisées par l'écran couleur.

> 💡 **Astuce de montage :** Si vous utilisez un connecteur femelle pour l'écran couleur ST7789, assurez-vous qu'il soit suffisamment haut (ou utilisez des entretoises) pour que le circuit de l'écran ne touche pas les composants métalliques du Raspberry Pi Pico situé juste en dessous.

## 💾 Le lecteur de carte MicroSD (Stockage de masse)

Sur le bord droit de la carte, juste sous le connecteur de l'écran alternatif OLED, se trouve un lecteur de carte **MicroSD (TF Card)**. Il permet d'étendre considérablement la mémoire de votre projet pour stocker des images, des fichiers audio, des journaux de données (*datalogging*) ou des ressources pour vos jeux.

* **Bus SPI partagé :** Ce lecteur partage les lignes de communication SPI (**GP14** pour SCK, **GP15** pour MOSI et **GP12** pour MISO) avec le connecteur des modules de communication (*Add-on Module*). La sélection de la carte SD s'effectue via la broche **GPIO 13** (Chip Select).
* **Particularité matérielle :** Pour économiser des broches sur le Pico, la détection mécanique de présence de carte (*Card Detect*) n'est pas câblée sur le Junior. L'initialisation se fait directement par logiciel lors du montage du système de fichiers en MicroPython.


## 🎮 Les boutons de contrôle et de réinitialisation

En bas à droite du circuit se regroupent les commandes physiques permettant d'interagir directement avec vos programmes :

* **Le bouton RESET (jaune) :** Situé à gauche du groupe de boutons, il est relié directement à la broche `RUN` du Raspberry Pi Pico. Une simple pression permet de redémarrer instantanément votre microcontrôleur sans avoir à débrancher l'alimentation.
* **Les 3 boutons d'action (BTN1, BTN2, BTN3) :** Alignés côte à côte, ces trois boutons poussoirs servent à naviguer dans vos menus ou à contrôler vos jeux.
  * **Astuce électronique (Échelle analogique) :** Pour n'utiliser qu'une seule broche du Pico au lieu de trois, ces boutons sont montés en pont diviseur de tension (via les résistances R7, R8, R9 et R10) et reliés à l'entrée analogique **GPIO 26 (ADC0)**. Chaque bouton envoie une tension différente que votre code lit pour identifier quelle touche est pressée.

## 🔌 Le bornier principal d'extension (Header H1)

Tout au long du bord inférieur gauche s'étend un connecteur mâle à **14 broches** (identifié **H1**) au pas standard de **2,54 mm**. C'est la porte d'entrée idéale pour le prototypage sur plaque d'essai (*breadboard*) avec des câbles Dupont, ou pour y clipser les cartes d'extension de l'écosystème comme le robot **uCompute Rover** ou la manette **uCompute Remote**.

* **Brochage complet (de gauche à droite) :**
  1. **5V** : Alimentation directe (issue de l'USB-C ou du Pico)
  2. **GND** : Masse commune
  3. **3V3** : Alimentation régulée 3,3V
  4. **GND** : Masse commune
  5. **GP16** : Broche numérique / SPI / I2C / PWM
  6. **GP17** : Broche numérique / SPI / I2C / PWM
  7. **GP18** : Broche numérique / SPI / I2C / PWM
  8. **GP19** : Broche numérique / SPI / I2C / PWM
  9. **GP22** : Broche numérique / PWM
  10. **GP07** : Broche numérique / PWM *(remplace le GP24 du modèle original)*
  11. **GP27** : Entrée analogique **ADC1** (ou numérique)
  12. **GP28** : Entrée analogique **ADC2** (ou numérique)
  13. **GP01 / RX** : Réception série UART 0
  14. **GP00 / TX** : Transmission série UART 0

> ⚠️ **Rappel de sécurité :** Comme sur tout Raspberry Pi Pico, les broches d'entrée/sortie (GPIO) du bornier H1 fonctionnent exclusivement en **3,3V**. N'appliquez jamais de signal **5V** directement sur une broche GPIO au risque d'endommager irrémédiablement le processeur.


