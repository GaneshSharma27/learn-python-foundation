# --------- Regular Expression ---------
import re

phone_number_regex = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")  # using `re.compile()` to create regex object also it requires raw string
mo = phone_number_regex.search("My phone number is 415-555-4242.")
print("Phone number found: " + mo.group())  # passing `0` or keeping it blank, then `group()` method will return the entire matched text
print("The area code is " + mo.group(1))    # the first set of parentheses will be in group 1
print("The rest of the phone number is " + mo.group(2))     # the second set of parentheses will be in group 2
print("Retrive all the groups:", mo.groups())     # note the plural form of the `groups()`, this returns tuple
area_code, main_phone_number = mo.groups()      # can also work with multiple assignment to separate variables
print("The area code is " + area_code)      # multiple assignment trick
print("The main phone number is " + main_phone_number)      # multiple assignment trick
print()

# ---------- What if the area code is written in parentheses ----------
phone_number_regex1 = re.compile(r"(\(\d\d\d\)) (\d\d\d-\d\d\d\d)")
mobile = phone_number_regex1.search("My phone number is (412) 555-4242.")
print("The area code is", mobile.group(1))
print("The main phone number is", mobile.group(2))
print()

# .  ^  $  *  +  ?  {  }  [  ]  \  |  (  )      --> In regular expression these characters have special meaning
# if you want to use them as it is then you need to add escape character, backslash \
# \.  \^  \$  \*  \+  \?  \{  \}  \[  \]  \\  \|  \(  \)

superhero_regex = re.compile(r"Batman|Superman")
superhero1 = superhero_regex.search("Batman and Superman")
print("Superhero:", superhero1.group())
superhero2 = superhero_regex.search("Superman and Batman")
print("Superhero:", superhero2.group())
print()

bat_regex = re.compile(r"Bat(man|mobile|copter|bat)")
bat = bat_regex.search("Batmobile lost a wheel")
print(bat.group())      # returns the full matched text 'Batmobile'
print(bat.group(1))     # returns just the part of the matched text inside the first parentheses group, 'mobile'
print()

# --------- Optional matching with the question mark ---------
batpeople_regex = re.compile(r"Bat(wo)?man")    # (wo)? part of the regular expression means that the pattern 'wo' is an optional group
batpeople1 = batpeople_regex.search("The adventures of Batman")
print(batpeople1.group())
batpeople2 = batpeople_regex.search("The adventures of Batwoman")
print(batpeople2.group())
# if there is `?` then regex will match text that has zero or one instances of 'wo' in the text
print()

# ------------ Match zero or more with the asterisk ------------
# `*` means match zero or more times
bat_regex_asterisk = re.compile(r"Bat(wo)*man")
bat1 = bat_regex_asterisk.search("The adventures of Batman")
print(bat1.group())
bat2 = bat_regex_asterisk.search("The adventures of Batwoman")
print(bat2.group())
bat3 = bat_regex_asterisk.search("The adventures of Batwowowoman")
print(bat3.group())
print()

# ------------- Matching one or more with the plus sign -------------
# `+` means match one or more times
# by using `+` that means that group must appear at least once, it is not optional
bat_regex_plus = re.compile(r"Bat(wo)+man")
bat_plus_1 = bat_regex_plus.search("The adventures of Batwoman")
print(bat_plus_1.group())
bat_plus_2 = bat_regex_plus.search("The adventures of Batwowowoman")
print(bat_plus_2.group())
bat_plus_3 = bat_regex_plus.search("The adventures of Batman")
# print(bat_plus_3.group())   # this will give an error since its None, since `wo` should be matched atleast one time
print("Checking bat_plus_3 == None:", bat_plus_3 == None)
print()

# ------------ Matching specific repetitions with braces ------------
# `(Ha){3}` means group 'Ha' can repeat 3 times, and this will match string 'HaHaHa'
# `(Ha){3, 5}` means group 'Ha' can repeat minimum 3 and maximum 6 times, and this will match strings 'HaHaHa', 'HaHaHaHa', and 'HaHaHaHaHa'
# `(Ha){3, }` means group 'Ha' can repeat minimum 3 to maximum unbound
# `(Ha){, 5}` means group 'Ha' can repeat can repeat from minimum zero to maximum five times
ha_regex = re.compile(r"(Ha){3}")
ha_1 = ha_regex.search("HaHaHa")
print(ha_1.group())
ha_2 = ha_regex.search("Ha")
# print(ha_2.group())       # will give out an error
print("Check if ha_2 == None:", ha_2 == None)
print()

