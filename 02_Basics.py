# lists
list_1 = ["Hello", 3.14, True, 42, "cat", "dog"]
print("List:", list_1)
print("This is 1st item of the list:", list_1[0])       # integer number in the square brackets are indexes of the list
print("This is 1st item of the list:", list_1[1])       # indexes range from 0 to (n - 1) items in the list
print("This is 1st item of the list:", list_1[2])       # indexes can only be integer values and not floating-point number
print("Negative indexing:", list_1[-1])         # negative indexing starts index from last of the list and -1 means last item
print("Negative indexing:", list_1[-2])         # -2 means second-last item of the list
print()

list_2 = []     # empty list

list_3 = [["cat", "dog", "elephant"], [1, 2, 3, 4, 5, 6]]       # there can exist a list in a list
print("Another example:", list_3[0])
print("Another example:", list_3[0][1])         # indexing of a list inside a list
print()

# slicing of the list
list_4 = ["cat", "dog", "elephant", "horse", "cheetah", "jaguar", "leopard"]
print("Sliced list:", list_4[1:4])          # it slices the list from the first index and upto the second index but won't include it
print("Sliced list with leaving the last item:", list_4[0:-1])
print("Sliced list with first index empty:", list_4[:4])        # it'll start from zeroth index and go upto second index excluding it
print("Sliced list with second index empty:", list_4[3:])       # it'll start from third index and go upto last of list
print()

# length of the list - using len() function
print("The length of the list is:", len(list_4))        # len() function returns the length of the list/string/etc.
print()

# changing values of the list with indexes
list_5 = ["cat", "dog", "falcon", "horse", "cheetah", "jaguar", "rabbit", "cow", "buffalo"]
list_5[3] = "eagle"
print("Changed the value of 3rd index from horse -> eagle:", list_5)
print()

# list concatenation and list replication
concatenated_list = [1, 2, 3] + ['A', 'B', 'C']
print("Concatenated list:", concatenated_list)
replicated_list = ['X', 'Y', 'Z'] * 3
print("Replicated list:", replicated_list)
eg_list = [1, 2, 3]
eg_list = eg_list + [4, 5, 6]
print("Appending list:", eg_list)
print()

# removing item from the list - using 'del' statement
item_remove = ["lion", "tiger", "cheetah", "jaguar", "leopard"]
del item_remove[3]          # 'del' statement can also be used on a simple variable to delete it
print("Deleted 3rd index item from the list:", item_remove)
print()

# working with lists
catNames = []
while True:
    print("Enter the name of cat " + str(len(catNames) + 1) + " (Or enter nothing to stop.):")
    name = input()
    if name == "":
        break
    catNames = catNames + [name]  # list concatenation
print("The cat names are:")
for name in catNames:
    print("  " + name)
print()

# in and not in operators
myPets = ["Zophie", "Pooka", "Fat-tail"]
print("Enter a pet name:")
name = input()
if name not in myPets:
    print("I do not have a pet named", name)
else:
    print(name, "is my pet.")
print()

# looping with lists
supplies = ["pens", "pencils", "erasers", "sharpeners", "staplers", "paper clips", "markers"]
for i in range(len(supplies)):
    print("Index", i, "in supplies is:", supplies[i])
print()

# using enumerate() function with lists
# instead of using range(len(anyLists)) rather use enumerate() function it returns two values first index and second item
stationarySupplies = ["notebooks", "tapes", "pens", "pencils", "erasers", "paper clips", "pages"]
for index, item in enumerate(stationarySupplies):
    print("Index", index, "in supplies is:", item)
print()

# using random.choice() and random.shuffle() functions with lists
import random
animals = ["lions", "tigers", "hynas", "wolves", "leopards", "cheetahs", "giraffes"]
print("Any random animal:", random.choice(animals))
print()

# random.shuffle() - this function doesn't returns anything but modifies the list
people = ["Alice", "Bob", "Carol", "David"]
print("Here's list:", people)
random.shuffle(people)
print("Here's same shuffled list:", people)
print()

# augmented assignment operator
# spam += 1 --> spam = spam + 1
# spam -= 1 --> spam = spam - 1
# spam *= 1 --> spam = spam * 1
# spam /= 1 --> spam = spam / 1
# spam %= 1 --> spam = spam % 1
eg = "Hello"
eg += " World!"
print("Using augmented assignment operator:", eg)

food = ["Burger", "Chipottle", "Pizza"]
food *= 2
print("Using augmented assignment operator:", food)
print()

# methods - index(), append(), insert(), remove(), sort(), reverse()
# A method is the same thing as a function, except it is "called on" a value, Each data type has its own set of methods
# methods are list methods and can be called only on list values, not on other values such as strings or integers
list_6 = ["hello", "hi", "howdy", "heya", "howdy"]
print("The index of 'hi' is", list_6.index("hi"))       # returns the index of the value, and if the value doesn't exists then produces ValueError
print("The index of 'howdy' is", list_6.index("howdy"))     # if there exists two same values then the index of the first appearance is returned
# print("This doesn't exists:", list_6.index("namaste"))        # produces ValueError
print()

# append()
birds = ["pigeon", "crow", "peacock", "falcon", "sparrow", "eagle", "vulture"]
print("List:", birds)
birds.append("owl")     # append() method call adds the argument to the end of the list
print("Modified list after appending 'owl':", birds)

# insert() - this method call can insert a value at any index in the list
# first argument of the method is the index for the new value and second argument is the new value to be inserted
birds.insert(2, "hen")
print("Modified list after inserting 'hen' at 2nd index:", birds)

# remove() - this method is passed the value to be removed from the list
# attempting to delete the value which doesn't exists will result in a ValueError
# if there are two instances of the value then only the first instance of the value will be removed
birds.remove("pigeon")
print("Modified list after removing 'pigeon':", birds)

# sort() - number list or string list can be sorted with this method call, and it doesn't return any value it just modifies the list
# cannot sort lists that have both number values and string values in them, since Python doesn’t know how to compare these values
# uses "ASCIIbetical order" rather than actual alphabetical order for sorting strings - means uppercase before lowercase
number_list = [6, 3, 0, -3, 39, 23, 2, -2, -5, -10]
number_list.sort()
print("The sorted number list:", number_list)    # sorts the list in ascending order
number_list.sort(reverse=True)
print("The sorted number list:", number_list)    # sorts the list in descending order

string_list = ["cats", "cows", "fish", "dogs", "horses", "tortoises"]
string_list.sort()
print("Sorted string list:", string_list)

sort_list_example = ["a", "z", "A", "Z"]
sort_list_example.sort(key=str.lower)
print("For sorting this way:", sort_list_example)

# reverse() - doesn't returns any value
reverse_list = ["cat", "ant", "dog"]
reverse_list.reverse()
print("Reversed list:", reverse_list)
print()