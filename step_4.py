"""
Задание 4.
Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и только арифметические операции.
Не используйте взятие по индексу.
Пример:
Ведите целое положительное число: 123456789
Самая большая цифра в числе: 9
"""
number = int(input("Введите целое число: "))
maximum = number % 10
number = number // 10
while number > 0:
     if number % 10 > maximum:
         maximum = number % 10
     number = number // 10
print("Самая большая цифра в числе:", maximum)