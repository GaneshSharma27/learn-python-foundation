# mutable and immutable data types
# mutable - type of data types that can change, remove the values stored in it
# list is a mutable data type, however the string is immutable data type, it cannot be changed
name = "Zophie is a cat"        # immutable, therefore not modified
newName = name[0:7] + "the" + name[11:15]       # instead created a new string
print(newName)
print()

# lists are mutable
example_list = [1, 2, 3, 4]
print("Original list:", example_list)
example_list = [6, 7, 8, 9]
print("Modified list:", example_list)
print()

# Tuple - An immutable data type
example_tuple = ("hello", 1, 4, 0.25)
print("Tuple item:", example_tuple[0])
print("Tuple item:", example_tuple[1:4])
print("Length of the tuple:", len(example_tuple))

# example_tuple[0] = 7.8        # will give out error

# converting types with list() and tuple() function
new_tuple = tuple(["cat", "dog", 5])
print("List [\"cat\", \"dog\", 5] to tuple:", new_tuple)
new_list = list(("cat", "dog", 5))
print("Tuple (\"cat\", \"dog\", 5) to list:", new_list)
print("List(\"hello\"):", list("hello"))
print()

# reference
x1 = 32        # when 32 is assigned in x1, it assigns the reference of the 32 stored in the computer memory
x2 = x1        # when x1 is assigned in x2, it assigns the reference of the 32 stored in the computer memory
print("Value of x1:", x1)
print("Value of x2:", x2)
x1 = 100        # when 100 is assigned in x1, it assigns the new reference of the new value 100 stored in the memory location
print("Value of x1:", x1)
print("Value of x2:", x2)       # since integers are immutable value, x2 remains unchanged
print()

l1 = [1, 2, 3, 4, 5, 6]     # lists are mutable
l2 = l1
print("List 1:", l1)
print("List 2:", l2)
l2[1] = "hi"
print("List 1:", l1)
print("List 2:", l2)
print()

# identity and the id() function - it returns the memory address where the string is stored
# python picks this address based on which memory bytes happen to be free on the computer at that time
# so each time when you execute this program it'll be different
print("Memory address of the string 'Howdy':", id("Howdy"))
word = "Hello"
print("The memory address of the variable 'word' that stores string 'Hello':", id(word))
word += " World!"
print("The memory address changed, variable 'word' now refers to a completely different string:", id(word))
print()

# however this is different in case of lists
list_id = ["Milo", "Rookie", "Sam", "Zara"]
print("Memory address of the list:", id(list_id))
list_id.append("Monica")
print("Memory address of the same list (hasn't changed):", id(list_id))
print()

# copy module's copy() and deepcopy() function
# it is used to make copy of the mutable data types like lists, or dictionaries
# it doesn't make the copy of the reference (memory address)
import copy
list_example = ["A", "B", "c", "D"]
print("Memory address of the list 'list_example':", id(list_example))
list_copy = copy.copy(list_example)
print("Memory address of the list 'list_copy':", id(list_copy))
list_copy[2] = 32
print("List_example:", list_example)
print("List_copy:", list_copy)
print()
