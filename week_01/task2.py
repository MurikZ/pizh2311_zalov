import random


class Warrior:
    def setHealth(self,health):
        self.health = health
    def getAttack(self):
        self.health -=20
first = Warrior()
second = Warrior()
first.setHealth(100)
second.setHealth(100)

while first.health!=0 or second.health!=0:
    rand = random.randint(1, 2)
    if rand == 1:
        second.getAttack()
        print("первый игрок нанес урон ")
        print("у второго игрока осталось здоровья ",second.health)

    else:
        first.getAttack()
        print("второй игрок нанес урон ")
        print("у первого игрока осталось здоровья ", first.health)
    if first.health==0:
        print("второй игрок победил")
        break
    if second.health==0:
        print("первый игрок победил")
        break


