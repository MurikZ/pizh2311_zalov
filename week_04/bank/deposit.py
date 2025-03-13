class Deposit:
    """
    Базовый класс для представления банковского вклада.

    Атрибуты:
        summa (float): Сумма вклада.
        procent (float): Годовая процентная ставка.
        period (int): Срок вклада в годах.
    """

    def __init__(self, summa: float, procent: float, period: int) -> None:
        """
        Инициализирует объект вклада.

        Аргументы:
            summa (float): Сумма вклада.
            procent (float): Годовая процентная ставка.
            period (int): Срок вклада в годах.
        """
        self.procent = procent
        self.period = period
        self.summa = summa


class Srochniy(Deposit):
    """
    Класс для представления срочного вклада с расчетом по формуле простых процентов.
    Наследует атрибуты и методы класса Deposit.
    """

    def __init__(self, procent: float, period: int, summa: float) -> None:
        """
        Инициализирует объект срочного вклада.

        Аргументы:
            procent (float): Годовая процентная ставка.
            period (int): Срок вклада в годах.
            summa (float): Сумма вклада.
        """
        super().__init__(summa, procent, period)

    def calculate_srochiy(self) -> float:
        """
        Рассчитывает прибыль по срочному вкладу по формуле простых процентов.

        Формула:
            Прибыль = (Сумма * Процентная ставка * Срок) / 100

        Возвращает:
            float: Прибыль по вкладу.
        """
        return self.summa * self.period * self.procent / 100


class Bonus(Deposit):
    """
    Класс для представления бонусного вклада.
    Наследует атрибуты и методы класса Deposit.
    """

    def __init__(self, procent: float, period: int, summa: float, bonus_limit: float, bonus_procent: float) -> None:
        """
        Инициализирует объект бонусного вклада.

        Аргументы:
            procent (float): Годовая процентная ставка.
            period (int): Срок вклада в годах.
            summa (float): Сумма вклада.
            bonus_limit (float): Порог прибыли для начисления бонуса.
            bonus_procent (float): Процент бонуса от прибыли.
        """
        super().__init__(summa, procent, period)
        self.bonus_limit = bonus_limit
        self.bonus_procent = bonus_procent

    def calculate_bonus(self) -> float:
        """
        Рассчитывает прибыль по бонусному вкладу.

        Формула:
            1. Прибыль = (Сумма * Процентная ставка * Срок) / 100
            2. Если прибыль > bonus_limit, добавляется бонус:
               Бонус = Прибыль * (bonus_procent / 100)

        Возвращает:
            float: Итоговая прибыль с учетом бонуса.
        """
        profit = self.procent * self.period * self.summa / 100
        if profit > self.bonus_limit:
            profit += profit * (self.bonus_procent / 100)
        return profit


class Capital(Deposit):
    """
    Класс для представления вклада с капитализацией процентов.
    Наследует атрибуты и методы класса Deposit.
    """

    def __init__(self, procent: float, period: int, summa: float, capital: int) -> None:
        """
        Инициализирует объект вклада с капитализацией.

        Аргументы:
            period (int): Срок вклада в годах.
            summa (float): Сумма вклада.
            procent (float): Годовая процентная ставка.
            capital (int): Количество периодов капитализации в год.
        """
        super().__init__(summa, procent, period)
        self.capital = capital

    def calculate_capital(self) -> float:
        """
        Рассчитывает итоговую сумму по вкладу с капитализацией процентов.

        Формула:
            Итоговая сумма = Сумма * (1 + (Процентная ставка / (100 * капитализация))^(капитализация * срок)

        Возвращает:
            float: Итоговая сумма с учетом капитализации.
        """
        return self.summa * (1 + self.procent / (100 * self.capital)) ** (self.capital * self.period)