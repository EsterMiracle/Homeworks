'''1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.'''


def ur_numb(a, b):
    if a > 0 and b > 0:
        print(a / b)
    else:
        print("Вы ввели некоректное значение!")

ur_numb(a = int(input("Введите ваше число №1: ")),
        b = int(input("Введите ваше число №2: ")))