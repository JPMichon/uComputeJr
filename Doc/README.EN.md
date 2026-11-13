# 👋 Hardware Walkthrough: uCompute Junior (Rev 1.0)

Great, you now have your **uCompute Junior** (version 1.0 shown in the photo) in hand! It is time for a guided tour of the board to understand all its features, starting with the power section in the top-left corner.

<img width="1050" height="724" alt="Plain_junior_V1" src="https://github.com/user-attachments/assets/48943b12-aabe-4664-ba01-e11337469098" />

## 🔌 The USB-C Port (Power Only)

Located on the top-left edge, this USB-C connector is dedicated exclusively to power and does not transfer any data. It serves three main purposes:

1. **Standalone operation:** Powering the Junior without needing to connect it to a computer via the Raspberry Pi Pico's USB port.
2. **Powering NeoPixels:** Supplying the 5V required for addressable LEDs connected to the 3-pin header located just below it.
3. **Distribution to Header H1:** Supplying 5V to pin 1 (**5V**) of the main **H1** header at the bottom of the board.

## ⚡ Power Options and Safety

* **Alternative power sources:** In addition to the USB-C port, you can power the board directly by feeding 5V into **pin 1 (5V) of the H1 header**. *Quick tip:* the **5V** pin on the **NEOPIXEL** header is connected to the same rail and can also serve as a power input.
* **Only one external power source at a time:** Never connect a power source to the board's USB-C port and another one to the 5V pin of H1 (or the NeoPixel header) simultaneously.
* **Built-in reverse-current protection:** Thanks to its protection diode (D1), the Junior is designed to safely accept external power (via its USB-C port) at the same time as the USB cable connecting your computer to the Raspberry Pi Pico, with no risk of electrical conflict.

## 💡 Indicator LEDs (Status Lights)

Right above the USB-C connector are two very handy LEDs to diagnose the status of your board at a glance:

