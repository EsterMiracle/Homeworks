'''4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.'''

dict = {"One" : "Один", "Two" : "Два", "Three" : "Три", "Four" : "Четыре"}
my_file = []
with open("text_4quest.txt", encoding = "utf-8") as my_obj:
    for i in my_obj:
        i = i.split(" ", 1)
        my_file.append(dict[i[0]] + " " + i[1])
    print(my_file)

with open("text_4quest_final.txt", "w", encoding = "windows-1251") as my_obj_2:
    my_obj_2.writelines(my_file)