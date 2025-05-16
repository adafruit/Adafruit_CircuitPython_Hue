# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
from os import getenv

import board
import busio
import neopixel
from adafruit_esp32spi import adafruit_esp32spi
from adafruit_esp32spi.adafruit_esp32spi_wifimanager import WiFiManager
from digitalio import DigitalInOut

# Import Philips Hue Bridge
from adafruit_hue import Bridge

# Get WiFi details, ensure these are setup in settings.toml
ssid = getenv("CIRCUITPY_WIFI_SSID")
password = getenv("CIRCUITPY_WIFI_PASSWORD")

# ESP32 SPI
esp32_cs = DigitalInOut(board.ESP_CS)
esp32_ready = DigitalInOut(board.ESP_BUSY)
esp32_reset = DigitalInOut(board.ESP_RESET)
spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
esp = adafruit_esp32spi.ESP_SPIcontrol(spi, esp32_cs, esp32_ready, esp32_reset)
status_pixel = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.2)
wifi = WiFiManager(esp, ssid, password, status_pixel=status_pixel)

# Attempt to load bridge username and IP address from settings.toml
username = getenv("hue_username")
bridge_ip = getenv("bridge_ip")

if username is None or bridge_ip is None:
    # Perform first-time bridge setup
    my_bridge = Bridge(wifi)
    ip = my_bridge.discover_bridge()
    username = my_bridge.register_username()
    raise KeyError(
        f'Please add these values to your settings.toml: \
                            \n\t"bridge_ip":"{ip}", \
                            \n\t"hue_username":"{username}"'
    )

my_bridge = Bridge(wifi, bridge_ip, username)

# Enumerate all lights on the bridge
my_bridge.get_lights()

# Turn on the light
my_bridge.set_light(1, on=True)

# RGB colors to Hue-Compatible HSL colors
hsl_y = my_bridge.rgb_to_hsb([255, 255, 0])
hsl_b = my_bridge.rgb_to_hsb([0, 0, 255])
hsl_w = my_bridge.rgb_to_hsb([255, 255, 255])
hsl_colors = [hsl_y, hsl_b, hsl_w]

# Set the light to Python colors!
for color in hsl_colors:
    my_bridge.set_light(1, hue=int(color[0]), sat=int(color[1]), bri=int(color[2]))
    time.sleep(5)

# Set a predefinedscene
# my_bridge.set_group(1, scene='AB34EF5')

# Turn off the light
my_bridge.set_light(1, on=False)
