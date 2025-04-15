import cv2

# Kamerayı başlat
kamera = cv2.VideoCapture(0)
# Kamera çözünürlüğünü ayarla
#kamera.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
#kamera.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)
# Kamera açılıp açılmadığını kontrol et


if not kamera.isOpened():
    print("Kamera açılamadı!")
    exit()

while True:
    # Kameradan görüntü al
    ret, frame = kamera.read()
    if not ret:
        print("Görüntü alınamadı!")
        break

    # Görüntüyü göster
    cv2.imshow("Kamera Görüntüsü", frame)

    # 'q' tuşuna basıldığında çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kaynakları serbest bırak
kamera.release()
cv2.destroyAllWindows()