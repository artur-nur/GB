# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
# года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Date:
    @classmethod
    def date_numbers(cls, date):
        return [int(i) for i in date.split('-')]


    @staticmethod
    def validate_numbers(date_list):
        if 1 <= date_list[0] <= 31:
            print("Day is correct!")
        if 1 <= date_list[1] <= 12:
            print("Month is correct!")
        if 1900 <= date_list[2] <= 2100:
            print("Year is correct!")


d = Date().date_numbers("01-05-2021")
print(d)
Date.validate_numbers(d)


# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать
# эту ситуацию и не завершиться с ошибкой.

class MyError(Exception):
    def __init__(self, text):
        self.text = text

class MyException:
    def __init__(self, numerator, denumerator):
        self.numerator = numerator
        self.denumerator = denumerator

    @property
    def divide_zero(self):
        try:
            num = float(self.numerator)
            denum = float(self.denumerator)
            if denum == 0:
                raise MyError("You entered '0' as the denominator!")
        except ValueError:
            return f"You entered wrong number!"
        except MyError:
            return MyError("Division to zero! Please enter a non-zero denominator.")
        else:
            return f"Result of division {num} to {denum} is {num / denum}."


div1 = MyException(40, 2)
print(div1.divide_zero)
div2 = MyException(40, 0)
print(div2.divide_zero)
param1 = input("Please enter a numerator: ")
param2 = input("Please enter a denominator: ")
div3 = MyException(param1, param2)
print(div3.divide_zero)


# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.
#
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит
# работу скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.
#
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. При вводе пользователем
# очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число.
# Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
# При этом работа скрипта не должна завершаться.


class MyError1(Exception):
    def __init__(self, text):
        self.text = text


class MyList:
    my_list = []

    def __init__(self, number):
        self.number = number

    def append_list(self):
        try:
            if not self.number.isdigit():
                raise MyError1("You entered non-digit value. Try again.")
        except MyError1 as err:
            print(err)
        else:
            MyList.my_list.append(int(self.number))
            return f"Number {self.number} has been successfully added to the list."


while True:
    digit = input("Please enter a number. To interrupt the input process, please enter 'stop': ")
    MyList(digit).append_list()
    if digit == "stop":
        print(MyList.my_list)
        break


# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.

class Warehouse:
    def __init__(self, wh_name, location, square):
        self.wh_name = wh_name
        self.location = location
        self.square = square
        print(f"Office Equipment Warehouse '{self.wh_name}' in {self.location}"
              f" has {self.square} sqm.")


class OfficeEquipment:
    def __init__(self, dept, name):
        self.dept = dept
        self.name = name


class Printer(OfficeEquipment):
    pr_count = 0

    def __init__(self, dept, name, color, pr_type, **kwargs):
        super(Printer, self).__init__(dept, name, **kwargs)
        self.color = color
        self.pr_type = pr_type
        Printer.pr_count += 1

    def __str__(self):
        return f"You have added {self.pr_type, self.color} Printer" \
               f"{self.name} to {self.dept} dept.\nTotally there are {Printer.pr_count} pcs."


class Scanner(OfficeEquipment):
    sc_count = 0

    def __init__(self, dept, name, scan_speed, **kwargs):
        super(Scanner, self).__init__(dept, name, **kwargs)
        self.scan_speed = scan_speed
        Scanner.sc_count += 1

    def __str__(self):
        return f"You have added Scanner " \
               f"{self.name} with scanning speed of {self.scan_speed} ppm " \
               f"to {self.dept} dept.\nTotally there are {Scanner.sc_count} pcs."


class Xerox(Printer, Scanner):
    xrx_count = 0

    def __init__(self, dept, name, color, pr_type, scan_speed, pr_format):
        self.pr_format = pr_format
        super(Xerox, self).__init__(
            dept=dept,
            name=name,
            color=color,
            pr_type=pr_type,
            scan_speed=scan_speed
        )
        Xerox.xrx_count += 1

    def __str__(self):
        return f"You have added Xerox " \
               f"{self.name} with copying format of {self.pr_format} ppm " \
               f"to {self.dept} dept.\nTotally there are {Xerox.xrx_count} pcs."


