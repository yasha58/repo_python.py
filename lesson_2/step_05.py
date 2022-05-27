"""
Реализовать структуру «Рейтинг», представляющую собой не возрастающий
набор натуральных чисел. У пользователя необходимо запрашивать новый
элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми
значениями, то новый элемент с тем же значением должен разместиться после них.
"""

my_list = [7, 5, 3, 3, 2]
print(my_list)
number = int(input("Введите новый элемент рейтинга: "))
for i in range(len(my_list)):
    if number == my_list[i]:
        my_list.insert(i + 1, number)
        break
    elif number > my_list[0]:
        my_list.insert(0, number)
        break
    elif number < my_list[-1]:
        my_list.append(number)
        break
    elif my_list[i] > number > my_list[i + 1]:
        my_list.insert(i + 1, number)
        break
print(my_list)