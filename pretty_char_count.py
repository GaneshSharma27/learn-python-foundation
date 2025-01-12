import pprint
message = str(input("Enter your message: "))
count = {}

# for adding the values in count dictionary
for each_char in message:
    count.setdefault(each_char, 0)
    count[each_char] = count[each_char] + 1
pprint.pprint(count)
