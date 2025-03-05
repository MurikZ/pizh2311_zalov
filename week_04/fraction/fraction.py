import json
from math import gcd

class Fraction:
    """
    Класс для работы с обыкновенными дробями.

    Атрибуты:
        numerator (int): Числитель дроби.
        denominator (int): Знаменатель дроби.
    """

    def __init__(self, numerator: int, denominator: int) -> None:
        """
        Инициализирует объект дроби.

        Аргументы:
            numerator (int): Числитель дроби.
            denominator (int): Знаменатель дроби.

        Исключения:
            ValueError: Если знаменатель равен нулю.
        """
        if denominator == 0:
            raise ValueError("Знаменатель не может быть равен нулю.")
        common_divisor = gcd(numerator, denominator)
        self.numerator = numerator // common_divisor
        self.denominator = denominator // common_divisor

    def __str__(self) -> str:
        """
        Возвращает строковое представление дроби.

        Возвращает:
            str: Строка в формате "числитель/знаменатель".
        """
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other: 'Fraction') -> 'Fraction':
        """
        Складывает две дроби.

        Аргументы:
            other (Fraction): Другая дробь.

        Возвращает:
            Fraction: Новая дробь, результат сложения.
        """
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other: 'Fraction') -> 'Fraction':
        """
        Вычитает одну дробь из другой.

        Аргументы:
            other (Fraction): Другая дробь.

        Возвращает:
            Fraction: Новая дробь, результат вычитания.
        """
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other: 'Fraction') -> 'Fraction':
        """
        Умножает две дроби.

        Аргументы:
            other (Fraction): Другая дробь.

        Возвращает:
            Fraction: Новая дробь, результат умножения.
        """
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other: 'Fraction') -> 'Fraction':
        """
        Делит одну дробь на другую.

        Аргументы:
            other (Fraction): Другая дробь.

        Возвращает:
            Fraction: Новая дробь, результат деления.

        Исключения:
            ValueError: Если знаменатель результата равен нулю.
        """
        if other.numerator == 0:
            raise ValueError("Деление на ноль невозможно.")
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    @classmethod
    def from_string(cls, str_value: str) -> 'Fraction':
        """
        Создает объект Fraction из строки.

        Аргументы:
            str_value (str): Строка в формате "числитель/знаменатель".

        Возвращает:
            Fraction: Объект Fraction.

        Исключения:
            ValueError: Если строка имеет неправильный формат.
        """
        try:
            numerator, denominator = map(int, str_value.split('/'))
            return cls(numerator, denominator)
        except (ValueError, IndexError):
            raise ValueError("Строка должна быть в формате 'числитель/знаменатель'.")

    def save(self, filename: str) -> None:
        """
        Сохраняет объект Fraction в JSON-файл.

        Аргументы:
            filename (str): Имя файла для сохранения.
        """
        with open(filename, 'w') as file:
            json.dump({"numerator": self.numerator, "denominator": self.denominator}, file)

    @classmethod
    def load(cls, filename: str) -> 'Fraction':
        """
        Загружает объект Fraction из JSON-файла.

        Аргументы:
            filename (str): Имя файла для загрузки.

        Возвращает:
            Fraction: Объект Fraction.
        """
        with open(filename, 'r') as file:
            data = json.load(file)
            return cls(data["numerator"], data["denominator"])

    def to_float(self) -> float:
        """
        Преобразует дробь в число с плавающей точкой.

        Возвращает:
            float: Значение дроби как число с плавающей точкой.
        """
        return self.numerator / self.denominator

    def is_proper(self) -> bool:
        """
        Проверяет, является ли дробь правильной.

        Возвращает:
            bool: True, если дробь правильная, иначе False.
        """
        return abs(self.numerator) < abs(self.denominator)