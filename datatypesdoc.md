# Python Data Structures — Complete Reference

## List, Tuple, Set, Dictionary

---

## 1. Quick Overview

| Feature | List | Tuple | Set | Dict |
| :--- | :--- | :--- | :--- | :--- |
| **Syntax** | `[1, 2, 3]` | `(1, 2, 3)` | `{1, 2, 3}` | `{"a": 1, "b": 2}` |
| **Ordered?** | ✅ Yes | ✅ Yes | ❌ No | ✅ Yes (3.7+) |
| **Mutable?** | ✅ Yes | ❌ No | ✅ Yes | ✅ Yes |
| **Duplicates?** | ✅ Allowed | ✅ Allowed | ❌ Not allowed | ❌ Keys unique |
| **Indexing?** | ✅ Yes | ✅ Yes | ❌ No | ❌ No (uses keys) |
| **Hashable?** | ❌ No | ✅ Yes* | ❌ No | ❌ No |
| **Can be dict key?** | ❌ No | ✅ Yes* | ❌ No | ❌ No |

*Tuple is hashable only if all its items are hashable.

---

## 2. Creation

```python
# List
my_list = [1, 2, 3]
my_list = list((1, 2, 3))

# Tuple
my_tuple = (1, 2, 3)
my_tuple = tuple([1, 2, 3])
my_tuple = 1, 2, 3           # parentheses optional
single = (42,)               # ⚠️ Comma needed for single-item tuple!

# Set
my_set = {1, 2, 3}
my_set = set([1, 2, 3])
empty_set = set()            # ⚠️ {} creates a DICT, not a set!

# Dict
my_dict = {"a": 1, "b": 2}
my_dict = dict(a=1, b=2)
empty_dict = {}
```

---

## 3. Accessing Elements

| Action | List | Tuple | Set | Dict |
| :--- | :--- | :--- | :--- | :--- |
| **By index** | `lst[0]` ✅ | `tup[0]` ✅ | ❌ | ❌ |
| **By key** | ❌ | ❌ | ❌ | `d["a"]` ✅ |
| **Negative index** | `lst[-1]` ✅ | `tup[-1]` ✅ | ❌ | ❌ |
| **Slicing** | `lst[1:3]` ✅ | `tup[1:3]` ✅ | ❌ | ❌ |
| **`in` check** | `x in lst` ✅ | `x in tup` ✅ | `x in s` ✅ | `k in d` ✅ (keys) |

---

## 4. Modifying (Mutability)

| Action | List | Tuple | Set | Dict |
| :--- | :--- | :--- | :--- | :--- |
| **Add item** | `lst.append(x)` | ❌ | `s.add(x)` | `d[key] = val` |
| **Remove item** | `lst.remove(x)` | ❌ | `s.remove(x)` | `del d[key]` |
| **Change item** | `lst[0] = x` | ❌ | ❌ | `d[key] = new` |
| **Clear all** | `lst.clear()` | ❌ | `s.clear()` | `d.clear()` |
| **Sort in place** | `lst.sort()` | ❌ | ❌ | ❌ |

---

## 5. Operations

| Operation | List | Tuple | Set | Dict |
| :--- | :--- | :--- | :--- | :--- |
| **Length** | `len(lst)` | `len(tup)` | `len(s)` | `len(d)` |
| **Concatenate** | `lst1 + lst2` | `tup1 + tup2` | ❌ | ❌ |
| **Repeat** | `lst * 3` | `tup * 3` | ❌ | ❌ |
| **Union** | ❌ | ❌ | `s1 \| s2` | ❌ |
| **Intersection** | ❌ | ❌ | `s1 & s2` | ❌ |
| **Difference** | ❌ | ❌ | `s1 - s2` | ❌ |
| **Merge** | ❌ | ❌ | ❌ | `d1 \| d2` (3.9+) |

---

## 6. Methods Comparison

