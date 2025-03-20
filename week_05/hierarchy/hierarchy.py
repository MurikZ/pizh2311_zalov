class TravelTicket:
    """
    Базовый класс для билетов на поездки.
    """

    def __init__(self, ticket_id: str) -> None:
        """
        Инициализирует билет с уникальным идентификатором.

        :param ticket_id: Уникальный идентификатор билета
        """
        self.ticket_id: str = ticket_id  # ID билета
        self._rides_used: int = 0  # защищенное поле: количество использованных поездок
        self.__is_active: bool = True  # приватное поле: активен ли билет

    def use_ride(self) -> None:
        """
        Метод использования поездки. Должен быть переопределен в подклассах.

        :raises NotImplementedError: если метод не переопределен
        """
        raise NotImplementedError("Этот метод должен быть переопределен в подклассе")

    def _increment_rides_used(self) -> None:
        """
        Защищенный метод для увеличения счетчика поездок.
        """
        self._rides_used += 1

    def __deactivate_ticket(self) -> None:
        """
        Приватный метод для деактивации билета.
        """
        self.__is_active = False

    def get_info(self) -> str:
        """
        Возвращает информацию о билете.

        :return: Строка с информацией о билете
        """
        return f"Билет ID: {self.ticket_id}, Поездок использовано: {self._rides_used}, Активен: {self.__is_active}"


class UnlimitedTicket(TravelTicket):
    """
    Класс безлимитного билета.
    """

    def use_ride(self) -> None:
        """
        Использует поездку без ограничений.
        """
        self._increment_rides_used()
        print(f"Безлимитный билет {self.ticket_id} использован. Всего поездок: {self._rides_used}")


class LimitedTicket(TravelTicket):
    """
    Класс билета с ограниченным числом поездок.
    """

    def __init__(self, ticket_id: str, max_rides: int) -> None:
        """
        Инициализирует билет с ограниченным числом поездок.

        :param ticket_id: Уникальный идентификатор билета
        :param max_rides: Максимальное количество поездок
        """
        super().__init__(ticket_id)
        self.max_rides: int = max_rides

    def use_ride(self) -> None:
        """
        Использует поездку, если не превышено ограничение.
        """
        if self._rides_used < self.max_rides:
            self._increment_rides_used()
            print(
                f"Билет с ограничением {self.ticket_id} использован. Поездок использовано: {self._rides_used}/{self.max_rides}")
        else:
            print(f"Билет с ограничением {self.ticket_id} достиг максимального количества поездок.")


class LimitedRideTicket(TravelTicket):
    """
    Класс билета с ограничением на количество поездок, который деактивируется при достижении лимита.
    """

    def __init__(self, ticket_id: str, max_rides: int) -> None:
        """
        Инициализирует билет с ограниченным числом поездок, который деактивируется при исчерпании поездок.

        :param ticket_id: Уникальный идентификатор билета
        :param max_rides: Максимальное количество поездок
        """
        super().__init__(ticket_id)
        self.max_rides: int = max_rides

    def use_ride(self) -> None:
        """
        Использует поездку, если не превышено ограничение, иначе деактивирует билет.
        """
        if self._rides_used < self.max_rides:
            self._increment_rides_used()
            print(
                f"Билет с ограничением поездок {self.ticket_id} использован. Поездок использовано: {self._rides_used}/{self.max_rides}")
        else:
            self._TravelTicket__deactivate_ticket()  # Деактивация билета
            print(f"Билет с ограничением поездок {self.ticket_id} деактивирован. Максимум поездок достигнут.")


# Пример использования
if __name__ == "__main__":
    # Создаем объекты билетов
    unlimited_ticket = UnlimitedTicket("U123")
    limited_ticket = LimitedTicket("L456", 5)
    limited_ride_ticket = LimitedRideTicket("LR789", 3)

    # Используем поездки
    unlimited_ticket.use_ride()
    limited_ticket.use_ride()
    limited_ride_ticket.use_ride()

    # Выводим информацию о билетах
    print(unlimited_ticket.get_info())
    print(limited_ticket.get_info())
    print(limited_ride_ticket.get_info())

    # Тестируем ограничения
    print("\nТестируем ограничения:")
    for _ in range(5):
        limited_ticket.use_ride()
        limited_ride_ticket.use_ride()
