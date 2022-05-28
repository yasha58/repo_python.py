"""
Реализовать структуру данных «Товары». Она должна представлять собой
список кортежей. Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
"""

number = int(input("Сколько товаров вы хотите добавить?: "))
goods = {}
goods_list = []
final_list = {}
i = 0
while i != number:
    name_list = []
    price_list = []
    amount_list = []
    unit_list = []
    name = input("Введите название товара: ")
    name_list.append(name)
    price = input("Введите цену товара: ")
    price_list.append(price)
    amount = input("Введите количество товара: ")
    amount_list.append(amount)
    unit = input("Введите единицу измерения: ")
    unit_list.append(unit)
    goods = dict({"название": name,
                  "цена": price,
                  "количество": amount,
                  "единица измерения": unit})
    goods_list.append((i + 1, goods))
    final_list = dict({"название": name_list,
                       "цена": price_list,
                       "количество": amount_list,
                       "единица измерения": unit_list})
    i += 1
print(goods_list)
print(final_list)