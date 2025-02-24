
# Лабораторная работа Week02  
  
**Залов Мурат** **ПИЖ-Б-О-23-1**   
## Класс "Воздушный замок" (AirCastle)  
  
### Описание  
Класс «Воздушный Замок» (AirCastle)
Экземпляр класса инициализируется с аргументами:  
– высота;  
– количество составляющих облаков;  
– цвет.  
Класс должен реализовывать методы:  
– change_height(value) – изменить высоту на value, может уменьшаться только до нуля;  
– сложить с числом, добавляется n облаков к замку, одновременно увеличивается высоту  
на n // 5;  
– экземпляр класса можно вызвать с аргументом – целым числом, означающим  
прозрачность облаков; метод возвращает значение видимости замка, рассчитанное по  
формуле: высота // прозрачность * количество облаков;  
_str_  – возвращает строковое представление в виде:  
“The AirCastle at an altitude of <высота> meters is <цвет> with <количество облаков> clouds”.  
– экземпляры можно сравнивать: сначала по количеству облаков, затем по высоте, затем  
по цвету по алфавиту; для этого нужно реализовать методы сравнения: >, <, >=, <=, ==, !=.
### Методы  
  
#### Изменение высоты  
```python  
def change_height(self, value):  
 if value >= 0: self.height = value  
```  
Метод изменяет высоту на заданное значение `value`. Если значение отрицательное, высота остается неизменной.  
  
#### Увеличение облаков и высоты  
```python  
def sum(self, n):  
 self.n_clouds += n self.height += n // 5  
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
 def __init__(self, height, n_clouds, color, magic_power): super().__init__(height, n_clouds, color) self.magic_power = magic_power  
 def cast_spell(self): return f"Магическая мощь {self.magic_power}!"  
```  
  
## Композиция  
Создан класс `Cloud`, который описывает облака. Затем реализован класс `AirCastleWithClouds`, использующий композицию (список объектов `Cloud`).  
  
```python  
class Cloud:  
 def __init__(self, size): self.size = size  
 def __str__(self): return f"Количество облаков: {self.size}"  
class AirCastleWithClouds:  
 def __init__(self, height, clouds, color): self.height = height self.clouds = [Cloud(size) for size in clouds] self.color = color  
 def __str__(self): clouds_info = ", ".join(str(cloud) for cloud in self.clouds) return f"The AirCastle at an altitude of {self.height} meters is {self.color} with clouds: {clouds_info}"  
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
# Лабораторная работа Week_03
## Задание "Римское число"
### Описание
Создайте класс Roman (РимскоеЧисло), представляющий римское число и поддерживающий операции +, -, *, /.
Совет*
При реализации класса следуйте рекомендациям:
-   операции +, -, *, / реализуйте как специальные методы (**add**  и др.);
-   методы преобразования имеет смысл реализовать как статические методы, позволяя не создавать экземпляр объекта в случае, если необходимо выполнить только преобразования чисел.

При выполнении задания необходимо построить UML-диаграмма классов приложения
## Использование
### Конструктор
Создаем конструктор с агрументами значений для сложения, умножения, вычитания, деления, а также агрумент со словарем, состоящим из пар ключ - значения, необходимых для преобразования арабских чисел в римские.
```python
def __init__(self, arg_plus, arg_minus, arg_umn, arg_del, roman_numbers) -> None:  
    self.arg_plus = arg_plus  
    self.arg_minus = arg_minus  
    self.arg_umn = arg_umn  
    self.arg_del = arg_del  
    self.roman_numbers = roman_numbers
```
### Метод для преобразования
Создаем метод с агрументом, который нужно преобразовать и перебираем значения из словаря, пока аргумент больше чем значение из словаря мы присваиваем перменной значение ключа, а у аргумента отнимаем значение этого ключа
```python
def roma(self, number) -> str:  
num = ''  
  for key, value in self.roman_numbers.items():  
        while number >= value:  
            num += key  
            number -= value  
    return num
```
### Создание экземпляра класса
Создаем экземпляр со случайными числами, а также словарем с значениями римских чисел
```python
roman = Roman(3, 5, 4, 5, {
    'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
    'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
    'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1
})
```

### Арифметические операции
- **Сложение (`+`)**: складывает значение `arg_plus` с переданным числом.
- **Вычитание (`-`)**: вычитает переданное число из `arg_minus`.
- **Умножение (`*`)**: умножает `arg_umn` на переданное число.
- **Деление (`/`)**: делит `arg_del` на переданное число и возвращает результат в виде `float`.
```python
def __add__(self, other) -> int:  
    return self.arg_plus + other  
  
def __sub__(self, other) -> int:  
	return self.arg_minus - other  
  
def __mul__(self, other) -> int:  
  return self.arg_umn * other  
  
def __truediv__(self, other) -> float:  
   return self.arg_del / other
```

### Преобразование числа в римскую систему

```python
print(roman.roma(plus))
print(roman.roma(minus))
print(roman.roma(multiply))
print(roman.roma(int(divide)))
```


