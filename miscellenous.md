# Python Miscellaneous Topics — Complete Reference

## 1. Pillow — Creating GIFs

```python
import sys
from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "sample.gif",
    save_all=True,
    append_images=images[1:],   # ✅ All remaining images
    duration=200,
    loop=0
)
```

### Why `append_images` needs a list:

| Code | What it does |
| :--- | :--- |
| `append_images=images[1]` | ❌ Passes a single image (TypeError) |
| `append_images=[images[1]]` | ✅ Passes a list with 1 image (2 frames total) |
| `append_images=images[1:]` | ✅ Passes all remaining images (N frames) |

**Why a list?** Because Pillow needs to **iterate** over multiple frames.

---

## 2. Memory Diagrams — Classes & Objects

### Class variables vs instance variables:

```
CLASS: Student
┌─────────────────────────┐
│  school = "Hogwarts"    │ ← Shared by all
│  introduce(self)        │ ← Method
└─────────────────────────┘
         ▲          ▲
    ┌────┴────┐ ┌───┴─────┐
    │ harry   │ │ ron     │
    │ name=   │ │ name=   │ ← Unique per object
    │ "Harry" │ │ "Ron"   │
    └─────────┘ └─────────┘
```

### Object creation flow:

```
Student("Harry", "Gryffindor")
    │
    ├─→ Create empty object
    ├─→ Call __init__(self, "Harry", "Gryffindor")
    │       ├─→ self.name = "Harry"
    │       └─→ self.house = "Gryffindor"
    └─→ Return completed object
```

### `@property` memory layout:

```
┌──────────────────────────────────────┐
│           Student Object             │
│                                      │
│  name = "Harry"       (plain attr)   │
│  _house = "Gryffindor" (raw storage) │
│                                      │
│  house (property):                   │
│  ├─ GET: obj.house → getter → _house │
│  └─ SET: obj.house = x → setter      │
└──────────────────────────────────────┘
```

---

## 3. Hashability — Why Tuples Can Be Dict Keys

> **Dictionary keys must be hashable (immutable).**

| Type | Mutable? | Hashable? | Can be dict key? |
| :--- | :--- | :--- | :--- |
| `int`, `str`, `float` | ❌ | ✅ | ✅ |
| `tuple` (of immutables) | ❌ | ✅ | ✅ |
| `frozenset` | ❌ | ✅ | ✅ |
| `list` | ✅ | ❌ | ❌ |
| `dict` | ✅ | ❌ | ❌ |
| `set` | ✅ | ❌ | ❌ |

```python
grid = {(0, 0): "start", (1, 0): "wall"}
print(grid[(0, 0)])   # "start"

# grid = {[0, 0]: "start"}   # ❌ TypeError: unhashable type: 'list'
```

**Rule:** A tuple is hashable only if all items inside are hashable.
```python
(1, 2, 3)       # ✅ Hashable
(1, [2, 3])     # ❌ Not hashable (contains a list)
(1, (2, 3))     # ✅ Hashable (nested tuple)
```

---

## 4. Time Complexity

| Operation | List | Tuple | Set | Dict |
| :--- | :--- | :--- | :--- | :--- |
| **Index access** | O(1) | O(1) | ❌ | O(1) by key |
| **Search (`in`)** | O(n) | O(n) | **O(1)** | **O(1)** |
| **Insert** | O(1) at end | ❌ | O(1) | O(1) |
| **Delete** | O(n) | ❌ | O(1) | O(1) |

**Takeaway:** Use sets/dicts for large collections where you need fast `in` checks.

---

## 5. CSV Quoting

When a field contains a comma, CSV wraps it in quotes:

```python
writer.writerow(["Harry", "Diagon, Alley"])
```

**File content:**
```
Harry,"Diagon, Alley"
```

**Why?** Without quotes, the comma would be treated as a column separator.

| Input | Without quotes | With quotes |
| :--- | :--- | :--- |
| `Diagon, Alley` | `Harry,Diagon, Alley` (3 columns!) | `Harry,"Diagon, Alley"` (2 columns) |

---

## 6. Empty Lines in CSV

**Cause:** Missing `newline=""` when opening the file.

```python
# ❌ Without newline=""
with open("file.csv", "a") as f:
    writer = csv.writer(f)
    writer.writerow([name, home])
# Result: blank line between rows

# ✅ With newline=""
with open("file.csv", "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([name, home])
# Result: no blank lines
```

---

## 7. Unpacking Works with Any Iterable

```python
a, b, c = [1, 2, 3]           # List
a, b, c = (1, 2, 3)           # Tuple
a, b, c = {1, 2, 3}           # Set (order random)
a, b, c = "abc"               # String
a, b = {"x": 1, "y": 2}       # Dict (keys only)

# Star (*) grabs the rest
first, *rest = [1, 2, 3, 4]   # first=1, rest=[2, 3, 4]

# Swap works with any values
a, b = b, a
```

---

## 8. `dict.fromkeys()` — Classmethod Example

```python
d = dict.fromkeys(["a", "b", "c"], 0)
print(d)   # {'a': 0, 'b': 0, 'c': 0}
```

**Why classmethod?** Subclasses work:
```python
from collections import OrderedDict
od = OrderedDict.fromkeys(["a", "b"])
print(type(od))   # <class 'collections.OrderedDict'>
```

---

## 9. `@classmethod` — Alternative Constructors

```python
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, date_str):
        year, month, day = map(int, date_str.split("-"))
        return cls(year, month, day)   # 'cls' respects inheritance

d = Date.from_string("2026-09-13")
print(d.year)   # 2026
```

**Why `cls` instead of `Date`?** Subclasses work:
```python
class SpecialDate(Date):
    pass

sd = SpecialDate.from_string("2026-09-13")
print(type(sd))   # <class 'SpecialDate'>
```

---

## 10. `@classmethod` vs `@staticmethod` vs Instance Method

| Feature | Instance Method | Class Method | Static Method |
| :--- | :--- | :--- | :--- |
| **First arg** | `self` | `cls` | None |
| **Receives** | Instance | Class | Nothing |
| **Can access instance data?** | ✅ | ❌ | ❌ |
| **Can access class data?** | ✅ | ✅ | ❌ |
| **Called on** | Instance | Class or instance | Class or instance |
| **Use for** | Actions on instance | Factory methods, class state | Utility functions |

---

## Golden Rules

1. **`append_images`** in Pillow needs a list.
2. **Methods live on the class**, data lives on instances.
3. **Immutable = hashable = can be dict key.**
4. **Sets and dicts are O(1)** for `in` checks.
5. **CSV quotes fields** that contain commas.
6. **`newline=""`** prevents blank lines in CSV.
7. **Unpacking works with any iterable**, not just tuples.
8. **`@classmethod` uses `cls`** to support inheritance.
9. **Use `@classmethod` for alternative constructors.**