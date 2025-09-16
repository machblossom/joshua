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
print(bool("abc")) # True, contains a string (is not empty)
print(bool(123)) # True, contains numbers (is not empty)
print(bool(["apple", "cherry", "banana"])) # True, contains words in a list (is not empty)
print(bool(True)) # True, True truth value returns True
print(bool(False)) # False, False truth value returns False
print(bool(0)) # False, contains a zero integer
print(bool("")) # False, string is empty
print(bool(" ")) # True, string is not empty (whitespace is not empty)
print(bool(())) # False, parentheses are empty
print(bool([])) # False, brackets are empty
print(bool({})) # False, curly brackets are empty
print(bool(True and False)) # False, "and" requires both to be True
print(bool(True and True)) # True, both are true
print(bool(False and False)) # False, "and" requires both to be True
print(bool(True or False)) # True, "or" requires at least one to be True
print(bool(True or True)) # True, "or" requires at least one to be True
print(bool(False or False)) # False, neither are True
print(bool(not(False))) # True, not() reverses the truth value of False
print(bool(not(True))) # False, not() reverses the truth value of True

"""
1. The expressions returning True contain values or "something" inside of it,
   like strings or numbers in between things. Those returning False
   contain nothing, or have the value 0.
2. The expression result that surprised me was "print(bool(" "))" in that it
   returned True. Even a spacec in parentheses can be interpreted as being 
   "something" in between things.
3. "print(bool([" "]))" Will return True. It contains quotation marks (string)
   indicating that there is "something" in between the brackets.
4. "print(bool([ ]))" will return False. Even though there is a space in
   between the brackets, it isn't inside quotation marks (string) so it
   will return False.
"""

# --- Operators --- 

print(10 + 5) # 15, + performs addition
print(10 - 5) # 5, - performs subtraction
print(2 * 4) # 8, * performs multiplication
print(6 / 3) # 2.0, / performs division (leaves as float)
print(5 % 2) # 1, % performs division (but prints out the remainder)
print(3 ** 2) # 9, ** performs exponentials
print(15 // 2) # 7, performs division (does not leave as float (rounds down))

print(5 == 2) # False, == returns truth value stating if A is equivalent to B
print(10 != 10) # False, != returns truth value stating if A isn't equivalent to B
print(2 < 5) # True, < returns truth value stating if A is smaller than B
print(12 > 5) # True, > returns truth value stating if A is bigger than B
print(5 <= 6) # True, <= returns truth value stating if A is smaller or equal to B
print(1 >= 10) # False, >= returns truth value stating if A is bigger or equal to B

x = 5 
print(x) 
x += 5 # 10, adds 5 to original value of x (5 + 5 = 10)
print(x)
x -= 4 # 6, subtracts 4 from previous value of x (10 - 4 = 6)
print(x)
x *= 3 # 18, multiplies 3 to the previous value of x (6 * 3 = 18)
print(x)

"""
1. The logic operator "and" returns a True truth value if all 
   operands have a True truth value.
   a = 2
   b = 5
   True: print(a > 1 and b < 10)
   False: print(a > 1 and b > 10)
2. The logic operator "or" returns a True truth value if at
   least ONE operand has a True truth value.
   a = 1
   b = 2
   True: print(a == 1 or b == 5)
   False: print(a == 4 or b == 9)
3. The logic operator "not" returns the reversed truth value
   of the expression.
   True: print(bool(not(False)))
   False: print(bool(not(True)))

1. "/" leaves the quotient as a float. "//" leaves the quotient 
   as an integer.
2. "%" prints out the remainder of a division problem. "//"
   leaves the quotient as an integer, without the remainder.
3. When calculating the remainder by dividing two numbers,
   one must use the "%" operator.
   print(36 % 5) # Prints out 1
4. Assignment operators work by assigning values or characters
   to variables.
"""

# --- Strings ---

my_string = "hello"

print(my_string) # Prints: hello
print(my_string[0]) # Prints: h
print(my_string[1]) # Prints: e
print(my_string[2]) # Prints: l
print(my_string[3]) # Prints: l
print(my_string[4]) # Prints: o
print(my_string[-1]) # Prints: o
print(my_string[1:3]) # Prints: el (slicing)
print(my_string[0:5:2]) # Prints: hlo (slicing)
print(len(my_string)) # Prints: 5
my_string += "goodbye"
print(my_string) # Prints: hellogoodbye
my_string = "hello"
print(my_string * 7) # Prints: hellohellohellohellohellohellohello

"""
1. Slicing returns a new sequences of strings from our original
   expression. Slicing was done for 8. and 9. 
2. The result is "Hello, my name is Oski".
3. The result is "Hello, my name is Oski".
4. f strings allow for expressions like variables, function, 
   and operations to be directly embedded within the string
   by enclosing them in curly braces {}.
"""

# --- Terminal Commands ---

# cd
# Changes directories. Use it to move from one folder to another.
# Example: cd Desktop
# ls
# Lists all content in current directory.
# Example: (while in python_decal_fall25) ls
# ls -a
# Lists all content (hidden as well) in current directory.
# Example: (while in python_decal_fall25) ls -a
# mkdir
# Creates a new daughter directory in current (parent) directory.
# Example: mkdir new_directory
# cat
# Prints out the script of code from file.
# Example: cat test.py
# pwd
# Prints out the current working directory.
# Examples: (while in python_decal_fall25) pwd
# cd ..
# Moves up one directory (to parent)
# Example: cd ..
# cd .
# Changes directory to the current directory
# Example: cd .
# cd ~
# Changes directory to the user's home directory
# Example: cd ~
# cp
# Copies files and directories to paste them to others.
# Example: cp test.py lecture_notes/
# mv
# Moves files to directories and can rename them.
# Example: mv test.py joshua/
# rm
# Removes files from a Git repository.
# Example: rm test.py
# clear
# Clears the terminal screen.
# Example: clear
# grep
# Looks for specific content in text files
# Example: grep "dog" animals.txt

"""
1. "head" prints out the beginning of a file: head homework1.py
   "tail" prints out the end of a file: tail homework1.py
   "history" prints out a list of previously used commands: history
2. "ls" prints out all content from a directory. "ls -a" prints out
   all content from a directory, including hidden content.
3. A hidden file is a file that is not displayed by default in a 
   file browser.
4. "-l" the -l flag from ls -l displays a long list of content.
   "-i" the -i flag from rm -i prompts for confirmation before deletion.
   "-f" the -f flag from rm -f forces deletion without prompting.
"""