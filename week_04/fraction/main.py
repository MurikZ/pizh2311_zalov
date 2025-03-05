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