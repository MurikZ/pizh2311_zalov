class Pizza:
    def __init__(self,name,testo,sauce,nachinka,price)->None:
        self.name = name
        self.testo = testo
        self.sauce = sauce
        self.nachinka = nachinka
        self.price = price
    def __str__(self)->str:
        return f"{self.name}, тесто: {self.testo}, соус: {self.sauce}, начинка: {', '.join(self.nachinka)}, цена: {self.price} руб."
    def prepare(self)->str:
        return f"подготавливаем {self.name}"
    def cook(self)->str:
        return f"испекаем{self.testo}"
    def slice(self)->str:
        return f"режем{self.name}"
    def packet(self)->str:
        return f"упаковываем {self.name}"

class Pizza_barbeku(Pizza):
    def __init__(self)->None:
        super().__init__("ПиццаБарбекю","обычное","барбекю",["курица,колбаски,помидор"],500)
class Pizza_pepperoni(Pizza):
    def __init__(self)->None:
        super().__init__("Пепперони","обычное", "томатный",["пепперони","помидоры","сыр"],550)
class Pizza_sea(Pizza):
    def __init__(self)->None:
        super().__init__("Дары моря","обычное", "томатный",["морепродукты","помидоры","сыр"],400)
class Order:
    def __init__(self)->None:
        self.list_of_orders = []
        self.count_of_orders = 0

    def __str__(self)->str:
        return f"Заказ: {len(self.list_of_orders)} пицц, общая стоимость: {self.price()} руб."
    def add_pizza(self,pizza)->None:
        self.list_of_orders.append(pizza)
        self.count_of_orders += 1
    def price(self)->int:
        return sum(pizza.price for pizza in self.list_of_orders)
order = Order()

# Добавляем пиццы в заказ
order.add_pizza(Pizza_pepperoni())
order.add_pizza(Pizza_barbeku())
pep = Pizza_pepperoni()
print(pep.__str__())


# Выводим информацию о заказе
print(order)