# uCompute Junior (Bring your own PICO)

## [Version française disponible ici](./README.md)<br>

The **uComputeJunior** is a streamlined and highly accessible version of the [RP2040 uCompute platform](https://github.com/JPMichon/RP2040_uCompute). Designed specifically for **novice hobbyists and makers**, it features a "Bring your own Pico" framework: it eliminates the need to solder complex surface-mount devices (SMD) by directly hosting a standard, ready-to-use Raspberry Pi Pico module.

This board serves as a hardware entry gateway to seamlessly integrate into the global uCompute environment, while also simplifying the onboarding and access to ecosystem projects like the programmable [uCompute Rover robot](https://github.com/JPMichon/uCompute_Rover).


<img width="558" height="367" alt="image" src="https://github.com/user-attachments/assets/9ae96d46-1b85-4960-8d46-99c5ffb2fcdd" />


---

## 🎓 A Perfect Solution for Education and Fablabs

The **uCompute Junior** stands out as the perfect tool for introducing electronics and embedded systems, whether in school environments (**middle and high schools**) or within **Fablabs**.

* **For the educational sector:** Thanks to its "Bring your own Pico" approach, it greatly simplifies classroom setup by hosting a standard, off-the-shelf **Raspberry Pi Pico** module. By combining the power of the Raspberry Pi Pico community, the clarity of the **MicroPython** language, and the flexibility of the **uCompute ecosystem**, teachers have a turnkey environment to structure engaging practical workshops (ranging from simple LED blinking to driving the _uCompute Rover Robot_).
* **For Fablabs and hands-on workshops:** Although the board requires surface-mount soldering (SMD), the design deliberately uses **0805-sized** components, which are particularly easy to handle and hand-solder. This makes it an excellent educational medium to demystify and teach SMD soldering without requiring complex industrial equipment (such as a reflow oven or a hot plate).


The entire project is driven by Open Hardware values and shared under the **CC BY-NC-SA 4.0** license. Since all manufacturing files (Gerbers, schematics) are freely accessible, schools and Fablabs can order, modify, or locally produce their own boards at a minimal cost, fostering total technological autonomy and frictionless knowledge sharing without budget constraints.

💵 **Budget-Friendly:** With an estimated cost of only **$20 CAD (~$16 USD)** per board (including PCB, Pi Pico, and screen), it is the perfect low-cost solution to equip an entire classroom or Fablab.

> [!NOTE]
> If you are a beginner and have never ordered printed circuit boards before, you should know that there are many online platforms available. Personally, I use JLCPCB's services. If you want to test their website, you can use my referral link: **[JLCPCB](https://jlcpcb.com/?from=REDLD)**. This will allow you to get discount coupons for your first prints, while offering me credits to support and finance my future projects. Of course, you are under no obligation to do so, but it is an excellent way to give the channel a helping hand!

---

### 📻 Extension Modules & Backward Compatibility (Add-ons)

The main highlight of the **uCompute Junior** lies in the native integration of its add-on extension socket and its I/O pin header (Header H1). Despite being a streamlined version, the board maintains **full backward compatibility with all communication and extension modules from the uCompute ecosystem**.

This allows you to instantly upgrade your Junior (wireless links, robotic telemetry, remote control) by directly plugging in daughterboards from the main project or the Rover Robot.

👉 **[Access the ecosystem modules repository (RP2040_uCompute Modules)](https://github.com/JPMichon/RP2040_uCompute/tree/main/Modules)**

| Location on Junior | Compatible Module | Description & Features | Hardware Render |
| :--- | :--- | :--- | :--- |
| **Add-On module** <br>(Communication) | **Wi-Fi Module** <br>(ESP-12F) | Adapter board embedding an ESP8266 to add full Wi-Fi connectivity. | <img width="100" height="133" alt="Module Wi-Fi ESP-12F" src="https://github.com/user-attachments/assets/f0c80621-1b07-46e6-844b-4594e3d338f9" /> |
| **Add-On module** <br>(Communication) | **Radio Module** <br>(NRF24L01) | Adapter for 2.4 GHz radio links, ideal for bidirectional communication. | <img width="112" height="140" alt="Module Radio NRF24L01" src="https://github.com/user-attachments/assets/a6a0a83b-80ed-4dbc-bc28-06579f64b54c" /> |
| **Add-On module** <br>(Communication) | **LoRa Module** <br>(RFM95W) | Long-range adapter exploiting LoRa radio technology. | <img width="112" height="140" alt="Module LoRa RFM95W" src="https://github.com/user-attachments/assets/729ed810-e456-4e6b-88fb-1f3c61edea25" /> |
| **Header H1** <br>(I/O Connector) | **µCompute Remote** <br>| Extension board integrating an analog joystick and buttons for RC piloting. | <img width="175" height="131" alt="Manette uCompute Remote" src="https://github.com/user-attachments/assets/25dda003-8ab8-48c4-a7d1-1a45fdbca7a4" /> |
| **Header H1** <br>(I/O Connector) | **µCompute Rover** <br> | Controller for DC motors (2+2), servo motor, HC-SR04 sensor, and Neo-6M GPS module. | <img width="220" height="145" alt="Contrôleur uCompute Rover" src="https://github.com/user-attachments/assets/90114819-d70b-4cbb-8cfd-5e95b66cca84" /> |

> ℹ **Technical note regarding network support (W5500 Module):**
> Although the **U7** add-on socket is natively designed to accommodate a **W5500** Ethernet module, using this wired connectivity under MicroPython requires special software attention. Unlike standard scripts, activating the W5500 network features **requires a custom recompilation of the MicroPython firmware** to directly integrate the network stack drivers (C drivers) required by this component.

---

## 🛠️ Manufacturing & Assembly (Do It Yourself)

This project is fully Open Hardware. The **Gerber** file, electrical schematics, and the complete Bill of Materials (BOM) are available in the Hardware/ folder. You are free to export these files to have your printed circuit boards (PCBs) manufactured by the supplier of your choice.

⚠ **Required Technical Level & Tools:**  
Manual assembly of the PCB is a stimulating but **perfectly accessible challenge for most makers**, even if it is your very first transition to surface-mount components (SMD).

To facilitate hand-soldering and avoid frustration, the circuit was designed with smart hardware constraints:
* **Comfortable component size:** The smallest surface chips and resistors use the **0805** format. This is the ideal size for beginners, as the parts remain highly visible and easy to manipulate with tweezers.
* **No complex packages:** The board eliminates micro-components with invisible leads (such as QFN or BGA) that require a hot air station or a heating plate. A simple traditional soldering iron equipped with a fine tip is more than enough.

💡 **To succeed with your assembly, simply equip yourself with:**
* A classic fine-tip soldering iron (adjustable temperature recommended).
* High-quality fine solder wire.
* A jar or pen of **soldering flux** (the indispensable magic ingredient to cleanly align tin on SMD pads).
* High-precision tweezers.
* Good lighting, a dose of patience, and your uCompute Junior will come to life in less than an hour!

---

## 🛠 Hardware Specifications

| Feature | Component / Specification | Main Function |
| :--- | :--- | :--- |
| **Core** | Raspberry Pi Pico Socket (U1) | General computation and control |
| **Power Supply** | USB-C Input (6-pin) + Protective Fuse | General 5V |
| **Add-on** | Communication Module Socket (U7) | Wired network connectivity (SPI) |
| **Storage** | MicroSD Card Reader (TF Card) | Mass storage and file systems |
| **Main Display** | 1.3" IPS ST7789 LCD Screen (240x240) | High-resolution color graphical interface |
| **Optional Display** | SSD1306 OLED Screen Support (I2C) | Optional monochrome display |
| **EEPROM Memory** | CAT24CxxxWI-G (U5) | Non-volatile configuration backup |
| **Audio** | Active/passive piezoelectric buzzer (BUZ) | Sound alerts and audio effects |
| **Inputs** | 3-button resistor ladder (BTN1-BTN3) | User navigation and interaction (ADC reading) |
| **Extension** | UART Connector + NeoPixel Header + Header H1 | Serial connectivity, LED strips, and free GPIOs |

---
## 📋 Bill of Materials, Pinout, and Subsystems

| Quantity | Value / Reference | Designator | Component Name | Footprint |
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
| 2 | 20-pin female connector | Pico Socket (U1) | 1x20 Female Header 2.54mm Pitch | CONN-TH_20P-P2.54mm |
| 2 | 6-pin female connector | Module Socket (U7) | 1x6 Female Header 2.54mm Pitch | CONN-TH_6P-P2.54mm |
| 1 | 14-pin male connector | Prototyping Connector (H1) | 1x14 Male Header 2.54mm Pitch | HDR-TH_14P-P2.54-V-M |

## 📺 Display Options of Your Choice

The circuit features a dual footprint, giving you the freedom to install the visual interface best suited to your needs:

| ST7789 TFT IPS Screen (1.3" - 240x240 px) | SSD1306 OLED Screen (0.96" - 128x64 px) |
| :---: | :---: |
| **Color graphical option (SPI Bus)** | **Budget monochrome option (I2C Bus)** |
| <img width="226" height="181" alt="Écran TFT IPS ST7789 couleur" src="https://github.com/user-attachments/assets/8058baaa-8250-4343-b1ee-2f4264cbfdd8" /> | <img width="175" height="164" alt="Écran OLED SSD1306 monochrome" src="https://github.com/user-attachments/assets/af83c2a7-cb08-471e-b7a2-98eef86f3fd2" /> |



---

## 📌 GPIO Pinout and Assignments

> ⚠ **Important note regarding GPIO differences:**
> Unlike the original uCompute board, the Junior version does not have access to pins GP23 and GP24. To overcome this hardware limitation, the following modifications and reallocations have been applied:
> * **On the I/O pin header (Header H1)**: Pin **GP24** has been replaced by pin **GP07**.
> * **For the NeoPixel connector**: The control signal, originally on **GP23**, has been remapped to pin **GP06**.
> 
> **Software and hardware consequences:**
> 1. The uCompute Junior no longer has a dedicated pin for **hardware MicroSD card presence detection**.
> 2. Hardware backlight control (**BLK**) for the ST7789 LCD screen is no longer available.

---

All connections between the Raspberry Pi Pico and the board's peripherals are listed below:

| Périphérique | Broche Pico (GPIO) | Fonction SPI / I2C / UART / ADC |
| :--- | :--- | :--- |
| **UART (Console)** | GPIO 0 | TX (Red status LED) |
| **UART (Console)** | GPIO 1 | RX (Green status LED) |
| **ST7789 LCD Screen** | GPIO 2 | SCL (SPI Clock) |
| **ST7789 LCD Screen** | GPIO 3 | SDA (SPI Data / MOSI) |
| **ST7789 LCD Screen** | GPIO 4 | RES (Reset) |
| **ST7789 LCD Screen** | GPIO 5 | DC |
| **NeoPixel Strip** | GPIO 6 | NeoPixel Pin |
| **Communication Module**| GPIO 8 | INT (Interrupt) |
| **Communication Module**| GPIO 9 | CS (Chip Select) |
| **Shared SPI Bus (Network/SD)**| GPIO 10 | SCLK (Clock SPI) |
| **Shared SPI Bus (Network/SD)**| GPIO 11 | MOSI (Master Out Slave In) |
| **Shared SPI Bus (Network/SD)**| GPIO 12 | MISO (Master In Slave Out) |
| **MicroSD Card Reader** | GPIO 13 | CS (Chip Select Carte SD) |
| **Buzzer** | GPIO 16 | Audio Signal  (PWM) |
| **OLED Screen / EEPROM** | GPIO 20 | SDA (Main I2C Bus) |
| **OLED Screen / EEPROM** | GPIO 21 | SCL (Main I2C Bus) |
| **Button Resistor Ladder** | GPIO 26 | Analog Input ADC0 (BTN1, BTN2, BTN3) |

### The terminal block (1x14 pins Header):
The terminal block (pins Header) facilitates prototyping. The pitch is standard at 2.54 mm, allowing it to be plugged into a prototyping board (Protoboard) or connected using jumper wires with Dupont connectors to link your circuits or modules.

### Power supplies and signals:
1. **5V** (Direct power supply from the USB, ideal for power)
2. **3.3V** 
3. **GND** (Common ground)
4. **UART 0** : `GP0` (TX) & `GP1` (RX)
5. **2 Analog Inputs  (ADC) :** `GP27` (ADC1) & `GP28` (ADC2)
6. **6 Digital Pins  (GPIO) :** `GP16`, `GP17`, `GP18`, `GP19`, `GP22`, `GP07`

<BR>

> [!CAUTION]
> **The RP2040 is not 5V tolerant.** 
> According to the Absolute Maximum Ratings section of the [official RP2040 datasheet (Datasheet)](https://pip-assets.raspberrypi.com/categories/814-rp2040/documents/RP-008371-DS-1-rp2040-datasheet.pdf),  the maximum absolute voltage on I/O pins (IOVDD) is **3.63V**. Applying 5V directly will destroy the microcontroller.
<BR>

---

## 🔌 Subsystem Architecture

### 1.  Power Supply and Protection
The circuit uses a robust USB-C connector limited to the main power lines.
* **Security**: A resettable fuse (FUSE) protects the board against overcurrents.
* **Anti-backflow**: An MBR120LSFT Schottky diode (**D1**) prevents power conflicts when the Pico is simultaneously plugged into its native USB and onto the board.

### 2. Input Management (Analog Resistor Ladder)
To save Pico pins, buttons **BTN1, BTN2**, and **BTN3** share a single analog pin (**GPIO 26 / ADC0**).
* Each button press modifies the voltage read by the ADC thanks to a unique voltage divider ladder (R7, R8, R9, R10).

### 3. Communication Buses
* **I2C Bus**: Shared between the configuration storage EEPROM memory and the standard OLED screen connector (SSD1306). 10kΩ pull-up resistors (R3, R4) stabilize the bus.
* **SPI Bus**: Efficiently shared between the communication module and the MicroSD card reader thanks to separate Chip Select lines on GPIO 9 and 13.

---

## 📜 License

The hardware (design files, schematics, layouts) and software of this project are made available under the terms of the **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0)**.

❌ **Commercial use of this project (reselling bare PCBs, kits, or assembled retroPico boards) is strictly prohibited without prior authorization from the author.**

Check the [LICENSE](LICENSE) file to read the full terms.

## ☕ Support the Project

If you appreciate my work and would like to buy me a coffee to support my future soldering and coding projects on a voluntary basis, you can leave me a [**tip on Ko-fi** ](https://ko-fi.com/jpmichon). It is entirely optional and greatly appreciated!
