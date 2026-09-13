# Python Syntax & Gotchas — Complete Reference

## 1. Walrus Operator `:=`

Assigns a value **and** returns it in the same expression. (Python 3.8+)

### Without walrus:
```python
data = input("Enter: ")
if data:
    print(data)
```

### With walrus:
```python
if (data := input("Enter: ")):
    print(data)
```

### In a while loop:
```python
while (line := input("> ")) != "quit":
    print(line)
```

### In a list comprehension:
```python
squares = [sq for n in range(10) if (sq := n * n) > 20]
```

---

## 2. f-strings

Always use `f` before the string to interpolate variables.

```python
name = "Harry"
print(f"Hello, {name}")     # ✅ "Hello, Harry"
print("Hello, {name}")      # ❌ "Hello, {name}" (literal)
```

### ⚠️ Without `f`, curly braces create SETS:
```python
name = "Harry"
print({name})               # {"Harry"}  ← Set!
print(f"{name}")            # "Harry"    ← f-string
```

### Expressions inside f-strings:
```python
print(f"{2 + 2}")           # "4"
print(f"{name.upper()}")    # "HARRY"
print(f"{name:>10}")        # "     Harry" (right-aligned)
print(f"{3.14159:.2f}")     # "3.14" (2 decimal places)
```

---

## 3. `removeprefix()` and `removesuffix()`

(Python 3.9+)

```python
"https://example.com".removeprefix("https://")   # "example.com"
"file.txt".removesuffix(".txt")                  # "file"
"@Senthur".removeprefix("@")                     # "Senthur"
```

### Before Python 3.9:
```python
text = "Hello, World!"
prefix = "Hello, "
if text.startswith(prefix):
    result = text[len(prefix):]
```

| Method | Removes from |
| :--- | :--- |
| `removeprefix()` | Start |
| `removesuffix()` | End |
| `strip()` | Both ends (whitespace) |

---

## 4. `None` from `.append()`

Methods that modify in place return `None`.

```python
names = []
result = names.append("Harry")
print(result)   # None
print(names)    # ["Harry"]
```

### ⚠️ Common bug:
```python
print("Hello", names.append("Harry"))
# Output: Hello None
```

### ✅ Fix:
```python
names.append("Harry")
print("Hello", names[-1])   # Hello Harry
```

### Methods that return `None`:
| Method | Returns |
| :--- | :--- |
| `list.append()` | `None` |
| `list.sort()` | `None` |
| `list.reverse()` | `None` |
| `set.add()` | `None` |
| `dict.update()` | `None` |

---

## 5. Commas Create Tuples

```python
def get_point():
    return 10, 20           # Returns a TUPLE (10, 20)

def __str__(self):
    return self.name, self.house   # ❌ Tuple, not string!
```

### ✅ Correct:
```python
def __str__(self):
    return f"{self.name} from {self.house}"   # String!
```

---

## 6. `and` vs `+` for Strings

```python
"Harry" and "Stag"   # "Stag" (last truthy value)
"Harry" or "Stag"    # "Harry" (first truthy value)
"Harry" + "Stag"     # "HarryStag" (concatenation)
```

### ⚠️ Common bug:
```python
def __str__(self):
    return self.name and self.house   # ❌ Returns only self.house!
```

### ✅ Fix:
```python
def __str__(self):
    return f"{self.name} has {self.house}"
```

---

## 7. `__init__` Must Return `None`

```python
def __init__(self, name):
    self.name = name
    return f"Hello {name}"   # ❌ TypeError!
```

**Fix:** Remove the `return`. Use `__str__` for string representation.

---

## 8. `__str__` Must Return a String

```python
def __str__(self):
    return print(self.name)        # ❌ Returns None
    return self.name, self.house   # ❌ Returns tuple
    return {self.name}             # ❌ Returns set
```

### ✅ Correct:
```python
def __str__(self):
    return f"{self.name} from {self.house}"
```

---

## 9. `assert` Has No Colon

```python
assert square(3) == 9:    # ❌ SyntaxError
assert square(3) == 9     # ✅ Correct
```

---

## 10. Uppercase vs Lowercase in File Modes

```python
open("file.txt", "W")   # ❌ ValueError
open("file.txt", "w")   # ✅ Correct
open("file.txt", "A")   # ❌ ValueError
open("file.txt", "a")   # ✅ Correct
```

**Always lowercase:** `"r"`, `"w"`, `"a"`, `"r+"`, `"w+"`.

---

## 11. `{}` is an Empty Dict, Not a Set

```python
type({})            # <class 'dict'>
type(set())         # <class 'set'>
type({1, 2, 3})     # <class 'set'>
```

**For an empty set:** Use `set()`.

---

## 12. Single-Item Tuple Needs a Comma

```python
type((5))       # <class 'int'>  ← Parentheses are just grouping
type((5,))      # <class 'tuple'> ✅
```

---

## 13. `input()` Returns a String

```python
x = input("Enter: ")   # x = "5" (string)
x + 1                  # ❌ TypeError: can only concatenate str

x = int(input("Enter: "))   # ✅ x = 5 (integer)
```

---

## 14. Mutable Default Arguments

```python
def add_item(item, my_list=[]):    # ❌ Shared across calls!
    my_list.append(item)
    return my_list

add_item("a")   # ["a"]
add_item("b")   # ["a", "b"]  ← Surprise!
```

### ✅ Fix:
```python
def add_item(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list
```

---

## 15. Integer Division and Modulo

```python
5 / 2      # 2.5 (true division)
5 // 2     # 2 (floor division)
5 % 2      # 1 (modulo)
```

---

## 16. `is` vs `==`

```python
a = [1, 2, 3]
b = [1, 2, 3]

a == b     # True (same values)
a is b     # False (different objects)

x = None
x is None  # ✅ Recommended
x == None  # ⚠️ Works but not Pythonic
```

---

## 17. Truthy and Falsy Values

**Falsy values:** `False`, `0`, `0.0`, `""`, `[]`, `{}`, `()`, `set()`, `None`

**Everything else is truthy.**

```python
if []:
    print("Truthy")     # Never runs

if [1, 2]:
    print("Truthy")     # Runs!
```

---

## Golden Rules

1. **Use `f"..."`** for string interpolation.
2. **`append()` returns `None`** — separate the action from printing.
3. **Commas create tuples** — don't use them in `__str__`.
4. **`and` is boolean**, not string concatenation.
5. **`__init__` returns `None`**, `__str__` returns a string.
6. **File modes are lowercase.**
7. **`{}` is an empty dict**, use `set()` for a set.
8. **Single-item tuple needs a comma:** `(5,)`.
9. **`input()` returns a string** — convert with `int()` or `float()`.
10. **Never use mutable default arguments.**