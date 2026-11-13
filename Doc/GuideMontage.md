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

## 📐 2. La technique de soudure CMS (en 5 étapes)

Pour toutes les résistances, condensateurs et DEL de format **0805** :

1. **Appliquer du flux :** Déposez une petite touche de flux de soudure sur les deux pastilles du circuit imprimé avant de commencer.
2. **Étamer une seule pastille :** Déposez une minuscule goutte d'étain sur l'une des deux pastilles.
3. **Positionner et maintenir le composant :** Saisissez le composant avec la pince, chauffez la goutte d'étain et glissez le composant en place. **Appliquez une légère pression verticale** sur le dessus du composant avec la pince afin qu'il reste bien à plat contre le circuit (cela évite l'effet « pierre tombale » ou *tombstoning*, où un côté du composant se soulève). Retirez le fer et maintenez la pression 2 secondes le temps que l'étain fige.
4. **Souder le deuxième côté :** Déposez une petite goutte d'étain directement sur la pointe de votre fer à souder, puis venez faire contact simultanément sur la seconde pastille et l'extrémité du composant. Grâce au flux appliqué à l'étape 1, la soudure se formera instantanément.
5. **Finaliser le premier côté :** Repassez brièvement sur la première soudure avec une pointe de flux pour obtenir un joint brillant et solide.

---

## 📋 3. Étapes de montage (du plus plat au plus haut)

> 🖌️ **Astuce technique — Le soudage par brossage (*Drag Soldering*) :**
> Pour souder efficacement les rangées de petites broches serrées (connecteur **USB-C**, lecteur **MicroSD** et puce **EEPROM**), inutile de les souder une par une :
> 1. Appliquez généreusement du **flux de soudure** sur l'ensemble des broches.
> 2. Faites fondre une petite quantité d'étain sur la pointe de votre fer à souder.
> 3. **Brossez légèrement** les broches d'un mouvement fluide et continu dans une seule direction. Grâce au flux, l'étain va naturellement se répartir sur chaque patte.
> 4. **En cas de pont de soudure :** Si deux broches se retrouvent reliées par une goutte d'étain, nettoyez complètement la pointe de votre fer (sur votre laine de laiton ou éponge humide), ajoutez une touche de flux sur le pont, puis repassez le fer propre sur les broches pour retirer l'excédent d'étain par capillarité.

### Étape 1 : Les connecteurs CMS (USB-C et MicroSD)
*On commence par eux car l'espace autour est encore totalement dégagé.*
1. **Connecteur USB-C (`USB-C`) :** Alignez les ergots en plastique dans les trous du PCB. Soudez d'abord les grosses pattes de fixation latérales pour bloquer solidement la pièce, puis appliquez la **technique du brossage** sur les petites broches arrière.
2. **Lecteur MicroSD (`U6`) :** Positionnez le boîtier métallique sur son empreinte, soudez les pattes de maintien sur les côtés, puis soudez les broches de contact à l'arrière par **brossage**.

### Étape 2 : Les circuits intégrés et la protection
⚠️ **Attention au sens de montage (polarité) !**
1. **Mémoire EEPROM (`U5` - CAT24Cxxx) :** Repérez le petit point ou l'encoche sur la puce (broche 1) et alignez-le avec le repère dessiné sur le circuit imprimé. Immobilisez une première patte, puis soudez les deux rangées de broches par **brossage**.
2. **Diode Schottky (`D1` - MBR120LSFT) :** La bande blanche dessinée sur le composant doit être alignée avec le trait blanc sur le PCB.
3. **Fusible réarmable (`FUSE`) :** Aucun sens à respecter, soudez-le comme une résistance.

### Étape 3 : Les résistances et condensateurs (Format 0805)
Ces composants n'ont pas de sens de montage. Utilisez la méthode en 5 étapes vue à la section précédente et procédez valeur par valeur pour ne pas les mélanger :
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

## 🧼 6. Nettoyage et finition (Retrait du flux)

Une fois toutes vos soudures terminées, il reste souvent des résidus collants de flux de soudure autour des composants. Les nettoyer permet de rendre votre carte impeccable et de mieux inspecter la qualité de vos joints.

* **L'astuce économique :** Pas besoin d'acheter des produits spécialisés coûteux. Utilisez simplement des **tampons imbibés d'alcool** (tampons antiseptiques d'alcool isopropylique à 70 % ou plus), disponibles à très bas prix dans les pharmacies ou les magasins à un dollar.
* **Comment nettoyer :**
  1. Frottez délicatement les zones soudées (dessus et dessous de la carte) avec un tampon imbibé d'alcool pour dissoudre les traces de flux.
  2. Pour les endroits difficiles d'accès entre les broches, vous pouvez vous aider d'un coton-tige ou d'une vieille brosse à dents souple légèrement imbibée d'alcool.
  3. **Précaution :** Évitez de faire pénétrer du liquide à l'intérieur des boutons poussoirs, du lecteur MicroSD ou dans le trou du buzzer.
  4. Laissez la carte sécher à l'air libre pendant **1 à 2 minutes** (l'alcool s'évapore très rapidement) avant de la rebrancher.


## 🎉 **Félicitations ! <br> Votre uCompute Junior est maintenant assemblé, propre et prêt à recevoir son premier script MicroPython.**
