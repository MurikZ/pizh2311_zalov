from random import randint

class Person:
    count = 0
    def __init__(self,c):
        self.id = Person.count
        Person.count += 1
        self.command = c
class Hero(Person):
    def __init__(self,c):
        Person.__init__(self,c)
        self.level = 1
    def upgradeLvl(self):
        self.level+=1
class Soldier(Person):
    def __init__(self,c):
        Person.__init__(self,c)
        self.my_hero = None
    def follow(self,hero):
        self.my_hero = hero.id
h1 = Hero(1)
h2 = Hero(2)

army1 = []
army2 = []

for i in range(20):
    n =  randint(1,2)
    if n == 1:
        army1.append(Soldier(n))
    else:
        army2.append(Soldier(n))
print(len(army1),len(army2))

if len(army1) > len(army2):
    h1.upgradeLvl()
else:
    h2.upgradeLvl()
army1[0].follow(h1)
print(army1[0].id, h1.id)


