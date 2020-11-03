'''7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.'''


class ComplexNumber:
    def __init__(self, numb_1, numb_2, *args):
        self.numb_1 = numb_1
        self.numb_2 = numb_2
        self.numbers = "numb_1 + numb_2 * i"

    def __add__(self, other):
        print(f"Суммы x_1 и x_2 равны.")
        return f"numbers = {self.numb_1 + other.numb_1} + {self.numb_2 + other.numb_2} * i"

    def __mul__(self, other):
        print(f"Произведение x_1 и x_2 равны.")
        return f"numbers = {self.numb_1 * other.numb_1 - (self.numb_2 * other.numb_2)} + {self.numb_2 * other.numb_1} * i"

    def __str__(self):
        return f"numbers = {self.numb_1} + {self.numb_2} * i"


x_1 = ComplexNumber(13, 7)
x_2 = ComplexNumber(31, 14)
print(x_1)
print(x_1 + x_2)
print(x_1 * x_2)
