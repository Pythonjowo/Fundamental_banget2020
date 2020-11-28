"""
Loop
-While
"""
count = 0

while count < 5:
    print("Yeyyy Saya akan menikah")
    count = count+1
else:
    print('Akhirnya Berhenti')

"""
Loop
-For in
"""
orang = ['Hilman', 'Boss','Komeng']
for var in orang:
    print(f"Nama namanya adalah {var}")

a = 1

while a <5:
    b = 0
    while b <a:
        print('*', end="")
        b = b +1
    print()
    a = a+1

for a in range(1,5):
    for b in range(1,5):
        c = a*b
        print(c, end=' ')
    print()


