# 🛠️ Fichiers Matériels, Schémas et Gerber / Hardware Files, Schematics & Gerbers

<img width="1221" height="854" alt="image" src="https://github.com/user-attachments/assets/c1f4fc4a-4bc2-4072-a7db-ae871a6176db" />

---

## :fr: Français

Ce répertoire contient tous les fichiers nécessaires pour inspecter le circuit électrique et faire fabriquer vos propres cartes **uCompute Junior** chez un fabricant de circuits imprimés (comme JLCPCB, PCBWay, etc.).

> [!NOTE]
> Si vous débutez et n'avez jamais commandé de circuits imprimés, sachez qu'il existe de nombreuses plateformes en ligne. De mon côté, j'utilise les services de JLCPCB. Si vous voulez tester leur site, vous pouvez utiliser mon lien de parrainage : **[JLCPCB](https://jlcpcb.com/?from=REDLD)**. Cela vous permettra d'obtenir des coupons de réduction pour vos premières impressions, tout en m'offrant des crédits pour soutenir et financer mes futurs projets. Rien ne vous y oblige bien sûr, mais c'est un excellent moyen de donner un coup de pouce à la chaîne !
>

---

### 📦 Contenu du répertoire

* **Fichiers de fabrication (`.zip`) :** Ces archives contiennent les **fichiers Gerber** prêts à être téléversés directement sur le site de votre fabricant de PCB pour lancer la production.
* **Schémas électriques (`.pdf`) :** Ces documents présentent l'évolution matérielle de la carte à travers ses différentes révisions.

### 🔄 Historique et détails techniques des révisions matérielles

* **Version 1.0 (PDF uniquement — Référence seulement) :** Version initiale de la carte. Elle n'inclut aucune protection matérielle sur le port **UART** ni d'étage d'amplification ou de limitation sur le **buzzer**. Ce schéma est conservé uniquement à titre de référence historique.
* **Version 1.1 (PDF + Fichier Gerber `.zip`) :** Première révision de production améliorée intégrant deux ajouts majeurs :
  * **Protection et stabilisation du port UART :** Ajout d'une diode Schottky (`MBR120LSFT`) pour éviter tout retour de courant indésirable sur l'alimentation **3,3V** lorsque le port UART est branché avant la mise sous tension du Junior, ainsi que de deux résistances de rappel (*pull-down*) de **100 kΩ** sur les lignes **TX** et **RX** pour éliminer les états flottants et empêcher les DEL d'état de briller faiblement au repos.
  * **Commande du buzzer par transistor (`BC847`) :** Le buzzer n'est plus piloté directement par la broche du microcontrôleur, mais via un transistor NPN, ce qui protège la sortie GPIO du Raspberry Pi Pico contre les appels de courant excessifs.
- **Version 1.2 (PDF uniquement) :** Ajout d'une résistance de 200 Ω et d'une diode de roue libre (`1N4148`) pour atténuer le volume du buzzer.
- **Version 1.3 (PDF + Gerber `.zip` — Recommandée) :** Optimisation de l'alimentation USB (condensateurs céramiques CMS `C5` de 4,7 µF et `C6` de 10 µF).


---

## :us: English

This directory contains all the files required to inspect the electrical circuit and have your own **uCompute Junior** printed circuit boards manufactured by a PCB fabrication service (such as JLCPCB, PCBWay, etc.).

> [!NOTE]
> If you are a beginner and have never ordered printed circuit boards before, you should know that there are many online platforms available. Personally, I use JLCPCB's services. If you want to test their website, you can use my referral link: **[JLCPCB](https://jlcpcb.com/?from=REDLD)**. This will allow you to get discount coupons for your first prints, while offering me credits to support and finance my future projects. Of course, you are under no obligation to do so, but it is an excellent way to give the channel a helping hand!
> 

---

### 📦 Directory Contents

* **Manufacturing Files (`.zip`):** These archives contain the ready-to-use **Gerber files** that can be uploaded directly to your PCB manufacturer's website to order boards.
* **Electrical Schematics (`.pdf`):** These documents detail the hardware evolution of the board across its different revisions.

### 🔄 Hardware Revision History & Technical Details

* **Version 1.0 (PDF only — Reference Only):** Initial release of the board. It does not include any hardware protection on the **UART** port or driver/limiting circuitry on the **buzzer**. This schematic is kept for historical reference only.
* **Version 1.1 (PDF + Gerber `.zip`):** First updated production revision introducing two major hardware improvements:
  * **UART Port Protection & Stabilization:** Addition of a Schottky diode (`MBR120LSFT`) to prevent back-powering the **3.3V** rail if an external UART device is connected while the Junior is unpowered, along with two **100 kΩ** pull-down resistors on the **TX** and **RX** lines to eliminate floating states and prevent the status LEDs from dimly glowing when idle.
  * **Transistor-Driven Buzzer (`BC847`):** The buzzer is no longer driven directly by the microcontroller pin, but switched through an NPN transistor, protecting the Raspberry Pi Pico's GPIO pin from excessive current draw.
- **Version 1.2 (PDF only):** Added a 200 Ω series resistor and `1N4148` flyback diode for buzzer volume reduction.
- **Version 1.3 (PDF + Gerber `.zip` — Recommended):** Updated USB power stage filtering (`C5` 4.7 µF, `C6` 10 µF SMD ceramic caps).

---

⬅️ [Retour à l'accueil du projet / Back to Project Home](../README.md)
