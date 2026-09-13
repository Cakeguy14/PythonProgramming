# Python Modules & Packages — Complete Reference

## 1. Importing Modules

```python
import math                          # Import whole module
from math import sqrt                # Import specific function
from math import sqrt, pi            # Import multiple
import math as m                     # Alias
from math import sqrt as square_root # Alias a function
```

---

## 2. `pip` — Installing Packages

```bash
pip install requests           # Install a package
pip install pillow             # Note: install "pillow", import "PIL"
pip install requests==2.28.0   # Specific version
pip uninstall requests         # Remove
pip list                       # Show installed packages
```

### ⚠️ Never run `pip install` inside Python (`>>>`)!
```python
>>> pip install requests   # ❌ SyntaxError
```

Run it in the **terminal**, not the Python interpreter.

---

## 3. Import Name vs Install Name

| Install with `pip` | Import in Python |
| :--- | :--- |
| `pillow` | `PIL` |
| `scikit-learn` | `sklearn` |
| `opencv-python` | `cv2` |
| `beautifulsoup4` | `bs4` |

**Example:**
```bash
pip install pillow
```
```python
from PIL import Image   # ✅
```

---

## 4. `__init__.py` — Marking a Package

A folder becomes a Python package when it contains `__init__.py`.

```
my_project/
├── my_package/
│   ├── __init__.py      ← Makes this a package
│   ├── module1.py
│   └── module2.py
└── main.py
```

### Without `__init__.py`:
```python
from my_package import module1   # ❌ ImportError
```

### With `__init__.py` (even empty):
```python
from my_package import module1   # ✅ Works
```

### Uses of `__init__.py`:

| Purpose | Example |
| :--- | :--- |
| Mark folder as package | Empty file |
| Control `import *` | `__all__ = ["module1"]` |
| Expose clean API | `from .module1 import my_function` |
| Initialization code | `print("Loading package...")` |

---

## 5. Common Standard Library Modules

| Module | Purpose |
| :--- | :--- |
| `sys` | Command-line args, exit |
| `os` | File paths, directories |
| `math` | Math functions |
| `random` | Random numbers |
| `datetime` | Dates and times |
| `json` | JSON parsing |
| `csv` | CSV files |
| `re` | Regular expressions |
| `collections` | `Counter`, `defaultdict`, etc. |
| `itertools` | Iteration tools |
| `functools` | `reduce`, `lru_cache` |

---

## 6. Common Third-Party Libraries

| Library | Purpose | Install |
| :--- | :--- | :--- |
| `requests` | HTTP requests | `pip install requests` |
| `pillow` | Image processing | `pip install pillow` |
| `yaml` | YAML parsing | `pip install pyyaml` |
| `numpy` | Numerical computing | `pip install numpy` |
| `pandas` | Data analysis | `pip install pandas` |
| `flask` | Web framework | `pip install flask` |
| `cowsay` | Fun ASCII art | `pip install cowsay` |

---

## 7. `sys` Module Examples

```python
import sys

# Command-line arguments
print(sys.argv)              # ['script.py', 'arg1', 'arg2']

# Exit the program
sys.exit(0)                  # 0 = success, 1 = error

# Python version
print(sys.version)           # '3.13.0 ...'

# Platform
print(sys.platform)          # 'win32' or 'linux'
```

---

## 8. `random` Module Examples

```python
import random
from random import choice, randint, shuffle

random.random()              # 0.0 to 1.0
random.randint(1, 100)       # 1 to 100 (inclusive)
random.choice(["a", "b"])    # Random element
random.shuffle(my_list)      # Shuffles IN PLACE (returns None)
random.sample(range(100), 5) # 5 unique random numbers
```

### ⚠️ `shuffle()` returns `None`:
```python
my_list = [1, 2, 3]
result = random.shuffle(my_list)
print(result)   # None
print(my_list)  # [3, 1, 2] (shuffled)
```

---

## 9. `os` Module Examples

```python
import os

os.getcwd()                        # Current directory
os.listdir(".")                    # Files in current directory
os.path.isfile("file.txt")         # True if file exists
os.path.isdir("folder")            # True if directory exists
os.path.join("folder", "file.txt") # "folder/file.txt" (correct separator)
os.makedirs("new/folder", exist_ok=True)
```

---

## 10. `requests` Module Example

```python
import requests

response = requests.get(
    "https://itunes.apple.com/search",
    params={"entity": "song", "limit": 1, "term": "Queen"}
)
data = response.json()
print(data)
```

### ⚠️ Don't mix URL params and `params`:
```python
# ❌ Wrong — appends "Queen" as a separate param
requests.get(".../search?term=", "Queen")

# ✅ Correct — let requests build the URL
requests.get(".../search", params={"term": "Queen"})
```

---

## 11. `yaml` Module Example

```python
import yaml

with open("config.yaml") as f:
    data = yaml.safe_load(f)

print(data)
```

---

## Golden Rules

1. **`pip install` in the terminal**, `import` in Python.
2. **`pillow` installs as `PIL`.**
3. **`__init__.py`** marks a folder as a package.
4. **Always use `r"..."`** for regex patterns.
5. **`random.shuffle()` returns `None`** — modifies in place.
6. **Use `os.path.isfile()`** to check file existence.
7. **`sys.argv[0]`** is the script name.
8. **Check `len(sys.argv)`** before accessing arguments.