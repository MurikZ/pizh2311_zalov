
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
## Задание "Пицца"

Данный проект реализует систему заказа пиццы с возможностью выбора различных видов пицц, оформления заказа и его обработки.
### Описание 
Пиццерия предлагает клиентам три вида пиццы: Пепперони, Барбекю и Дары Моря, каждая из которых определяется тестом, соусом и начинкой.

Требуется спроектировать и реализовать приложение для терминала, позволяющее обеспечить обслуживание посетителей.

### Дополнительная информация

В бизнес-процессе работы пиццерии в контексте задачи можно выделить три сущности (объекта):

-   **Терминал**: отвечает за взаимодействие с пользователем:
    
    -   вывод меню на экран;
    -   прием команд от пользователя (выбор пиццы, подтверждение заказа, оплата и др.).
-   **Заказ**: содержит список заказанных пицц, умеет подсчитывать свою стоимость.
    
-   **Пицца**: содержит заявленные характеристики пиццы, а также умеет себя подготовить (замесить тесто, собрать ингредиенты и т. д.), испечь, порезать и упаковать.  
    Так как пиццерия реализует несколько видов пиццы, которые различаются характеристиками, логично будет сделать общий класс **Пицца**, а в дочерних классах (например, **ПиццаБарбекю**) уточнить характеристики конкретной пиццы.
### Классы
`Pizza`

Базовый класс для представления пиццы.

#### Конструктор

```python
 def __init__(self, name, testo, sauce, nachinka, price) -> None:

```

-   `name` — Название пиццы.
-   `testo` — Тип теста.
-   `sauce` — Соус.
-   `nachinka` — Начинка (список ингредиентов).
-   `price` — Цена.

#### Методы

-   `__str__()` — Возвращает строковое представление пиццы.
-   `prepare()` — Этап подготовки пиццы.
-   `cook()` — Этап выпекания пиццы.
-   `slice()` — Этап нарезки пиццы.
-   `packet()` — Этап упаковки пиццы.

### `Pizza_barbeku`

Наследуется от `Pizza`. Создает объект пиццы Барбекю.

### `Pizza_pepperoni`

Наследуется от `Pizza`. Создает объект пиццы Пепперони.

### `Pizza_sea`

Наследуется от `Pizza`. Создает объект пиццы "Дары моря".

### `Order`

Класс заказа, содержащий список выбранных пицц.

#### Конструктор

```python
def __init__(self) -> None:

```

-   Создает пустой список `list_of_orders` для хранения заказанных пицц.

#### Методы

-   `__str__()` — Возвращает строковое представление заказа.
-   `add_pizza(pizza)` — Добавляет пиццу в заказ.
-   `price()` — Возвращает общую стоимость заказа.
-   `process_order()` — Обрабатывает заказ (готовка, выпекание, нарезка, упаковка).

## Использование

### Меню

Создаются экземпляры пицц и отображается меню:

```python
print(Pizza_pepperoni())
print(Pizza_sea())
print(Pizza_barbeku())

```

### Оформление заказа

Пользователь выбирает пиццы с помощью ввода чисел:

```python
zakaz = int(input("Введите заказ\n1-Пепперони\n2-Барбекю\n3-Дары моря\n0-Завершить заказ\n"))

```

Выбранные пиццы добавляются в заказ:

```python
if zakaz == 1:
    order.add_pizza(Pizza_pepperoni())
elif zakaz == 2:
    order.add_pizza(Pizza_barbeku())
elif zakaz == 3:
    order.add_pizza(Pizza_sea())

```

### Вывод заказа и процесса приготовления

После завершения выбора пицц отображается информация о заказе и процесс его приготовления:

```python
print(order)
print("\nПроцесс приготовления:\n")
print(order.process_order())

```

# Лабораторная работа week_04
## **4.3.3. Банковские вклады**
### Описание проекта

Банк предлагает ряд вкладов для физических лиц:

-   **Срочный вклад**: расчет прибыли осуществляется по формуле простых процентов;
-   **Бонусный вклад**: бонус начисляется в конце периода как % от прибыли, если вклад больше определенной суммы;
-   **Вклад с капитализацией процентов**.

Реализуйте приложение, которое позволит подобрать клиенту вклад по заданным параметрам.

При выполнении задания необходимо построить UML-диаграмму классов приложения.

## Классы

### 1. `Deposit`

Базовый класс для представления банковского вклада.

-   `summa (float)`: Сумма вклада.
    
-   `procent (float)`: Годовая процентная ставка.
    
