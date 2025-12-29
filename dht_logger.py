#!/usr/bin/env python3
import time, csv
import board, adafruit_dht
from datetime import datetime

CSV_FILE = "dht_log.csv"
dhtDevice = adafruit_dht.DHT22(board.D4)  # ใช้ GPIO4 (pin 7)

# สร้างไฟล์ถ้ายังไม่มี
try:
    with open(CSV_FILE, "x", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["datetime", "temperature", "humidity"])
except FileExistsError:
    pass

while True:
    try:
        temp_c = dhtDevice.temperature
        hum = dhtDevice.humidity
        if temp_c is not None and hum is not None:
            with open(CSV_FILE, "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), temp_c, hum])
            print(f"Saved: {temp_c} °C, {hum} %")
    except Exception as e:
        print(f"Error: {e}")

    time.sleep(5)  # เก็บทุก 5 วินาที
