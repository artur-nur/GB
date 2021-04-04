# Task1. Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

textlines = []
while True:
    textline = input("Please enter some text: ")
    if textline:
        textlines.append(textline + "\n")
    else:
        break
file_name1 = "user_input1"
with open(file_name1, "w") as f1:
    f1.writelines(textlines)


# Task2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

file_name2 = "scratch.txt"
with open(file_name2) as f2:
    text_lines = f2.readlines()
    print(f"File {file_name2} has {len(text_lines)} rows")
    [print(f"Row {i} has {len(line.split())} words")
     for i, line in enumerate(text_lines)]


# Task3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и
# величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

# employees_salaries.txt:
# 1,Ivanov,200000
# 2,Petrov,100000
# 3,Sidorov,50000
# 4,Krasnov,25000
# 5,Popov,15000
# 6,Emelin,10000

def split_line(line):
    return line.strip().split(',')


salary_limit = 20000
file_name3 = "employees_salaries.txt"
with open(file_name3) as f3:
    text_lines = f3.readlines()
    [print(f"{split_line(line)[1]} earns {split_line(line)[2]} per month.")
     for line in text_lines if int(split_line(line)[2]) < salary_limit]
    salaries_list = [int(split_line(line)[2]) for line in text_lines]
    print(f"Average salary is {sum(salaries_list)/len(salaries_list)}")


# Task4. Создать (не программно) текстовый файл со следующим содержимым:
#
# One — 1
#
# Two — 2
#
# Three — 3
#
# Four — 4
#
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

translation_list = [
    ("One", "Один"),
    ("Two", "Два"),
    ("Three", "Три"),
    ("Four", "Четыре")
]
file_name4 = 'simple_file.txt'
with open(file_name4) as f4:
    text = f4.read()
    for pair in translation_list:
        text = text.replace(pair[0], pair[1])

with open("new_file.txt", "w") as new_f:
    new_f.writelines(text)


# Task5. Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и
# выводить ее на экран.


digits = ""
while True:
    digit = input("Please enter some number: ")
    if digit:
        digits += digit + " "
    else:
        break

file_name5 = "user_input2"
with open(file_name5, "w") as f5:
    f5.write(digits)

with open(file_name5, "r") as f5:
    nums = [int(i) for i in f5.read().split()]
    print(f"Total sum: {sum(nums)}")


# Task6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает
# учебный предмет и наличие лекционных, практических и лабораторных занятий
# по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
# были все типы занятий. Сформировать словарь, содержащий название предмета и
# общее количество занятий по нему. Вывести словарь на экран.

# Примеры строк файла:
# Информатика:   100(л)   50(пр)   20(лаб).
# Физика:   30(л)   —   10(лаб)
# Физкультура:   —   30(пр)   —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}


def get_nums(string):
    return int(''.join([x for x in string if x.isdigit()]))


def get_sum(course):
    keys, values = course.strip().split(":")
    hours = sum([get_nums(value) for value in values.split() if len(value) > 1])
    return keys, hours


file_name6 = "courses.txt"
with open(file_name6, "r") as f6:
    courses = f6.readlines()

results = dict(get_sum(course) for course in courses)
print(results)


# Task7. Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка будет содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.

# Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки,
# в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки,
# также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.


class Company:
    def __init__(self, name, type, revenue, costs):
        self.name = name
        self.type = type
        self.revenue = int(revenue)
        self.costs = int(costs)

    def get_profit(self):
        return self.revenue - self.costs


file_name7 = 'companies_data.txt'
data = []
while True:
    row = input("Enter space separated a company's name, type, revenue, costs (Leave empty to quit): ")
    if row:
        data.append(row + "\n")
    else:
        break
with open(file_name7, "w") as f7:
    f7.writelines(data)

with open(file_name7, "r") as f7:
    file_text = f7.readlines()

profits = []
data_base = {}
for line in file_text:
    name, type, revenue, costs = line.strip().split()
    comp = Company(name, type, revenue, costs)
    comp_name = comp.name
    comp_profit = comp.get_profit()
    data_base[comp_name] = comp_profit
    if comp_profit > 0:
        profits.append(comp_profit)
average_profit = sum(profits)/len(profits)
results = [data_base, {'average_profit': average_profit}]
print(results)



