"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000


def test_apply_discount():
    Item.pay_rate = 0.8
    # применяем скидку
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    assert item1.apply_discount() == 8000
    assert item2.apply_discount() == 16000


def test_name_getter():
    item = Item('Телефон', 189990, 2)
    assert item.name == 'Телефон'


def test_name_setter():
    item = Item('Телефон', 189990, 2)
    assert item.name == 'Телефон'

    item = Item('МегаУльтраЭкстраТелефон', 89990, 1)
    item.name = 'МегаУльтраЭкстраТелефон'
    assert item.name == 'МегаУльтра'


def test_instantiate_from_csv():
    Item.instantiate_from_csv('src/items.csv')

    assert len(Item.all) == 5

    item1 = Item.all[3]
    item2 = Item.all[1]

    assert item1.name == 'Мышка'
    assert item2.name == 'Ноутбук'

    item3 = Item.all[4]

    assert item3.name == 'Клавиатура'
    assert item3.price == 75
    assert item3.amount == 5


def test_string_to_number():
    assert Item.string_to_number('-2.3') == -2
    assert Item.string_to_number('-3') == -3
    assert Item.string_to_number('0') == 0
    assert Item.string_to_number('0.0') == 0
    assert Item.string_to_number('4') == 4
    with pytest.raises(ValueError):
        Item.string_to_number('abc')
