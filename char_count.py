message = str(input("Enter your message: "))
count = {}

# for adding the values in count dictionary
for each_char in message:
    count.setdefault(each_char, 0)
    count[each_char] = count[each_char] + 1

# for printing the values on each line
for each_key, each_key_value in count.items():
    print(each_key + " --> " + str(each_key_value))
