# tipe data skalar /tipe data sederahan
siswa1 = 'Fauzi'
siswa2 = 'DImas'
siswa3 = 'Indah'
siswa4 = 'Wahyu'

print('siswa1')
print('siswa2')
print('siswa3')
print('siswa4')

print('\nTipe Data List/Daftar/array')
anak = ['Fauzi', 'DImas', 'Indah', 'Wahyu']
print(anak)
anak.append('Ibnu')
print(anak)

print('\nSapa Anak terakhir')
print('Nama '+str(anak[4]))

print('\nSapa Semua anak')
for sapa in anak:
    print('Hai '+str(sapa))

print("\nSapa semua anak : Cara Ribet")
for ribet in range(0, len(anak)):
    print('Ribet '+str(anak[ribet]))





