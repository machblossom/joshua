# File: homework4.py

# --- Lists ---


# List Operations

favFoods = ["pizza", "chicken wings", "watermelon", "tacos", "burger"]

print(favFoods[1])
print(favFoods[-1])

favFoods.append("broccoli")
favFoods.insert(0, "apple")
favFoods.remove("chicken wings")

print(len(favFoods))

for food in favFoods: 
    print(food.upper())
    
newFood = favFoods[0:6:5]  

if ("potato" in favFoods):
    print("A potato!")
else: 
    print("No potato!")


# Slicing and Striding

numbers = list(range(21))

def get_first_15(numbers):
    return numbers[0:15]

def get_every_5th(lst):
    return lst[::5]

def reverse_and_stride(lst):
    lst.reverse()
    return lst[::3]


step1 = get_first_15(numbers)
step2 = get_every_5th(step1)
step3 = reverse_and_stride(step2)


# Nested Lists

numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def sum_nested(lst):
    sum = 0
    for row in lst:
        for num in row:
            sum += num
    return sum


print(numbers[2])
print(numbers[1][1])
numbers.append([10, 11, 12])
sum_nested(numbers)


# Create a 5x5 List

def create_list():
    lst = []
    number = 1
    for i in range(5):
        row = []
        for j in range(5):
            row.append(number)
            number += 1
        lst.append(row)
    return lst

def replace_mult_of_three(lst):
    new_lst = []
    for row in lst:
        new_row = []
        for num in row:
            if num % 3 == 0: 
                new_row.append("?")
            else:
                new_row.append(num)
        new_lst.append(new_row)        
    return new_lst

def sum_integer_elements(lst):
    sum = 0
    for row in lst:
        for integer in row:
            if integer != "?":
                sum += integer
    return sum            


five_by_five = create_list()
fbf_mult_of_three = replace_mult_of_three(five_by_five)
fbf_sum_elements = sum_integer_elements(fbf_mult_of_three)


# --- Dictionaries ---


# Dictionary Operations

ages = {
    "Katie": 30,
    "Mariam": 42,
    "Safia": 25,
    "Mira": 48
}


print(ages['Katie'])
ages['Mira'] = 100
ages["Milana"] = 52
del ages['Mariam']

for key, value in ages.items():
    print(key, ":", value)



fbf_sum_elements = sum_integer_elements(fbf_mult_of_three)
print(fbf_sum_elements)