# ------------ Greedy and non-greedy matching ------------
# by default python returns 'HaHaHaHaHa' after all 'HaHaHa' and 'HaHaHaHa' are also valid matches
# this is because python's regex are greedy by default, which means they will always match the longest string possible
greedy_regex = re.compile(r"(Ha){3,5}")
text_1 = greedy_regex.search("HaHaHaHaHa")
print("Greedy matching:", text_1.group())
# Non-greedy matching which matches the shortest string possible, has a closing braces followed by a question mark
# Note: Question mark can have two meanings in regular expression, declaring a non-greedy match or flagging an optional group
non_greedy_regex = re.compile(r"(Ha){3,5}?")
text_2 = non_greedy_regex.search("HaHaHaHaHa")
print("Non-greedy matching:", text_2.group())

# ----------------- The findall() method -----------------
phone_number_regex_findall = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
phone_number_search = phone_number_regex_findall.search("Cell: 415-555-9999 Work: 212-555-0000")
# `search()` returns the match of the first instance of matching text
print("By using search() method:", phone_number_search.group())
# `findall()` returns a list of strings, each string is the match of the searched string that matched the regular expression
# the only condition is that in regex statement there shouldn't any group
phone_number_findall = phone_number_regex_findall.findall("Cell: 415-555-9999 Work: 212-555-0000")
print("By using findall() method:", phone_number_findall)
print()

phone_number_regex_findall_group = re.compile(r"(\d\d\d)-(\d\d\d)-(\d\d\d\d)")  # if there are groups in regex
# then it will return a list of tuples
phone_number_findall_group = phone_number_regex_findall_group.findall("Cell: 415-555-9999 Work: 212-555-0000")
print("Groups in regex, therefore it returned list of tuples:", phone_number_findall_group)
print()

# ------------------- Character class in Regex -------------------

# \d ---> Any numeric digit from 0 to 9
# \D ---> Any character that is not a numeric digit from 0 to 9
# \w ---> Any letter, numeric digit, or the underscore character (Think of this as matching “word” characters)
# \W ---> Any character that is not a letter, numeric digit, or the underscore character
# \s ---> Any space, tab, or newline character. (Think of this as matching “space” characters)
# \S ---> Any character that is not a space, tab, or newline
# [0-5] ---> will match only the numbers 0 to 5
# no shorthand character class that matches only letters
# [a-zA-Z] ---> will match only the letters from a to z and A to Z

x_mas_regex = re.compile(r"\d+\s\w+")
print(x_mas_regex.findall("12 drummers, 11 pipers, 10 lords, 9 ladies, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge"))
print()

# ----------------- Making your own character class -----------------
# when you want to match the set of characters but shorthand characters are too broad
# then you can create your own character class, by writing them in square brackets
# normal regular expression symbols are not interpreted in the square brackets
# [0-5.] ---> this'll match from 0 to 5 and a period, you don't need to write `[0-5\.]`
vowel_regex = re.compile(r"[aeiouAEIOU]")
print("Regex looking for vowels:", vowel_regex.findall("RoboCop eats baby food. BABY FOOD."))
# you can use range of letters, numbers by using hyphens
range_regex = re.compile(r"[a-gA-G2-7]")    # this'll match from a to g, A to G, and 2 to 7
print()

# ------------- Negative character class -------------
# ^ this is caret character used for negative character class
# it'll match all the characters that aren't in the character class
consonant_regex = re.compile(r"[^aeiouAEIOU]")
print("Consonants using negative character class:", consonant_regex.findall("RoboCop eats baby food. BABY FOOD."))
print()

# --------------- Caret and dollar sign characters ---------------
# ^ ---> use this symbol at the start of a regex to indicate that match must occur at the beginning of the searched text
# $ ---> at the end of the regex to indicate the string must end with this regex pattern
# ^ and $ together to indicate that the entire string must match the regex
begins_with_hello = re.compile(r"^Hello")
print("Check if the string begins with 'Hello':", begins_with_hello.search("Hello, World!"))
print("Check if the string begins with 'Hello':", begins_with_hello.search('He said hello.'))
print()

# --------------- Ends with ---------------
ends_with_number = re.compile(r"\d$")
print("String ends with number?", ends_with_number.search("Your number is 42"))
print("String ends with number?", ends_with_number.search("Your number is Forty-two"))
whole_string_isnum = re.compile(r"^\d+$")
print("Whole string is number?", whole_string_isnum.search("1234567890"))
print("Whole string is number?", whole_string_isnum.search("12345xyz67890"))
print("Whole string is number?", whole_string_isnum.search("12345 67890"))
print()

