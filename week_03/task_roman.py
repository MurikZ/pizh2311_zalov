class Roman:
    """
    Класс для работы с римскими числами и арифметическими операциями.
    """

    def __init__(self, arg_plus, arg_minus, arg_umn, arg_del, roman_numbers) -> None:
        """
        Инициализирует объект класса Roman.

        :param arg_plus: Число для операции сложения
        :param arg_minus: Число для операции вычитания
        :param arg_umn: Число для операции умножения
        :param arg_del: Число для операции деления
        :param roman_numbers: Словарь соответствия римских цифр и их значений
        """
        self.arg_plus = arg_plus
        self.arg_minus = arg_minus
        self.arg_umn = arg_umn
        self.arg_del = arg_del
        self.roman_numbers = roman_numbers

    def roma(self, number) -> str:
        """
        Преобразует арабское число в римское.

        :param number: Целое число, которое нужно преобразовать
        :return: Строка с римским представлением числа
        """
        num = ''
        for key, value in self.roman_numbers.items():
            while number >= value:
                num += key
                number -= value
        return num

    def __add__(self, other) -> int:
        """
        Операция сложения.

        :param other: Второй операнд (число)
        :return: Сумма self.arg_plus и other
        """
        return self.arg_plus + other

    def __sub__(self, other) -> int:
        """
        Операция вычитания.

        :param other: Второй операнд (число)
        :return: Разность self.arg_minus и other
        """
        return self.arg_minus - other

    def __mul__(self, other) -> int:
        """
        Операция умножения.

        :param other: Второй операнд (число)
        :return: Произведение self.arg_umn и other
        """
        return self.arg_umn * other

    def __truediv__(self, other) -> float:
        """
        Операция деления.

        :param other: Второй операнд (число)
        :return: Частное от деления self.arg_del на other
        """
        return self.arg_del / other


# Создание экземпляра класса Roman
roman = Roman(3, 5, 4, 5, {
    'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
    'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
    'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1
})

# Выполнение арифметических операций
plus = roman.__add__(4)
minus = roman.__sub__(4)
umnozhit = roman.__mul__(4)
razdelit = roman.__truediv__(4)

# Вывод результатов в римской системе
print(roman.roma(plus))
print(roman.roma(minus))
print(roman.roma(umnozhit))
print(roman.roma(int(razdelit)))  # Преобразуем результат деления в int, чтобы избежать ошибок
