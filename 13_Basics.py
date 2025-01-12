# --------------- Lambda functions ---------------
# these are anonymous functions i.e. without any name
# for defining normal function `def` keyword is used but
# for defining lambda function `lambda` keyword is used
# these lambda functions can have only one expressions and it is always returned

x = "An example string"
# print(lambda x : x)         # this will return memory location and not the string
(lambda x : print(x))(x)

# Difference between normal and lambda function
def normalFunctionCube(randomNumber):           # Normal function
    return randomNumber ** 3

lambdaFunctionCube = lambda x : x ** 3          # Lambda function

print("Using normal function:", normalFunctionCube(5))   # calling normal function
print("\nUsing lambda function:", lambdaFunctionCube(3))   # calling lambda function

# ------------- Lambda function with list comprehension -------------
tables = [lambda z=z : z * 10 for z in range(1, 11)]    # `x = x` ensures the current value of x is captured
for table in tables:
    print(table())

# -------------- Lambda function with if-else --------------
Max = lambda a, b : a if(a > b) else b
print("\nMaximum number is", Max(1, 2))

# ---------- Lambda function with multiple statement ----------
# lambda function doesn't allow multiple statements, but we can create two lambda functions
# and then call the other lambda function as a parameter to the first parameter to the first function
list = [[2, 3, 4], [1, 4, 16, 64], [3, 6, 9, 12]]
sortList = lambda x : (sorted(i) for i in x)
secondLargest = lambda x, f : [y[len(y) - 2] for y in f(x)]
res = secondLargest(list, sortList)
print(res)

# reversing a string by using `[::-1]` indexing
exampleString = "\nReverse string"
print(exampleString[::-1])

# reversing a string by using built-in join and reversed function
reverseString = "".join(reversed(exampleString))    # `reversed()` function doesn't returns string
print(reverseString)                                # it returns a reversed iterator of the characters in the string

# some more about `join()` method
# basic syntax: `separator.join(iterable)`
wordsJoin = ["Hello", "World", "!"]
print(" ".join(wordsJoin))
print()

charactersJoin = ["H", "e", "l", "l", "o"]
print("".join(charactersJoin))
print()

numbers = ["1", "2", "3", "4", "5", "6", "7", "8"]
print("-".join(numbers))
print()

# deleting and updating from a string
# strings are immutable, therefore updation and deletion of characters isn't allowed
# although entire string could be deleted with built-in `del` keyword

# string1 = "Initial string"        # this block of code isn't working i tried everything
# string_list = list(string1)
# string_list[2] = "x"
# print("".join(string_list))

# updating entire string
stringExample1 = "This is initial string."
print(stringExample1)
stringExample1 = "This is updation of the entire string."
print(stringExample1)
print()

# deletion of a character
stringExample2 = "Deleting a character from this string."
print("Initial string:", stringExample2)
updatedString = stringExample2[0:3] + stringExample2[4:]
print("Updated string after deleting a character:", updatedString)
print()

# deleting an entire string
stringExample3 = "An example string."
print("Initial string:", stringExample3)
del stringExample3              # using `del` keyword we can delete an entire string
# print("String after deleting entire string:", stringExample3)     # printing that string will produce an error
print()

# formating a string
# strings can be formatted with the use of format() method
# `{}` act as a placeholders that can hold arguments
stringExample4 = "{} {} {}".format("Bus", "Train", "Aeroplane") # default order formatting
print("Strings in default order:", stringExample4)

stringExample5 = "{2} {0} {1}".format("Bus", "Train", "Aeroplane")  # positional formatting
print("Strings in positional order:", stringExample5)

stringExample6 = "{l} {o} {m}".format(m="Train", l="Bus", o="Aeroplane")    # keyword formatting
print("Strings in keyword order:", stringExample6)
print()

# printing single and double quotes
# print('It'll give an error - Single quotation between single quotes')                 # gives an error
print("It won't give error - Single quotation between double quotes")                   # won't give error
# print("This language is called "Python" - Double quotation between double quotes")    # gives an error
print('This language is called "Python" - Double quotation between single quotes')      # won't give error
print()

# Programming convention (Generally)
# Single quotes - are used for regular expressions, dict keys, and SQL
# Double quotes - are used for string representation

# Escape character - `\`
# employ a backslash `\` before a double quote and it is escaped
stringUsingEscape = "This text is in between \"double quotes\" and \"escape character\""     # using `\` before the double quote
print("Escape character string:", stringUsingEscape)
print()

# Another method ---> Using triple quotes
stringUsingTripleQuotes = """This text is in between "triple quotes" """
print("Triple quotes string:", stringUsingTripleQuotes)
print()
