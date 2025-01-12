import pyinputplus as pyip

response = pyip.inputNum("Enter a number: ")

# -------------- min, max, greaterThan, lessThan --------------
# keyword arguments are optional
# 'min' ---> input cannot be less than them though the input can be equal to them
# 'max' ---> input cannot be greater than them though the input can be equal to them
# 'greaterThan' ---> the input must be greater than them and input cannot be equal to them
# 'lessThan' ---> the input must be lesser than them and input cannot be equal to them
response_1 = pyip.inputNum("Enter number (not less than 4): ", min=4)
response_2 = pyip.inputNum("Enter a number (greater than 5): ", greaterThan=5)
response_3 = pyip.inputNum("Enter a number (not less than 4 and less than 6): ", min=4, lessThan=6)
print()

# ----------------- blank keyword argument -----------------
# by default blank input isn't allowed unless the blank keyword argument is set to True
blank_input = pyip.inputNum("Enter a number (try keeping it blank): ")      # this won't proceed and keep prompting the user, if kept blank
blank_input = pyip.inputNum(blank=True)
print()

# ------------- limit, timeout, and default keyword arguments -------------
limit = pyip.inputNum("Enter a number (for limits): ", limit=2)   # if valid input isn't entered in two tries, then it raises an exception
limit_default = pyip.inputNum("Enter a number (limits with default value): ", limit=2, default="N/A")
print(limit_default)    # if not entered valid input in two tries, then prints 'default' value
print()

# --------------- allowRegexes and blockRegexes keyword arguments ---------------
allow_regex = pyip.inputNum("Enter a word (I/V/X/L/C/D/M are allowed): ", allowRegexes=[r"(I|V|X|L|C|D|M)+", r"zero"])
block_regex = pyip.inputNum("Enter a number (0/2/4/6/8 these are blocked): ", blockRegexes=[r"[02468]$"])
# if you use both 'allowRegexes' and 'blockRegexes' arguments, the allow list overrides the block list
print()

# ---------------- passing a custom validation function to inputCustom() ----------------
def add_upto_ten(numbers):
    numbers_list = list(numbers)
    for i, digit in enumerate(numbers_list):
        numbers_list[i] = int(digit)
    if sum(numbers_list) != 10:
        raise Exception("The digits must add up to 10, not %s." %(sum(numbers_list)))
    else:
        print("Done!")
    return int(numbers)

print("Enter the numbers such that they add upto 10: ", end="")
total_ten = pyip.inputCustom(add_upto_ten)
print()

