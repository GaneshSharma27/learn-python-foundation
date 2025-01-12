#! python3

import re
import pyperclip

# Phone number regex
phone_regex = re.compile(r"""
    (
        (\d{3}|\(\d{3}\))?             # area code (optional)
        (\s|-|\.)?                     # separator (optional)
        \d{3}                          # first 3 digits
        (\s|-|\.)                      # separator
        \d{4}                          # last 4 digits
        (\s*(ext|x|ext.)\s*\d{2,5})?   # extension (optional)
    )
    """, re.VERBOSE)  # 're.VERBOSE' allows including whitespaces and comments within the regular expression

# Email regex
email_regex = re.compile(r"""
    (
        [a-zA-Z0-9._%+-]+      # username
        @                      # @ symbol
        [a-zA-Z0-9.-]+         # domain name
        (\.[a-zA-Z]{2,4})      # dot something
    )
    """, re.VERBOSE)

# Get the text off the clipboard
text = str(pyperclip.paste())

matches = []

# Extract phone numbers
for groups in phone_regex.findall(text):
    area_code = groups[1] if groups[1] else ""
    first_part = groups[2] if groups[2] else ""
    middle_part = groups[3] if groups[3] else ""
    last_part = groups[4] if groups[4] else ""
    extension = " x" + groups[6] if groups[5] else ""

    phone_number = f"{area_code}{first_part}{middle_part}{last_part}{extension}"
    matches.append(phone_number.strip())

# Extract emails
for groups in email_regex.findall(text):
    matches.append(groups[0])

# Copy results to clipboard
if matches:
    pyperclip.copy("\n".join(matches))
    print("Copied to clipboard!")
    print("\n".join(matches))
else:
    print("No phone numbers or email addresses found.")
