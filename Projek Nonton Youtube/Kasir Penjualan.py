print('-----Toko Ittihad Shop----')

print('Menjual berbagai macam Koko')

def total(harga,  jumlah):
    return harga*jumlah

x = str(input('Nama Barang :' ))
y = str(input('Ukuran :' ))
harga = int(input('Masukkan Harga Barang: '))
jumlah = int(input(('Masukkan jumlah pakaian yang dibeli :')))
Total = total(harga, jumlah)

if Total > 100000:
    Total = Total - 0.5*Total
    print(f'Total harga Rp. {Total}')
    bayar = int(input('Masukkan Uang Pembeli : '))
    Totalbayar = (bayar-Total)
    print(f'Kembalian anda adalah {Totalbayar}')
else:
    Total = Total - 0 *Total
    print(f'Total harga Rp. {Total}')
    bayar = int(input('Masukkan Uang Pembeli : '))
    Totalbayar = (bayar - Total)
    print(f'Kembalian anda adalah {Totalbayar}')
    print('Trima kasih atas kepercayaan Anda')