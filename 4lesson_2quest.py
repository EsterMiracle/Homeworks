'''2. Представлен список чисел. Необходимо вывести элементы исходного списка,
 значения которых больше предыдущего элемента.'''

hw_list = [3, 2, 5, 16, 12, 15, 4, 10, 7, 1, 78, 123, 55]
my_list_big = [el for el in hw_list if el > hw_list[hw_list.index(el)-1]]
my_list_small = [el for el in hw_list if el < hw_list[hw_list.index(el)-1]]
print(f"{my_list_big}\n"
      f"{my_list_small}")
