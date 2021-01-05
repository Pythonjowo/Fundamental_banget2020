class Hero:

    def __init__(self, nama, health,):
        self.nama = nama
        self.health = health

class Hero_intelligent(Hero):
    pass

class Hero_enggine(Hero_intelligent):
    pass

lina = Hero('fauzi', 50)
teaches = Hero_intelligent('Testing',10)
axe = Hero_enggine('Uji',100)

print(lina.nama)
print(teaches.nama)
print(axe.nama)