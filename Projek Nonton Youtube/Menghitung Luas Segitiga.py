print('Menghitung Luas Segitiga')

a = int(input('Masukkan alas segitiga =' ))
t = int(input('Masukkan Tinggi Segitiga = '))

if   a >= 100:
     print('Baleni Neh cukk')

elif 0 < a < 100 and 0 < t < 100:
     hitung = (0.5*a*t)
     print(f'Luas segitiga anda Adalah {hitung}')
else:
     print('Harap Masukkan Angka antar 0-100')


while True:
    print('Apakah anda ingin melanjutkan menghitung kembali..?')
    P = str(input('Jawab Ya, jika Mau Melan410jutkan atau Tidak ?? '))
    if P == 'Ya':
        a = int(input('Masukkan alas segitiga ='))
        t = int(input('Masukkan Tinggi Segitiga = '))
        if a>= 100:
            print('Baleni Neh cukk')
        elif 0 < a < 100 and 0 < t < 100:
            hitung = (0.5*a*t)
            print(f'Luas segitiga anda Adalah {hitung}')
        else:
            print('Harap Masukkan Angka antar 0-100')
    elif P == 'Tidak':
        print('Oke lah Makasih')
        break
    else:
        print('Masukkan Ya atau Tidak')