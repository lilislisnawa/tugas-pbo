kalimat = input("Masukkan sebuah kalimat: ")
kalimat = kalimat.lower()  # Ubah ke huruf kecil agar tidak tergantung pada huruf besar atau kecil

jumlah_vokal = 0
jumlah_konsonan = 0
jumlah_spasi = 0

for karakter in kalimat:
    if karakter in 'aeiou':
        jumlah_vokal += 
    elif karakter.isalpha():
        jumlah_konsonan += 1
    elif karakter.isspace():
        jumlah_spasi += 1

print("Jumlah huruf vokal:", jumlah_vokal)
print("Jumlah huruf konsonan:", jumlah_konsonan)
print("Jumlah karakter spasi:", jumlah_spasi)

# List yang berisi angka-angka
angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

jumlah_genap = 0

for num in angka:
    if num % 2 == 0:
        jumlah_genap += 1

print("Jumlah bilangan genap dalam list:", jumlah_genap)

teks = "Hello, 123 world!"

huruf = angka = karakter_khusus = spasi = 0

for karakter in teks:
    if karakter.isalpha():
        huruf += 1
    elif karakter.isdigit():
        angka += 1
    elif karakter.isspace():
        spasi += 1
    else:
        karakter_khusus += 1

print("Jumlah huruf:", huruf)
print("Jumlah angka:", angka)
print("Jumlah karakter khusus:", karakter_khusus)
print("Jumlah spasi:", spasi)