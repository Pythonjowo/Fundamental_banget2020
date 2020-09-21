##Tipe Data yang menghubungkan antara Key dan Value

terjemah = {'Ayah': 'Father', 'Ibu': 'Mother', 'Kakek': 'Granpa', 'Nenek': 'GrandMa'}

print(terjemah)
print(terjemah['Ayah'])
print(terjemah['Nenek'])

print('\nData ini sedang dikirimkan oleh server Doku!, Info Data Pengguna')
data_drdoku = dict(tanggal='2020-10-05',
                   driver_list=[{'Nama': 'Fauzi', 'Jarak': '100m'},
                                {'Nama': 'DImas', 'Jarak': '200m'},
                                {'Nama': 'Indah', 'Jarak': '250m'},
                                {'Nama':'Wahyu','Jarak':'300m'}]
                   )

print(data_drdoku)
print('\nDriver Sekitar Kota Anda'+ str(data_drdoku))
print('\nDriver Terbaik 1 ' + str(data_drdoku['driver_list'][1]['Nama']))
print('\nDriver Terbaik 2 ' + str(data_drdoku['driver_list'][3]['Nama']))
print('\nJarak Driver Paling Jauh ' + str(data_drdoku['driver_list'][3]['Jarak']))
