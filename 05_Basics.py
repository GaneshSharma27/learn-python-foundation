# ----------------------------------- Manipulating Strings -----------------------------------

# -------------- string literals --------------
print("Written using double quotes: " + "Alice has a cat.")
print('Written using single quotes: ' + 'Alice has a cat.')
print()

# -------------- escape character --------------
# represented by `\` backslash
# `\'` for single quotation
# `\"` for double quotation
# `\n` for newline (line break)
# `\t` for tab
# `\\` for backslash
print('This is Tia\'s shoes.')    # if there wasn't `\` then Python would assume that string ended at Tia and rest will be considered invalid
print("This is \"double quotation\" using escape character.")
print("This is\nnewline.")
print("\tThis is tab.")
print("This is \\ backslash")
print()

# ----------------- raw sting -----------------
# represented by `r` before begining of quotation mark
# raw string completely ignores all the escape characters
print(r"This string is using raw string and here I've added \ an escape character.")
print(r"The file location is D:\Programming\Python Fundamentals")
print()

# -------------- multiline strings --------------
# represented with triple single quotes or triple double quotes
print("""Respected Sir/Mam,
      
      I'm XYZ writing this block of code using triple double-quotation marks.""")       # also works with single-quotation marks
print()

# --------- indexing and slicing of the strings ---------
index_string = "Hello World!"
print("First index of the string:", index_string[0])
print("Last index of the string:", index_string[-1])
print("First five indexes of the string:", index_string[0:5])
print("First five indexes of the string:", index_string[:5])
print("Last seven indexes of the string:", index_string[6:])
print()

# --------- in and not in operator with strings ---------
# `in` and `not in` operator can be used with strings just like with list value
new_word = "Hello world!"
print("Hello" in new_word)
print("HELLO" in new_word)
print("" in new_word)
spam = "cats and dogs"
print("cats" not in spam)
print()

# ---------- putting strings inside other strings ----------
candidate_name = "Mike"
candidate_age = 20
print("Hello, my name is " + candidate_name + " and my age is " + str(candidate_age) + ".")   # tedious way of doing it
print("Hello, my name is %s and my age is %s." %(candidate_name, candidate_age))    # this is called string interpolation
# in string interpolation, `%s` operator inside the string acts as the marker to be replaced by values following the string
# one benefit is that `str()` function doesn't need to be called to convert values to string
print()

# --------------- f-string ---------------
print(f"My name is {candidate_name} and my age is {candidate_age}.")    # instead of %s `{}` are used and variables are directly placed inside
# the curly braces.
# like raw-string, in f-string `f` needs to be the prefix before the quotation marks
print()

# ------------ string methods ------------
# upper(), lower(), isupper(), and islower() methods
# upper() and lower() return a new string, they don't modify the string but return new string
sentence_1 = "This is programming language."
sentence_1 = sentence_1.upper()
print("Uppercase:", sentence_1)
sentence_2 = sentence_1.lower()
print("Lowercase:", sentence_2)
# islower() and isupper() will return boolean value
sentence_3 = "Check for lower/upper"
print("Upper?", sentence_3.isupper())
print("Lower?", sentence_3.islower())
print("abc123 is lower?", "abc123".islower())
print("ABC123 is upper?", "ABC123".isupper())
print("12345 is lower?", "12345".islower())
print("12345 is upper?", "12345".isupper())
print("HELLO".lower().islower())
print()

# there are several other string methods that have name beginning with word `is`
# isalpha() returns `True` if the string consists of only letters and isn't blank
# isalnum() returns `True` if the string consists of only letters and numbers and isn't blank
# isdecimal() returns `True` if the string consists of only numeric character and isn't blank
# isspace() returns `True` if the string consists only of spaces, tabs and newlines and isn't blank
# istitle() returns `True` if the string consists only of words that begin with uppercase letter followed by lowercase letters

# ----------- startswith() and endswith() -----------
# returns boolean values only
print("Hello World! starts with 'Hello'? ", end="")
print("Hello World!".startswith("Hello"))
print("Hello World! ends with 'World!'? ", end="")
print("Hello World!".endswith("World!"))
print()

# --------------- join() and split() ---------------
# join() used for converting list of string to single string value
# split() used for converting single string value to list of string values
print("Example of join():", ", ".join(["cats", "dogs", "mouse"]))
print("Example of join():", " ".join(["cats", "dogs", "mouse"]))
print("Example of split():", "My name is Mike".split())

# example for using split() method call
sample_sentence = """Hello, This is Ben.
I'm pursuing Computer Science at Bharat College of Engineering.
This is currently my third year learning this course."""
print("Split at new-line:", sample_sentence.split("\n"))
print()

# -------- spliting strings with the partition() method call --------
# this method call returns a tuple in order of `before separator string`, `separator string` and `after separator string` as shown below
# if separator string has more than one occurance then `partition()` only splits first occurance
sample_sentence_1 = "This is going to be a partitioned string."
print("Partitioned string:", sample_sentence_1.partition("to"))
print()

# justification texts `rjust()`, `ljust()` and `center()` method call
# these method call return padded version of the string
# these take argument of integer, which means total how many character string including whitespaces added for padding
# for example: "Hello".rjust(10) here "Hello" is five character string so 5 whitespaces will be added total making it 10
print("Right justified string".rjust(40))
print("Right justified string with any char.".rjust(70, "-"))
print("Left justified string with any char.".ljust(70, "-"))
print("Center justified string.".center(50))
print("Center justified string.".center(50, "-"))
print()

# -------- removing whitespace with strip(), rstrip(), and lstrip() method --------
# these methods strip off the whitespace characters (space, tab, and newline) from left, right or both side of the string
# strip() returns a new string without any whitespace characters at the beginning or the end
# lstrip() and rstrip() strip off the whitespace characters from left and right ends, respectively
strip_sentence = "           Hello World!           "
print("Without striping:", strip_sentence)
print("Stripped:", strip_sentence.strip())
print("Left stripped:", strip_sentence.lstrip())
print("Right stripped:", strip_sentence.rstrip())
print()

sentence_sample = "SpamSpamBaconSpamEggsSpamSpam"
print("Original sentence:", sentence_sample)
print("Stripped at 'ampS':", sentence_sample.strip("ampS"))    # strip off a, m, p, and S and order of the strip doesn't matter
print()

# -------- numeric values of characters with the ord() and chr() functions --------
# computer store information as bytes (strings of binary numbers), which means we need to convert texts to numbers
# because of this, every text character has a corresponding numeric value called a Unicode code point
# use `ord()` to get code point of a one-character string
# use `chr()` to get one-character string of an integer code point
print("Code point of 'A':", ord("A"))
print("Code point of '4':", ord("4"))
print("Code point of '!':", ord("!"))
print("One-character string of 65:", chr(65))
# these functions are useful when you need to do an ordering or mathematical operation on characters
print("Code point of 'B':", ord("B"))
print("ord(\"A\") < ord(\"B\"):", ord("A") < ord("B"))
print("chr(ord(\"A\")):", chr(ord("A")))
print("chr(ord(\"A\") + 1):", chr(ord("A") + 1))
print()

# -------- copying and pasting strings with the paperclip module --------
# it has copy() and paste() functions that can send text to and receive text from computer's clipboard
import pyperclip
pyperclip.copy("Hello World!")      # copy
print(pyperclip.paste())            # paste



