# Continue from `13_Basics.py` file

# Printing escape character in Python
escapeString = "Using\nnew line and\thorizontal tab"
print("String using escape character:", escapeString)
print()

# Using `repr()` function - returns a string in printable format (doesn't resolve the escape character)
stringExample1 = "Using\nnewline and\thorizontal tab"
print("Without repr() function:", stringExample1)
print()
print("Using repr() function:", repr(stringExample1))
print()

# Using `r` or `R` - triggers a repr() function internally and stops from resolving the escape character
stringExample2 = r"Using\nnewline and\thorizontal tab"
print("Without r string:", stringExample1)
print()
print("With r string:", stringExample2)
print()

# Updatation of a character
stringExample3 = "This is an initial example string"
print("Initial string:", stringExample3)
list1 = list(stringExample3)        # since string is immutable, therefore we can't update a character in them
list1[14] = "x"                     # therefore, first converting to list and then changing then joining them as a string
stringExample4 = "".join(list1)
print("After updation of a character:", stringExample4)
print()

# Updatation of a character - 2nd way
stringExample5 = stringExample3[0:14] + "s" + stringExample3[15:]
print("After updation of a character:", stringExample5)
print()

# ------------------- Important string methods -------------------
# find(), rfind(), startwith(), endwith(), islower(), isupper(), lower(), upper(), swapcase(),

# --------------------------- find() ---------------------------
# finds the position of the substring within a string
# find("string", beg, end) - syntax
# by default `beg=0` and `end=len(string)`, beg and end are the indexes of the string
string1 = "The Great Wall of China is in China."
print("Doesn't exists then:", string1.find("Exist")) # returns `-1` if sub-string isn't found in the given string range
print("Exists then:", string1.find("Wall"))          # returns `11` since `example` is at 11th index
print()

# --------------------------- rfind() ---------------------------
# similar working as `find()`, but it returns the position of the last occurrence of string
# rfind("string", beg, end) - syntax
# by default `beg=0` and `end=len(string)`, beg and end are the indexes of the string
string2 = "New Delhi is the capital city of India. Mumbai is the capital city of the state of Maharashtra."
print("Doesn't exists then:", string2.rfind("Town")) # returns `-1` if usb-string isn't found in the given string range
print("Exists then:", string2.rfind("capital"))      # returns `54` since `capital` last occurance is at 54th index
print()

# --------------------------- startswith() ---------------------------
# returns true if the string begins with mentioned sub-string (prefix), else returns false
# startswith("string", beg, end) - syntax
# by default `beg=0` and `end=len(string)`, beg and end are the indexes of the string
string3 = "New York"
print("Begins with 'New':", string3.startswith("New"))   # returns True if string begins with mentioned sub-string
print("Begins with 'Baltimore':", string3.startswith("Baltimore"))   # returns False, if doesn't begins with mentioned sub-string
print()

# --------------------------- endswith() ---------------------------
# returns true if the string ends with mentioned sub-string (suffix), else returns false
# endswith("string", beg, end) - syntax
# by default `beg=0` and `end=len(string)`, beg and end are the indexes of the string
string4 = "Washington"
print("Ends with 'ton':", string4.endswith("ton"))   # returns True if string ends with mentioned sub-string
print("Ends with 'Wash':", string4.endswith("Wash"))  # returns False if doesn't ends with mentioned sub-string
print()

# --------------------------- islower() ---------------------------
# returns True if all the letters in the string are lower cased, otherwise False
string5 = "lowercase"
string6 = "UPPERCASE"
print("All lowercase?", string5.islower())
print("All lowercase?", string6.islower())
print()

# --------------------------- isupper() ---------------------------
# returns True if all the letters in the string are upper cased, otherwise False
print("All uppercase?", string6.isupper())
print("All uppercase?", string5.isupper())
print()

# --------------------------- lower() ---------------------------
# returns the new string with all the letters converted into its lower case
toLower = "India, USA, Canada, UK, Australia, New Zealand."
print("Converting to lowercase:", toLower.lower())
print()

# --------------------------- upper() ---------------------------
# returns the new string with all the letters converted into its upper case
toUpper = "there are many starving strayed dogs, and they need food and shelter."
print("Converting to uppercase:", toUpper.upper())
print()

# --------------------------- swapcase() ---------------------------
# used to swap the cases of string i.e upper case is converted to lower case and vice versa
swappingCases = "The Sun, The Moon, The Ocean, Iron, Aluminium, Copper - all are precious gifts of the nature."
print("Swapping the cases:", swappingCases.swapcase())
print()

