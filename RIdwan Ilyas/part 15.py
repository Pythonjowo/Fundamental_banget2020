class Titik:
    y = 0.0
    x = 0.0

p = Titik()

iy = float(input('Y :'))
ix = float(input('X :'))

p.x = ix
p.y = iy

if p.x == 0.0 and p.y == 0.0:
    print('Tidak masuk kuadran')
else:

    if p.x > 0:
        if p.y > 0:
            print('Kuadaran I')
        else:
            print('Kuadarn IV')
    else:
        if p.y > 0:
            print('Kuadaran II')
        else:
            print('Kuadaran III')