-   `period (int)`: Срок вклада в годах.
    

### 2. `Srochniy`

Класс для срочного вклада, рассчитываемого по формуле простых процентов.

-   Метод `calculate_srochiy()`: Возвращает прибыль по вкладу по формуле:
    
    ```python
    # Прибыль = (Сумма * Процентная ставка * Срок) / 100
    def calculate_srochiy(self) -> float:  
		return self.summa * self.period * self.procent / 100
### 3. `Bonus`

Класс для бонусного вклада, который начисляет дополнительный процент при превышении порога прибыли.

-   `bonus_limit (float)`: Порог прибыли для начисления бонуса.
    
-   `bonus_procent (float)`: Процент бонуса от прибыли.
    
-   Метод `calculate_bonus()`: Возвращает прибыль по формуле:
    
    ```python
    #Прибыль = (Сумма * Процентная ставка * Срок) / 100
    #Если прибыль > bonus_limit, добавляется бонус: 
    #Бонус = Прибыль * (bonus_procent / 100)
    def calculate_bonus(self) -> float:  
    profit = self.procent * self.period * self.summa / 100  
    if profit > self.bonus_limit:  
        profit += profit * (self.bonus_procent / 100)  
	    return profit
### 4. `Capital`

Класс для вклада с капитализацией процентов.

-   `capital (int)`: Количество периодов капитализации в год.
    
-   Метод `calculate_capital()`: Возвращает итоговую сумму с капитализацией по формуле:
    
    ```python
    #Итоговая сумма = Сумма * (1 + (Процентная ставка / (100 * капитализация)))^(капитализация * срок)
    def calculate_capital(self) -> float:  
	    return self.summa * (1 + self.procent / (100 * self.capital)) ** (self.capital * self.period)

## Пример использования

```python
import deposit

    summa = get_input("Введи сумму вклада: ")
    period = get_input("Введи срок вклада: ")
    if a == 1:
        sr = deposit.Srochniy(5, period, summa)
        print(f"Прибыль: {sr.calculate_srochiy()}")
    elif a == 2:
        srB = deposit.Bonus(5, period, summa, 10000, 3)
        print(f"Прибыль: {srB.calculate_bonus()}")
    elif a == 3:
        srC = deposit.Capital(5, period, summa, 12)
        print(f"Прибыль: {srC.calculate_capital()}")
    else:
        print("Неверный выбор вклада.")
```
## 4.3.4. Простой класс  
### Описание проекта
**10 Fraction обыкновенная дробь**

Перед тем как приступить к написанию кода:

-   изучите предметную область выбранного объекта и доступные для него операции;
    
-   для каждого поля и метода определите его область видимости и необходимость использования свойств.
    

Класс должен включать:

-   специальные методы:
    
    -   `__init__(self, ...)`  - инициализация с необходимыми параметрами;
        
    -   `__str__(self)`  - представление объекта в удобном для человека виде;
        
    -   специальные методы для поддержки операций, таких как сложение, вычитание и других, которые должен поддерживать класс;
        
-   методы класса:
    
    -   `from_string(cls, str_value)`  - создает объект на основе строки  `str_value`;
        
-   поля, методы и свойства:
    
    -   необходимые поля для выбранного класса;
        
    -   метод  `save(self, filename)`  - сохраняет объект в JSON-файл  `filename`;
        
    -   метод  `load(self, filename)`  - загружает объект из JSON-файла  `filename`;
        
    -   не менее трех дополнительных методов и свойств, определенных на этапе изучения класса.
        

Реализуйте класс в отдельном модуле и создайте файл  `main.py`  для тестирования всех его возможностей.

## Функциональность

### Основные возможности

-   Создание дробей с автоматическим сокращением.
    
-   Арифметические операции: сложение, вычитание, умножение, деление.
    
-   Преобразование в строку и в число с плавающей точкой.
    
-   Проверка правильности дроби.
    
-   Создание дроби из строки.
    
-   Сохранение дроби в JSON-файл и загрузка из него.
    

## Класс `Fraction`

```python
class Fraction:
```

### Атрибуты

-   `numerator (int)`: Числитель дроби.
    
-   `denominator (int)`: Знаменатель дроби (не может быть равен нулю).
    

### Методы

#### Конструктор

```python
Fraction(numerator: int, denominator: int)
```

Создает дробь и автоматически сокращает её.

#### Арифметические операции

```python
__add__(self, other: 'Fraction') -> 'Fraction'  # сложение
__sub__(self, other: 'Fraction') -> 'Fraction'  # вычитание
__mul__(self, other: 'Fraction') -> 'Fraction'  # умножение
__truediv__(self, other: 'Fraction') -> 'Fraction'  # деление
```

#### Преобразование и вывод

```python
__str__(self) -> str  # Преобразует дробь в строку "числитель/знаменатель"
to_float(self) -> float  # Преобразует дробь в число с плавающей точкой
is_proper(self) -> bool  # Проверяет, является ли дробь правильной
```

#### Создание дроби из строки

```python
from_string(cls, str_value: str) -> 'Fraction'
```

Создает объект `Fraction` из строки формата `"числитель/знаменатель"`.

#### Сохранение и загрузка дроби

```python
save(self, filename: str) -> None  # Сохраняет дробь в JSON-файл
load(cls, filename: str) -> 'Fraction'  # Загружает дробь из JSON-файла
```

## Установка и использование

### Установка

Для работы требуется Python 3.6+.

### Использование

```python
from fraction import Fraction

