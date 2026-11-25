#!/usr/bin/env python3
import time

selamlar = [
    "Merhaba",
    "Selam",
    "Naber",
    "Günaydın",
    "İyi günler",
    "Hoş geldin",
    "Selamün aleyküm"
]

def sonsuz_selam():
    print("Sonsuz Selam Botu aktif...")
    i = 0
    while True:
        print(f"{selamlar[i % len(selamlar)]}! (sayı: {i+1})")
        i += 1
        time.sleep(0.5)

if __name__ == "__main__":
    try:
        sonsuz_selam()
    except KeyboardInterrupt:
        print("\nSelamlar durdu. Ama yarın devam.")
