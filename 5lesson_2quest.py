'''2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.'''

my_file = ["Я узнал что у меня,\n", "Есть огромная семья!\n", "И тропинка, и лесок,\n", "В поле каждый колосок..\n"]
with open("text_2quest.txt", "w+") as file_obj:
    file_obj.writelines(my_file)
with open("text_2quest.txt") as file_obj:
    lines = 0
    letters = 0
    for line in file_obj:
        lines += line.count("\n")
        letters = len(line) - 1
        print(f"Количество символов в линии: {letters}")
    print(f"Количество строк в файле: {lines}")

