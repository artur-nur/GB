# Task 1
def divide_nums(divident, divider):
    if divider != 0:
        return print(divident / divider)
    else:
        print("Division to zero! Please enter a non-zero divider")


divident = float(input("Please enter a divident: "))
divider = float(input("Please enter a divider: "))
divide_nums(divident, divider)


# Task2
def print_user_data(name, surname, city, email, phone):
    return print(name, surname, city, email, phone)


print_user_data(name="Artur", surname="Nur", city="London",
                email="artur.nur@tesla.com", phone=999999999)


# Task3
def my_func(arg1, arg2, arg3):
    minimal_num = min(arg1, arg2, arg3)
    return print(arg1 + arg2 + arg3 - minimal_num)

[arg1, arg2, arg3] = [1000, 200, 300]
my_func(arg1, arg2, arg3)


# Task4
def my_func(x, y):
    pass

# поздно начал, не успел, как перенести срок