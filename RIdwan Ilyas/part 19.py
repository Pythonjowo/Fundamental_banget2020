N, i, j = 0,0,0

N = int(input('Masukkan tinggi :'))

for i in range(0, N+1):
    for j in range(0,i):
        print('*',end='')
    print()

