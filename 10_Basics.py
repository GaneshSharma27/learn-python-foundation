# ---------------- Python lambda ----------------
# it is a small anonymous function, it can take any number of arguments and can only have one expression
x = lambda a : a + 10
print("Using lambda function:", x(5))
multiply = lambda num_1, num_2 : num_1 * num_2
print("Multiplication using lambda function:", multiply(6, 4))
print()

# -------------------- Arrays --------------------
cars = ["Ford", "Volvo", "BMW", "Volkswagen", "Mercedes", "Hyundai", "Tata", "KIA"]
print("First array item:", cars[0])     # get the value of first array item
cars[0] = "Toyota"                      # modify the value of the first array item
print("Length of an array:", len(cars)) # use len() function to return the length of an array

# looping in an array
for x in cars:
    print(x)
print()

# adding array element
cars.append("Honda")
print("List after appending:", cars)
print()

# removing an element from an array
cars.pop(3)                         # pop() deletes using index of any array
print("List after poping:", cars)
cars.remove("Volvo")                # remove() deletes the item of an array, it only removes the first occurance of the specified value
print("List after removing an element:", cars)
print()

# array methods
# append() ---> Adds an element at the end of the list
# clear() ---> Removes all elements from the list
# copy() ---> Returns a copy of the list
# count() ---> Returns a number of elements with a specified value
# extend() ---> Adds the elements of the list (or any iterable), to the end of the current list
# insert() ---> Adds an element at the specified position
# index() ---> Returns the index of the first element with the specified value
# pop() ---> Removes the element at the specified position
# remove() ---> Removes the first item with the specified value
# reverse() ---> Reverses the order of the list
# sort() ---> Sorts the list

# append() method
fruits = ["apple", "banana", "mango"]
print("List before appending:", fruits)
fruits.append("orange")             # it appends at the end of the list
print("List after appending:", fruits)

list_1 = ["potato", "tomato", "chili", "lemon"]
list_2 = ["Ford", "BMW", "Toyota", "Tata"]
list_1.append(list_2)           # appends the list 2 as a list in list 1
print("List after appending list 2 in list 1:", list_1)
print()

# clear() method
fruit_example = ["Apple", "Mango", "Pineapple", "Orange", "Pomogranate", "Chickoo"]
print("List before using clear() method:", fruit_example)
fruit_example.clear()       # removes all the elements from the list
print("List after using clear() method:", fruit_example)
print()

# copy() method
exampleList = ["Pen", "Paper", "Ink", "Stamp", "Tape", "Ruler", "Compass"]
copiedList = exampleList.copy()
print("Copied list:", copiedList)
print()

# count() method
fruits = ["apple", "banana", "cherry", "kiwi", "mango", "chickoos", "cherry"]
cherryCount = fruits.count("cherry")
print("The cherry count is", cherryCount)


