class Item:
    """
        Создаем класс для представления товара в магазине
    """
    pay_rate = 1.0  # Хранит уровень цен с учетом скидки (н: 0.85, при скидке 15%)
    all = []  # Хранит созданные экземпляры класса

    def __init__(self, product_name: str, price: float, amount: int) -> None:
        """
            Добавляем атрибуты:
            :param product_name: название товара
            :param price: цена за единицу товара
            :param amount: количество товара в магазине
        """
        self.product_name = product_name
        self.price = price
        self.amount = amount
        Item.all.append(self)

    def calculate_total_price(self) -> float:
        """
            Метод получает общую стоимость конкретного товара в магазине
        """
        return self.price * self.amount

    def apply_discount(self) -> float:
        """
            Метод принемяет установленную скидку для конкретного товара
        """
        self.price *= self.pay_rate
        return self.price
