"""Создать программно файл в текстовом формате, записать
в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

with open('first.txt', 'w') as f:
    while True:
        data = input('Введите данные: ')
        if data == ' ':
            break
        f.write(data + '\n')
