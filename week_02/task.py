class AirCastle:
    """
    Класс, представляющий воздушный замок.
    """

    def __init__(self, height: int, n_clouds: int, color: str) -> None:
        """
        Создает объект воздушного замка.

        :param height: Высота замка в метрах.
        :param n_clouds: Количество облаков вокруг замка.
        :param color: Цвет замка.
        """
        self._height = height  # Используем инкапсуляцию
        self.n_clouds = n_clouds
        self.color = color

    @property
    def height(self) -> int:
        """Геттер для высоты замка."""
        return self._height

    @height.setter
    def height(self, value: int) -> None:
        """Сеттер для высоты, проверяющий корректность значения."""
        if value >= 0:
            self._height = value
        else:
            raise ValueError("Высота не может быть отрицательной.")

    def change_height(self, value: int) -> None:
        """
        Изменяет высоту замка, если переданное значение корректно.

        :param value: Новое значение высоты.
        """
        self.height = value

    def sum(self, n: int) -> None:
        """
        Увеличивает количество облаков и при необходимости высоту замка.

        :param n: Количество добавляемых облаков.
        """
        self.n_clouds += n
        self.height += n // 5

    def __call__(self, transparency: int) -> int:
        """
        Вычисляет некоторый параметр, зависящий от прозрачности.

        :param transparency: Коэффициент прозрачности.
        :return: Вычисленное значение.
        """
        return self.height // transparency * self.n_clouds

    def __str__(self) -> str:
        """
        Возвращает текстовое представление замка.
        """
        return f"The AirCastle at {self.height} meters is {self.color} with {self.n_clouds} clouds"

    def __eq__(self, other) -> bool:
        return (self.n_clouds, self.height, self.color) == (other.n_clouds, other.height, other.color)

    def __lt__(self, other) -> bool:
        return (self.n_clouds, self.height, self.color) < (other.n_clouds, other.height, other.color)

    def __le__(self, other) -> bool:
        return (self.n_clouds, self.height, self.color) <= (other.n_clouds, other.height, other.color)

    def __gt__(self, other) -> bool:
        return (self.n_clouds, self.height, self.color) > (other.n_clouds, other.height, other.color)

    def __ge__(self, other) -> bool:
        return (self.n_clouds, self.height, self.color) >= (other.n_clouds, other.height, other.color)

    def __ne__(self, other) -> bool:
        return (self.n_clouds, self.height, self.color) != (other.n_clouds, other.height, other.color)


class MagicAirCastle(AirCastle):
    """
    Класс, представляющий волшебный воздушный замок.
    """

    def __init__(self, height: int, n_clouds: int, color: str, magic_power: int) -> None:
        """
        Создает объект волшебного замка.

        :param height: Высота замка в метрах.
        :param n_clouds: Количество облаков вокруг замка.
        :param color: Цвет замка.
        :param magic_power: Магическая сила.
        """
        super().__init__(height, n_clouds, color)
        self.magic_power = magic_power

    def cast_spell(self) -> str:
        """
        Возвращает строку с описанием магической силы замка.
        """
        return f"магическая мощь {self.magic_power}!"


class Cloud:
    """
    Класс, представляющий облако.
    """

    def __init__(self, size: int) -> None:
        """
        Создает объект облака.

        :param size: Размер облака.
        """
        self.size = size

    def __str__(self) -> str:
        """
        Возвращает текстовое представление облака.
        """
        return f"количество облаков {self.size}"


class AirCastleWithClouds:
    """
    Класс, представляющий воздушный замок с облаками (композиция).
    """

    def __init__(self, height: int, clouds: list, color: str) -> None:
        """
        Создает объект замка с облаками.

        :param height: Высота замка в метрах.
        :param clouds: Список размеров облаков.
        :param color: Цвет замка.
        """
        self.height = height
        self.clouds = [Cloud(size) for size in clouds]
        self.color = color

    def __str__(self) -> str:
        """
        Возвращает текстовое представление замка с облаками.
        """
        clouds_info = ", ".join(str(cloud) for cloud in self.clouds)
        return f"The AirCastle at {self.height} meters is {self.color} with clouds: {clouds_info}"


# Тестирование классов
num1 = AirCastle(23, 3, "green")
num1.change_height(3)
num2 = AirCastle(13, 4, "red")

print(f"num2 >= num1 = {num2 >= num1}")
print(f"Прозрачность: {num1(2)}")
print(num1)
