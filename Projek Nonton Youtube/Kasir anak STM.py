#Membuat Variable dengan A,B,C

print('Selamat datang di menu')
print('Fauzi Bariq Mahya')
print('XI TKJ 2')

A = str(input('Masukkan nama Barang : '))
B = int(input('Masukkan Harga Barang : ' ))
C = int(input('Masukkan jumlah yang dibeli : '))

TOTAL = (B*C)
print(f'Anda Membeli {A} Total Pembayaran anda = Rp.{TOTAL}')
print('Terima kasih')