| Method | List | Tuple | Set | Dict |
| :--- | :--- | :--- | :--- | :--- |
| `.append()` | ✅ | ❌ | ❌ | ❌ |
| `.add()` | ❌ | ❌ | ✅ | ❌ |
| `.remove()` | ✅ | ❌ | ✅ | ❌ |
| `.pop()` | ✅ | ❌ | ✅ | ✅ |
| `.index()` | ✅ | ✅ | ❌ | ❌ |
| `.count()` | ✅ | ✅ | ❌ | ❌ |
| `.sort()` | ✅ | ❌ | ❌ | ❌ |
| `.reverse()` | ✅ | ❌ | ❌ | ❌ |
| `.keys()` | ❌ | ❌ | ❌ | ✅ |
| `.values()` | ❌ | ❌ | ❌ | ✅ |
| `.items()` | ❌ | ❌ | ❌ | ✅ |
| `.get()` | ❌ | ❌ | ❌ | ✅ |
| `.update()` | ❌ | ❌ | ✅ | ✅ |

---

## 7. Performance (Time Complexity)

| Operation | List | Tuple | Set | Dict |
| :--- | :--- | :--- | :--- | :--- |
| **Index access** | O(1) | O(1) | ❌ | O(1) by key |
| **Search (`in`)** | O(n) | O(n) | **O(1)** | **O(1)** by key |
| **Insert** | O(1) at end | ❌ | O(1) | O(1) |
| **Delete** | O(n) | ❌ | O(1) | O(1) |
| **Memory** | Medium | **Low** | High | High |

**Key takeaway:** Sets and dicts are much faster for lookups on large collections.

---

## 8. Iteration

```python
# List
for item in [1, 2, 3]:
    print(item)

# Tuple
for item in (1, 2, 3):
    print(item)

# Set
for item in {1, 2, 3}:
    print(item)   # ⚠️ Order not guaranteed

# Dict — three ways
for key in {"a": 1, "b": 2}:
    print(key)                    # Keys only

for value in {"a": 1, "b": 2}.values():
    print(value)                  # Values only

for key, value in {"a": 1, "b": 2}.items():
    print(key, value)             # Both
```

---

## 9. Comprehensions

```python
# List comprehension
squares = [x**2 for x in range(5)]           # [0, 1, 4, 9, 16]

# Tuple — no direct comprehension!
squares = tuple(x**2 for x in range(5))      # Generator → tuple

# Set comprehension
squares = {x**2 for x in range(5)}           # {0, 1, 4, 9, 16}

# Dict comprehension
squares = {x: x**2 for x in range(5)}        # {0: 0, 1: 1, 2: 4, ...}
```

---

## 10. When to Use Each

| Use Case | Best Choice | Why |
| :--- | :--- | :--- |
| **Ordered collection of items** | List | Order matters, mutable |
| **Fixed data that shouldn't change** | Tuple | Immutable, safe, hashable |
| **Unique items, fast lookup** | Set | O(1) `in`, no duplicates |
| **Key-value pairs** | Dict | Mapping keys to values |
| **Function returning multiple values** | Tuple | Automatic packing |
| **Coordinates / RGB values** | Tuple | Immutable, hashable |
| **Removing duplicates** | Set | Automatic deduplication |
| **Counting frequencies** | Dict | `count[item] += 1` |
| **Config / settings** | Dict | Named lookups |
| **Queue / stack** | List | `.append()` / `.pop()` |

---

## 11. Real-World Examples

### List — Todo items
```python
todos = ["Buy groceries", "Walk dog", "Read book"]
todos.append("Call mom")
todos.remove("Walk dog")
```

### Tuple — Coordinates
```python
point = (10, 20)
x, y = point
# point[0] = 99   # ❌ Can't modify
```

### Set — Unique visitors
```python
visitors = {"Alice", "Bob", "Alice", "Charlie"}
print(visitors)   # {"Alice", "Bob", "Charlie"} — duplicates removed!
```

### Dict — Phone book
```python
phonebook = {
    "Alice": "555-1234",
    "Bob": "555-5678"
}
print(phonebook["Alice"])   # "555-1234"
```

---

## 12. Converting Between Types

