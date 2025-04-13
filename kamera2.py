#nisan 2025 kamera ve keran düzgün çalışıyor
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------------
import cv2
from pyzbar import pyzbar
import numpy as np
from datetime import datetime
import time
#----------------------------------------------------------------------------------
from smbus2 import SMBus
from RPLCD.i2c import CharLCD

# Define I2C address and bus number
i2c_address = 0x3f#27  # Change this to your I2C address
i2c_busnum = 1      # Change this to your I2C bus number if necessary

# Initialize the I2C interface
bus = SMBus(i2c_busnum)

# Define LCD column and row size for 20x4 LCD.
lcd_columns = 20
lcd_rows = 4

# Initialize the LCD using the I2C interface
lcd = CharLCD(i2c_expander='PCF8574', address=i2c_address, port=i2c_busnum,
              cols=lcd_columns, rows=lcd_rows, charmap='A00', auto_linebreaks=True)

# Function to replace Turkish characters with their English equivalents
def replace_turkish_chars(text):
    replacements = {
        'Ğ': 'G', 'Ü': 'U', 'Ş': 'S', 'İ': 'I', 'Ç': 'C', 'Ö': 'O', 'ı': 'i', 'ğ': 'g', 'ü': 'u', 'ş': 's', 'ç': 'c', 'ö': 'o'
    }
    for turkish_char, english_char in replacements.items():
        text = text.replace(turkish_char, english_char)
    return text

# Write the text to the LCD
turkish_text = 'Program Çalışıyor'
english_text = replace_turkish_chars(turkish_text)

lcd.clear()
lcd.cursor_pos = (0, 0) # ilk sayı satır, ikinci sayı sütun, 0enüst 3enalt
lcd.write_string(english_text[:lcd_columns])
lcd.cursor_pos = (1, 0)
lcd.write_string(english_text[lcd_columns:lcd_columns*2])
#----------------------------------------------------------------------------------
# Global değişkeni tanımla
son = ""

def decode_qr(frame):
    global son  # Global değişkeni kullan
    decoded_objects = pyzbar.decode(frame)
    for obj in decoded_objects:
        # QR kodunun içeriğini yazdır
        qr_data = obj.data.decode("utf-8")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if son != qr_data:
            with open("qr_codes.txt", "a") as file:
                file.write(f"QR Code: {qr_data} | Timestamp: {timestamp}\n")
            son = qr_data  # Global değişkeni güncelle
            lcd.clear()
            lcd.cursor_pos = (0, 0)
            lcd.write_string(replace_turkish_chars( qr_data)[:lcd_columns])
            lcd.cursor_pos = (1, 0)
            lcd.write_string(replace_turkish_chars( qr_data)[lcd_columns:lcd_columns*2])
            lcd.cursor_pos = (2, 0)
            lcd.write_string(replace_turkish_chars( timestamp)[:lcd_columns])
            print(f"QR Code: {qr_data} | Timestamp: {timestamp}")
        if qr_data == "exit":
            exit()
        # QR kodunun etrafına dikdörtgen çiz
#        points = obj.polygon
#        if len(points) == 4:
#            pts = [(point.x, point.y) for point in points]
#            pts = np.array(pts, dtype=np.int32)
#            cv2.polylines(frame, [pts], isClosed=True, color=(0, 255, 0), thickness=2)
    return frame

# Kamerayı başlat
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Kamera açılamadı")
    exit()
#cap.set(3, 1024)
#cap.set(4, 768)

while True:
    
    # Bir kare yakala
    ret, frame = cap.read()
    if not ret:
        print("Kare yakalanamadı")
        break

    # QR kodlarını tara
    frame = decode_qr(frame)

    # Sonucu göster bu satırı iptal ederek daha performanslı çalışıyor ekranda kamera görünmüyor
 ###    cv2.imshow("QR Code Reader", frame)

    # 'q' tuşuna basıldığında çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamerayı serbest bırak ve pencereleri kapat
cap.release()
cv2.destroyAllWindows()