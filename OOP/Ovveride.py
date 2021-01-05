class Hero:

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def showInfo(self):
        print('Ovveride di Class Hero')
        print('{} health {}'.format(self.name, self.health))

class Hero_inteligent(Hero):

    def __init__(self,name):
        super().__init__(name, 100)

    def showInfo(self):
        print('Ovveride di SubClass Hero')
        print('{} health {}'.format(self.name, self.health))

class Hero_strenght(Hero):

    def __init__(self, name):
         super().__init__(name, 100)

lina = Hero_inteligent('Lina')
Axe = Hero_strenght('Fauzi')

print(lina.showInfo())
print(Axe.showInfo())