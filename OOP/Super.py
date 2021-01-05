class Hero:

    def __init__(self, nama, health,):
        self.nama = nama
        self.health = health

    def showInfo(self):
        print('{} memeliki health dengan {}'.format(self.nama, self.health))

class Hero_intelligent(Hero):

    def __init__(self, nama, health, ):
        # Hero.__init__(self,nama,100)
        super().__init__(nama,100)
        super().showInfo()
class Hero_strenght(Hero):

    def __init__(self, nama, health,):
        # Hero.__init__(self, nama, 200)
        super().__init__(nama,200)
        super().showInfo()

lina = Hero_strenght('Fauzi',122)
Axe = Hero_intelligent('Testing', 35)

print(lina.nama , ' ', lina.health)
print(Axe.nama, ' ', Axe.health)