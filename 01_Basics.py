print("Hello World!")

# string concatenation
word_1 = "Hey"
word_2 = "World"
print("[Concatenated]: " + word_1 + word_2)
# print("Hello" + 42)   # won't work
print("Alice" * 4)      # prints "Alice" 4 times by concatenating
number_1 = 5
number_2 = 6
print("[By using string concatenated] Sum = " + str(number_1 + number_2))
print("Sum =", number_1 + number_2)
print()     # to add new line

# len() function
myName = "Your Name"
print("The length of 'Your Name' is", len(myName))
print()     # to add new line

# str(), int(), float() - data types
number = 45
print("[int to string]:", str(number))
print("[int to float]:", float(number))
print()     # to add new line

# operators/operands
# True = 2 + 2      # you can't assign values to a keyword - keyword are words that serve a specific functions
#                     and keyword cannot be used as a variable name, function name, etc.
print("'cat' == 'cat' is", "cat" == "cat")      # == checks if the left operand and right operand are equal or not, if yes then returns True.
print("'cat' != 'dog' is", "cat" != "dog")      # == checks if the left operand and right operand are equal or not equal, if yes then returns False.
print("42 == 42.0 is", 42 == 42.0)              # comparing integer 42 with float 42.0, and yes they're equal
print("'42' == 42 is", "42" == 42)              # string 42 is not equal to integer 42
print()     # to add new line

# boolean operators - and, or, not
print("True and True is", True and True)
print("True and False is", True and False)
print("True or True is", True or True)
print("True or False is", True or False)
# and - if both the operands are True then it returns True
# or - if any one the two operands is True then it returns True
print("not True is", not True)      # not - makes it opposite
print()     # to add new line

# mixing boolean and comparison operator
print("(4 < 5) and (5 < 6) is", (4 < 5) and (5 < 6))    # both happened to be True
print("(4 < 5) and (9 < 6) is", (4 < 5) and (9 < 6))    # (9 < 6) happened to be False, therefore whole statement is False
print("(1 == 2) or (2 == 2) is", (1 == 2) or (2 == 2))
print()     # to add new line

# flow control statements
number = int(input("Enter number: "))
if number % 2 == 0:
    print("Even.")
else:
    print("Odd.")
print()

# while loop
count = 0
while count < 5:
    print("Hello!")
    count = count + 1
print()

# break statement
randomWord = "Code"
while True:
    inputWord = input("Enter 'Code' as it is: ")
    if inputWord == randomWord:
        break           # break - this ends the loop, when the execution reaches break statement it immediately exits the loop
print()

# continue statement
while True:
    skipNumber = int(input("Enter number: "))
    if 0 <= skipNumber <= 10:
        break
    else:
        print("Only numbers between 0 to 10 are acceptable!")
for i in range(0, 11):
    if i == skipNumber:
        continue        # when execution reaches at the continue statement, then execution jumps back to the condition and revaluates the condition
    else:
        print(i)
print()

# functions
# the values which are passed while function call in the parentheses are called as function arguments
# the variable that you define in parentheses while defining function is called as function parameters
def greet(yourName):        # yourName - function parameter
    print("Hello", yourName.title() + "!")
greet("ganesh")             # "ganesh" - function argument
print()

# return statements and return values
# len() function returns the length of the string passed to it
def sum(num1, num2):
    return num1 + num2
print("The sum of 2 and 5 is", sum(2, 5))
print()

# global and local scope
# local scope - variables that are assigned inside the function are called as local scope, when the function returns the local scope variable destroys
# global scope - variable that are assigned outside the function are called as global scope, when the program exits the global scope variable destroys
# code in global scope cannot access local scope
# code in local scope can access the global variables
eggs = 10
def count():
    countOfEggs = eggs      # here local variable 'countOfEggs' has the access of global variable 'eggs'
    return countOfEggs
print("Number of eggs are", count())

def bookNumber():
    numberOfBooks = 99
    return numberOfBooks
# print(numberOfBooks)      # this won't execute, since 'numberOfBooks' is a local variable and it cannot be accessed globally

