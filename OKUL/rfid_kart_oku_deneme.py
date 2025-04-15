from mfrc522 import SimpleMFRC522

import RPi.GPIO as GPIO
son=0
reader = SimpleMFRC522()

try:
    print("Kartınızı okutun...")
 
    file = open("rfid_kart.txt", "a") 
    
    while True:
        id, text = reader.read()
        if son != id:
            # Kart bilgilerini dosyaya yaz  
            # file.write(f"Kart ID: {id} | Kart Verisi: {text}\n")
            # Kart bilgilerini ekrana yazdır
            
            file.write(f"{id}\n")
 
            print(f"Kart ID: {id}")
            print(f"Kart Verisi: {text}")
            son = id
            print("Kartı tekrar okutabilirsiniz...")
        if id == 146286183806:
            break
except KeyboardInterrupt:
    print("\nProgram sonlandırılıyor...")
finally:
    GPIO.cleanup()
file.close()