'''3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.'''

my_firm = {"Messi": 22, "Ronaldo": 19, "Mbappe": 17, "Neymar": 18}
try:
    my_file = open("text_3quest.txt", "w")
    for last_name, salary in my_firm.items():
        my_file.write(f"{last_name} : {salary}\n")
except IOError:
    print("Упс.. ошибка ввода-вывода!")
finally:
    my_file.close() #не понимаю, почему IDE подсвечивает my_file?!

summa = 0
count = 0
workers = []
with open("text_3quest.txt", "r") as my_file:
    for line in my_file:
        print(line, end = "")
        tokens = line.split(":")
        if int(tokens[1]) <= 20:
            workers.append(tokens[0])
        summa += int(tokens[1])
        count += 1
result = summa / count
print(f"Сотрудники с зарплатой менее 20тыс : {workers}")
print(f"Средний доход сотрудников: {result}")