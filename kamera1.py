# filepath: /c:/Users/Asus/git_okul/okul/okul/kamera1.py
import cv2

# Kamerayı başlat
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Kamera açılamadı")
    exit()

# Bir kare yakala
ret, frame = cap.read()

if not ret:
    print("Kare yakalanamadı")
    exit()

# Fotoğrafı kaydet
cv2.imwrite("captured_image.jpg", frame)

# Kamerayı serbest bırak
cap.release()

print("Fotoğraf kaydedildi: captured_image.jpg")