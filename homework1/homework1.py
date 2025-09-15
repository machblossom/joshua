# File: homework1.py

# --- Variables and Data Types ---

a = 10
print(a)
print(type(a)) # a is an integer, a whole number with no decimals

b = 1.5
print(b)
print(type(b)) # b is a floating-point number, a number with decimals
 
c = 3j
print(c)
print(type(c)) # c is a complex number, contains a real and an imaginary part

d = "hello"
print(d)
print(type(d)) # d is a string, sequences of characters

e = [1, 2, 3]
print(e)
print(type(e)) # e is a list, ordered, mutable collections of items

f = {"name": "Ellen", "favorite fruit": "Strawberry"}
print(f)
print(type(f)) # d is a dictionary, unordered collections of key-valued pairs

g = (1, 2)
print(g)
print(type(g)) # g is a tuple, ordered, immutable collections of items

h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) # h is a list, ordered, mutable collections of items

i = True
print(i)
print(type(i)) # i is a boolean, representing truth values: True or False

j = None
print(j)
print(type(j)) # j is a NoneType, represents the absence of a value

k = [True, "blue", 12]
print(k)
print(type(k)) # k is a list, ordered, mutable collections of items

l = str(14)
print(l)
print(type(l)) # l is a string, sequences of characters

m = 1e4
print(m)
print(type(m)) # m is a floating-point number, a number with decimals

n = range(9)
print(n)
print(type(n)) # n is a range variable, it generates a sequence of numbers

"""
1. I found 9 different data types. 
2. I found: integer, float, complex, string, list, dictionary, tuple, boolean, and NoneType.
3. Variables b and m, d and l, e h and k have the same data types.
4. l has a string data type. It's not an integer because 14 is a string, the str() function
   converts a specific value into a string.
5. n = range(9)
"""

# --- Booleans ---

print(10 > 9) # True, 10 is greater than 9
print(10 == 9) # False, 10 is not equivalent to 9
print(10 <= 9) # False, 10 is not smaller than or equal to 9
print(bool("abc")) # True, 
print(bool(123)) # True, 
print(bool(["apple", "cherry", "banana"])) #True, 
print(bool(True)) # True, 
print(bool(False)) # False, 
print(bool(0)) # False, 
print(bool("")) # False, 
print(bool(" ")) # True, 
print(bool(())) # False,
print(bool([])) # False,
print(bool({})) # False,
bool(True and False)
bool(True and True)
bool(False and False)
bool(True or False)
bool(True or True)
bool(False or False)
bool(not(False))
bool(not(True))