'''2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.

Например: 20м * 5000м * 25кг * 5см = 12500 т'''

class Road:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def _massa(self):
        return self.length * self.width

class MassCount(Road):
    def __init__(self, _length, _width, volume):
        super().__init__(_length, _width)
        self.volume = volume

result = MassCount(20, 5000, 125)
print(result._massa())