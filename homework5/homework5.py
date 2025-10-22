# File: homework5.py


# --- Homework 1 + 2 Review ---

# 3.1 Vocabulary Review

"""

1. Git vs Github: Git is a control system whereas GitHub is a platform that hosts Git repositories.

2. Terminal vs Command Line: Terminal is the program that provides the environment for interacting with the command line.

3. Local vs Remote Repository: Local repository stays on the user's computer whereas Remote is accessible through internet or a network.

4. Version Control: The practice of tracking and managing changes to files like source code.

5. Staging Area: The space to prepare changes before committing them to the repository.

6. git add: A command used to add changes from the working directory to the Git staging area.

7. git commit: A command used to record changes to the local repository.

8. git push: A command used to upload local repository content to a remote repository like GitHub.

9. git status: A command used to display the current state of the Git working directory and the staging area.

10. git pull: A command used to fetch and download content from a remote repository and immediately update the local repository.

11. pwd: A command meaning print working directory used to show the path of the current directory you are in.

12. ls: A command meaning list used to list directory contents.

13. cd: A command meaning change directory which quite literally is used to change directory.

14. nano: A command used to edit files directly in the terminal.

15. touch: A command used to create empty files in the terminal.

16. mv: A command used to move and rename files and directories.

17. rm: A command used to remove files and directories.

18. cat: A command used to concatenate files.

"""

# 3.2 A Directory Tree

"""

1.  You have been plopped into Judy's directory system. What command will tell you what your
    current working directory is?
    pwd

2.  The terminal responds by saying you are in ~/python decal/judy decal. What command
    will list all the files in your current working directory?
    ls

3.  Oh no! Brianna just sent out an announcement saying that there was a typo in homework.py.
    You will need to pull the brianna repo repository to find the updated file. What command(s)
    will let you move to the correct repository and pull the latest changes?
    git pull

4.  How would you move this new homework.py to the homework/ folder in your personal repos-
    itory?
    mv homework.py brianna_repo/

5.  How would you move yourself to the same repository as homework.py?
    cd ~/python_decal/brianna_repo.py

6.  You want to see the contents of homework.py in your terminal, how would you do this?
    python3 homework.py

7.  Great job! You just finished the homework for this week. What command(s) allow you to
    save the changes and push from your local repository to your remote repository?
    git push

8.  Oh no! Git gave you the following error. What commands should you call to resolve this
    error and push your homework properly? What does the error mean? (i.e. what did “Judy”
    do wrong when trying to push?)
    "Judy" did not use the git pull command first.

9.  What absolute path will allow you to move to Recents/?
    ~/Recent/

"""


# --- Homework 3 Review ---

# 4.1 Data Types

input = 0

def checkDataType(input):
    return str(type(input))

print(checkDataType(input))

# 4.2 Conditionals

integer = 2

def evenOrOdd(integer):
    if ((integer % 2) == 0):
        return "Even"
    else:
        return "Odd"
    
print(evenOrOdd(integer))


# --- Loops ---

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lenOfnumbers = len(numbers)

def sumWithLoop(numbers):
    sum = 0
    for i in range(0,lenOfnumbers):
        sum += numbers[i]
    return sum

print(sumWithLoop(numbers))


# --- Homework 4 Review ---

# 6.1 Lists

listOfSomething = ['a', 'b', 'c']

def duplicateList(listo):
    newList = []
    for i in listo:
        newList.append(i)
        newList.append(i)
    return newList

print(duplicateList(listOfSomething))

# 6.2 Debugging

num = 5

"""
def square(num)
    return num * num
"""

def square(num): # The error in the above code is that the function didn't have a colon ":"
    return num * num

print(square(num))




# 7.2 In Your VS Code Terminal

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lenOfnumbers = len(numbers)

def sumWithLoop(numbers):
    sum = 0
    for i in range(0,lenOfnumbers):
        sum += numbers[i]
    return sum

print(sumWithLoop(numbers))

