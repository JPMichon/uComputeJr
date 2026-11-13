# 🛠️ Assembly Guide: uCompute Junior (Schools & Fablabs)

This step-by-step guide is designed to walk students, teachers, and makers through the manual assembly of the **uCompute Junior**.

* **Estimated time:** 45 to 60 minutes
* **Skill level:** Beginner / Intermediate (ideal for a first introduction to 0805 SMD components)

---

## 🧰 1. Preparing Your Workstation

Before starting, make sure you have all the required tools and supplies within reach:

* **Soldering tools:** Fine-tip soldering iron (set between **320 °C and 350 °C** / **610 °F and 660 °F**), damp sponge or brass wool tip cleaner.
* **Consumables:** Fine solder wire (0.5 mm or 0.6 mm), **soldering flux** pen or syringe (essential!), desoldering braid/wick (in case of excess solder).
* **Handling:** Precision tweezers and good lighting (a magnifying lamp is a plus).
* **Safety:** Safety glasses and a fume extractor (or a well-ventilated room).

> 💡 **The golden rule of SMD soldering:** Always solder **the lowest-profile (flattest) components first** and **the tallest connectors last**, so the printed circuit board always rests flat and stable on your workbench.

---

## 📐 2. The SMD Soldering Technique (in 5 Steps)

For all **0805** resistors, capacitors, and LEDs:

1. **Apply flux:** Place a small dab of soldering flux on both PCB pads before starting.
2. **Tin a single pad:** Melt a tiny drop of solder onto one of the two pads.
3. **Position and hold the component:** Pick up the component with your tweezers, reheat the tinned pad, and slide the component into place. **Apply gentle downward pressure** on top of the component with your tweezers so it sits completely flat against the PCB (this prevents "tombstoning," where one end of the component lifts up). Remove the iron and keep holding it down for 2 seconds until the solder solidifies.
4. **Solder the second side:** Melt a small drop of solder directly onto the tip of your soldering iron, then touch it simultaneously to the second pad and the end of the component. Thanks to the flux applied in step 1, the joint will form instantly.
5. **Reflow the first side:** Briefly touch up the first solder joint with a tiny bit of flux to achieve a shiny, solid connection.

---

## 📋 3. Assembly Steps (From Lowest to Tallest)

> 🖌️ **Pro Tip — Drag Soldering:**
> To efficiently solder rows of closely spaced pins (such as the **USB-C** connector, **MicroSD** reader, and **EEPROM** chip), there is no need to solder them one by one:
> 1. Apply a generous amount of **soldering flux** across all the pins.
> 2. Melt a small amount of solder onto the tip of your soldering iron.
> 3. **Lightly brush (drag)** the iron tip across the pins in a smooth, continuous motion in a single direction. Thanks to the flux, the solder will naturally flow onto each pin.
> 4. **If solder bridges form:** If two pins get shorted together by a blob of solder, completely clean the tip of your iron (using brass wool or a damp sponge), add a touch of flux over the bridge, and drag the clean iron across the pins again to wick away the excess solder.

### Step 1: SMD Connectors (USB-C and MicroSD)
*We start with these while the surrounding area is completely clear.*
1. **USB-C Connector (`USB-C`):** Align the plastic alignment pegs with the holes in the PCB. First, solder the large side mounting tabs to firmly anchor the connector in place, then use the **drag soldering technique** on the small rear pins.
2. **MicroSD Card Reader (`U6`):** Position the metal housing onto its footprint, solder the side mounting tabs, and then solder the rear contact pins using **drag soldering**.

### Step 2: Integrated Circuits and Protection
⚠️ **Watch the orientation (polarity)!**
1. **EEPROM Memory (`U5` - CAT24Cxxx):** Locate the small dot or notch on the chip (pin 1) and align it with the pin 1 marking on the PCB silkscreen. Tack one corner pin in place first, then solder both rows of pins using **drag soldering**.
2. **Schottky Diode (`D1` - MBR120LSFT):** The white band printed on the component body must align with the white line on the PCB silkscreen.
3. **Resettable Fuse (`FUSE`):** Non-polarized (no specific orientation); solder it just like a resistor.