def example():
    global book
    book = 45       # this is global variable
    pen = 8         # this is local variable
example()           # but to access this global variable you need to call function first
print("This is global variable, but was assigned locally", book)

# exceptional handling
def spam(divideBy):
    return 42 / divideBy
try:
    print(spam(2))
    print(spam(12))
    print(spam(0))      # when the execution will reach this line it will cause whole program to crash
    print(spam(1))
except ZeroDivisionError:       # this is where except statement comes into play, it handles whatever will cause the program to crash
    print('Error: Invalid argument.')       # by generating any error message which the programmer wants to show, even it can perform any specific function too
print()

# ------------ Functions arguments and parameters ------------
def greet_person(name):     # here 'name' is a function parameter
    print("Hello " + name + "!")
greet_person("Simon")       # here 'Simon' is a function argument
# function parameters are called when function is defined
# function arguments are called when function is called
# the number of function arguments should always match with the number of function parameters
print()

# ------------------ Arbitrary arguments *args ------------------
# if you're unsure of number of arguments that will be passed into the function then
# add a * before the function parameter name while defining the function
def my_kids(*kid):
    print("My youngest kid is " + kid[2])
my_kids("Rohan", "Simran", "Tarun")
print()

# ---------------- More on function arguments ----------------
# you can also send arguments with the key = value syntax
# this makes the order of the arguments redundant
def my_kids1(kid_3, kid_1, kid_2):
    print("My youngest kid is " + kid_3)
my_kids1(kid_1="Rohan", kid_2="Simran", kid_3="Tarun")
print()

# ------------------- Arbitrary keyword arguments '**kwargs' -------------------
# if you don't know how many arguments that will be passed into your function
# add two ** before the parameter name while defining the function
# this will result in function receiving dictionary of arguments, and can access the items accordingly
def my_children(**kid):
    print("My eldest kid is " + kid["kid_1"])
my_children(kid_1 = "Rohan", kid_2 = "Simran", kid_3 = "Tarun")
print()

# ---------------------- Default parameter value ----------------------
def my_function(country = "Norway"):
  print("I am from " + country)
my_function("Sweden")       # here, country is set to "Sweden"
my_function("India")
my_function()               # since, no arguments in passed the default parameter value "Norway" is returned
my_function("Brazil")
print()

# ------------------- Passing a list as an argument -------------------
# you can send any data type of arguments into the function - strings, lists, integers, floats, dictionaries, etc.
def passing_list(food):
    for x in food:
        print(x)
fruits = ["Apple", "Mango", "Pineapple", "Banana", "Chickoo"]
passing_list(fruits)
print()

# --------------------- Positional-only arguments ---------------------
# to specify that a function can have only positional arguments, add ', /' after the arguments
def postional_arguments(x, /):
    print(x)
# postional_arguments(x = 3)        # will give an error
# without the ', /' you are actually allowed to use keyword arguments even if the function expects positional arguments
postional_arguments(3)
print()

# --------------------- Keyword-only arguments ---------------------
# to specify that a function can have only keyword arguments, add '*, ' before the arguments
def keyword_arguments(*, x, y):
    print(f"Using keyword-only arguments ---> {x} + {y} = {x + y}")
keyword_arguments(x = 3, y = 4)
# keyword_arguments(3, 4)           # will give an error
# without the '*, ' you are allowed to use positionale arguments even if the function expects keyword arguments
print()

# -------------- Combined Positional-only and Keyword-only --------------
# you can combine both positional and keyword arguments in the same function
# any argument before the '/ ,' are positional-only, and any argument after the '*, ' are keyword-only
def combine_positional_keyword_argument_function(a, b, /, *, c, d):
    print(a + b + c + d)
combine_positional_keyword_argument_function(5, 6, c=7, d=8)
print()

# ------------------- Recursion -------------------
def recursive_function(k):
    if (k > 0):
        result = k + recursive_function(k - 1)
        print(result)
    else:
        result = 0
    return result
print("Recursive function")
recursive_function(6)