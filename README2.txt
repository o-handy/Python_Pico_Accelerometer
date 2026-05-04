Raspberry Pi Pico Accelerometer using LIS3DH

This project uses an Raspberry Pi Pico 2, a LIS3DH 3-axis accelerometer with datalogging.
Along with an external battery pack, this can easily be mounted on vehicles, drones, or similar to record acceleration.

------------------------------------------------------------------------

Overview

-   3-axis (x,y,z) Acceleration measured with LIS3DH
-   Conversion to m/s^2, time stamp and data logging with Pico

------------------------------------------------------------------------

Hardware

-   Raspberry Pi Pico 2
-   Adafruit LIS3DH 3-axis accelerometer (2g/4g/8g)
-   Jumper wires

------------------------------------------------------------------------

Wiring

LIS3DH to Pico using I2C: 
- VIN → 5V 
- GND → GND
- SCL → GP1
- SDA → GP0


For external power supply using 3xAA battery pack:
- Positive → VSYS
- Negative → GND
------------------------------------------------------------------------