"""
Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
"""


start_list = [2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(f'Изначальный список: {start_list}')
new_list = [el for num, el in enumerate(start_list) if start_list[num - 1] < start_list[num]]
print(f'Новый список: {new_list}')

"""
Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
Необходимо решить задание в одну строку.
"""

print(f'Числа, кратные 20 и 21 в  пределах от 20 до 240: '
      f'{[el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]}')