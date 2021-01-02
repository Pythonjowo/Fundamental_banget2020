#Program Konversi Waktu Ke detik

class Waktu:
    jam = 0
    mm = 0
    dd = 0

Jam = Waktu()

TotalDetik = 0

#Alogoritma

j = input('Masukkan jam : ')
m = input('Masukkan Menit : ')
d = input('Masukkan Detik : ')

Jam.jam = int(j)
Jam.mm = int(m)
Jam.dd = int(d)

# print(f'Jam {Jam.jam} Menit {Jam.mm} Detik {Jam.dd}')

TotalDetik = Jam.dd
TotalDetik = TotalDetik + (Jam.mm * 60)
TotalDetik = TotalDetik + (Jam.jam * 3600)

print(f'Total Detik {TotalDetik}')