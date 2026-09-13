# Python Loops & Control Flow — Complete Reference

## 1. `for` Loop

Iterates over any iterable (list, tuple, string, range, dict, etc.).

```python
for i in range(5):
    print(i)        # 0 1 2 3 4

for fruit in ["apple", "banana", "cherry"]:
    print(fruit)

for char in "hello":
    print(char)
```

---

## 2. `while` Loop

Repeats as long as the condition is `True`.

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

---

## 3. `while True` — Infinite Loop with `break`

```python
while True:
    name = input("Enter name (or 'quit'): ")
    if name == "quit":
        break
    print(f"Hello, {name}")
```

---

## 4. `for _ in range(n)` — Throwaway Variable

The underscore `_` means "I don't care about this value."

```python
for _ in range(3):
    print("Hello")   # Prints "Hello" 3 times
```

---

## 5. Nested Loops

```python
for i in range(3):
    for j in range(3):
        print(f"({i},{j})", end=" ")
    print()
```

**Output:**
```
(0,0) (0,1) (0,2)
(1,0) (1,1) (1,2)
(2,0) (2,1) (2,2)
```

### ⚠️ Common mistake: printing the whole list instead of the item
```python
dummy = ["a", "b", "c"]

for fruit in dummy:
    print(dummy)     # ❌ Prints the whole list 3 times
    print(fruit)     # ✅ Prints each item
```

---

## 6. `break` — Exit the Loop

```python
for i in range(10):
    if i == 5:
        break
    print(i)         # 0 1 2 3 4
```

---

## 7. `continue` — Skip to Next Iteration

```python
for i in range(5):
    if i == 2:
        continue
    print(i)         # 0 1 3 4
```

---

## 8. `else` on Loops

The `else` block runs if the loop completes **without** `break`.

```python
for i in range(5):
    if i == 10:
        break
else:
    print("Loop finished normally")   # Runs!
```

---

## 9. `range()` Variants

```python
range(5)         # 0, 1, 2, 3, 4
range(2, 5)      # 2, 3, 4
range(0, 10, 2)  # 0, 2, 4, 6, 8
range(5, 0, -1)  # 5, 4, 3, 2, 1
```

---

## 10. `enumerate()` — Index + Value

```python
fruits = ["apple", "banana", "cherry"]

for i, fruit in enumerate(fruits):
    print(i, fruit)
# 0 apple
# 1 banana
# 2 cherry

# Start at 1
for i, fruit in enumerate(fruits, start=1):
    print(i, fruit)
```

---

## 11. `zip()` — Loop Over Multiple Iterables

```python
names = ["Harry", "Ron"]
houses = ["Gryffindor", "Gryffindor"]

for name, house in zip(names, houses):
    print(f"{name} is in {house}")
```

---

## 12. Common Loop Patterns

### Asking for input until valid
```python
while True:
    try:
        n = int(input("Enter a positive integer: "))
        if n > 0:
            break
    except ValueError:
        print("Not a number!")
```

### Finding the first match
```python
for item in items:
    if condition(item):
        result = item
        break
else:
    result = None
```

---

## Golden Rules

1. **`for`** when you know how many times to loop.
2. **`while`** when you loop until a condition changes.
3. **`while True` + `break`** for input loops.
4. **`_`** for throwaway variables.
5. **`enumerate()`** when you need both index and value.
6. **`zip()`** when looping over multiple lists together.
7. **Nested loops** run inner loop fully for each outer iteration.