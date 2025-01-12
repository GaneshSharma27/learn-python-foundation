#! python3

import re, pyperclip

phone_regex = re.compile(r"""
                         (
                            (\d{3}|\(\d{3}\))?             # area code
                            (\s|-|\.)?                     # separator
                            \d{3}                          # first 3 digits
                            (\s|-|\.)                      # separator
                            \d{4}                          # last 4 digits
                            (\s*(ext|x|ext.)\s*\d{2,5})?   # extension
                         )
                         """, re.VERBOSE)              # 're.VERBOSE' allows to include whitespaces, comments within the regular expression

email_regex = re.compile(r"""
                         (
                            [a-zA-Z0-9._%+-]+      # username
                            @                      # @ symbol
                            [a-zA-Z0-9.-]+         # domain name
                            (\.[a-zA-Z]{2,4})      # dot something
                         )
                         """, re.VERBOSE)

text = str(pyperclip.paste())

matches = []
for groups in phone_regex.findall(text):
    # phone_number = "-".join([groups[1], groups[3], groups[5]])
    area_code = groups[1] if groups[1] else ""
    separator1 = groups[2] if groups[2] else ""
    first_part = groups[3]
    separator2 = "-"
    second_part = groups[5]
    extension = " x" + groups[6] if groups[5] else ""
    phone_number = f"{area_code}{separator1}{first_part}{separator2}{second_part}{extension}"
    matches.append(phone_number)

for groups in email_regex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy("\n".join(matches))
    print("Copied to clipboard!")
    print("\n".join(matches))
else:
    print("No phone numbers or email addresses found.")
