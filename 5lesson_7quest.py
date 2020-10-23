'''7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные
о фирме: название, форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список.
Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.'''

import json

summary = {}
pr = {}
profit = 0
profit_average = 0
i = 0
with open("text_7quest.txt", "r", encoding = "utf-8") as file:
    for line in file:
        name, firm, earning, damage = line.split()
        summary[name] = int(earning) - int(damage)
        if summary.setdefault(name) >= 0:
            profit = profit + summary.setdefault(name)
            i += 1
    if i != 0:
        profit_average = profit / i
        print(f"Прибыль средняя - {profit_average:.2f}")
    else:
        print(f"Прибыль средняя - отсутсвует. Все работают в убыток")
    pr = {"Cредняя прибыль" : round(profit_average)}
    summary.update(pr)
    print(f"Прибыль каждой компании - {summary}")

with open("jsonfile.json", "w") as write_js:
    json.dump(summary, write_js)

    js_str = json.dumps(summary)
    print(f"Создан файл с расширением json со следующим содержимым: \n {js_str}")

# Не совсем уверен в правильности выполнения задания =(