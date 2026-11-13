# 🛠️ Guide d'assemblage : uCompute Junior (Écoles & Fablabs)

Ce guide étape par étape est conçu pour accompagner les élèves, les enseignants et les makers lors du montage manuel du **uCompute Junior**. 

* **Temps estimé :** 45 à 60 minutes
* **Niveau :** Débutant / Intermédiaire (idéal pour une première initiation aux composants CMS 0805)

---

## 🧰 1. Préparation du poste de travail

Avant de commencer, assurez-vous d'avoir tout le matériel à portée de main :

* **Outils de soudure :** Fer à souder à pointe fine (réglé entre **320 °C et 350 °C**), éponge humide ou laine de laiton.
* **Consommables :** Étain fin (0,5 mm ou 0,6 mm), stylo ou seringue de **flux de soudure** (indispensable !), tresse à dessouder (en cas de surplus d'étain).
* **Manipulation :** Une pince brucelle de précision (tweezers) et un bon éclairage (une loupe de table est un plus).
* **Sécurité :** Lunettes de protection et extracteur de fumées (ou pièce bien ventilée).

> 💡 **La règle d'or de la soudure CMS :** On soude toujours **les composants les plus plats en premier** et **les connecteurs les plus hauts à la fin**, afin que le circuit imprimé reste toujours bien stable sur la table.

---

## 📐 2. La technique de soudure CMS (en 4 étapes)

Pour toutes les résistances, condensateurs et DEL de format **0805** :
1. **Étamer une seule pastille :** Déposez une minuscule goutte d'étain sur l'une des deux pastilles du circuit.
2. **Positionner le composant :** Saisissez le composant avec la pince, chauffez la goutte d'étain et glissez le composant en place. Retirez le fer et attendez 2 secondes que l'étain fige.
3. **Souder le deuxième côté :** Ajoutez un peu de flux sur l'autre pastille, puis soudez-la proprement.
4. **Finaliser le premier côté :** Repassez brièvement sur la première soudure avec un peu de flux pour obtenir un joint brillant et solide.

---

## 📋 3. Étapes de montage (du plus plat au plus haut)

### Étape 1 : Les composants difficiles (Connecteur USB-C et MicroSD)
*On commence par eux car l'espace autour est encore totalement dégagé.*
1. **Connecteur USB-C (`USB-C`) :** Appliquez généreusement du flux sur les petites broches arrière. Alignez les ergots en plastique dans les trous du PCB. Soudez d'abord les grosses pattes de fixation latérales pour bloquer la pièce, puis passez le fer sur les petites broches à l'arrière. *(Utilisez la tresse à dessouder s'il y a un pont d'étain entre deux broches).*
2. **Lecteur MicroSD (`U6`) :** Positionnez le boîtier métallique sur son empreinte, soudez les pattes de maintien sur les côtés, puis les broches de contact à l'arrière.

### Étape 2 : Les circuits intégrés et la protection
⚠️ **Attention au sens de montage (polarité) !**
1. **Mémoire EEPROM (`U5` - CAT24Cxxx) :** Repérez le petit point ou l'encoche sur la puce (broche 1) et alignez-le avec le repère dessiné sur le circuit imprimé.
2. **Diode Schottky (`D1` - MBR120LSFT) :** La bande blanche dessinée sur le composant doit être alignée avec le trait blanc sur le PCB.
3. **Fusible réarmable (`FUSE`) :** Aucun sens à respecter, soudez-le comme une résistance.

### Étape 3 : Les résistances et condensateurs (Format 0805)
Ces composants n'ont pas de sens de montage. Procédez valeur par valeur pour ne pas les mélanger :
* **Résistances 270 Ω (`R2`)** : 1 pièce
* **Résistances 1 kΩ (`R7`, `R8`, `R9`)** : 3 pièces
* **Résistances 2 kΩ (`R1`, `R5`, `R6`, `R13`)** : 4 pièces
* **Résistances 5,1 kΩ (`R11`, `R12`)** : 2 pièces *(essentielles pour la détection USB-C)*
* **Résistances 10 kΩ (`R3`, `R4`, `R10`)** : 3 pièces
* **Condensateurs 10 nF (`C1`, `C2`, `C3`)** : 3 pièces

### Étape 4 : Les témoins lumineux (DEL 0805)
⚠️ **Les DEL ont un sens obligatoire !**
* Repérez la marque verte (ou le petit triangle/point) au dos de la DEL qui indique la cathode (**`-`**) et alignez-la avec le repère négatif sur le PCB :
  * **DEL d'alimentation :** `5V` (Orange) et `3V3` (Verte)
  * **DEL de communication :** `TX` (Rouge) et `RX` (Verte)

### Étape 5 : Les condensateurs électrolytiques et le buzzer
1. **Condensateurs 100 µF (`C4`, `C15`) :** ⚠️ **Polarisés !** La partie noire (ou le signe `-`) sur le dessus du condensateur cylindrique doit correspondre à la zone hachurée sur le circuit imprimé.
2. **Buzzer piézoélectrique (`BUZ`) :** Alignez le signe **`+`** inscrit sur le buzzer avec le **`+`** dessiné sur la carte.

### Étape 6 : Les boutons poussoirs
* Insérez et soudez les 3 boutons de navigation (`BTN1`, `BTN2`, `BTN3`) ainsi que le bouton `RESET`.

---

## ✅ 4. Point de contrôle (Test d'alimentation)

**Avant de souder les connecteurs femelles et les écrans**, faites cette vérification rapide :
1. Inspectez vos soudures à la loupe (surtout autour du port USB-C) pour vérifier qu'aucune goutte d'étain ne relie deux broches voisines.
2. Branchez un câble USB-C sur le port d'alimentation du Junior.
3. **Résultat attendu :** La **DEL orange (`5V`)** doit s'allumer immédiatement. Si elle ne s'allume pas ou si le câble chauffe, débranchez tout de suite et vérifiez le sens de la diode `D1` et les soudures du port USB-C.

---

## 📌 5. Étape finale : Les connecteurs traversants (Headers)

Retournez la carte pour souder ces pièces par le dessous :
1. **Emplacement du Pico (`U1`) :** Insérez les deux connecteurs femelles de 20 broches. *Astuce : enfichez votre Raspberry Pi Pico dedans avant de souder pour garder les connecteurs bien droits et parallèles !*
2. **Port d'extension (`U7`) :** Soudez les deux connecteurs femelles de 6 broches.
3. **Bornier principal (`H1`) :** Soudez le connecteur mâle de 14 broches (ainsi que les connecteurs I2C, UART et NeoPixel si vous utilisez des broches).
4. **Écran au choix :** Soudez soit l'écran couleur **ST7789** (7 broches), soit l'écran monochrome **OLED SSD1306** (4 broches).

🎉 **Félicitations ! Votre uCompute Junior est prêt à recevoir son premier script MicroPython.**
