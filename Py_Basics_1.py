# Task1

def get_data():
    name = input("Please enter your first name: ")
    surname = input("You surname please: ")
    age = input("Your age: ")
    num = input("What is your favourite number? ")
    return print(
        f"You entered: \n name: {name},\n surname: {surname},\n "
        f"age: {age},\n favourite number: {num}."
    )


get_data()


# Task2

import datetime


def seconds_to_time(num):
    return print(str(datetime.timedelta(seconds=int(num))))


secs = input("Please a number of seconds to see the time in HH:MM:SS format: ")
seconds_to_time(secs)


# Task3

def sum_numbers(n):
    return print(int(n)+int(n + n)+int(n + n + n))


number = input("Please enter a number to return a sum of n+nn+nnn: ")
sum_numbers(number)


# Task4

def max_digit(num):
    return print(max(set(num)))


max_digit(input("Please enter an integer number: "))


# Task5

def profit_per_employee(result):
    staff_count = int(input("How many people have you employed? "))
    profit_per_empl = result / staff_count
    return print(
        "Your profit per employer is {:.2f}".format(profit_per_empl)
    )


def fin_result(revenue, expenses):
    result = revenue - expenses
    if result > 0:
        print(f"Your profit is {result}")
        profit_per_employee(result)
    elif result < 0:
        print(f"Your losses are {result}")
    else:
        print("Your have no money left!")
    return None


rev = int(input("How much have you earned: "))
exp = int(input("How much have you spent: "))
fin_result(rev, exp)


# Task6

def distance_increase(dist):
    growth_rate = 10
    return dist * (1 + growth_rate / 100)


def days_count(initial_dist, target_dist):
    day_count = 1
    distance = initial_dist
    while distance < target_dist:
        distance = distance_increase(distance)
        day_count += 1
    return print(f"On the day {day_count} you'll reach your target distance.")


a = int(input("Please enter the distance you ran in the first day (km): "))
b = int(input("Enter your target distance (km): "))
days_count(a, b)
