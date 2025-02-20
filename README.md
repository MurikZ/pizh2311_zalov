# Лабораторная работа Week02

**Залов Мурат**  
**ПИЖ-Б-О-23-1**  

## Класс "Воздушный замок" (AirCastle)

### Описание
Создаем класс `AirCastle` с конструктором, содержащим три параметра:
- **Высота (`height`)**
- **Количество облаков (`n_clouds`)**
- **Цвет (`color`)**

### Методы

#### Изменение высоты
```python
def change_height(self, value):
    if value >= 0:
        self.height = value
```
Метод изменяет высоту на заданное значение `value`. Если значение отрицательное, высота остается неизменной.

#### Увеличение облаков и высоты
```python
def sum(self, n):
    self.n_clouds += n
    self.height += n // 5
```
Метод увеличивает количество облаков на `n` и высоту на `n // 5`.

#### Определение прозрачности
```python
def __call__(self, transparency):
    return self.height // transparency * self.n_clouds
```
Метод рассчитывает прозрачность на основе переданного значения `transparency`.

### Операции сравнения
Для организации операций сравнения реализованы следующие методы:
- `__eq__` (равенство)
- `__lt__` (меньше)
- `__le__` (меньше или равно)
- `__gt__` (больше)
- `__ge__` (больше или равно)
- `__ne__` (не равно)

## Наследование
Создан класс `MagicAirCastle`, который наследует `AirCastle` и расширяет функционал добавлением магической силы `magic_power`.
```python
class MagicAirCastle(AirCastle):
    def __init__(self, height, n_clouds, color, magic_power):
        super().__init__(height, n_clouds, color)
        self.magic_power = magic_power

    def cast_spell(self):
        return f"Магическая мощь {self.magic_power}!"
```

## Композиция
Создан класс `Cloud`, который описывает облака. Затем реализован класс `AirCastleWithClouds`, использующий композицию (список объектов `Cloud`).

```python
class Cloud:
    def __init__(self, size):
        self.size = size

    def __str__(self):
        return f"Количество облаков: {self.size}"

class AirCastleWithClouds:
    def __init__(self, height, clouds, color):
        self.height = height
        self.clouds = [Cloud(size) for size in clouds]
        self.color = color

    def __str__(self):
        clouds_info = ", ".join(str(cloud) for cloud in self.clouds)
        return f"The AirCastle at an altitude of {self.height} meters is {self.color} with clouds: {clouds_info}"
```

## Пример использования
```python
num1 = AirCastle(23, 3, "green")
num1.change_height(3)
num2 = AirCastle(13, 4, "red")

print(f"num2 >= num1 = {num2 >= num1}")
print(f"Прозрачность: {num1(2)}")
print(num1)
```
**Вывод:**
```
num2 >= num1 = True
Прозрачность: 3
The AirCastle at an altitude of 3 meters is green with 3 clouds
```

