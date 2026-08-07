# Program menentukan angka ganjil atau genap

# Input angka
angka = int(input("Masukkan sebuah angka: "))

# Mengecek apakah angka genap atau ganjil
if angka % 2 == 0:
    print(angka, "adalah bilangan genap")
else:
    print(angka, "adalah bilangan ganjil")
