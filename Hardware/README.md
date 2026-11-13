# 🛠️ Fichiers Matériels, Schémas et Gerber / Hardware Files, Schematics & Gerbers

<img width="940" height="662" alt="image" src="https://github.com/user-attachments/assets/b8a9ec69-8dfc-4981-867d-9f80f5ed3610" />


## :fr: Français

Ce répertoire contient tous les fichiers nécessaires pour inspecter le circuit électrique et faire fabriquer vos propres cartes **uCompute Junior** chez un fabricant de circuits imprimés (comme JLCPCB, PCBWay, etc.).

### 📦 Contenu du répertoire

* **Fichiers de fabrication (`.zip`) :** Ces archives contiennent les **fichiers Gerber** prêts à être téléversés directement sur le site de votre fabricant de PCB pour lancer la production.
* **Schémas électriques (`.pdf`) :** Ces documents présentent l'évolution matérielle de la carte à travers ses différentes révisions.

### 🔄 Historique des révisions matérielles

* **Version 1.0 (PDF uniquement — Référence seulement) :** Version initiale de la carte. Elle n'inclut aucune protection matérielle sur le port **UART** ni sur le circuit du **buzzer**. Ce schéma est conservé uniquement à titre de référence historique.
* **Version 1.1 (PDF + Fichier Gerber `.zip`) :** Première révision de production corrigée, ajoutant les protections nécessaires au bon fonctionnement et à la fiabilité des interfaces (notamment sur le port UART).
* **Version 1.2 (PDF + Fichier Gerber `.zip` — Recommandée) :** Dernière révision matérielle. Elle intègre l'ajout d'une **résistance et d'une diode** sur le circuit du **buzzer piézoélectrique** afin de limiter le courant et d'adoucir son volume sonore (le rendant beaucoup plus agréable en classe ou en Fablab).

---

## :us: English

This directory contains all the files required to inspect the electrical circuit and have your own **uCompute Junior** printed circuit boards manufactured by a PCB fabrication service (such as JLCPCB, PCBWay, etc.).

### 📦 Directory Contents

* **Manufacturing Files (`.zip`):** These archives contain the ready-to-use **Gerber files** that can be uploaded directly to your PCB manufacturer's website to order boards.
* **Electrical Schematics (`.pdf`):** These documents detail the hardware evolution of the board across its different revisions.

### 🔄 Hardware Revision History

* **Version 1.0 (PDF only — Reference Only):** Initial release of the board. It does not include any hardware protection on the **UART** port or the **buzzer** circuit. This schematic is kept for historical reference only.
* **Version 1.1 (PDF + Gerber `.zip`):** First updated production revision, adding essential interface protections (such as on the UART port) for improved reliability.
* **Version 1.2 (PDF + Gerber `.zip` — Recommended):** Latest hardware revision. It adds a **resistor and a diode** to the **piezoelectric buzzer** circuit to limit current and reduce its volume level (making it much more comfortable to use in classrooms or Fablabs).

---

⬅️ [Retour à l'accueil du projet / Back to Project Home](../README.md)
