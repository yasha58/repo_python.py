"""
Реализовать функцию my_func(), которая принимает
три позиционных аргумента, и возвращает сумму
наибольших двух аргументов.
"""

def my_func(a, b, c):
    numbers = [a, b, c]
    final = []
    num_1 = max(numbers)
    final.append(num_1)
    numbers.remove(num_1)
    num_2 = max(numbers)
    final.append(num_2)
    numbers.remove(num_2)
    print(sum(final))


my_func(34, 5, -15)