def main() -> None:
    """
    Основная функция для тестирования класса Fraction.
    Создает объекты Fraction, выполняет операции с ними и сохраняет/загружает их в/из файла.
    """
    # Создание объектов Fraction
    frac1: Fraction = Fraction(3, 4)
    frac2: Fraction = Fraction.from_string("2/5")

    # Вывод дробей
    print(f"Дробь 1: {frac1}")
    print(f"Дробь 2: {frac2}")

    # Операции с дробями
    print(f"Сумма: {frac1 + frac2}")
    print(f"Разность: {frac1 - frac2}")
    print(f"Произведение: {frac1 * frac2}")
    print(f"Деление: {frac1 / frac2}")

    # Преобразование в float
    print(f"Дробь 1 как float: {frac1.to_float()}")

    # Проверка, является ли дробь правильной
    print(f"Дробь 1 правильная? {frac1.is_proper()}")

    # Сохранение и загрузка из файла
    frac1.save("frac1.json")
    loaded_frac: Fraction = Fraction.load("frac1.json")
    print(f"Загруженная дробь: {loaded_frac}")

if __name__ == "__main__":
    main()
```

# Лабораторная работа week_05
## **4.3.5. Класс-контейнер**
### Описание проекта


Создайте класс-контейнер, который будет содержать набор объектов из предыдущей задачи. Например, класс VectorCollection будет содержать объекты класса Vector.

Для класса-контейнера предусмотрите:

-   специальные методы:
    
    -   `__init__(self, ...)`  - инициализация с необходимыми параметрами;
        
    -   `__str__(self)`  - представление объекта в удобном для человека виде;
        
    -   `__getitem__()`  - индексация и срез для класса-контейнера.
        
-   поля, методы, свойства:
    
    -   `_data`  - содержит набор данных;
        
    -   метод  `add(self, value)`  - добавляет элемент value в контейнер;
        
    -   метод  `remove(self, index)`  - удаляет элемент из контейнера по индексу index;
        
    -   метод  `save(self, filename)`  - сохраняет объект в JSON-файл filename;
        
    -   метод  `load(self, filename)`  - загружает объект из JSON-файла filename.
        

При выполнении задания необходимо построить UML-диаграмму классов приложения.


## Классы и методы

### Класс `FractionCollection`

Класс предназначен для хранения и управления коллекцией дробей. Внутренне использует список `_data` для хранения объектов `Fraction`. Конструктор класса, инициализирует пустую коллекцию дробей.
```python
class FractionCollection:  
  def __init__(self) -> None:  
	self._data: list[Fraction] = []
 ```


----------

### Получение строкового представления коллекции дробей
```python
def __str__(self) -> str:  
	return ', '.join(str(f) for f in self._data)
```
----------

### Метод для получения дроби по индексу
```python
def __getitem__(self, index: int) -> Fraction:  
	return self._data[index]
 ```

Позволяет получить дробь по индексу.

#### Параметры:

-   `index (int)`: Индекс дроби в коллекции.
    

#### Возвращает:

-   `Fraction`: Дробь по указанному индексу.
    

#### Исключения:

-   `IndexError`: Если индекс выходит за границы списка.
    

----------

### Метод добавления дробей в коллекцию
```python
def add(self, value: Fraction) -> None:  
	if isinstance(value, Fraction):  
        self._data.append(value)  
    else:  
        raise ValueError("Можно добавлять только объекты Fraction")
