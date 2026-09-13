# Python File Handling — Complete Reference

## 1. Opening a File

```python
f = open("file.txt", "r")   # Read mode (default)
f = open("file.txt", "w")   # Write mode (overwrites!)
f = open("file.txt", "a")   # Append mode (adds to end)
f = open("file.txt", "r+")  # Read and write
```

| Mode | Meaning | Creates file? | Overwrites? |
| :--- | :--- | :--- | :--- |
| `"r"` | Read only | ❌ | ❌ |
| `"w"` | Write | ✅ | ✅ Yes |
| `"a"` | Append | ✅ | ❌ |
| `"r+"` | Read + write | ❌ | ❌ |
| `"w+"` | Write + read | ✅ | ✅ Yes |

### ⚠️ `"W"` (uppercase) is invalid!
```python
open("file.txt", "W")   # ❌ ValueError: invalid mode: 'W'
open("file.txt", "w")   # ✅ Lowercase
```

---

## 2. Reading a File

```python
# Read entire file
with open("file.txt", "r") as f:
    content = f.read()

# Read line by line
with open("file.txt", "r") as f:
    for line in f:
        print(line.rstrip())   # rstrip() removes \n

# Read all lines into a list
with open("file.txt", "r") as f:
    lines = f.readlines()
```

---

## 3. Writing to a File

```python
# Write (overwrites the file)
with open("file.txt", "w") as f:
    f.write("Hello\n")
    f.write("World\n")

# Append (adds to end)
with open("file.txt", "a") as f:
    f.write("New line\n")
```

### `write()` vs `print(file=f)`

| Method | Newline added? |
| :--- | :--- |
| `f.write("Hello")` | ❌ No |
| `f.write("Hello\n")` | ✅ Manual |
| `print("Hello", file=f)` | ✅ Automatic |

---

## 4. Closing a File

```python
f = open("file.txt", "r")
content = f.read()
f.close()   # ✅ Always close!
```

### ⚠️ `NameError` if `f` was never defined:
```python
f.close()   # ❌ NameError: name 'f' is not defined
```

---

## 5. `with` Statement — Auto-Close

```python
with open("file.txt", "r") as f:
    content = f.read()
# File is automatically closed here
```

**Why use `with`?** It closes the file even if an error occurs inside the block.

---

## 6. `newline=""` — CSV Files

Always use `newline=""` when working with CSV files on Windows.

```python
with open("file.csv", "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([name, home])
```

**Without `newline=""`:** You get empty lines between rows.

| Code | Result |
| :--- | :--- |
| `open("file.csv", "a")` | `Harry,Diagon Alley`<br><br>`Ron,The Burrow` ← blank line! |
| `open("file.csv", "a", newline="")` | `Harry,Diagon Alley`<br>`Ron,The Burrow` ✅ |

---

## 7. CSV Module

### `csv.writer` — Uses lists
```python
import csv

with open("file.csv", "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "home"])       # Headers
    writer.writerow([name, home])           # Data
```

### `csv.DictWriter` — Uses dictionaries
```python
import csv

with open("file.csv", "a", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "home"])
    writer.writeheader()                    # Auto writes "name,home"
    writer.writerow({"name": name, "home": home})
```

### Comparison:

| Feature | `csv.writer` | `csv.DictWriter` |
| :--- | :--- | :--- |
| Input | List `[name, home]` | Dict `{"name": name, "home": home}` |
| Column order | By list position | By `fieldnames` |
| Header | Manual `writerow(["name", "home"])` | Auto `writeheader()` |
| Safety | Risk of swapping | Keys protect order |

---

## 8. CSV Quoting

If a field contains a comma, CSV wraps it in quotes:

```python
writer.writerow(["Harry", "Diagon, Alley"])
```

**File content:**
```
Harry,"Diagon, Alley"
```

**Why?** Without quotes, the comma would be treated as a column separator.

---

## 9. Checking If a File Exists

```python
import os

if os.path.isfile("file.csv"):
    print("File exists!")
else:
    print("File doesn't exist!")
```

### Use case: Write headers only once
```python
import csv
import os

file_exists = os.path.isfile("file.csv")

with open("file.csv", "a", newline="") as f:
    writer = csv.writer(f)
    if not file_exists:
        writer.writerow(["name", "home"])
    writer.writerow([name, home])
```

---

## 10. `rstrip()` — Remove Newlines

```python
with open("file.txt") as f:
    for line in f:
        name = line.rstrip()   # Removes trailing \n
        print(name)
```

---

## 11. Sorting Lines from a File

```python
with open("file.txt") as f:
    for line in sorted(f):
        print(line.rstrip())

# Case-insensitive sort
with open("file.txt") as f:
    for line in sorted(f, key=str.lower):
        print(line.rstrip())
```

---

## 12. YAML Files

```python
import yaml
import sys

if len(sys.argv) > 1:
    file_path = sys.argv[1]
    with open(file_path, "r") as f:
        data = yaml.safe_load(f)
    print(data)
```

---

## 13. Common Errors

| Error | Cause | Fix |
| :--- | :--- | :--- |
| `ValueError: invalid mode: 'W'` | Uppercase mode | Use lowercase `"w"` |
| `NameError: name 'f' is not defined` | `f` never opened | Open file first |
| `FileNotFoundError` | File doesn't exist | Check path or use `"a"` mode |
| `TypeError: expected str, not list` | Passed list to `open()` | Use `sys.argv[1]` not `sys.argv[1:]` |
| Empty lines in CSV | Missing `newline=""` | Add `newline=""` |

---

## Golden Rules

1. **Use `with open(...)`** — auto-closes files.
2. **`"w"` overwrites**, `"a"` appends.
3. **Always use `newline=""`** for CSV files.
4. **`print(..., file=f)`** adds newlines automatically.
5. **`rstrip()`** removes `\n` when reading lines.
6. **Check `os.path.isfile()`** before writing headers.
7. **Lowercase modes only** — `"r"`, `"w"`, `"a"`.