## KOndisi Percabangan Sederhana
angka1 = input('Masukkan Angka Pertama = ')
angka2 = input('Masukkan Angka Kedua = ')
an = int(angka1)
un = int(angka2)
if angka1 <= angka2:
    print("Iya")
    print(f'Angkamu {angka1}')
else:
    print("Tidak")
    print(f'Angkamu {angka2}')

# Logical Operator dan Lebih Dari Satu Syarat
"""
Lebih dari satu syarat
and or not
& | !=
"""

syarat1 = True
syarat2 = False

if syarat1 | syarat2:
    print("Anda Benar!")
else:
    print("Anda Salah!")

if (1<2) != (6>5):
    print("Anda Benar")
else:
    print("Anda Salah")


