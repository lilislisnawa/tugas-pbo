import math

def hitung_luas_permukaan_bola(jari_jari):
    luas_permukaan = 4 * math.pi * jari_jari**2
    return luas_permukaan

def hitung_volume_bola(jari_jari):
    volume = (4/3) * math.pi * jari_jari**3
    return volume

# Masukkan jari-jari bola
jari_jari = float(input("Masukkan jari-jari bola: "))

luas_permukaan = hitung_luas_permukaan_bola(jari_jari)
volume = hitung_volume_bola(jari_jari)

print(f"Luas Permukaan Bola: {luas_permukaan}")
print(f"Volume Bola: {volume}")