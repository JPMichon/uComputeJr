# 📦 Bibliothèques et Pilotes MicroPython / MicroPython Libraries & Drivers

[Français](#-français) | [English](#-english)

---

## <img src="https://flagcdn.com" width="24" height="18" alt="Drapeau France"> Français

Ce répertoire regroupe l'ensemble des **bibliothèques et pilotes MicroPython** utilisés dans le cadre du projet **uCompute Junior** (gestion des écrans ST7789 et SSD1306, cartes SD, polices de caractères, modules de communication, etc.).

### 📥 Installation sur votre Raspberry Pi Pico

Pour que les jeux (`games/`) et les scripts de diagnostic (`testcode/`) fonctionnent correctement, **il est conseillé de copier les fichiers requis sur votre Pico** avant d'exécuter vos programmes :

1. Connectez votre **Raspberry Pi Pico** à votre ordinateur et ouvrez l'éditeur **Thonny**.
2. Dans l'explorateur de fichiers de Thonny, créez un dossier nommé `lib` à la racine de votre Pico (s'il n'existe pas déjà).
3. Sélectionnez uniquement les fichiers `.py` nécessaires à votre projet dans ce répertoire et téléversez-les dans le dossier `/lib` (ou directement à la racine `/`) de votre Pico.

> 💡 **Bon à savoir :** Il n'est pas nécessaire de copier toutes les bibliothèques d'un coup. Ne transférez que celles requises par le script que vous souhaitez exécuter afin d'économiser l'espace mémoire de votre microcontrôleur.

---

## <img src="https://flagcdn.com" width="24" height="18" alt="US Flag"> English

This directory contains all the **MicroPython libraries and hardware drivers** used across the **uCompute Junior** project (ST7789 and SSD1306 display drivers, SD card support, fonts, communication modules, etc.).

### 📥 Installing onto Your Raspberry Pi Pico

For the games (`games/`) and diagnostic scripts (`testcode/`) to run properly, **it is recommended to copy the required library files onto your Pico** before executing your code:

1. Connect your **Raspberry Pi Pico** to your computer and open the **Thonny** IDE.
2. Using Thonny's file browser, create a folder named `lib` in the root directory of your Pico (if it does not already exist).
3. Select only the `.py` files required for your specific project from this directory and upload them into the `/lib` folder (or directly into the `/` root directory) of your Pico.

> 💡 **Good to know:** You do not need to copy every single library at once. Only transfer the ones required by the script you plan to run in order to save flash storage space on your microcontroller.

---

⬅️ [Retour à l'accueil du projet / Back to Project Home](../README.md)
