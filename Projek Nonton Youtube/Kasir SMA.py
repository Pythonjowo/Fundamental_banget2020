print('Halaman Input Data')
kode = int(input('KOde Barang : '))
nama = input('Nama Barang : ')
harga = int(input('Harga : '))
jumlahitem = int(input('Jumlah Item :'))

total = jumlahitem*harga

if total > 100000:
    diskon = 10/100*total
    jumlahafter = total - diskon
    print(f'Anda mendapatkan potongan {jumlahafter}')
    print(f'Total Bayar Rp.{total}')
else:
    print(f'Total Bayar Rp.{total}')