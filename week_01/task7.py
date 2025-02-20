import math


class WinDoor:
    def __init__(self, w, h):
        self.square = w * h


class Room:
    def __init__(self, l, w, h):
        self.length = l
        self.width = w
        self.height = h
        self.wd = []

    def add_wd(self, w, h):
        self.wd.append(WinDoor(w, h))

    def full_surface(self):
        return 2 * self.height * (self.length + self.width)

    def work_surface(self):
        new_square = self.full_surface()
        for i in self.wd:
            new_square -= i.square
        return new_square

    def wallpapers(self, l, w):
        return math.ceil(self.work_surface() / (w * l))


print("Размеры помещения:")
l = float(input("Длина - "))
w = float(input("Ширина - "))
h = float(input("Высота - "))
r1 = Room(l, w, h)

flag = input("Есть неоклеиваемая поверхность? (1 - да, 2 - нет) ")
while flag == '1':
    w = float(input("Ширина - "))
    h = float(input("Высота - "))
    r1.add_wd(w, h)
    flag = input("Добавить еще? (1 - да, 2 - нет) ")

print("Размеры рулона:")
l = float(input("Длина - "))
w = float(input("Ширина - "))

print("Площадь оклейки", r1.work_surface())
print("Количество рулонов", r1.wallpapers(l, w))