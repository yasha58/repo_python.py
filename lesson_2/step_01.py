"""
Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
 """


my_list = ["qwerty", 123, 17.5, "robot", False, {12, 3}, [1, 11], "Mary"]
for number in my_list:
    print(type(number))