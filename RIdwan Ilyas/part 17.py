i, n , faktorial  = 0,0,1
n = int(input('Masukkan Nilai '))

for i in range(1, n+1):
    faktorial *= i

print(f'Faktorial {faktorial}')