```python
lst = [1, 2, 2, 3]

tuple(lst)      # (1, 2, 2, 3)
set(lst)        # {1, 2, 3}  ← duplicates removed
list(set(lst))  # [1, 2, 3]  ← deduplicate a list

# Dict from list of tuples
pairs = [("a", 1), ("b", 2)]
dict(pairs)     # {"a": 1, "b": 2}

# Dict to list
d = {"a": 1, "b": 2}
list(d)         # ["a", "b"]   (keys)
list(d.values()) # [1, 2]
list(d.items())  # [("a", 1), ("b", 2)]
```

---

## 13. Unpacking & Swapping

Unpacking works with **any iterable** (list, tuple, set, string, dict, range, generator).

```python
# Unpacking
a, b, c = [1, 2, 3]           # List
a, b, c = (1, 2, 3)           # Tuple
a, b, c = {1, 2, 3}           # Set (order random)
a, b, c = "abc"               # String
a, b = {"x": 1, "y": 2}       # Dict (keys only!)

# With star (*)
first, *rest = [1, 2, 3, 4]   # first=1, rest=[2, 3, 4]
*start, last = [1, 2, 3, 4]   # start=[1, 2, 3], last=4

# Swapping (works with any values — Python creates a temp tuple)
a, b = b, a
```

---

## 14. Dictionary Keys — Hashability Rule

> **Dictionary keys must be hashable (immutable).**

| Type | Mutable? | Hashable? | Can be dict key? |
| :--- | :--- | :--- | :--- |
| `int`, `str`, `float` | ❌ No | ✅ Yes | ✅ Yes |
| `tuple` (of immutables) | ❌ No | ✅ Yes | ✅ Yes |
| `frozenset` | ❌ No | ✅ Yes | ✅ Yes |
| `list` | ✅ Yes | ❌ No | ❌ No |
| `dict` | ✅ Yes | ❌ No | ❌ No |
| `set` | ✅ Yes | ❌ No | ❌ No |

**Example:**
```python
grid = {
    (0, 0): "start",
    (1, 0): "wall",
    (2, 0): "treasure",
}
print(grid[(2, 0)])   # "treasure"

# grid = {[0, 0]: "start"}   # ❌ TypeError: unhashable type: 'list'
```

---

## 15. Common Gotchas

| Gotcha | Example |
| :--- | :--- |
| **`{}` is an empty DICT, not a set** | `type({})` → `dict` |
| **Single-item tuple needs a comma** | `(5)` is int, `(5,)` is tuple |
| **Sets have no order** | `{3, 1, 2}` might print as `{1, 2, 3}` |
| **Lists can't be dict keys** | `{[1]: "x"}` → TypeError |
| **Tuples with lists aren't hashable** | `{(1, [2]): "x"}` → TypeError |
| **Dicts preserve insertion order (3.7+)** | Not guaranteed in older Python |
| **`set()` for empty set** | `{}` creates a dict, not a set! |

---

## 16. Summary Table

| | List | Tuple | Set | Dict |
| :--- | :--- | :--- | :--- | :--- |
| **Syntax** | `[a, b]` | `(a, b)` | `{a, b}` | `{k: v}` |
| **Ordered** | ✅ | ✅ | ❌ | ✅ |
| **Mutable** | ✅ | ❌ | ✅ | ✅ |
| **Duplicates** | ✅ | ✅ | ❌ | ❌ (keys) |
| **Indexed** | ✅ | ✅ | ❌ | ❌ |
| **Hashable** | ❌ | ✅* | ❌ | ❌ |
| **Lookup speed** | O(n) | O(n) | O(1) | O(1) |
| **Best for** | Ordered data | Fixed data | Unique items | Key-value pairs |

---

## Golden Rules

1. **Need order?** → List or Tuple
2. **Need immutability?** → Tuple
3. **Need uniqueness + fast lookup?** → Set
4. **Need key-value mapping?** → Dict
5. **Need hashability?** → Tuple (of immutables) or frozenset
6. **Unpacking works with any iterable** — not just tuples
7. **Sets and dicts are O(1) for `in` checks** — use them for large collections