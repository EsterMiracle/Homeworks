'''5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.'''

def summ():
    try:
        with open("text_5quest.txt", "w+") as my_obj:
            line = input("Введите ваш список цифр через пробел: \n")
            my_obj.writelines(line)
            my_numb = line.split()
            print(sum(map(int, my_numb)))
    except IOError:
        print("Уппсс.. ошибка в файле!")
    except ValueError:
        print("Упсс.. ошибка ввода! Вводите цифры, и всё получится! =)")

summ()