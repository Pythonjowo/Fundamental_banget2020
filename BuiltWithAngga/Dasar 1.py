#Belajar variable

#membuat variable (text atau string)

hewan = "unicorn"
buah = "Pisang"
print(f'{buah} {hewan}')


#Belajar Tipe Data

#Profile User
nama = 'Shayna'
age = 22
passion = 'Designer'

#Booelan pada Python
isMarried = True

#Print Data
print(nama)

#Operator Matematika
#Dompet Digital

dompetDIgital = 120000

#beli emas, buku, dvd
totalBelanja = 50000
pajak = totalBelanja * 10 //100

hargaTotal = totalBelanja + pajak
kembalian = dompetDIgital - hargaTotal
print('Total Belanja anda', + hargaTotal)
print(f'Kembalian anda {kembalian}')

#Assigment Operator

age = 20
age = age // 2
age //= 2
print(age)

firstname = 'Fauzi'
lastname = 'Bariq'

complateName = firstname + " " + lastname

print(complateName)



#Comparasion Perbandingan

#Toko online

#Dompet Digital
dompet = 150000

# membeli macbook
total = 300000

#validasi dompet sebelum sukses

print(dompet >= total)

#Login FUnction

username = "Fauzi"
pasword = "Dating123"

#Prosess checking database

usernameDiDatabase = "Fauzii"
print(usernameDiDatabase == username)


#Logical Operator
#Mengombiinasikan suatu statement
a = 2
print(a < 2)

#Register USer Baru
pasword = 'Dating1233'

confirmPasword = 'Dating123'
print(pasword == 'Dating1233' and confirmPasword == pasword)

#Check  Kekayaan kredit bank si Budi

isiKerja = False
isiUsaha = False

print(isiKerja == True or isiUsaha == True)


#List Data Type

cars = ['bmw','Honda','porsce', 'Toyota', 'Renault','Nissan']

print(cars[2:])
print(cars[3:6])

print(len(cars))

houses = ['ciputra','lippo','meikarta']
#Mengitung panjang
print(len(houses[1]))
#Menambahkan pada list
houses.append('tes')
print(houses)

#Merubah Ciputra jadi Semarang
houses[0] = 'Semarang'
print(houses)


#Marge Data List
#My foods
foods = ['Ayam', 'Ikan','Sayur','Nasi']
#MyDrinks

drinks = ['Teh','Jahe Angat','Kopi']
#Membuat variable untuk marge data
daily_drinks = foods + drinks
print(daily_drinks[4])

#Menggabungkan variable dengan extends
foods.extend(drinks)
print(foods)
print(foods[6])

#Membuat variable untuk marge data
daily_meal = foods + drinks
print(daily_meal)
print(daily_meal[5])

#Mengurutkan data yang ada pada  python

foods = ['ikan', 'Sayur','nasi','Ayam','Sayur']
hitungSayur = foods.count('Sayur')
print(hitungSayur)
#Mengurutkan berdasarkan Huruf awal
foods.sort()
print(foods[0])

#Dibalik

foods.sort(reverse=True)
print(foods)
