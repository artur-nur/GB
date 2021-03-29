# Task 1
def divide_nums(arg1, arg2):
    if arg2 != 0:
        return print(arg1 / arg2)
    else:
        print("Division to zero! Please enter a non-zero denominator")


arg1 = float(input("Please enter a numerator: "))
arg2 = float(input("Please enter a denominator: "))
divide_nums(arg1, arg2)


# Task2
def print_user_data(name, surname, city, email, phone):
    return print(name, surname, city, email, phone)


print_user_data(name="Artur", surname="Nur", city="South_Pole",
                email="a.n@expert.py", phone=999999999)


# Task3
def my_func(arg1, arg2, arg3):
    args = (arg1, arg2, arg3)
    return sum(args) - min(args)

print(my_func(1000, 200, 300))


# Task4
def my_func1(x, y):
    return x ** y


def my_func2(x, y):
    temp = 1
    for i in range(abs(y)):
        temp = temp * x
    return 1/temp


print(my_func1(4, -3))
print(my_func2(4, -3))

# Task5
def sum_nums():
    nums = 0
    while True:
        list_nums = input("Please enter numbers separated by spaces. "
                          "Type 'q' to interrupt the process: ").split()
        for num in list_nums:
            try:
                nums += int(num)
            except ValueError:
                return print(f"Total value is {nums}")
        print(f"Current sum is {nums}")


sum_nums()

# Task6
def int_func(word):
    return word.capitalize()


def cap_sentence(sentence):
    return " ".join([int_func(word) for word in sentence.split()])


print(int_func("python"))
print(cap_sentence("practice makes perfect!"))

