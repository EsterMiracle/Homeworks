'''2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна
корректно обработать эту ситуацию и не завершиться с ошибкой.'''


class DivisionByZero:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_zero(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"Деление на ноль недопустимо")


item = DivisionByZero(10, 100)
print(DivisionByZero.divide_by_zero(10, 0))
print(DivisionByZero.divide_by_zero(10, 0.1))
print(item.divide_by_zero(100, 0))

# Через input() пытался, ничего не вышло =( так и не понял где его прокинуть необходимо..