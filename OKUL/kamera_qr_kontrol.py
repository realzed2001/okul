import cv2
from pyzbar import pyzbar
import numpy as np
from datetime import datetime

# Global değişkeni tanımla
son = ""

# Kullanıcı isimlerini dosyadan oku
with open("kullanicilar.txt", "r") as file:
    kullanicilar = [line.strip() for line in file.readlines()]

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

            # Kullanıcı kontrolü
            if qr_data in kullanicilar:
                print(f"Kullanıcı var: {qr_data} | Timestamp: {timestamp}")
            else:
                print(f"Kullanıcı yok: {qr_data} | Timestamp: {timestamp}")

        # QR kodunun etrafına dikdörtgen çiz
        points = obj.polygon
        if len(points) == 4:
            pts = [(point.x, point.y) for point in points]
            pts = np.array(pts, dtype=np.int32)
            cv2.polylines(frame, [pts], isClosed=True, color=(0, 255, 0), thickness=2)
    return frame

# Kamerayı başlat
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Kamera açılamadı")
    exit()

while True:
    # Bir kare yakala
    ret, frame = cap.read()
    if not ret:
        print("Kare yakalanamadı")
        break

    # QR kodlarını tara
    frame = decode_qr(frame)

    # Sonucu göster
    cv2.imshow("QR Code Reader", frame)

    # 'q' tuşuna basıldığında çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamerayı serbest bırak ve pencereleri kapat
cap.release()
cv2.destroyAllWindows()