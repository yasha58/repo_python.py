"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может
продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить
сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""

def sum_num():
    full_sum = 0
    number = None
    end = False
    while not end:
        number = input("Для выхода введите 'end'"
                       "\nВведите ваш порядок цисел: ").split()
        my_sum = 0
        for i in range(len(number)):
            if number[i] == "end":
                end = True
                break
            else:
                my_sum += int(number[i])
        full_sum += my_sum
        print("Сумма равна:", full_sum)


sum_num()