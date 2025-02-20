class AirCastle:
    def __init__(self, height, n_clouds, color):
        """
        Инициализация замка с заданной высотой, количеством облаков и цветом.

        :param height: Высота замка (в метрах).
        :param n_clouds: Количество облаков вокруг замка.
        :param color: Цвет замка.
        """
        self.height = height
        self.n_clouds = n_clouds
        self.color = color

    def change_height(self, value):
        """
        Изменяет высоту замка, если значение больше или равно 0.

        :param value: Новое значение высоты.
        """
        if value >= 0:
            self.height = value

    def sum(self, n):
        """
        Увеличивает количество облаков и соответственно высоту замка.

        :param n: Количество облаков, на которое увеличивается число.
        """
        self.n_clouds += n
        self.height += n // 5

    def __call__(self, transparency):
        """
        Возвращает результат вычислений, связанный с прозрачностью.

        :param transparency: Прозрачность, с которой связано вычисление.
        :return: Результат (высота / прозрачность) * количество облаков.
        """
        return self.height // transparency * self.n_clouds

    def __str__(self):
        """
        Возвращает строковое представление замка.

        :return: Описание замка (высота, цвет, количество облаков).
        """
        return f"The AirCastle at an altitude of {self.height} meters is {self.color} with {self.n_clouds} clouds"

    def __eq__(self, other):
        """
        Проверяет равенство двух замков по высоте, цвету и количеству облаков.

        :param other: Другой объект для сравнения.
        :return: True, если замки одинаковые, иначе False.
        """
        return (self.n_clouds, self.height, self.color) == (other.n_clouds, other.height, other.color)

    def __lt__(self, other):
        """
        Проверяет, меньше ли текущий замок другого по количеству облаков, высоте и цвету.

        :param other: Другой объект для сравнения.
        :return: True, если текущий замок меньше, иначе False.
        """
        return (self.n_clouds, self.height, self.color) < (other.n_clouds, other.height, other.color)

    def __le__(self, other):
        """
        Проверяет, меньше или равно ли текущее состояние замка состоянию другого замка.

        :param other: Другой объект для сравнения.
        :return: True, если текущий замок меньше или равен другому, иначе False.
        """
        return (self.n_clouds, self.height, self.color) <= (other.n_clouds, other.height, other.color)

    def __gt__(self, other):
        """
        Проверяет, больше ли текущий замок другого по количеству облаков, высоте и цвету.

        :param other: Другой объект для сравнения.
        :return: True, если текущий замок больше, иначе False.
        """
        return (self.n_clouds, self.height, self.color) > (other.n_clouds, other.height, other.color)

    def __ge__(self, other):
        """
        Проверяет, больше или равно ли текущее состояние замка состоянию другого замка.

        :param other: Другой объект для сравнения.
        :return: True, если текущий замок больше или равен другому, иначе False.
        """
        return (self.n_clouds, self.height, self.color) >= (other.n_clouds, other.height, other.color)

    def __ne__(self, other):
        """
        Проверяет, не равен ли текущий замок другому.

        :param other: Другой объект для сравнения.
        :return: True, если замки не равны, иначе False.
        """
        return (self.n_clouds, self.height, self.color) != (other.n_clouds, other.height, other.color)


class MagicAirCastle(AirCastle):
    def __init__(self, height, n_clouds, color, magic_power):
        """
        Инициализация волшебного замка с магической силой.

        :param height: Высота замка (в метрах).
        :param n_clouds: Количество облаков вокруг замка.
        :param color: Цвет замка.
        :param magic_power: Магическая сила замка.
        """
        AirCastle.__init__(self, height, n_clouds, color)  # Явный вызов конструктора родительского класса
        self.magic_power = magic_power

    def cast_spell(self):
        """
        Произносит заклинание с магической силой замка.

        :return: Строка с описанием магической силы.
        """
        return f"магическая мощь {self.magic_power}!"


# Композиция
class Cloud:
    def __init__(self, size):
        """
        Инициализация облака с заданным размером.

        :param size: Размер облака.
        """
        self.size = size

    def __str__(self):
        """
        Возвращает строковое представление облака.

        :return: Описание облака с его размером.
        """
        return f"количество облаков {self.size}"


class AirCastleWithClouds:
    def __init__(self, height, clouds, color):
        """
        Инициализация замка с облаками.

        :param height: Высота замка (в метрах).
        :param clouds: Список с размерами облаков.
        :param color: Цвет замка.
        """
        self.height = height
        self.clouds = [Cloud(size) for size in clouds]
        self.color = color

    def __str__(self):
        """
        Возвращает строковое представление замка с облаками.

        :return: Описание замка с облаками.
        """
        clouds_info = ", ".join(str(cloud) for cloud in self.clouds)
        return f"The AirCastle at an altitude of {self.height} meters is {self.color} with clouds: {clouds_info}"


# Использование
num1 = AirCastle(23, 3, "green")
num1.change_height(3)
num2 = AirCastle(13, 4, "red")

print(f"num2 >= num1 = {num2 >= num1}")
print(f"Прозрачность: {num1(2)}")
print(num1)

"""вывод:
num2 >= num1 = True
Прозрачность: 3
The AirCastle at an altitude of 3 meters is green with 3 clouds"""
