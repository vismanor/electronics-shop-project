import csv
import os
from math import floor


class Item:
    """
        Создаем класс для представления товара в магазине
    """
    pay_rate = 1.0  # Хранит уровень цен с учетом скидки (н: 0.85, при скидке 15%)
    all = []  # Хранит созданные экземпляры класса

    def __init__(self, name: str, price: float, amount: int) -> None:
        """
            Добавляем атрибуты:
            :param name: название товара
            :param price: цена за единицу товара
            :param amount: количество товара в магазине
        """
        self.__name = name  # Сделали атрибут name приватным
        self.price = price
        self.amount = amount
        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            self.__name = value[:10]  # Проверяем, что наименование товара не больше 10 симвовов, обрезаем, если больше
        else:
            self.__name = value

    def calculate_total_price(self) -> float:
        """
            Метод получает общую стоимость конкретного товара в магазине
        """
        return self.price * self.amount

    def apply_discount(self) -> float:
        """
            Метод принимает установленную скидку для конкретного товара
        """
        self.price *= self.pay_rate
        return self.price

    @classmethod
    def instantiate_from_csv(cls, file_path='src/items.csv'):
        """
            Класс-метод, инициализирующий экземпляры класса `Item` данными из файла _src/items.csv_
        """
        Item.all.clear()
        script_dir = os.path.dirname(__file__)  # Получаем путь к текущему файлу item.py
        file_path = os.path.join(script_dir, '..', file_path)  # Объединяем путь к файлу items.csv
        with open(file_path, 'r', newline='', encoding='UTF-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name = row['name']
                price = float(row['price'])
                amount = int(row['quantity'])
                cls(name, price, amount)

    @staticmethod
    def string_to_number(num_str: str) -> int:
        """
            Статический метод, возвращающий число из числа-строки
        """
        try:
            return int(float(num_str))
        except ValueError:
            raise ValueError('Ай-яй! Некорректный ввод. Введи допустимое числовое значение :)')
