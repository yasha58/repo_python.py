"""
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
"""

from itertools import count, cycle

# A

for el in count(int(input("Введите первое число: "))):
    if el > 10:
        break
    else:
        print(el)

# Б

my_list = [34, 125, "Anny", True, 12.5]
res = cycle(my_list)
for num in range(10):
    print(next(res))