#Program menghitung titik tengah diantara dua titik

class Titik:
    x = 0.0
    y = 0.0

p1 = Titik()
p2 = Titik()
p3 = Titik()

x1 = input('p1.x : ')
y2 = input('p1.y : ')
p1.x = float(x1)
p1.y = float(x1)

x2 = float(input('p2.x :  '))
y2 = float(input('p2.x :  '))
p2.x = float(x1)
p2.y = float(y2)

p3.x = (p1.x + p2.x)/2
p3.y = (p1.y + p2.y)/2

print(f'p3.x {p3.x}')
print(f'p3.y {p3.y}')

