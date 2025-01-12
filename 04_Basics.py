# unlike lists, the dictionaries have key-value pair, just like lists have index these have keys
# and indexes have values of them, here these have values of the keys, they're in key-value pair
my_dog = {"size": "fat", "color": "brown", "breed": "pug"}
# in above code snippet `size`, `color`, and `breed` are keys
# and `fat`, `brown`, and `pug` are its values respectively
print("The color of my dog is " + my_dog["color"])      # to access the value of any key we need to write it's key in place of index in lists
spam = {1234: "password combination", 47: "The answer"}     # dictionaries can use numbers as well for keys, but they shouldn't start from zero
print()

# dictionaries are unordered, unlike lists
list_1 = ["cats", "dogs", "horses"]
list_2 = ["dogs", "cats", "horses"]
print("list_1 == list_2:", list_1 == list_2)    # lists are different, when order is changed, because they're ordered
print()

# dictionaries are unordered
dict_1 = {"name": "mike", "age": 30, "occupation": "software engineer"}
dict_2 = {"age": 30, "occupation": "software engineer", "name": "mike"}
print("dict_1 == dict_2:", dict_1 == dict_2)        # even after changing the order the dictionaries are the same, because they're unordered
print()

# methods in dictionaries - key(), values(), and items()
# these return list-like values but they aren't lists, they cannot be modified and have an append() method, but can be used in loops
method_dict = {"color": "red", "age": 42}
for v in method_dict.values():      # `values()` method returns values of the keys in the dictionary
    print(v)
for k in method_dict.keys():        # `keys()` method returns the keys in the dictionary
    print(k)
for i in method_dict.items():       # `items()` method returns the tuple of key-value pair in the dictionary
    print(i)
print()

# if you want list-like return then
print("Return value of keys() method:", method_dict.keys())
print("Changing the return value of keys() method to list:", list(method_dict.keys()))
print()

# multiple assignment trick in the loop
for k, v in method_dict.items():
    print("Key: " + k + " and its value: " + str(v))
print()

# checking whether a key or value exists in a dictionary - `in` or `not in`
fruit_dictionary = {"name": "mango", "color": "yellow", "taste": "sweet", "price": 100}
print("Whether 'name' exists in the dictionary:", "name" in fruit_dictionary.keys())
print("Whether 'sweet' exists in the dictionary:", "sweet" in fruit_dictionary.values())
print("Whether 'apple' exists in the dictionary:", "apple" in fruit_dictionary.values())
print("Whether 'lemon' doesn't exists in the dictionary:", "lemon" not in fruit_dictionary.values())
print("Check 'number of fruits' exists in the dictionary:", "number of fruits" in fruit_dictionary)     # `in fruit_dictionary` is short for fruit_dictionary.keys()
print()

# `get()` method - it takes two arguments the key of the value to retrive and a fallback value to return if that key doesn't exists
picnic_items = {"apples": 5, "cups": 2, "bread": 3, "ketchup": 1, "mat": 1}
print("I am bringing " + str(picnic_items.get("cups", 0)) + " cups.")
print("I am bringing " + str(picnic_items.get("eggs", 0)) + " eggs.")   # since there's no `eggs` key in the dictionary,
#       then the default value 0 is returned by the `get()` method
# print("I am bringing " + str(picnic_items["eggs"]) + " eggs.")        # since there is no key named `eggs` but by this method this will give an error

# `setdefault()` method call - first argument passed to the method is the key to check for
# and the second argument is the value to set at that key if the key doesn't exists, if the key does exists then
# setdefault() method returns the key's value
info_dict = {"name": "mike", "age": 4}
info_dict.setdefault("color", "black")      # there wasn't key named `color` so `setdefault()` method set `color` to `black`
print("The dictionary is:", info_dict)
info_dict.setdefault("color", "white")      # there's already value for the key `color` so the setdefault doesn't change it to `white`
print("The dictionary is:", info_dict)
print()

# if `setdefault()` method call didn't existed
any_random_dict = {"name": "tim", "age": 43, "profession": "software engineer", "nationality": "russian"}
if "salary" not in any_random_dict:
    any_random_dict["salary"] = 100000
print("The dictionary:", any_random_dict)

if "salary" not in any_random_dict:
    any_random_dict["salary"] = 200000
print("The dictionary:", any_random_dict)
print()

# dictionaries can contain other lists and dictionaries
all_guests = {"Mike": {"apples": 3, "mangoes": 6, "pineapples": 5},
              "Matt": {"guavas": 2, "oranges": 3, "chickoos": 4},
              "Ben": {"pineapples": 4, "kiwis": 5, "mangoes": 8},
              "Stacy": {"apples": 10, "chickoos": 8, "oranges": 2}}

def total_items_bought(guests, item):
    total = 0
    for guest, fruit in guests.items():
        total = total + fruit.get(item, 0)
    return total

print("Apples     --> " + str(total_items_bought(all_guests, "apples")))
print("Mangoes    --> " + str(total_items_bought(all_guests, "mangoes")))
print("Oranges    --> " + str(total_items_bought(all_guests, "oranges")))
print("Guavas     --> " + str(total_items_bought(all_guests, "guavas")))
print("Kiwis      --> " + str(total_items_bought(all_guests, "kiwis")))
print("Chickoos   --> " + str(total_items_bought(all_guests, "chickoos")))
print("Pineapples --> " + str(total_items_bought(all_guests, "pineapples")))
print()
