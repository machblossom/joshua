# File: homework3.py

# --- Print Functions ---

name = "Joshua"
radius = 5

# prints a goodbye message
def say_goodbye(name):
    print("Goodbye,", name)

# prints the area of a circle based on a given radius
def area_of_circle(radius):
    pi = 3.14
    print(pi * (radius ** 2))

say_goodbye(name)
area_of_circle(radius)


# --- Return Fuctions ---

a = 2
b = 5

# Returns the difference of a and b
def subtract(a, b):
    return (a - b)

# Returns the product of a and b
def multiply(a, b):
    return (a * b)

# Returns the quotient of a and b
def divide(a, b):
    return (a / b)

print(subtract(a, b))
print(multiply(a, b))
print(divide(a, b))