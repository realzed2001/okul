# Raspberry pi camera QR code reader

import cv2
from picamera2 import Picamera2
import sqlite3

# --- SQLite setup ---
conn = sqlite3.connect("qr_log.db")
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS "giriş-çıkış" (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    qr_data TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")
conn.commit()

def auto_brightness_contrast(frame):
    # --- Auto brightness/contrast correction using CLAHE ---
    lab = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    cl = clahe.apply(l)
    limg = cv2.merge((cl, a, b))
    frame = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
    return frame

def detect_and_draw_qr(frame, qr_detector):
    data, bbox, _ = qr_detector.detectAndDecode(frame)
    if bbox is not None and data:
        print(f"QR Code Data: {data}")  # Print QR code data to terminal
        # --- Insert QR code data into SQLite ---
        cur.execute('INSERT INTO "giriş-çıkış" (qr_data) VALUES (?)', (data,))
        conn.commit()
        bbox = bbox.astype(int)  # Ensure integer coordinates
        n = len(bbox[0])
        for i in range(n):
            pt1 = tuple(bbox[0][i])
            pt2 = tuple(bbox[0][(i+1) % n])
            cv2.line(frame, pt1, pt2, (0, 255, 0), 2)
        cv2.putText(frame, data, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    return frame

qr_detector = cv2.QRCodeDetector()
picam2 = Picamera2()
picam2.start()

try:
    while True:
        frame = picam2.capture_array()
        frame = auto_brightness_contrast(frame)
        frame = detect_and_draw_qr(frame, qr_detector)
        cv2.imshow("Kamera", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    conn.close()
    cv2.destroyAllWindows()