# --------------- Wildcard character ---------------
# . ---> this is called wildcard character and it'll match any character except for a newline
# this dot character only matches just one character
# to match actual dot use escape character ---> \.
at_regex = re.compile(r".at")
print("Regex:", at_regex.findall("The cat in the hat sat on the flat mat."))
print()

# ---------- Matching with everything with dot-star ----------
name_regex = re.compile(r"First Name: (.*) Last Name: (.*)")
name = name_regex.search("First Name: Al Last Name: Sweigart")
print(name.group(1))
print(name.group(2))
# dot-star character class is a greedy method, to match in a non-needy manner, use a dot, star, and a question mark (.*?)
non_greedy_manner = re.compile(r"<.*?>")
non_greedy_dot_star = non_greedy_manner.search("<To serve man> for dinner.")
print("Non-greedy manner of dot-star:", non_greedy_dot_star.group())
greedy_manner = re.compile(r"<.*>")
greedy_dot_star = greedy_manner.search("<To serve man> for dinner.>")
print("Greedy manner of dot-star:", greedy_dot_star.group())
print()

# -------------- Matching newlines with the dot character --------------
no_newline_regex = re.compile(".*")
print("No new line:", no_newline_regex.search("Serve the public trust.\nProtect the innocent.\nUphold the law.").group())
new_line_regex = re.compile(".*", re.DOTALL)
print("New line:", new_line_regex.search("Serve the public trust.\nProtect the innocent.\nUphold the law.").group())
print()

"""
# --------------- Review of the Regex symbols ---------------
    ?      ---> matches 'zero' or 'one' of the preceeding group
    *      ---> matches 'zero' or 'more' of the preceeding group
    +      ---> matches 'one' or 'more' of the preceeding group
    {n}    ---> matches exactly 'n' of the preceeding group
    {n,}   ---> matches 'n' or 'more' of the preceeding group
    {,m}   ---> matches '0' to 'm' of the preceeding group
    {n,m}  ---> matches atleast 'n' and atmost 'm' of the preceeding group
    {n,m}? ---> performs a non-greedy match of the preceding group
    *?     ---> performs a non-greedy match of the preceding group
    +?     ---> performs a non-greedy match of the preceding group
    ^spam  ---> means the string must begin with 'spam'
    spam$  ---> means the string must end with 'spam'
    .      ---> matches any character except newline character
    \d     ---> matches digit character
    \w     ---> matches word character
    \s     ---> matches space character
    \D     ---> matches anything except digit character
    \W     ---> matches anything except word character
    \S     ---> matches anything except space character
    [abc]  ---> matches any character between the brackets (such as a, b, or c)
    [^abc] ---> matches any character that isn't between the brackets
"""

# -------------- Case-insensitive matching --------------
# to make regex case-insensitive you can pass 're.IGNORECASE' or 're.I'
robocop = re.compile(r"robocop", re.IGNORECASE)
print(robocop.search("Robocop is part man, part machine, all cop.").group())
print(robocop.search("ROBOCOP protects the innocent.").group())
print()

# ----------- Substituting strings with the sub() method -----------
names_regex = re.compile(r"Agent \w+")
print(names_regex.sub("CENSORED", "Agent Alice gave the secret documents to Agent Bob."))
agent_name_regex = re.compile(r"Agent (\w)\w*")
print(agent_name_regex.sub(r"\1****", "Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent."))
print()

# ---------------- Managing complex regex ----------------
# Regex are fine if the text pattern you need to match is simple
# But if you want to match complicated text patterns then you can use 're.VERBOSE' to ignore the whitespace and comments in regex string
# phone_regex = re.compile(r"((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)")
phone_regex = re.compile(r"""(
                         (\d{3}|\(\d{3}\))?             # area code
                         (\s|-|\.)?                     # separator
                         \d{3}                          # first 3 digits
                         (\s|-|\.)                      # separator
                         \d{4}                          # last 4 digits
                         (\s*(ext|x|ext.)\s*\d{2,5})?   # extension
                         )""", re.VERBOSE)
# this uses triple-quote syntax to create a multiline string so that you can spread
# regex definition over many lines

# ------------------- Combining re.IGNORECASE, re.DOTALL, and re.VERBOSE -------------------
# since 're.compile()' only takes only single value as its second argument
some_regex_value = re.compile("foo", re.IGNORECASE | re.DOTALL | re.VERBOSE)