* **3V3 LED (Green):** Indicates that the Raspberry Pi Pico is powered and its internal voltage regulator is properly generating 3.3V.
* **5V LED (Orange):** Confirms that 5V power is present on the board (supplied either by the Junior's USB-C port or the 5V pin on the H1 header).

> 💡 **Recommendation for standalone mode:** Using a portable power bank is ideal for powering your Junior via its USB-C port. Since the board only draws a few milliamps, a compact model with a capacity under **5,000 mAh** is more than enough.

## 🔗 The I2C Bus and EEPROM Memory

Moving to the right along the top edge, you will find the main **I2C bus** connector. This two-wire protocol makes it easy to connect a wide variety of external sensors or additional displays.

* **Pinout:** The connector provides the 4 standard signals: **3V3**, **GND**, **SCL** (GPIO 21), and **SDA** (GPIO 20).
* **Built-in pull-up resistors:** Two 10 kΩ pull-up resistors (R3 and R4) are already soldered onto the board. You do not need to add any on your external modules.
* **Onboard non-volatile memory:** Just to the right of this connector is an EEPROM memory chip (**AT24Cxx**, accessible at address `0x50`). It shares this same I2C bus and allows your programs to save settings or game high scores even when the board is unplugged.

## 📡 The UART Serial Port and TX / RX LEDs

Next to the EEPROM is the **UART** (serial communication) connector, ideal for debugging or communicating with other microcontrollers and modules (GPS, Bluetooth, etc.).

* **Pinout:** It provides access to **3V3**, **RX** (GPIO 1), **TX** (GPIO 0), and **GND**.
* **Activity indicator LEDs:** To the left of this connector, two LEDs let you monitor data traffic in real time:
  * **RX LED (Green):** Blinks when the Junior receives data on GPIO 1.
  * **TX LED (Red):** Blinks when the Junior transmits data via GPIO 0.

> ℹ️ **Why do the TX and RX LEDs glow dimly at startup?**
> If you notice that the TX and RX LEDs remain partially lit (at a low brightness) when you power on the board, **this is completely normal**. Until the UART port is explicitly initialized in your MicroPython code, GPIO 0 and GPIO 1 on the Raspberry Pi Pico remain in a floating (high-impedance) state, allowing a tiny residual current to pass through the LEDs. They will turn off completely as soon as the UART peripheral is configured in software.

## 🔊 The Piezoelectric Buzzer (Audio Output)

In the upper section of the board, between the UART connector and the communication module slot, sits a **piezoelectric buzzer**.

* **PWM Control:** It is driven by **GPIO 11**. By varying the frequency of the PWM (*Pulse Width Modulation*) signal in your code, you can generate everything from simple alert beeps to retro melodies and game sound effects.

## 📻 The *Add-on Module* Expansion Port (Communications)

In the top-right corner of the board is a dual 6-pin female header (labeled **U7**). This slot is specifically designed to house the wireless and wired communication modules of the uCompute ecosystem.

* **Full backward compatibility:** You can directly plug in the daughterboards designed for the original uCompute, including:
  * **Wi-Fi:** ESP-12F (ESP8266) module to connect your projects to the Internet.
  * **Short-range radio:** NRF24L01+ (2.4 GHz) module for telemetry or remote control (e.g., with the *uCompute Remote* controller).
  * **Long-range radio:** LoRa (RFM95W) module for long-distance wireless links.
  * **Wired network:** W5500 Ethernet module *(requires a custom-compiled MicroPython firmware with the corresponding C drivers)*.
* **Dedicated SPI architecture:** This port uses the Pico's hardware SPI bus to ensure fast and reliable data transfers:
  * **Power:** **3V3** and **GND** (pins located on the far right).
  * **SPI Bus:** **GP14** (SCK), **GP15** (MOSI), and **GP12** (MISO).
  * **Control signals:** **GP8** (Chip Select / CS), **GP9** (Interrupt / INT), and **GP10** (Reset / RST).

> ⚠️ **Watch the insertion orientation:** Before powering on the board, always double-check that the power pins (**GND** and **3V3**) on your daughterboard align with the silkscreen labels on the Junior. Plugging a module in backward could damage the radio module or the Pico's voltage regulator.

## 🧠 The Raspberry Pi Pico Slot (The Brain)

In the center-left area of the board are two long rows of 20-pin female headers. This is where the microcontroller that brings your uCompute Junior to life plugs in, following the *"Bring your own Pico"* approach.

* **Broad compatibility:** As shown on the silkscreen inside the footprint, the Junior supports the entire Pico family (RP2040 and RP2350 architectures):
  * **Raspberry Pi Pico** (standard model)
  * **Raspberry Pi Pico W** (with built-in Wi-Fi and Bluetooth)
  * **Raspberry Pi Pico 2** (newer, higher-performance generation)
  * **Raspberry Pi Pico 2 W** (newer generation with wireless connectivity)
* **Solder-free flexibility:** Using female headers allows you to remove or swap out the Pico at any time without any additional soldering. This makes it easy to reuse a single Pico across multiple projects or replace it quickly in a classroom setting.
* **Direct PC connection:** Once seated, the Pico's micro-USB (or USB-C) port remains easily accessible on the left edge of the board so you can program it in MicroPython using Thonny or VS Code.

> ⚠️ **Mandatory insertion orientation:** Always insert your Raspberry Pi Pico with its **USB connector facing to the left** (on the same side as the Junior's USB-C power port and aligned with the Raspberry Pi logo printed on the PCB). Inserting it backward will reverse the power pins and permanently damage the microcontroller.

## 📺 Display Options (Color or Monochrome Screen)

To make your projects interactive, the uCompute Junior features a dual footprint that lets you choose between a high-resolution color graphic display or a budget-friendly monochrome screen.

### 1. Primary Display: 1.3" TFT IPS ST7789 (Color)

Just to the right of the Raspberry Pi Pico slot is a vertical row of 7 pins dedicated to a **1.3-inch** color LCD module (**240 × 240 pixels** resolution) driven by the **ST7789** chip over SPI.

* **Stacked installation:** Once soldered (or mounted on a female header), this display sits directly **on top of the Raspberry Pi Pico**, creating a compact handheld-console form factor.
* **Pinout (from top to bottom):**
  * **BLK:** Backlight *(unconnected on the Junior version; the backlight remains permanently on)*
  * **DC:** Data/Command selection (**GPIO 5**)
  * **RES:** Reset (**GPIO 4**)
  * **SDA:** SPI Data / MOSI (**GPIO 3**)
  * **SCL:** SPI Clock (**GPIO 2**)
  * **3V3:** 3.3V power
  * **GND:** Common ground

### 2. Alternative Display: OLED SSD1306 (Monochrome)

Just above the MicroSD card slot, a horizontal 4-pin header (labeled *Alt Display*) allows you to use a **0.96-inch OLED** screen (**128 × 64 pixels**) based on the **SSD1306** controller.

* **I2C simplicity:** This module uses the main I2C bus (**GPIO 20** for SDA and **GPIO 21** for SCL) with the standard **GND - 3V3 - SCL - SDA** pin order.
* **Great for tight budgets:** It is an economical alternative for displaying menus, sensor readings, or debug messages while freeing up the SPI pins used by the color screen.

> 💡 **Assembly tip:** If you use a female header for the ST7789 color screen, make sure it is tall enough (or use standoffs) so that the back of the display PCB does not touch the metallic components on the Raspberry Pi Pico underneath.

## 💾 The MicroSD Card Reader (Mass Storage)

On the right edge of the board, right below the alternative OLED screen header, is a **MicroSD (TF Card)** slot. It significantly expands your project's storage capacity for images, audio files, data logs (*datalogging*), or game assets.

* **Shared SPI bus:** This reader shares the SPI communication lines (**GP14** for SCK, **GP15** for MOSI, and **GP12** for MISO) with the *Add-on Module* connector. The SD card is selected via **GPIO 13** (Chip Select).
* **Hardware note:** To save GPIO pins on the Pico, mechanical card-presence detection (*Card Detect*) is not wired on the Junior. Initialization is handled directly in software when mounting the filesystem in MicroPython.

## 🎮 Control and Reset Buttons

In the bottom-right corner of the PCB are the physical controls for interacting directly with your programs:

* **The RESET button (red):** Located to the left of the button group, it is wired directly to the Raspberry Pi Pico's `RUN` pin. A quick press immediately restarts your microcontroller without having to unplug the power.
* **The 3 action buttons (BTN1, BTN2, BTN3):** Lined up side by side, these pushbuttons are used to navigate menus or control your games.
  * **Hardware trick (Analog ladder):** To use only a single Pico pin instead of three, these buttons are wired as a voltage divider (via resistors R7, R8, R9, and R10) connected to analog input **GPIO 26 (ADC0)**. Each button sends a distinct voltage level that your code reads to identify which key is pressed.

## 🔌 The Main Expansion Header (Header H1)

Running along the bottom-left edge is a **14-pin** male header (labeled **H1**) with standard **2.54 mm** pitch. It is the ideal gateway for breadboard prototyping with Dupont jumper wires, or for plugging in ecosystem expansion boards like the **uCompute Rover** robot or the **uCompute Remote** controller.

* **Complete pinout (from left to right):**
  1. **5V**: Direct power (from USB-C or the Pico)
  2. **GND**: Common ground
  3. **3V3**: Regulated 3.3V power
  4. **GND**: Common ground
  5. **GP16**: Digital / SPI / I2C / PWM pin
  6. **GP17**: Digital / SPI / I2C / PWM pin
  7. **GP18**: Digital / SPI / I2C / PWM pin
  8. **GP19**: Digital / SPI / I2C / PWM pin
  9. **GP22**: Digital / PWM pin
  10. **GP07**: Digital / PWM pin *(replaces GP24 from the original model)*
  11. **GP27**: Analog input **ADC1** (or digital)
  12. **GP28**: Analog input **ADC2** (or digital)
  13. **GP01 / RX**: UART 0 serial receive
  14. **GP00 / TX**: UART 0 serial transmit

> ⚠️ **Safety reminder:** Just like on any Raspberry Pi Pico, the GPIO pins on header H1 operate strictly at **3.3V**. Never apply a **5V** signal directly to a GPIO pin, as this will permanently destroy the processor.

