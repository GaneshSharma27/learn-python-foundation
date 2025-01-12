print("------------- PIG LATIN GAME -------------")
print("Enter the message:")
message_input = str(input())

VOWELS = ("a", "e", "i", "o", "u")

pig_latin = []      # list for words in the pig latin

for each_words in message_input.split():
    # Separate the non-letters at the start of this word
    prefix_non_letters = ""
    while len(each_words) > 0 and not each_words[0].isalpha():
        prefix_non_letters += each_words[0]
        each_words = each_words[1:]
    if len(each_words) == 0:
        pig_latin.append(prefix_non_letters)
        continue

    # Separate the non-letters at the end of this word
    suffix_non_letters = ""
    while not each_words[-1].isalpha():
        suffix_non_letters = each_words[-1] + suffix_non_letters
        each_words = each_words[:-1]
    
    # Remember if the word was in uppercase or title case
    was_upper = each_words.isupper()
    was_title = each_words.istitle()
    
    each_words = each_words.lower()     # Make the word lowercase for translation

    # Separate the consonants at the start of this word
    prefix_consonants = ""
    while len(each_words) > 0 and not each_words[0] in VOWELS:
        prefix_consonants += each_words[0]
        each_words = each_words[1:]

    # Add the Pig Latin ending to the word
    if prefix_consonants  != "":
        each_words += prefix_consonants + "ay"
    else:
        each_words += "yay"

    # Set the word back to uppercase or title case
    if was_upper:
        each_words = each_words.upper()
    if was_title:
        each_words = each_words.title()

    # Add the non-letters back to the start or end of the word
    pig_latin.append(prefix_non_letters + each_words + suffix_non_letters)

# Join all the words back together into a single string
print(" ".join(pig_latin))




