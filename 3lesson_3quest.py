'''3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.'''

'''sum(my_list) - min(my_list)'''

def my_func(a, b, c):
    my_list = [a, b, c]
    amount = sum(my_list) - min(my_list)
    print(amount)

my_func(10, 15, 30)