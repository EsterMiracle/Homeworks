'''2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.'''

# Сразу хочу задать вопрос, а как применять функцию round() к f-строкам?
# Благодарю за ответ!

class Clothes:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def square_coat(self):
        return self.width / 6.5 + 0.5

    def square_suit(self):
        return self.height * 2 + 0.3

    @property
    def square_full(self):
        return str(f"Площадь общая ткани \n"
                   f"{(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}")


class Coat(Clothes):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.my_coat = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f"Площадь на пальто {self.my_coat}"


class Suit(Clothes):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.my_suit = round(self.height * 2 + 0.3)

    def __str__(self):
        return f"Площадь на костюм {self.my_suit}"


coat = Coat(12, 9)
suit = Suit(3, 7)
print(coat)
print(suit)
print(coat.square_full)
print(suit.square_full)
print(round(suit.square_coat(), 2))
print(round(suit.square_suit(), 2))
