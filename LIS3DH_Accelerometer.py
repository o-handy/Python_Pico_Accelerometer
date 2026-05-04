from machine import Pin, I2C
import time
import struct


g = 9.80665 # Gravitational acceleration (m/s^2)
data = "a_log.txt"

# Register addresses
LIS3DH = 0x18
I = 0x0F
CTRL_REG1 = 0x20
CTRL_REG4 = 0x23
OUT_X_L = 0x28


# I2C Setup
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400_000)

def write_reg(reg, value):
    i2c.writeto_mem(LIS3DH, reg, bytes([value]))

def read_reg(reg, length=1):
    return i2c.readfrom_mem(LIS3DH, reg, length)


# Initiate Sensor
def lis3dh_init():
    if read_reg(I)[0] != 0x33:
        raise RuntimeError("LIS3DH not detected")

    # 100 Hz, enable XYZ
    write_reg(CTRL_REG1, 0x57)

    # High resolution, ±2g
    write_reg(CTRL_REG4, 0x08)

    time.sleep_ms(10)

# Read Acceleration (m/s²)
def read_acceleration():
    data = read_reg(OUT_X_L | 0x80, 6)
    x, y, z = struct.unpack("<hhh", data)

    # Convert from left-justified 12‑bit
    x >>= 4
    y >>= 4
    z >>= 4

    scale_g = 0.001  # g per LSB (±2g, high‑res)

    ax = x * scale_g * g
    ay = y * scale_g * g
    az = z * scale_g * g

    return ax, ay, az

# Main
lis3dh_init()
print("LIS3DH initialized")

# Open file in append mode
with open(data, "a") as file:
    # Write header if needed
    file.write("time_ms,ax_ms2,ay_ms2,az_ms2\n")

    while True:
        t = time.ticks_ms()
        ax, ay, az = read_acceleration()

        line = "{},{:.3f},{:.3f},{:.3f}\n".format(t, ax, ay, az)
        file.write(line)
        file.flush()  # Important for data safety

        print(line.strip())
        time.sleep(0.1)