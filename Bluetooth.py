from m5stack import *
from m5ui import *
from uiflow import *
import ubluetooth as bluetooth
import binascii
import time

data = None

# Initialize the UI
setScreenColor(0x111111)
title0 = M5Title(title="BLE Scanner", x=3, fgcolor=0xFFFFFF, bgcolor=0x0000FF)

# Initialize Bluetooth and set it to active mode
ble = bluetooth.BLE()
if not ble.active():
    ble.active(True)

# Define a callback function to handle the results of the scan
def scan_callback(event, addr):
    global data
    byte_string = addr[1]
    hex_string = binascii.hexlify(byte_string).decode('utf-8')
    if hex_string == 'a4c13859da18':
        data = addr[4]
        print(data)
        print(type(data))
        #print(addr[1])
        print(addr)

# Start scanning for BLE devices
ble.gap_scan(0, 0, 0)

# Set the scan callback function
ble.irq(scan_callback)

# Wait for 10 seconds
time.sleep(60)

# Stop scanning for BLE devices
ble.gap_scan(None)

# Remove the scan callback function
ble.irq(None)

