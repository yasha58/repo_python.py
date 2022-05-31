"""
Создать текстовый файл (не программно), сохранить
в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""


with open('second.txt') as f:
    data = f.readlines()
    print(f'В данном файле всего {len(data)} строк')
    for data_num, words in enumerate(data, start=1):
        print(f'В {data_num} строке всего {words} слов')



