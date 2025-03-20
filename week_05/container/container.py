import json
from fractions import Fraction


class FractionCollection:
    """
    Класс для хранения и управления коллекцией дробей.
    """

    def __init__(self) -> None:
        """
        Инициализирует пустую коллекцию дробей.
        """
        self._data: list[Fraction] = []

    def __str__(self) -> str:
        """
        Возвращает строковое представление коллекции дробей.
        """
        return ', '.join(str(f) for f in self._data)

    def __getitem__(self, index: int) -> Fraction:
        """
        Позволяет получить дробь по индексу.

        :param index: Индекс дроби в коллекции
        :return: Дробь (Fraction) по указанному индексу
        """
        return self._data[index]

    def add(self, value: Fraction) -> None:
        """
        Добавляет дробь в коллекцию.

        :param value: Дробь (Fraction), которая будет добавлена
        :raises ValueError: Если передано не Fraction
        """
        if isinstance(value, Fraction):
            self._data.append(value)
        else:
            raise ValueError("Можно добавлять только объекты Fraction")

    def remove(self, index: int) -> None:
        """
        Удаляет дробь по индексу.

        :param index: Индекс удаляемой дроби
        :raises IndexError: Если индекс выходит за границы списка
        """
        if 0 <= index < len(self._data):
            del self._data[index]
        else:
            raise IndexError("Некорректный индекс")

    def save(self, filename: str) -> None:
        """
        Сохраняет коллекцию дробей в JSON-файл.

        :param filename: Имя файла для сохранения данных
        """
        with open(filename, 'w') as file:
            json.dump([str(f) for f in self._data], file)

    def load(self, filename: str) -> None:
        """
        Загружает коллекцию дробей из JSON-файла.

        :param filename: Имя файла для загрузки данных
        """
        with open(filename, 'r') as file:
            data = json.load(file)
            self._data = [Fraction(f) for f in data]


# Пример использования
if __name__ == "__main__":
    fc = FractionCollection()
    fc.add(Fraction(1, 2))
    fc.add(Fraction(3, 4))
    fc.add(Fraction(5, 6))

    print("Коллекция дробей:", fc)

    fc.save("fractions.json")
    fc.load("fractions.json")

    print("Загруженная коллекция:", fc)