Anak1 = 'Eko'
Anak2 = 'Dwi'
Anak3 = 'Tri'
Anak4 = 'Catur'

print(Anak1)
print(Anak2)
print(Anak3)
print(Anak4)


# Tipe Data List/Daftar/Array

anak = ['Eko' ,'Dwi', 'Tri', 'Catur']
anak.append('Limo')
print(anak)

# sapa anak ke -2
print(f'Hai  {anak[1]}')

print('\nSapa Semua ANak')
for a in  anak:
    print(a)

print('\nSapa Semua anak: Cara Ribet')
for a in range(0,len(anak)) :
    print(f'{a+1}.Hai anak {anak[1]}')

"""
Tipe data dictionary sekedar menghubungkan anatara KEY dan VALUE
KVP = Key Value Pair
Dictionary = kamus 
"""
print('\n')
kamus_ind_eng = {'anak': 'son', 'istri': 'wife', 'ayah': 'father', 'ibu': 'mother'}

print(kamus_ind_eng)
print(kamus_ind_eng['ayah'])
print(kamus_ind_eng['ibu'])

print('\n Data ini dikirimkan oleh server gojek , untuk memberikan info di sekitar pemakai aplikasi')
data_dari_server_gojek = {
    'tanggal' : '2020-06-10',
    'driver_list' : [{'Nama' : 'EKo', 'Jarak' : 10}, {'Nama' : 'Dwi', 'jarak' : 30},{'Nama' :'Tri', 'jarak' : 100}, {'Nama' : 'Catur', 'jarak':'1000'}]

}
print(data_dari_server_gojek)
print(f'Driver disekitar sini {data_dari_server_gojek["driver_list"]}')
print(f'Driver Pertama {data_dari_server_gojek["driver_list"][0]}')
print(f'Driver Kedua{data_dari_server_gojek["driver_list"][1]}')
print('Jarak Driver #1')
print(f'Driver dengan jarak terdekat {data_dari_server_gojek["driver_list"][0]["Jarak"]}m')

