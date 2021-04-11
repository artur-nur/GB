# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.
#
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
# складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, matrix_data):
        self.matrix_data = matrix_data

    def __str__(self):
        for row in self.matrix_data:
            print("[", end="")
            for i in row:
                print(f"{i:3} ", end="")
            print("]")
        return ""

    def __add__(self, other):
        is_rows_equal = len(self.matrix_data) == len(other.matrix_data)
        is_columns_equal = len(self.matrix_data[0]) == len(other.matrix_data[0])
        if is_rows_equal and is_columns_equal:
            for i in range(len(self.matrix_data)):
                for j in range(len(self.matrix_data[i])):
                    self.matrix_data[i][j] = self.matrix_data[i][j] + other.matrix_data[i][j]
            return Matrix.__str__(self)
        else:
            return f"Matrices must be of the same dimensions!"


m_data1 = [[31, 22], [37, 43], [51, 86]]
md1 = Matrix(m_data1)
print(md1)
m_data2 = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
md2 = Matrix(m_data2)
print(md2)
m_data3 = [[3, 5, 8, 3], [8, 3, 7, 1]]
md3 = Matrix(m_data3)
print(md3)
m_data4 = [[-30, -20], [-34, -39], [-46, -80]]
md4 = Matrix(m_data4)
m_data5 = [[-3, -5, -32], [-2, -4, -6], [1, -64, 8]]
md5 = Matrix(m_data5)
print(md1 + md4)    # складываем две одинаковые по размеру матрицы
print(md2 + md5)    # складываем две одинаковые по размеру матрицы
print(md1 + md5)    # складываем две разные матрицы, что недопустимо для сложения


# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс)
# этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и
# костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
#
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
#
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Cloth(ABC):
    def __init__(self, name):
        self._name = name

    @property
    @abstractmethod
    def consumption(self):
        return f"Textile to be consumed {self._name / 6.5 + 0.5 + 2 * self._name + 0.3} " \
               f"for the suit and coat."


class Coat(Cloth):
    @property
    def consumption(self):
        return f"Textile to be consumed {self._name / 6.5 + 0.5 :.2f} for the coat of {self._name} size."


class Suit(Cloth):
    @property
    def consumption(self):
        return f"Textile to be consumed {2 * self._name + 0.3} for the suit of {self._name}cm height."


c = Coat(48)
print(c.consumption)
s = Suit(170)
print(s.consumption)


# 3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
# вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).Данные методы должны применяться только к
# клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно.
# В методе деления должно осуществляться округление значения до целого числа.
#
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме
# ячеек исходных двух клеток.
#
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток
# больше нуля, иначе выводить соответствующее сообщение.
#
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как
# произведение количества ячеек этих двух клеток.
#
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как
# целочисленное деление количества ячеек этих двух клеток.
#
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.
#
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно
# переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
#
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n**.
#
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n*****.
#
# Подсказка: подробный список операторов для перегрузки доступен по ссылке.

class Cell:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return f"Sum of cells: {self.number + other.number}."

    def __sub__(self, other):
        return f"Difference of cells: {self.number - other.number}."

    def __mul__(self, other):
        return f"Multiplication of cells: {self.number * other.number}."

    def __truediv__(self, other):
        return f"Division of cells: {round(self.number / other.number)}."

    def make_order(self, num_in_row):
        print(f"{self.number} cells were organised in rows by {num_in_row} cells.")
        for i in range(1, self.number + 1):
            print("*", end="")
            if i % (num_in_row) == 0:
                print()


c1 = Cell(5)
c2 = Cell(8)
print(c1 + c2)
print(c2 - c1)
print(c1 * c2)
print(c2 / c1)
c3 = Cell(15)
c3.make_order(4)