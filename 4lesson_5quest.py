'''5. Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().'''

from functools import reduce

my_list = [el for el in range(100, 1001, 2)]
print(my_list)
def my_func(prev_numb, numb):
    return prev_numb * numb
print(reduce(my_func, my_list))