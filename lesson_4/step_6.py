"""
Реализовать генератор с помощью функции с ключевым словом yield,
создающим очередное значение. При вызове функции должен создаваться
объект-генератор. Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа, а в цикле необходимо выводить
только первые n чисел, начиная с 1! и до n!.
"""


from itertools import count
from math import factorial


def fibo_gen():
    for el in count(1):
        yield factorial(el)


num = fibo_gen()
x = 0
for n in num:
    if x < 15:
        print(n)
        x += 1
    else:
        break