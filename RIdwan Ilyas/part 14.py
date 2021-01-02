nilai = int(input('Masukkan Nilai'))


if nilai >= 90:
    index = 'A'
    print(f'Nilai Anda {index}')
elif nilai >= 80:
    index = 'B'
    print(f'Nilai Anda {index}')
elif nilai >= 70:
    index = 'C'
    print(f'Nilai Anda {index}')
elif nilai <= 60:
    index = 'D'
    print(f'Nilai Anda {index}')
else:
    index = 'E'
    print(f'Nilai Anda {index}')

while True:
    masukan = input('Masukkan Nilai Kembali ? ')
    if masukan == 'Y':
        nilai = int(input('Masukkan Nilai'))
        if nilai >= 90:
            index = 'A'
            print(f'Nilai Anda {index}')
        elif nilai >= 80:
            index = 'B'
            print(f'Nilai Anda {index}')
        elif nilai >= 70:
            index = 'C'
            print(f'Nilai Anda {index}')
        elif nilai <= 60:
            index = 'D'
            print(f'Nilai Anda {index}')
        else:
            index = 'E'
            print(f'Nilai Anda {index}')
    elif masukan == 'T':
        print('Matur tHankyou')
        break
    else:
        print('Rampungan')