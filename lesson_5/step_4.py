"""
Необходимо написать программу, открывающую файл на чтение
и считывающую построчно данные. При этом английские
числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""


with open('fourth_eng.txt') as f:
    data = f.readlines()

with open('fourth_rus.txt') as f:
    for num in data:
        if '1' in num:
            num = num.replace('One', 'Один')
        elif '2' in num:
            num = num.replace('Two', 'Два')
        elif '3' in num:
            num = num.replace('Three', 'Три')
        elif '4' in num:
            num = num.replace('Four', 'Четыре')
        f.write(num)

        