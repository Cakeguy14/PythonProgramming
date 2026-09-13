# Python Functions & Arguments — Complete Reference

## 1. Parameters vs Arguments

| Term | Where | Example |
| :--- | :--- | :--- |
| **Parameter** | In the function definition | `def greet(name):` → `name` is a parameter |
| **Argument** | In the function call | `greet("Harry")` → `"Harry"` is an argument |

```python
def greet(name):        # 'name' is a parameter
    return f"Hello, {name}"

greet("Harry")          # "Harry" is an argument
```

---

## 2. When to Use Parameters

> **Add a parameter ONLY if the function needs information from outside to do its job.**

| Function | Needs parameter? | Why? |
| :--- | :--- | :--- |
| `def square(n):` | ✅ Yes | Needs to know which number to square |
| `def test_square():` | ❌ No | Already knows what to test internally |
| `def greet(name):` | ✅ Yes | Needs to know who to greet |
| `def get_time():` | ❌ No | Just returns the current time |

```python
def square(n):          # ✅ Needs a number
    return n * n

def test_square():      # ✅ Doesn't need anything
    assert square(3) == 9
    assert square(4) == 16
```

---

## 3. `return` vs `print`

| Action | What it does | Where the value goes |
| :--- | :--- | :--- |
| `return x` | Sends value back to caller | Caller's variable |
| `print(x)` | Displays value on screen | Nowhere (returns `None`) |

```python
# RETURN — the value comes back
def square(n):
    return n * n

result = square(3)      # result = 9
print(result)           # 9

# PRINT — nothing comes back
def square(n):
    print(n * n)

result = square(3)      # prints 9, result = None
print(result)           # None
```

### ⚠️ Common bug:
```python
def greet(name):
    print(f"Hello, {name}")

print(greet("Harry"))
# Output:
# Hello, Harry
# None         ← because greet() returns None
```

---

## 4. Argument Evaluation Order

Python evaluates arguments **before** checking the function signature.

```python
def main():
    number = get_number(n)   # ❌ NameError: 'n' is not defined
```

**Step-by-step:**
1. Python looks for `n` in `main()`'s scope → not found → `NameError`.
2. The function signature check never happens.

### All three scenarios:

| Call | What Python checks first | Result |
| :--- | :--- | :--- |
| `get_number()` | Argument count: needs 1, got 0 | `TypeError` |
| `get_number(n)` | Does `n` exist? No. | `NameError` |
| `get_number(5)` | `5` exists. Count matches. | ✅ Works |

---

## 5. Function Definition Order

Python looks for a function **when it's called**, not when it's defined.

### ✅ Works (greet defined before main is called):
```python
def main():
    greet("Harry")

def greet(name):
    print(f"Hello, {name}")

main()   # ✅ Works
```

### ❌ Fails (greet called before defined):
```python
def main():
    greet("Harry")

main()   # ❌ NameError: 'greet' is not defined

def greet(name):   # Too late!
    print(f"Hello, {name}")
```

---

## 6. `end=""` — Print Without Newline

By default, `print()` adds a newline (`\n`) at the end. `end=""` removes it.

```python
# Default: each print on its own line
print("Hello")
print("World")
# Hello
# World

# With end="": all on same line
print("Hello", end="")
print("World", end="")
# HelloWorld
```

### Common uses:
```python
# Build a row character by character
for _ in range(5):
    print("?", end="")   # ????? 
print()                  # Move to next line

# Custom separator
print("Hello", end="!!!")   # Hello!!!
```

---

## 7. `sep` — Change the Separator

```python
print("a", "b", "c")              # a b c (default: space)
print("a", "b", "c", sep=", ")    # a, b, c
print("a", "b", "c", sep="-")     # a-b-c
print("a", "b", "c", sep="")      # abc
```

---

## 8. `print(..., file=f)` — Write to File

`print()` can write to a file instead of the screen.

```python
with open("output.txt", "a") as f:
    print("Hello", file=f)   # Writes "Hello\n" to file
```

**Why this is useful:** `print()` automatically adds a newline, so you don't need `f.write(name + "\n")`.

| Method | Newline added? |
| :--- | :--- |
| `f.write(name)` | ❌ No |
| `f.write(name + "\n")` | ✅ Yes (manual) |
| `print(name, file=f)` | ✅ Yes (automatic) |

---

## 9. Default Parameters

```python
def greet(name="World"):
    return f"Hello, {name}"

greet()           # "Hello, World"
greet("Harry")    # "Hello, Harry"
```

---

## 10. `*args` and `**kwargs`

```python
def sum_all(*args):          # Any number of positional args
    return sum(args)

sum_all(1, 2, 3)             # 6
sum_all(1, 2, 3, 4, 5)       # 15

def print_info(**kwargs):    # Any number of keyword args
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Harry", house="Gryffindor")
```

---

## 11. Common Errors & Fixes

| Error | Cause | Fix |
| :--- | :--- | :--- |
| `TypeError: missing 1 required positional argument` | Wrong number of args | Match the function signature |
| `NameError: name 'x' is not defined` | Variable/function doesn't exist | Define it before calling |
| `TypeError: greet() takes 0 positional arguments but 1 was given` | Too many args | Remove the argument or add a parameter |

---

## Golden Rules

1. **Add a parameter only if the function needs outside data.**
2. **`return` sends a value back; `print` displays it.**
3. **Arguments are evaluated before the function signature is checked.**
4. **Functions must be defined before they are called.**
5. **`end=""` keeps the cursor on the same line.**
6. **`print(..., file=f)` writes to a file with an automatic newline.**