wrh = Warehouse("RUS", "Moscow", 1000)
pr = Printer("Storage", "HP P-120", "color", "inkjet")
print(pr)
sc = Scanner("Storage", "Samsung H-100", 10)
print(sc)
cp = Xerox("Storage", "Xerox MFP-30", "black", "laserjet", 15, "A3")
print(cp)


# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
# определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.

class EquipStorage:
    storage = "Storage"
    _eq_list = {storage: []}

    def __init__(self, eq_type, name, price, quantity, dept=storage):
        self.eq_type = eq_type
        self.name = name
        self.price = price
        self.quantity = quantity
        self.dept = dept
        self.my_eq = {
            'Type': self.eq_type,
            'Model': self.name,
            'Price': self.price,
            'Quantity': self.quantity
        }

    def __str__(self):
        return f"Type: '{self.eq_type}', " \
               f"name: '{self.name}', " \
               f"price: {self.price}, " \
               f"quantity: {self.quantity}"

    def receive_eq_to_storage(self):
        EquipStorage._eq_list[EquipStorage.storage].append(self.my_eq)
        print(f'Equipment added to the storage:\n {EquipStorage._eq_list[self.dept][-1]}')

    def transfer_eq_to_dept(self, other_dept):
        if other_dept not in EquipStorage._eq_list.keys():
            EquipStorage._eq_list[other_dept] = []
        eq_list = EquipStorage._eq_list[EquipStorage.storage]
        eq_index = eq_list.index(self.my_eq)
        EquipStorage._eq_list[other_dept].append(eq_list.pop(eq_index))
        print(f'Equipment {EquipStorage._eq_list[other_dept]} moved to {other_dept}.')

    @staticmethod
    def get_remains():
        print(f'Equipment in all departments:')
        for i, dept in enumerate(EquipStorage._eq_list, start=1):
            print(i, dept, EquipStorage._eq_list[dept])


pr1 = EquipStorage("Printer", "HP", 300, 5)
pr2 = EquipStorage("Printer", "Samsung", 500, 2)
sc1 = EquipStorage("Scanner", "Canon", 100, 1)
print(pr1, pr2, sc1, sep="\n")
pr1.receive_eq_to_storage()
pr2.receive_eq_to_storage()
sc1.receive_eq_to_storage()
EquipStorage.get_remains()
pr1.transfer_eq_to_dept("Office")
EquipStorage.get_remains()


# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.


class Storage:

    def __init__(self, name, price, quantity, number_of_pages, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.num = number_of_pages
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Model': self.name, 'Price for 1 piece': self.price, 'Quantity': self.quantity}

    def __str__(self):
        return f'Name: {self.name}, price: {self.price}, quantity: {self.quantity}'

    def reception(self):
        try:
            unit = input(f'Enter name ')
            unit_p = int(input(f'Enter price for 1 piece '))
            unit_q = int(input(f'Enter quantity '))
            unique = {'Model': unit, 'price': unit_p, 'quantity': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Current list -\n {self.my_store}')
        except:
            return f'Wrong input'

        q = input(f"To stop enter 'q'")
        if q == 'q':
            self.my_store_full.append(self.my_store)
            return print(f'Total storage -\n {self.my_store_full}')
        else:
            return Storage.reception(self)


class Printer(Storage):
    def to_print(self):
        return f'To print {self.num} times.'


class Scanner(Storage):
    def to_scan(self):
        return f'To scan {self.num} times.'


class Copier(Storage):
    def to_copier(self):
        return f'To copier {self.num} times.'


eq_1 = Printer('Samsung', 5000, 2, 15)
eq_2 = Scanner('HP', 6000, 5, 5)
eq_3 = Copier('Xerox', 15000, 1, 150)
print(eq_1.reception())
print(eq_2.reception())
print(eq_3.reception())
print(eq_1.to_print())
print(eq_2.to_scan())
print(eq_3.to_copier())

# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
# создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.


class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        print(f'Sum of complex numbers:')
        return f's = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Multiplication of complex numbers:')
        return f'p = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'c = {self.a} + {self.b} * i'


cn1 = ComplexNumber(4, 7)
cn2 = ComplexNumber(-2, -10)
print(cn1, cn2, sep="\n")
print(cn1 + cn2)
print(cn1 * cn2)