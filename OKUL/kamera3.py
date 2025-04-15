import cv2
from pyzbar import pyzbar
import numpy as np
from datetime import datetime

# Global değişkeni tanımla
son = ""

def decode_qr(frame):
    global son  # Global değişkeni kullan
    decoded_objects = pyzbar.decode(frame)
    for obj in decoded_objects:
        # QR kodunun içeriğini yazdır
        qr_data = obj.data.decode("utf-8")
        
        if son != qr_data:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open("qr_codes.txt", "a") as file:
                file.write(f"QR Code: {qr_data} | Timestamp: {timestamp}\n")
            son = qr_data  # Global değişkeni güncelle

            print(f"QR Code: {qr_data} | Timestamp: {timestamp}")
        if qr_data == "exit":
            cap.release()
            cv2.destroyAllWindows()
            file.close()
            exit()

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


# Kamerayı serbest bırak ve pencereleri kapat
cap.release()
cv2.destroyAllWindows()
file.close()