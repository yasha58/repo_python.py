"""
Реализуйте базовый класс Car. У данного класса должны быть
следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны
сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar,
PoliceCar. Добавьте в базовый класс метод show_speed, который
должен показывать текущую скорость автомобиля. Для классов TownCar
и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Cars:
    name = None
    speed = None
    color = None

    def __init__(self, name, speed, color):
        self.name = name
        self.speed = speed
        self.color = color

    @staticmethod
    def go():
        return "Машина едет\n"

    @staticmethod
    def stop():
        return "Машина остановилась\n"

    @staticmethod
    def turn(direction):
        return f"Машина поворачивает {direction}\n"

    def show_speed(self):
        print(f'Текущая скорость машины {self.name} - {self.speed} км/ч')


class TownCar(Cars):

    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)
        if speed > 60:
            print("Превышение скорости!")


class SportCar(Cars):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)


class WorkCar(Cars):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)
        if speed > 40:
            print("Превышение скорости!")


class PoliceCar(Cars):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)


audi = TownCar('Audi', 45, 'Серая')
bmw = SportCar('bmw', 200, 'Красная')
ford = WorkCar('Ford', 90, 'Белая')
print(ford.name, ford.color, ford.speed)
print(ford.go(), ford.turn('Налево'), ford.stop())
