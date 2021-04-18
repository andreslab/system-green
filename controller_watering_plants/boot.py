try:
  import usocket as socket
except:
  import socket

from machine import Pin
import network

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = "UNE4GLTE35"
password = "4glte006635"

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

print('Connection ....')

while station.isconnected() == False:
    pass

print('Connection successful')
print(station.ifconfig())

led = Pin(2, Pin.OUT)
rele = Pin(5, Pin.OUT)
