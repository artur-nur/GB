# Task1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между режимами
# должно осуществляться только в указанном порядке (красный, желтый, зеленый). Проверить работу примера,
# создав экземпляр и вызвав описанный метод.
#
# Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.
#
import time
from itertools import cycle


class TrafficLight:
    previous_color = "Green"
    color_order_timings = {"Red": (1, 7), "Yellow": (2, 2), "Green": (0, 7)}
    # {color: (next_color_index, color_time_running_secs), ...}

    def __init__(self, color, limit=3):
        self.color = color
        self.limit = limit
        self.next_color_index = TrafficLight.color_order_timings[TrafficLight.previous_color][0]
        self.right_next_color = list(TrafficLight.color_order_timings)[self.next_color_index]
        self.current_color_time = TrafficLight.color_order_timings[self.color][1]
        TrafficLight.previous_color = self.color

    def running(self):
        if self.right_next_color == self.color:
            print(f"{self.color} light is ON for {self.current_color_time} secs")
            time.sleep(TrafficLight.color_order_timings[self.color][1])
            print(f"{self.color} light is OFF")
        else:
            print(f"You entered '{self.color}'. It's wrong color! "
                  f"Previous light was '{TrafficLight.previous_color}'. "
                  f"So, it's supposed to be '{self.right_next_color}' now.")

    def self_running_n_times(self):
        count = 0
        for color in cycle(TrafficLight.color_order_timings.keys()):
            print(f"{color} for {TrafficLight.color_order_timings[color][1]} secs")
            time.sleep(TrafficLight.color_order_timings[color][1])
            count += 1
            if count == self.limit:
                break


tr1 = TrafficLight("Red")
tr1.running()
tr2 = TrafficLight("Yellow")
tr2.running()
tr3 = TrafficLight("Green")
tr3.running()
tr4 = TrafficLight("Yellow")
tr4.running()
tr5 = TrafficLight("Red", 6)
tr5.self_running_n_times()

# Task2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * число см толщины полотна. Проверить работу метода.
#
# Например: 20м * 5000м * 25кг * 5см = 12500 т (!!!ошибка 125 тонн, так как толщина в см, а не метрах!!!)


class Road:
    height_in_cm = 5
    weight_kg_per_square_meter = 25

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate_weight(self):
        weight = self._width * self._length * Road.weight_kg_per_square_meter * Road.height_in_cm / 100 / 1000
        return print(f"Weight of total asfalt required for the road is {weight} ton.")


r = Road(20, 5000)
r.calculate_weight()


# Task3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход). Последний атрибут должен быть защищенным и
# ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker. В классе Position реализовать
# методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return print(f"The worker's fullname is {self.name} {self.surname}")

    def get_total_income(self):
        return print(f"The worker's total income is {self._income['wage'] + self._income['bonus']}")


w1 = Position("Ivan", "Ivanov", "Python Developer", 200000, 100000)
print(w1.position)
w1.get_full_name()
w1.get_total_income()


# Task4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        print(f"Speed is {self.speed} km/h now.")

    def go(self):
        print("The Car is going now.")

    def stop(self):
        print("The Car has stopped.")

    def turn(self, direction):
        print(f"The car has turned to the {direction}.")

class TownCar(Car):
    def show_speed(self):
        if self.speed <= 60:
            print(f"Speed is {self.speed} km/h now")
        else:
            print(f"Speed {self.speed} km/h is over the allowed limit.")

class SportCar(Car):
    print("This is the best sport car ever")

class WorkCar(Car):
    def show_speed(self):
        if self.speed <= 40:
            print(f"Speed is {self.speed} km/h now")
        else:
            print(f"Speed {self.speed} km/h is over the limit allowed.")

class PoliceCar(Car):
    print("Here is the police car. Be careful!")

car1 = Car(60, "White", "Toyota", False)
print(car1.name, car1.color)
print(car1.go(), car1.turn("right"), car1.stop())
car2 = WorkCar(60, "Orange", "JCB", False)
print(car2.show_speed())


# Task5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и
# метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить
# уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    def draw(self):
        print(f"Запуск отрисовки ручкой {self.title}.")


class Pencil(Stationery):
    def draw(self):
        print(f"Запуск отрисовки карандашом {self.title}.")


class Handle(Stationery):
    def draw(self):
        print(f"Запуск отрисовки марктером {self.title}.")


p = Pen("Monblanc")
p.draw()
pc = Pencil("ErichKrauser")
pc.draw()
h = Handle("Marker")
h.draw()