```

#### Параметры:

-   `value (Fraction)`: Дробь, которая будет добавлена в коллекцию.
    

#### Исключения:

-   `ValueError`: Если переданный аргумент не является объектом `Fraction`.
    

----------

### Метод для удаления дробей по индексу
```python
def remove(self, index: int) -> None:  
	if 0 <= index < len(self._data):  
        del self._data[index]  
    else:  
        raise IndexError("Некорректный индекс")
```
#### Параметры:

-   `index (int)`: Индекс удаляемой дроби.
    

#### Исключения:

-   `IndexError`: Если индекс выходит за границы списка.
    

----------
### Метод для сохранения коллекции в JSON-файл
```python
def save(self, filename: str) -> None:  
	with open(filename, 'w') as file:  
        json.dump([str(f) for f in self._data], file)
```
Сохраняет коллекцию дробей в JSON-файл. Дроби сохраняются в виде строковых представлений.
#### Параметры:

-   `filename (str)`: Имя файла для сохранения данных.

#### Исключения:

-   `OSError`: Если произошла ошибка при записи в файл.

----------

### Метод для загрузки коллекции из JSON-файла
```python
def load(self, filename: str) -> None:  
	with open(filename, 'r') as file:  
        data = json.load(file)  
        self._data = [Fraction(f) for f in data]
```
Загружает коллекцию дробей из JSON-файла. Читает строковые представления дробей и преобразует их обратно в `Fraction`.

#### Параметры:

-   `filename (str)`: Имя файла для загрузки данных.
    

#### Исключения:

-   `OSError`: Если произошла ошибка при чтении файла.
    
-   `ValueError`: Если данные в файле некорректны и не могут быть преобразованы в `Fraction`.

## **4.3.6. Иерархия классов**
### Описание проекта
Выберите класс под номером № (см. Таблицу 2), где № — это ваш порядковый номер в журнале. Если порядковый номер превышает количество доступных классов, отсчет продолжается с начала по кругу.
-   Постройте классы в иерархию, продумайте их общие и отличительные характеристики и действия.
-   Добавьте собственную реализацию методов базового класса в каждый из классов, предусмотрев:
    -   необходимые параметры для базовых методов (например, в метод воспроизведения в DVD-плеере можно передать абстрактный DVD-диск);
    -   необходимые поля для функционирования базовых методов (например, при остановке DVD-плеера имеет смысл сохранить текущую позицию воспроизведения); классы должны содержать как минимум по одному общедоступному, не общедоступному и закрытому полю/методу;
    -   вывод на экран работы метода (например, вызов метода остановки в DVD-плеере должен сообщать на экране, что плеер установлен на определенной позиции).
-   По желанию добавьте собственные методы в классы иерархии.

Реализуйте все классы в отдельном модуле, а также создайте `main.py`, который бы тестировал все его возможности.

По согласованию иерархия может быть расширена или выбрана самостоятельная индивидуальная тема для данной задачи.

При выполнении задания необходимо построить UML-диаграмму классов приложения.
**Вариант №5***
## Классы и методы

### Класс `TravelTicket`

Класс предназначен для представления билета на поездку.

#### Поля:

-   `ticket_id (str)`: Уникальный идентификатор билета.
    
-   `_rides_used (int)`: Количество использованных поездок (защищенное поле).
    
-   `__is_active (bool)`: Статус активности билета (приватное поле).
    

### Метод для использования поездки

Метод должен быть переопределен в подклассах.

#### Исключения:

-   `NotImplementedError`: Если метод вызывается без переопределения.
    

### Метод увеличения количества поездок

Защищенный метод, увеличивает счетчик поездок.

### Метод деактивации билета

Приватный метод, делает билет неактивным.

### Метод получения информации о билете

Возвращает информацию о билете в виде строки.

----------

### Класс `UnlimitedTicket`

Класс безлимитного билета, наследуется от `TravelTicket`.

Метод `use_ride()` увеличивает количество поездок без ограничений.

----------

### Класс `LimitedTicket`

Класс билета с ограниченным числом поездок.

#### Поля:

-   `max_rides (int)`: Максимальное количество поездок.
    

### Метод использования поездки

Метод `use_ride()` позволяет использовать поездку, если не достигнуто ограничение.

----------

### Класс `LimitedRideTicket`

Класс билета с ограничением на количество поездок, который деактивируется при достижении лимита.

### Метод использования поездки

Метод `use_ride()` увеличивает счетчик поездок, но деактивирует билет, если лимит достигнут.

----------

### Класс `TicketCollection`

Класс-контейнер для хранения объектов `TravelTicket` и его подклассов.

Класс позволяет добавлять, удалять билеты, сохранять их в файл и загружать обратно.
# Snake Game

## Описание

Этот проект представляет собой классическую игру "Змейка" на Python, созданную с использованием библиотеки Pygame. Игрок управляет змейкой, которая должна поедать яблоки, увеличиваясь в длине. Игра заканчивается, если змейка врезается в себя.

## Управление

-   **Стрелка вверх (↑)** – движение вверх
    
-   **Стрелка вниз (↓)** – движение вниз
    
-   **Стрелка влево (←)** – движение влево
    
-   **Стрелка вправо (→)** – движение вправо
    
-   **Закрытие окна** – выход из игры
    

## Разбор кода

### 1. Константы

В начале кода задаются основные параметры игры, включая размеры экрана, размеры сетки, цвета и скорость игры:

```python
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

