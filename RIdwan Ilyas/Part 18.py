N , x, i , jum = 0,0,0,0
ratarata = 0.0

N = int(input('banyaknya nilai : '))

for i in range(0, N):
    x = int(input('angka : '))
    jum += x
print('jumlah :' ,jum)
ratarata = jum/N

print('rata rata : ', ratarata)