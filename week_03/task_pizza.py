class Pizza:
    """
    Базовый класс для представления пиццы.
    """

    def __init__(self, name, testo, sauce, nachinka, price) -> None:
        """
        Инициализация пиццы.
        :param name: Название пиццы
        :param testo: Тип теста
        :param sauce: Соус
        :param nachinka: Начинка (список ингредиентов)
        :param price: Цена
        """
        self.name = name
        self.testo = testo
        self.sauce = sauce
        self.nachinka = nachinka
        self.price = price

    def __str__(self) -> str:
        """Возвращает строковое представление пиццы."""
        return f"{self.name}, тесто: {self.testo}, соус: {self.sauce}, начинка: {', '.join(self.nachinka)}, цена: {self.price} руб."

    def prepare(self) -> str:
        """Этап подготовки пиццы."""
        return f"Подготавливаем {self.name}..."

    def cook(self) -> str:
        """Этап выпекания пиццы."""
        return f"Испекаем пиццу с {self.testo} тестом..."

    def slice(self) -> str:
        """Этап нарезки пиццы."""
        return f"Режем {self.name} на порции..."

    def packet(self) -> str:
        """Этап упаковки пиццы."""
        return f"Упаковываем {self.name} в коробку..."


class Pizza_barbeku(Pizza):
    """Класс пиццы Барбекю."""

    def __init__(self) -> None:
        super().__init__("Пицца Барбекю", "обычное", "барбекю", ["курица", "колбаски", "помидор"], 500)


class Pizza_pepperoni(Pizza):
    """Класс пиццы Пепперони."""

    def __init__(self) -> None:
        super().__init__("Пепперони", "обычное", "томатный", ["пепперони", "помидоры", "сыр"], 550)


class Pizza_sea(Pizza):
    """Класс пиццы Дары моря."""

    def __init__(self) -> None:
        super().__init__("Дары моря", "обычное", "томатный", ["морепродукты", "помидоры", "сыр"], 400)


class Order:
    """
    Класс заказа, содержащий список пицц.
    """

    def __init__(self) -> None:
        """Инициализация заказа."""
        self.list_of_orders = []

    def __str__(self) -> str:
        """Возвращает строковое представление заказа."""
        return f"Заказ: {len(self.list_of_orders)} пицц, общая стоимость: {self.price()} руб."

    def add_pizza(self, pizza) -> None:
        """Добавляет пиццу в заказ."""
        self.list_of_orders.append(pizza)

    def price(self) -> int:
        """Возвращает общую стоимость заказа."""
        return sum(pizza.price for pizza in self.list_of_orders)

    def process_order(self) -> str:
        """
        Обрабатывает заказ, включая этапы приготовления, выпекания, нарезки и упаковки.
        :return: Строка с описанием процесса выполнения заказа.
        """
        process_steps = []
        for pizza in self.list_of_orders:
            process_steps.append(str(pizza))
            process_steps.append(pizza.prepare())
            process_steps.append(pizza.cook())
            process_steps.append(pizza.slice())
            process_steps.append(pizza.packet())
            process_steps.append("-" * 40)  # Разделитель между пиццами
        return "\n".join(process_steps)


# Меню
order = Order()
print("------------------Меню------------------")
print(Pizza_pepperoni())
print(Pizza_sea())
print(Pizza_barbeku())

# Оформление заказа
while True:
    zakaz = int(input("Введите заказ\n1-Пепперони\n2-Барбекю\n3-Дары моря\n0-Завершить заказ\n"))

    if zakaz == 1:
        order.add_pizza(Pizza_pepperoni())
    elif zakaz == 2:
        order.add_pizza(Pizza_barbeku())
    elif zakaz == 3:
        order.add_pizza(Pizza_sea())
    elif zakaz == 0:
        break
    else:
        print("Некорректный ввод, попробуйте снова.")

# Вывод заказа и процесса приготовления
print("\nВаш заказ оформлен!")
print(order)
print("\nПроцесс приготовления:\n")
print(order.process_order())
