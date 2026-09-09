#TODO:

#regular expression - its a library of functions which helps identigy a pattern and help get desired results.

#without regular expression

# mail = input("Enter your mail: ").strip()

# name, domain = mail.split("@")

# if name and "." in domain:
#     print("valid")
# else:
#     print("not valid")

# #or

# if name and domain.endswith(".com"):
#     print("valid")
# else:
#     print("not valid")

#with regular expressions

import re

mail = input("Enter your mail: ").strip()

if re.search("..*@..*", mail):
    print("valid")
else:
    print("invalid")

#or

if re.search(".+@.+", mail):
    print("valid")
else:
    print("invalid")

#or

if re.search(r"^[^@]+@[^@]+\.com$", mail):
    print("valid")
else:
    print("invalid")

#or

if re.search(r"^[a-zA-Z0-9_]+@[^@]+\.com$", mail):
    print("valid")
else:
    print("invalid")

#or  \w,\s,\d - it denotes entire word/number library. and when given \W,\S,\D - when caps it means the opp of each small letter functionality

if re.search(r"^\w+@\w+\.com$", mail):
    print("valid")
else:
    print("invalid")

#or (\w|\s) - either a word or space

if re.search(r"^(\w|\s)+@\w+\.com$", mail):
    print("valid")
else:
    print("invalid")