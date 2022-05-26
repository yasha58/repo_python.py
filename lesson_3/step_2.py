"""
Реализовать функцию, принимающую несколько параметров, описывающих данные
пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать
вывод данных о пользователе одной строкой.
"""
# решение 1


def data():
    name = input("Введите ваше имя: ")
    surname = input("Введите вашу фамилию: ")
    birth_year = input("Введите ваш год рождения: ")
    city = input("Введите ваш город: ")
    email = input("Введите ваш email: ")
    phn_num = input("Введите ваш номер телефона: ")
    data_dic = {"Имя:": name, "Фамилия:": surname, "Год рождения:": birth_year,
                 "Город:": city, "email:": email, "Номер телефона:": phn_num}
    print(data_dic)


data()


# решение 2

def data_2(name, surname, birth_year, city, email, phone):
    print(name, surname, birth_year, city, email, phone)


data_2(name='Влад', surname='Медведев', birth_year=2003, city='Краснодар', email='email', phone='1111')