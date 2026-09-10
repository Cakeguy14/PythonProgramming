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

if re.search(r"^(\w|\s)+@\w+\.com$", mail, re.IGNORECASE):
    print("valid")
else:
    print("invalid")

#or ? is allowing you say that the characters  before that are either allowed once or none. like 0 or 1 time only. so you can give the word and . or space in a paranthesis and consider that as a single thing

if re.search(r"^\w+@(\w+\.)?\w+\.com$", mail, re.IGNORECASE):
    print("valid")
else:
    print("invalid")

if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.com$", mail, re.IGNORECASE):
    print("valid")
else:
    print("invalid")

#or TODO: using the group function in re.search function
import re

name = input("enter your name: ").strip()

matches = re.search(r"(.+), (.+)", name)
if matches:
    name = matches.group(2)+" "+matches.group(1)
print(f"Hi, {name}")

#or TODO: using := - walrus function you can take the value into variable and return it back to further computations as well.
    #only used for while/if/for loops not for normal variable.
    #introduce only if immediately calling above variable in very next line into a loop.

if (matches := re.search(r"(.+), (.+)", name)):
    name = matches.group(2)+" "+matches.group(1)
print(f"Hi, {name}")

#or TODO: using replace function

url = input("enter your username: ")

username = url.replace("www.test.com.", "")

print(username)

#or TODO: using removeprefix function

username = url.removeprefix("www.test.com.")

print(username)

#or TODO: using ?: this is a iternary function helps you to neglect a group or whatever comes inside the paranthesis where this exists

username = url.removeprefix("(?:www.test.com).")

print(username)

if username := re.search(r"^(?:www)\.test\.com/(.+)", url, re.IGNORECASE):
    nameurl = username.group(1)
print(nameurl)


#or there are other fucntions in regex like re.split, re.findall, re.match as well.

# import re

# # ============================================================
# # 1. re.search() — Find first match anywhere
# # ============================================================
# text = "My email is senthur@gmail.com"
# match = re.search(r"\w+@\w+\.\w+", text)
# print(match.group())   # senthur@gmail.com


# # ============================================================
# # 2. re.match() — Match only at the START
# # ============================================================
# text = "Hello World"
# print(re.match(r"Hello", text))   # ✅ Match
# print(re.match(r"World", text))   # ❌ None (not at start)


# # ============================================================
# # 3. re.fullmatch() — Match the ENTIRE string
# # ============================================================
# print(re.fullmatch(r"\d{4}", "2026"))    # ✅ Match
# print(re.fullmatch(r"\d{4}", "2026ab"))  # ❌ None (extra chars)


# # ============================================================
# # 4. re.findall() — Return ALL matches as a list
# # ============================================================
# text = "Numbers: 10, 20, 30"
# print(re.findall(r"\d+", text))   # ['10', '20', '30']


# # ============================================================
# # 5. re.finditer() — Return ALL matches as match objects
# # ============================================================
# text = "cat bat rat"
# for m in re.finditer(r"\w+at", text):
#     print(m.group(), m.start())
# # cat 0
# # bat 4
# # rat 8


# # ============================================================
# # 6. re.sub() — Replace matches
# # ============================================================
# text = "I love cats"
# print(re.sub(r"cats", "dogs", text))   # I love dogs

# # Replace all digits with #
# print(re.sub(r"\d", "#", "abc123"))    # abc###


# # ============================================================
# # 7. re.subn() — Replace AND count
# # ============================================================
# result, count = re.subn(r"\d", "#", "abc123")
# print(result, count)   # abc### 3


# # ============================================================
# # 8. re.split() — Split by pattern
# # ============================================================
# text = "one1two2three3four"
# print(re.split(r"\d", text))   # ['one', 'two', 'three', 'four']

# print(re.split(r"[,;]", "a,b;c"))   # ['a', 'b', 'c']


# # ============================================================
# # 9. re.compile() — Pre-compile a pattern (faster for reuse)
# # ============================================================
# pattern = re.compile(r"\d+")
# print(pattern.findall("a1b22c333"))      # ['1', '22', '333']
# print(pattern.search("abc123").group())  # 123


# # ============================================================
# # 10. re.escape() — Escape special characters in a string
# # ============================================================
# text = "1 + 1 = 2?"
# print(re.escape(text))   # 1\ \+\ 1\ =\ 2\?


# # ============================================================
# # BONUS: Useful Flags
# # ============================================================
# # re.IGNORECASE / re.I  — Case-insensitive
# print(re.search(r"hello", "HELLO", re.I))   # ✅ Match

# # re.MULTILINE / re.M   — ^ and $ match at line breaks
# text = "line1\nline2\nline3"
# print(re.findall(r"^\w+", text, re.M))   # ['line1', 'line2', 'line3']

# # re.DOTALL / re.S      — . matches newlines too
# print(re.search(r"a.b", "a\nb", re.S))   # ✅ Match

# # re.VERBOSE / re.X     — Allow whitespace and comments in pattern
# pattern = re.compile(r"""
#     \d{4}       # Year
#     -           # Dash
#     \d{2}       # Month
#     -           # Dash
#     \d{2}       # Day
# """, re.VERBOSE)
# print(pattern.search("Date: 2026-09-10").group())   # 2026-09-10


# # ============================================================
# # BONUS: Match Object Methods
# # ============================================================
# m = re.search(r"(\w+)@(\w+)\.(\w+)", "senthur@gmail.com")

# print(m.group())    # senthur@gmail.com  (whole match)
# print(m.group(0))   # senthur@gmail.com  (same as group())
# print(m.group(1))   # senthur            (first capture group)
# print(m.group(2))   # gmail              (second capture group)
# print(m.groups())   # ('senthur', 'gmail', 'com')
# print(m.start())    # 0                  (start index)
# print(m.end())      # 17                 (end index)
# print(m.span())     # (0, 17)            (start, end)


# # ============================================================
# # QUICK REFERENCE
# # ============================================================
# # re.search()     → Find first match anywhere          → Match object or None
# # re.match()      → Match at start only                → Match object or None
# # re.fullmatch()  → Match entire string                → Match object or None
# # re.findall()    → Find all matches                   → List of strings
# # re.finditer()   → Find all matches                   → Iterator of match objects
# # re.sub()        → Replace matches                    → New string
# # re.subn()       → Replace and count                  → Tuple (new_string, count)
# # re.split()      → Split by pattern                   → List of strings
# # re.compile()    → Pre-compile pattern                → Compiled pattern object
# # re.escape()     → Escape special chars               → Escaped string
# #
# # GOLDEN RULE:
# #   Use search()   for finding
# #   Use findall()  for collecting
# #   Use sub()      for replacing
# #   Use split()    for breaking apart
# #   ALWAYS use raw strings r"..." for regex patterns!