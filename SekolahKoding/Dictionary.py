"""
Sequences
list [] - Tuple () - Dictionary {}
key:value
"""


data = dict(nama='Hilman', age='17', hobby='sing')

print('Namanya Adalah Hilman ' + data['nama'])

##Mengubah Data Pada Dictionary

data['nama '] = 'Fauzi'
print(data)

##Menghapus Data Pada Dictionary

del data['age']
print(data)

##Dictioanry dengan perulangan

for key,value in data.items():
    print(f'{key} {value}')


##Nested Dictionary

data = {1:{'nama':'Hilman', 'age':'17', 'hobby':'sing'},
        2: {'nama':'Fauzi', 'age':'19', 'hobby':'Hadroh'}}

print(data[2]['nama'])


for key,value in data.items():
    print(f'Keynya: {key}')
    for key2 in value:
        print(f'{key} {value[key2]}')