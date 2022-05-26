"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""

while True:
    number = int(input("Введите номер меяца: "))
    list_seasons = ["Зима", "Весна", "Лето", "Осень"]
    dict_seasons = {
         1: "Зима",
         2: "Весна",
         3: "Лето",
         4: "Осень"
    }
    if number == 1 or number == 2 or number == 12:
      season = list_seasons[0]
      # season = dict_seasons.get[0]
      print("Время года текущего меяца: {}".format(season))
    elif number == 3 or number == 4 or number == 5:
      season = list_seasons[1]
      # season = dict_seasons.get[1]
      print("Время года текущего меяца: {}".format(season))
    elif number == 6 or number == 7 or number == 8:
      season = list_seasons[2]
      # season = dict_seasons.get[2]
      print("Время года текущего меяца: {}".format(season))
    elif number == 9 or number == 10 or number == 11:
      season = list_seasons[3]
      # season = dict_seasons.get[3]
      print("Время года текущего меяца: {}".format(season))
    else:
      print("Введите цифру от 1 до 12")