import cv2

# Kamerayı başlat
cap = cv2.VideoCapture(0, cv2.CAP_V4L2)

if not cap.isOpened():
    print("Kamera açılamadı")
    exit()

# Kameradan görüntü al ve göster
while True:
    ret, frame = cap.read()
    if not ret:
        print("Kare yakalanamadı")
        break

    # Görüntüyü göster
    cv2.imshow("Kamera", frame)

    # 'q' tuşuna basıldığında çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamerayı serbest bırak ve pencereleri kapat
cap.release()
cv2.destroyAllWindows()