### Step 3: Resistors and Capacitors (0805 Package)
These components are non-polarized. Use the 5-step method from the previous section and work one value at a time so you don't mix them up:
* **270 Ω Resistors (`R2`)**: 1 pc
* **1 kΩ Resistors (`R7`, `R8`, `R9`)**: 3 pcs
* **2 kΩ Resistors (`R1`, `R5`, `R6`, `R13`)**: 4 pcs
* **5.1 kΩ Resistors (`R11`, `R12`)**: 2 pcs *(essential for USB-C power negotiation)*
* **10 kΩ Resistors (`R3`, `R4`, `R10`)**: 3 pcs
* **10 nF Capacitors (`C1`, `C2`, `C3`)**: 3 pcs

### Step 4: Status Indicator LEDs (0805 LEDs)
⚠️ **LEDs have a mandatory orientation!**
* Look for the green mark (or small triangle/dot) on the back of the LED indicating the cathode (**`-`**) and align it with the negative marking on the PCB:
  * **Power LEDs:** `5V` (Orange) and `3V3` (Green)
  * **Communication LEDs:** `TX` (Red) and `RX` (Green)

### Step 5: Electrolytic Capacitors and Buzzer
1. **100 µF Capacitors (`C4`, `C15`):** ⚠️ **Polarized!** The black stripe (or `-` sign) on top of the cylindrical capacitor must match the shaded area on the PCB footprint.
2. **Piezoelectric Buzzer (`BUZ`):** Align the **`+`** sign marked on the buzzer with the **`+`** symbol printed on the board.

### Step 6: Pushbuttons
* Insert and solder the 3 navigation buttons (`BTN1`, `BTN2`, `BTN3`) as well as the `RESET` button.

---

## ✅ 4. Checkpoint (Power Test)

**Before soldering the female headers and displays**, perform this quick test:
1. Inspect your solder joints with a magnifier (especially around the USB-C port) to ensure no solder bridges are shorting adjacent pins.
2. Plug a USB-C cable into the Junior's power port.
3. **Expected result:** The **orange LED (`5V`)** should light up immediately. If it does not turn on or if the cable gets warm, unplug it right away and double-check the orientation of diode `D1` and the USB-C port pins.

---

## 📌 5. Final Step: Through-Hole Connectors (Headers)

Flip the board over to solder these components from the underside:
1. **Pico Socket (`U1`):** Insert the two 20-pin female headers. *Pro tip: plug your Raspberry Pi Pico into the headers before soldering to keep them perfectly straight and parallel!*
2. **Add-on Expansion Port (`U7`):** Solder the two 6-pin female headers.
3. **Main Expansion Header (`H1`):** Solder the 14-pin male header (along with the I2C, UART, and NeoPixel headers if you are using pin headers for them).
4. **Display of your choice:** Solder either the **ST7789** color screen (7 pins) or the **OLED SSD1306** monochrome screen (4 pins).

---

## 🧼 6. Cleaning and Finishing (Flux Removal)

Once all your soldering is complete, sticky flux residue often remains around the components. Cleaning it off gives your board a professional look and makes it much easier to inspect your solder joints.

* **Budget-friendly tip:** No need to buy expensive specialized cleaners. Simply use **alcohol prep pads** (70% or higher isopropyl alcohol antiseptic wipes), widely available at dollar stores or pharmacies.
* **How to clean:**
  1. Gently wipe the soldered areas (top and bottom of the PCB) with an alcohol pad to dissolve the flux residue.
  2. For tight spaces between pins, you can use a cotton swab or an old soft-bristled toothbrush lightly dampened with isopropyl alcohol.
  3. **Caution:** Avoid getting liquid inside the pushbuttons, the MicroSD card slot, or the sound hole of the buzzer.
  4. Let the board air-dry for **1 to 2 minutes** (alcohol evaporates very quickly) before plugging it back in.

🎉 **Congratulations! Your uCompute Junior is now assembled, clean, and ready for its first MicroPython script.**
