"""
Задание 3.
Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.
Пример:
Введите число n: 3
n + nn + nnn = 369
"""
number = str(input("Введите число: "))

first_num = number
second_num = first_num + number
third_num = second_num + number

int_first_num = int(first_num)
int_second_num = int(second_num)
int_third_num = int(third_num)

sum_num = int_first_num + int_second_num + int_third_num
print("\n Считаем:\n", first_num, "+", second_num, "+", third_num, "=", sum_num)