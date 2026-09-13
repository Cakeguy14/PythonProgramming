# Python Command-Line Arguments — Complete Reference

## 1. `sys.argv`

`sys.argv` is a list of command-line arguments passed to the script.

```python
import sys

print(sys.argv)
```

**Run:**
```bash
python script.py hello world
```

**Output:**
```python
['script.py', 'hello', 'world']
```

| Index | Value |
| :--- | :--- |
| `sys.argv[0]` | `'script.py'` (script name) |
| `sys.argv[1]` | `'hello'` |
| `sys.argv[2]` | `'world'` |

---

## 2. Getting a Single Argument

```python
import sys

if len(sys.argv) == 2:
    name = sys.argv[1]
    print(f"Hello, {name}")
else:
    print("Usage: python script.py <name>")
```

---

## 3. `sys.argv[1:]` — List of All Arguments

```python
import sys

for arg in sys.argv[1:]:
    print(arg)
```

**Run:**
```bash
python script.py a b c
```

**Output:**
```
a
b
c
```

---

## 4. ⚠️ Common Mistake: Passing a List to `open()`

```python
file_path = sys.argv[1:]   # ❌ This is a LIST
with open(file_path, "r") as f:   # ❌ TypeError!
```

**Why:** `sys.argv[1:]` returns a **list**, but `open()` expects a **string**.

### ✅ Fix 1: Use `sys.argv[1]` (single file)
```python
file_path = sys.argv[1]   # ✅ A string
with open(file_path, "r") as f:
    ...
```

### ✅ Fix 2: Loop through multiple files
```python
for file_path in sys.argv[1:]:
    with open(file_path, "r") as f:
        ...
```

---

## 5. Full Example

```python
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <file>")
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        with open(file_path, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"File not found: {file_path}")

if __name__ == "__main__":
    main()
```

**Run:**
```bash
python script.py data.txt
```

---

## 6. Using `sys.argv` with APIs

```python
import sys
import requests

if len(sys.argv) > 1:
    term = sys.argv[1]
    response = requests.get(
        "https://itunes.apple.com/search",
        params={"entity": "song", "limit": 1, "term": term}
    )
    print(response.json())
```

**Run:**
```bash
python itunes.py "Taylor Swift"
```

---

## 7. `sys.exit()` — Exit the Program

```python
import sys

if len(sys.argv) < 2:
    print("Error: Missing argument")
    sys.exit(1)   # Exit with error code 1

# Continue...
```

| Code | Meaning |
| :--- | :--- |
| `sys.exit(0)` | Success (default) |
| `sys.exit(1)` | Error |

---

## Golden Rules

1. **`sys.argv[0]`** is always the script name.
2. **`sys.argv[1]`** is the first user argument.
3. **`sys.argv[1:]`** is a **list** of all arguments.
4. **Use `sys.argv[1]`** for a single file — not `sys.argv[1:]`.
5. **Always check `len(sys.argv)`** before accessing arguments.
6. **Quote arguments with spaces** in the terminal: `"my file.txt"`.