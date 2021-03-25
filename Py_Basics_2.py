# Task1
data_list = [1, 'Hi', {'a': 1, 'b': 2}, (2, 3), 3.141856, [100, 200]]

for i in range(len(data_list)):
    print(f"{i} element' type is {type(data_list[i])}")

# Task2
in_data =True
data_col = []
while in_data:
    data = input("Enter some data: ")
    if data:
        data_col.append(data)
        print(f"Data collection includes {len(data_col)}\n")
    else:
        break

data_col = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(len(data_col)//2):
    data_col[i*2 + 1], data_col[i*2] = data_col[i*2], data_col[i*2 + 1]
print(data_col)


# Task2 (list)
def define_season(month_number):
    season_list = ['winter', 'winter', 'spring', 'spring', 'spring', 'summer',
            'summer', 'summer', 'autumn', 'autumn', 'autumn', 'winter']
    if 0 < month_number < 13:
        print(f"Month with a number {month_number} is "
              f"{season_list[month_number-1]} month.")
    else:
        print("You entered out of required range number")
    return None


month_number = int(input("Please enter a number of "
                         "a month (from 1 through 12): "))
define_season(month_number)


# Task2 (dict)
def define_season(month_number):
    season_dict = {1: 'winter', 2: 'winter', 3: 'spring', 4: 'spring',
                   5: 'spring', 6: 'summer', 7: 'summer', 8: 'summer',
                   9: 'autumn', 10: 'autumn', 11: 'autumn', 12: 'winter'}
    if 0 < month_number < 13:
        season_name = [value for key, value in season_dict.items()
                       if key == month_number]
        print(f"Month with a number {month_number} is "
              f"{season_name[0]} month.")
    else:
        print("The number entered is out of required range.")
    return None


month_number = int(input("Please enter a number of "
                         "a month (from 1 through 12): "))
define_season(month_number)


# Task4
def create_words_list(words):
    words_list = words.split()
    for i, word in enumerate(words_list):
        print(i + 1, word[:11])
    return None


words = input("Enter a few words separated by a space: ")
create_words_list(words)


# Task5
def make_rating(data):
    my_list.append(data)
    my_list.sort(reverse=True)
    return print(my_list)

my_list = [7, 5, 3, 3, 2]
in_data =True
while in_data:
    data = input("Enter some number: ")
    if data:
        make_rating(int(data))
    else:
        break


# Task 6*
data_list = []
data_keys = ['название', 'цена', 'количество', 'eд']
questions = ["Enter asset's name: ",
             "Enter asset's price (only integer): ",
             "Enter asset's quantity (only integer): ",
             "Enter asset's measuring type: "]
print("Please enter required data. To quit, type 'q'.")
count = 1
in_data =True
while in_data:
    item_dict = {}
    for i in range(0, 4):
        input_data = input(questions[i])
        if input_data == 'q':
            item_dict = {}
            in_data = False
            break
        elif i == 1 or i == 2:
            input_data = int(input_data)
        else:
            input_data = input_data
        if  input_data:
            item_dict[data_keys[i]] = input_data
    print(f"You entered {item_dict}\n")
    data_list.append((count, item_dict))
    count += 1
print(data_list)