# --------------------------- title() ---------------------------
# converts the string to its title case i.e the first letter of every word of string is upper cased and else all are lower cased
toTitlize = "samsung is the largest smartphone manufacturer in the world"
print(toTitlize.title())
print()

# --------------------------- len() ---------------------------
# returns the length of the string
stringLength = "Mumbai"
print("The length of the string:", len(stringLength))
print()

# --------------------------- count() ---------------------------
# counts the occurrence of mentioned substring in whole string
# count("string", beg, end) - syntax
# by default `beg=0` and `end=len(string)`
stringCount = "Go Goa Gone"
print("Number of times 'Go' appeared in the string:", stringCount.count("Go"))
print()

# --------------------------- center() ---------------------------
# used to surround the string with a character repeated both sides of string multiple times
# center(length of string, character) - syntax
# by default the character is a whitespace
stringAlign = "Aeroplanes"
print("Center align:", stringAlign.center(10, "*"))  # won't do anything, because the length of string is itself 10
print("Center align:", stringAlign.center(16, "*"))
print()

# --------------------------- ljust() ---------------------------
# returns the original string shifted to left that has a character at its right
# ljust(length of string, character) - syntax
# by default the character is a whitespace
print("Left align:", stringAlign.ljust(16, "*"))
print()

# --------------------------- rjust() ---------------------------
# returns the original string shifted to right that has a character at its left
# rjust(length of string, character) - syntax
# by default the character is a whitespace
print("Right align:", stringAlign.rjust(16, "*"))
print()

# --------------------------- isalpha() ---------------------------
# returns true when all the characters in the string are alphabets else returns false
alphabeticalString = "Lucknow"
print("All are alphabets?", alphabeticalString.isalpha())
print()

# --------------------------- isalnum() ---------------------------
# returns true when all the characters in the string are combination of numbers and/or alphabets else returns false
alphaNumericalString = "Lucky1234"
print("All are alpha-numeric characters?", alphaNumericalString.isalnum())
print()

# --------------------------- isspace() ---------------------------
# returns true when all the characters in the string are spaces else returns false
spaceString = "Goa"
print("All string characters are space?", spaceString.isspace())
print()

# --------------------------- join() ---------------------------
# used to join a sequence of strings mentioned in its arguments with the string
stringJoin1 = "-"
stringJoin2 = ["Hello", "Welcome", "Hey", "Namaste", "Namaskaram"]
print("After joining:", stringJoin1.join(stringJoin2))
print()

# --------------------------- strip() ---------------------------
# used to delete all the leading and trailing characters mentioned in its argument
stringStripping = "......Tokyo......"
print("After stripping '.' from the string:", stringStripping.strip("."))
print()

# --------------------------- lstrip() ---------------------------
# used to delete all the leading characters mentioned in its argument
print("After stripping all leading characters:", stringStripping.lstrip("."))
print()

# --------------------------- rstrip() ---------------------------
# used to delete all the trailing characters mentioned in its argument
print("After stripping all trailing characters:", stringStripping.rstrip("."))
print()

# --------------------------- min() ---------------------------
# returns the minimum value alphabet from the string
stringMinMax = "Elephant"
print("Minimum value character:", min(stringMinMax))
print()

# --------------------------- max() ---------------------------
# returns the maximum value alphabet from string
print("Maximum value character:", max(stringMinMax))
print()

# --------------------------- maketrans() ---------------------------
# used to map the contents of string 1 with string 2 with respective indices to be translated later using translate()
# str.maketrans(string to be replaced, string to replace with) - syntax
# both string arguments should be of same length
translationTable = str.maketrans("abc", "123")
originalString = "apple, banana, cherry"
print("Original string:", originalString)
print()

# --------------------------- translate() ---------------------------
# used to swap the string elements mapped with the help of maketrans()
# string.translate(mappingTable) - syntax
# mappingTable is table created using maketrans()
translatedString = originalString.translate(translationTable)
print("Translated string:", translatedString)
print()

# --------------------------- replace() ---------------------------
# used to replace the substring with a new substring in the string
# replace(string to replace, new string which would replace) - syntax
replaceString = "Scale is used for measuring."
print("Original:", replaceString)
print("Replacing:", replaceString.replace("Scale", "Ruler"))
print()

