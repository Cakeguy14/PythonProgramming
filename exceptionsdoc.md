# Python Exception Handling — Complete Reference

## 1. Basic `try/except`

```python
try:
    x = int(input("Enter a number: "))
except ValueError:
    print("That's not a number!")
```

---

## 2. `try/except/finally`

The `finally` block **always runs**, even if there's a `return`.

```python
def get_number():
    while True:
        try:
            return int(input("Enter a number: "))
        except ValueError:
            pass
        finally:
            print("This always runs!")

get_number()
```

**Output:**
```
Enter a number: 5
This always runs!
```

**Key rule:** The `finally` block runs **before** the `return` actually returns.

---

## 3. `try/except/else`

The `else` block runs if **no exception** occurred.

```python
try:
    x = int(input("Enter a number: "))
except ValueError:
    print("Not a number!")
else:
    print(f"You entered: {x}")
```

---

## 4. Multiple Exceptions

```python
try:
    x = int(input())
    y = 10 / x
except ValueError:
    print("Not a number!")
except ZeroDivisionError:
    print("Can't divide by zero!")
```

### Catch multiple in one block:
```python
except (ValueError, TypeError) as e:
    print(f"Error: {e}")
```

---

## 5. `raise` — Manually Trigger an Exception

```python
def get_positive_number():
    while True:
        try:
            x = int(input("Enter a positive integer: "))
            if x < 0:
                raise ValueError("Negative numbers are not allowed.")
            return x
        except ValueError as e:
            print(e)
```

---

## 6. `pass` — Silently Ignore

```python
try:
    x = int(input())
except ValueError:
    pass   # Do nothing, silently ignore the error
```

---

## 7. `except ... as e` — Access the Error

```python
try:
    x = int("hello")
except ValueError as e:
    print(e)   # invalid literal for int() with base 10: 'hello'
```

---

## 8. Common Exception Types

| Exception | When it occurs |
| :--- | :--- |
| `ValueError` | Right type, wrong value (`int("abc")`) |
| `TypeError` | Wrong type (`"a" + 1`) |
| `NameError` | Variable not defined |
| `IndexError` | List index out of range |
| `KeyError` | Dict key doesn't exist |
| `AttributeError` | Method/attribute doesn't exist |
| `ZeroDivisionError` | Division by zero |
| `FileNotFoundError` | File doesn't exist |
| `ModuleNotFoundError` | Library not installed |
| `AssertionError` | `assert` statement failed |

---

## 9. `finally` vs `except` vs `else`

| Block | Runs when |
| :--- | :--- |
| `except` | An exception occurred |
| `else` | No exception occurred |
| `finally` | **Always** (even with `return` or `raise`) |

```python
try:
    x = int(input())
except ValueError:
    print("Error!")
else:
    print("Success!")
finally:
    print("Done!")
```

---

## 10. Real-World Example: Safe File Reading

```python
try:
    with open("data.txt") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("No permission to read file!")
else:
    print(content)
finally:
    print("Attempted to read file.")
```

---

## Golden Rules

1. **`try`** the risky code.
2. **`except`** handle specific errors.
3. **`else`** runs if no error.
4. **`finally`** always runs — even with `return`.
5. **`raise`** to manually trigger an error.
6. **`pass`** to silently ignore.
7. **`as e`** to access the error message.