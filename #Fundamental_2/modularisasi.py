# # #Minghitung Luas Segitiga Luas Segita = Alas * Tinggi / 2# # #

alas = 10
tinggi =5

print('Menghitung Luas Segitiga 1')
luas_segitiga = alas * tinggi/2

print('\nMenghitung Luas Segitiga Diketahui Alas ='+str(alas) + ' Tinggi =' + str(tinggi)
      + ' Luas Segitiga Adalah ='+str(luas_segitiga)
)

print('\nMenghitung Luas Segitiga 1 dengan copy paste')
luas_segitiga = alas * tinggi/2

print('\nMenghitung Luas Segitiga Diketahui Alas ='+str(alas) + ' Tinggi =' + str(tinggi)
      + ' Luas Segitiga Adalah ='+str(luas_segitiga)
)

print('\nMembuat Fungsi Menghitung Luas Segitiga')
def hitung_luas_segitiga(alas,tinggi):
    hitung_luas = alas * tinggi/2
    return hitung_luas
alas = 5
tinggi = 5
print('\nMenghitung Luas Segitiga Diketahui Alas ='+str(alas) + ' Tinggi =' + str(tinggi)
      + ' Luas Segitiga Adalah ='+str(hitung_luas_segitiga(alas,tinggi)))
print('Menghitung luas segitiga dengan fungsi '+ str(hitung_luas_segitiga(5,5)))
print('Menghitung luas segitiga dengan fungsi '+ str(hitung_luas_segitiga(100,5)))
