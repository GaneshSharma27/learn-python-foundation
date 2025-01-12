def is_phone_number(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != "-":
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != "-":
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

# print("Is 415-555-4242 a phone number?")
# print(is_phone_number("415-555-4242"))
# print("Is Moshi moshi a phone number?")
# print(is_phone_number("Moshi moshi"))

message = "Call me at 415-555-1011 tomorrow. 415-555-9999 is my office."
for i in range(len(message)):
    chunk = message[i:i + 12]   # on every iteration a chunk of 12 characters is assigned to the `chunk` variable
    # so at first iteration `i = 0` then `chunk` is assigned from `message[0:12]`
    # then at second iteration `i = 1` then `chunk` is assigned from `message[1:13]`
    if is_phone_number(chunk):
        print("Phone number found: " + chunk)
print("Done!")


