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
    print(f'Hai anak {anak[1]}')