BOARD_BACKGROUND_COLOR = (0, 0, 0)
BORDER_COLOR = (93, 216, 228)
APPLE_COLOR = (255, 0, 0)
SNAKE_COLOR = (0, 255, 0)

SPEED = 20

```

### 2. Базовый класс GameObject

Все игровые объекты (например, яблоко и змейка) наследуются от `GameObject`. Этот класс хранит позицию и цвет объекта:

```python
class GameObject:
    def __init__(self, position=None, body_color=None):
        self.position = position if position else (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.body_color = body_color

    def draw(self):
        pass

```

### 3. Класс Apple (Яблоко)

Этот класс отвечает за создание и случайное расположение яблока на игровом поле:

```python
class Apple(GameObject):
    def __init__(self):
        super().__init__(body_color=APPLE_COLOR)
        self.randomize_position()

    def randomize_position(self):
        self.position = (
            randint(0, GRID_WIDTH - 1) * GRID_SIZE,
            randint(0, GRID_HEIGHT - 1) * GRID_SIZE
        )

    def draw(self):
        rect = pygame.Rect(self.position, (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, rect)
        pygame.draw.rect(screen, BORDER_COLOR, rect, 1)

```

### 4. Класс Snake (Змейка)

Змейка управляется игроком, увеличивается при съедании яблок и проверяет столкновения:

```python
class Snake(GameObject):
    def __init__(self):
        super().__init__(body_color=SNAKE_COLOR)
        self.reset()

    def reset(self):
        self.length = 1
        self.positions = [self.position]
        self.direction = RIGHT
        self.next_direction = None

    def update_direction(self):
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None

    def move(self):
        head = self.get_head_position()
        x, y = self.direction
        new_position = (
            (head[0] + (x * GRID_SIZE)) % SCREEN_WIDTH,
            (head[1] + (y * GRID_SIZE)) % SCREEN_HEIGHT
        )

        if len(self.positions) > self.length - 1:
            self.positions.pop()

        self.positions.insert(0, new_position)

    def get_head_position(self):
        return self.positions[0]

    def draw(self):
        for position in self.positions:
            rect = pygame.Rect(position, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, self.body_color, rect)
            pygame.draw.rect(screen, BORDER_COLOR, rect, 1)

```

### 5. Обработка ввода с клавиатуры

Функция `handle_keys(snake)` следит за нажатыми клавишами и меняет направление движения змейки:

```python
def handle_keys(snake):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction != DOWN:
                snake.next_direction = UP
            elif event.key == pygame.K_DOWN and snake.direction != UP:
                snake.next_direction = DOWN
            elif event.key == pygame.K_LEFT and snake.direction != RIGHT:
                snake.next_direction = LEFT
            elif event.key == pygame.K_RIGHT and snake.direction != LEFT:
                snake.next_direction = RIGHT
    return True

```

### 6. Основной игровой цикл

Функция `main()` управляет всеми процессами игры: движением змейки, проверкой столкновений и отрисовкой экрана:

```python
def main():
    pygame.init()
    global screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Змейка')
    clock = pygame.time.Clock()

    snake = Snake()
    apple = Apple()

    running = True
    while running:
        clock.tick(SPEED)

        running = handle_keys(snake)

        snake.update_direction()
        snake.move()

        if snake.get_head_position() == apple.position:
            snake.length += 1
            apple.randomize_position()
            while apple.position in snake.positions:
                apple.randomize_position()

        if snake.get_head_position() in snake.positions[1:]:
            snake.reset()

        screen.fill(BOARD_BACKGROUND_COLOR)
        snake.draw()
        apple.draw()
        pygame.display.update()

    pygame.quit()

```

### 7. Запуск игры

Если этот файл запускается как основная программа, то выполняется функция `main()`:

```python
if __name__ == '__main__':
    main()

```

