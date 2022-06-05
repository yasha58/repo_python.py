"""
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия
всего дорожного полотна. Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги
асфальтом, толщиной в 1 см*число см толщины полотна.
Проверить работу метода. Например: 20м*5000м*25кг*5см = 12500 т
"""

class Road:
    length = None
    width = None
    weight = None
    gauge = None

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def intake(self):
        self.weight = 25
        self.gauge = 0.05
        intake = int(self.length * self.width * self.weight * self.gauge / 10)
        print(f'Необходимо {intake} т для данной дороги')


road_to_village = Road(20, 5000)
road_to_village.intake()
