# Welcome to Printers_farm!
We have several 3D printers and we want to work as a professional 3d Printing farm. For the optimal work of that farm, the conditions (environment) of the printers should be tightly controlled.

## Definition
The farm can contain several 3D printers as stated before, each 3D Printer is composed by a **PrinterEnclosure** and a **FilamentEnclosure**.
> The **PrinterEnclosure** contains it's own two sensors (Temperature and Humidity) and it's own two actuators (a fan and a gate).
> The **FilamentEnclosure** contains it's own three sensors (Temperature, Humidity and FilamentRunOut) and also, it's own two actuators (a fan and a gate)

## Sensors

- Temperature sensors generates a random value, simulating a true lecture, between 20 and 50 (ºC). If the value is greater than 45 ºC, the program is going to automatically **start the fan of the enclosure containing the sensor and notificate via Telegram**

- Humidity sensors generates a random value, simulating a true lecture, between 0 and 100 (%). If the value is greater than 95%, the program is going to automatically **open the gate of the enclosure containing the sensor and notificate via Telegram**

- Filament Run Out sensors has a 95% chance of giving a "FILAMENT RUN OUT" output. **The program has to notificate via Telegram**

## Actuators

- The fan can be activated or deactiveted independently from Printer Enclosure or Filament Enclosure.
- The gate can be opened or closed independently from Printer Enclosure or Filament Enclosure.

## Class diagram

![enter image description here](https://i.postimg.cc/FFVDtSv4/Whats-App-Image-2022-06-05-at-8-26-19-PM.jpg)

## Instructions

1) Install mosquitto broker - https://mosquitto.org/download/
Start broker ------ `mosquitto -c mosquitto.conf`

2) Install requirements -------- `pip install -r requirements.txt`

3) Edit the config.yaml with your telegram bot token, and your chat_id.
Also, you can modify the timer parameter, which is the time the software waits between sensor readings.

4) Start the Farm ----------- `py main.py --c config.yaml`

5) (Optional) ------------  You can modify mqtt_subscriber.py to recieve the publications in other computers.
