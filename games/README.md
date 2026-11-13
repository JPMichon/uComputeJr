# 🎮 Jeux et Démos Graphiques / Games & Graphic Demos

[Français](#-français) | [English](#-english)

---

## <img src="https://flagcdn.com" width="24" height="18" alt="Drapeau France"> Français

Ce répertoire regroupe des jeux rétro et des animations graphiques développés en **MicroPython** spécialement pour le **uCompute Junior**. Ils tirent parti de l'écran couleur **TFT IPS ST7789 (240×240)**, du buzzer piézoélectrique et des boutons de navigation intégrés.

### 🕹️ Liste des programmes

* **[st7789_BREAKOUT.py](st7789_BREAKOUT.py)** — Le grand classique du casse-briques. Déplacez la raquette avec les boutons pour détruire tous les blocs à l'écran sans laisser tomber la balle.
* **[st7789_PONG.py](st7789_PONG.py)** — Le célèbre jeu d'arcade de tennis de table. Affrontez l'ordinateur dans des échanges de plus en plus rapides.
* **[st7789_GameOfLife.py](st7789_GameOfLife.py)** — Une simulation visuelle de l'automate cellulaire du *Jeu de la vie* de John Conway, illustrant l'évolution de générations de cellules à l'écran.
* **[st7789_DigitalRain.py](st7789_DigitalRain.py)** — Une animation graphique inspirée de la célèbre « pluie numérique » de *Matrix*.

### ⚙️ Prérequis et lancement

1. **Matériel requis :** Un **uCompute Junior** équipé de son **écran couleur ST7789 (240×240)** et d'un Raspberry Pi Pico (ou Pico W / Pico 2).
2. **Bibliothèques :** Assurez-vous d'avoir préalablement copié les pilotes nécessaires depuis le dossier [`lib/`](../lib/) sur la mémoire de votre Pico.
3. **Exécution :** Ouvrez le fichier souhaité dans **Thonny** (ou votre éditeur MicroPython) et lancez-le directement sur la carte, ou renommez-le en `main.py` pour qu'il démarre automatiquement à la mise sous tension.

---

## <img src="https://flagcdn.com" width="24" height="18" alt="US Flag"> English

This directory contains retro games and visual demos written in **MicroPython** specifically for the **uCompute Junior**. They take full advantage of the **ST7789 IPS color display (240×240)**, the onboard piezoelectric buzzer, and the navigation pushbuttons.

### 🕹️ Available Programs

* **[st7789_BREAKOUT.py](st7789_BREAKOUT.py)** — The classic brick-breaker arcade game. Move the paddle using the onboard buttons to clear all the bricks without dropping the ball.
* **[st7789_PONG.py](st7789_PONG.py)** — The iconic table-tennis arcade game. Compete against the CPU as the ball speed gradually increases.
* **[st7789_GameOfLife.py](st7789_GameOfLife.py)** — A visual simulation of John Conway's *Game of Life* cellular automaton, watching generations of cells evolve in real time.
* **[st7789_DigitalRain.py](st7789_DigitalRain.py)** — A visual demo inspired by the iconic *Matrix* digital rain effect.

### ⚙️ Requirements & How to Run

1. **Required hardware:** A **uCompute Junior** fitted with the **ST7789 color LCD screen (240×240)** and a Raspberry Pi Pico (or Pico W / Pico 2).
2. **Libraries:** Make sure you have copied the required display drivers from the [`lib/`](../lib/) folder onto your Pico's filesystem first.
3. **Running a game:** Open the desired `.py` file in **Thonny** (or your preferred MicroPython IDE) and run it on the board, or rename it to `main.py` to launch it automatically on boot.

---

⬅️ [Retour à l'accueil du projet / Back to Project Home](../README.md)
