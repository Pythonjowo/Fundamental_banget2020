"""
Program menghitung luas segitiga
Luas_Segitiga = alas * tinggi/2
"""

alas = 10
tinggi = 6
luas_segetiga = alas * tinggi/2
print(f'Segitiga dengan alas={alas} dan tinggi={tinggi} memiliki luas {luas_segetiga}')

alas = 20
tinggi = 6
luas_segetiga = alas * tinggi/2
print(f'Segitiga dengan alas={alas} dan tinggi={tinggi} memiliki luas {luas_segetiga}')

def hitug_luas_segitiga(alas, tinggi):
    luas_segetiga = alas * tinggi / 2
    return luas_segetiga
print(f'Menghitung segitiga dengan fungsi, hasilnya = {hitug_luas_segitiga(10,6)}')
print(f'Menghitung segitiga dengan fungsi, hasilnya = {hitug_luas_segitiga(20,6)}')
