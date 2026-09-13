# Python OOP — Complete Reference

## Classes, Objects, Methods, Properties, Inheritance

---

## 1. Quick Overview

| Concept | Purpose |
| :--- | :--- |
| **Class** | Blueprint for creating objects |
| **Object** | Instance created from a class |
| **`__init__`** | Initializer — sets up the object |
| **`self`** | Reference to the current instance |
| **Attribute** | Data stored on an object |
| **Method** | Function defined inside a class |
| **`@property`** | Getter — access like an attribute |
| **`@x.setter`** | Setter — validate on assignment |
| **`@classmethod`** | Method that receives the class (`cls`) |
| **`@staticmethod`** | Method that receives nothing |
| **Inheritance** | Child class inherits from parent |
| **`super()`** | Call parent class methods |
| **Dunder methods** | Special methods like `__str__`, `__add__` |

---

## 2. Defining a Class

```python
class Student:
    # Class variable (shared by all instances)
    school = "Hogwarts"

    def __init__(self, name, house):
        # Instance variables (unique per object)
        self.name = name
        self.house = house

    def introduce(self):        # Instance method
        return f"I'm {self.name} from {self.house}"
```

---

## 3. Creating Objects

```python
harry = Student("Harry", "Gryffindor")
ron = Student("Ron", "Gryffindor")

print(harry.name)        # "Harry"
print(ron.name)          # "Ron"
print(harry.school)      # "Hogwarts" (falls back to class)
```

### Memory:
```
CLASS: Student
┌─────────────────────────┐
│  school = "Hogwarts"    │ ← Shared
│  introduce(self)        │ ← Method
└─────────────────────────┘
         ▲          ▲
    ┌────┴────┐ ┌───┴─────┐
    │ harry   │ │ ron     │
    │ name=   │ │ name=   │ ← Unique per object
    │ "Harry" │ │ "Ron"   │
    └─────────┘ └─────────┘
```

---

## 4. `__init__` — The Initializer

```python
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
```

| Rule | Explanation |
| :--- | :--- |
| **Called automatically** | When you create an object |
| **Must return `None`** | Never `return` a value |
| **First param is `self`** | Reference to the new object |
| **Used for validation** | Check data before storing |

### ❌ Wrong:
```python
def __init__(self, name):
    return f"Hello {name}"   # ❌ TypeError!
```

### ✅ Correct:
```python
def __init__(self, name):
    self.name = name          # ✅ Just set attributes
```

---

## 5. `self` — The Instance Reference

```python
def introduce(self):
    return f"I'm {self.name}"
```

- `self` is the **specific object** the method is called on.
- `harry.introduce()` → Python calls `introduce(harry)` → `self = harry`.
- `ron.introduce()` → Python calls `introduce(ron)` → `self = ron`.

---

## 6. Instance vs Class Variables

| | Instance Variable | Class Variable |
| :--- | :--- | :--- |
| **Defined** | Inside `__init__` with `self.` | Inside class, outside methods |
| **Scope** | Unique per object | Shared by all objects |
| **Example** | `self.name` | `school = "Hogwarts"` |
| **Changed via** | `obj.attr = x` (affects one) | `Class.attr = x` (affects all) |

```python
class Student:
    school = "Hogwarts"          # Class variable

    def __init__(self, name):
        self.name = name         # Instance variable

harry = Student("Harry")
ron = Student("Ron")

harry.name = "Harry Potter"      # Affects only harry
Student.school = "Durmstrang"    # Affects all students
```

---

## 7. Method Types

| Type | First arg | Decorator | Can access |
| :--- | :--- | :--- | :--- |
| **Instance method** | `self` | None | Instance + class data |
| **Class method** | `cls` | `@classmethod` | Class data only |
| **Static method** | None | `@staticmethod` | Nothing (utility) |

```python
class Student:
    school = "Hogwarts"

    def introduce(self):              # Instance method
        return f"I'm {self.name}"

    @classmethod
    def get_school(cls):              # Class method
        return cls.school

    @staticmethod
    def is_valid_name(name):          # Static method
        return len(name) > 0
```

### When to use each:
- **Instance method:** Needs `self` (specific object data).
- **Class method:** Needs `cls` (class-wide data or alternative constructor).
- **Static method:** Needs neither (just a helper function).

---

## 8. `@property` — Controlled Access

Turns a method into an attribute-like accessor.

```python
class Student:
    VALID_HOUSES = {"gryffindor", "slytherin", "hufflepuff", "ravenclaw"}

    def __init__(self, name, house):
        self.name = name
        self.house = house       # Triggers setter

    @property
    def house(self):             # Getter
        return self._house

    @house.setter
    def house(self, house):      # Setter (with validation)
        if house.lower() not in Student.VALID_HOUSES:
            raise ValueError("Invalid house")
        self._house = house
```

| Part | Purpose |
| :--- | :--- |
| `@property` | Defines the getter — runs on `obj.house` |
| `@house.setter` | Defines the setter — runs on `obj.house = x` |
| `self._house` | The raw stored value (underscore = private) |
| `self.house` | The property (uses getter/setter) |

### Why the underscore?
```python
@house.setter
def house(self, house):
    self.house = house    # ❌ Infinite recursion!
    self._house = house   # ✅ Stores directly
```

---

## 9. Read-Only Properties

Define only `@property` (no setter):

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    def area(self):           # Read-only!
        return 3.14159 * self._radius ** 2

c = Circle(5)
print(c.area)     # 78.53975
c.area = 100      # ❌ AttributeError: can't set attribute
```

---

## 10. Inheritance

```python
class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("missing name")
        self.name = name

    def __str__(self):
        return self.name


class Student(Wizard):
    def __init__(self, name, patronus):
        super().__init__(name)         # Call parent's __init__
        self.patronus = patronus

    def __str__(self):
        return f"{super().__str__()} has a {self.patronus}"


class Professor(Wizard):
    def __init__(self, name, patronus):
        super().__init__(name)
        self.patronus = patronus

    def __str__(self):
        return f"{super().__str__()} has a {self.patronus}"
```

### `super()` — Call the Parent

```python
super().__init__(name)         # Calls Wizard.__init__
super().__str__()              # Calls Wizard.__str__
```

**Why use `super()`?** So you don't have to rewrite the parent's validation logic.

---

## 11. Dunder (Magic) Methods

| Method | Triggered by | Purpose |
| :--- | :--- | :--- |
| `__init__(self, ...)` | `ClassName(...)` | Initialize object |
| `__str__(self)` | `print(obj)`, `str(obj)`, `f"{obj}"` | Human-readable string |
| `__repr__(self)` | `repr(obj)` | Developer-readable string |
| `__add__(self, other)` | `obj1 + obj2` | Addition |
| `__sub__(self, other)` | `obj1 - obj2` | Subtraction |
| `__eq__(self, other)` | `obj1 == obj2` | Equality |
| `__lt__(self, other)` | `obj1 < obj2` | Less than |
| `__len__(self)` | `len(obj)` | Length |
| `__getitem__(self, key)` | `obj[key]` | Indexing |

---

## 12. `__str__` — String Representation

```python
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"
```

| Rule | Explanation |
| :--- | :--- |
| **Must return a string** | Never a tuple, list, or set |
| **Called automatically** | By `print()`, `str()`, f-strings |
| **Without it** | Prints `<__main__.Student object at 0x...>` |

### ❌ Common mistakes:
```python
def __str__(self):
    return print(self.name)              # ❌ print returns None!
    return {self.name}, {self.house}     # ❌ Returns a tuple!
    return self.name and self.house      # ❌ Returns self.house only!
```

### ✅ Correct:
```python
def __str__(self):
    return f"{self.name} from {self.house}"
```

---

## 13. `__add__` — Operator Overloading

```python
class Coins:
    def __init__(self, thousands, hundreds, tens):
        self.thousands = thousands
        self.hundreds = hundreds
        self.tens = tens

    def __str__(self):
        return f"{self.thousands}, {self.hundreds}, {self.tens}"

    def __add__(self, other):
        return Coins(
            self.thousands + other.thousands,
            self.hundreds + other.hundreds,
            self.tens + other.tens
        )

potter = Coins(100, 50, 25)
ron = Coins(50, 25, 25)
total = potter + ron       # Calls potter.__add__(ron)
print(total)               # "150, 75, 50"
```

- `self` = left side (`potter`)
- `other` = right side (`ron`)
- Returns a **new object** (doesn't modify originals)

---

## 14. Validation in `__init__`

```python
class Student:
    VALID_HOUSES = {"gryffindor", "slytherin", "hufflepuff", "ravenclaw"}

    def __init__(self, name, house):
        if not name:
            raise ValueError("Name cannot be empty")
        if house.lower() not in Student.VALID_HOUSES:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
```

---

## 15. Alternative Constructors with `@classmethod`

```python
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, date_str):
        year, month, day = map(int, date_str.split("-"))
        return cls(year, month, day)     # 'cls' respects inheritance!

    @classmethod
    def today(cls):
        import datetime
        d = datetime.date.today()
        return cls(d.year, d.month, d.day)

# Three ways to create:
d1 = Date(2026, 9, 13)
d2 = Date.from_string("2026-09-13")
d3 = Date.today()
```

**Why `cls` instead of `Date`?** So subclasses work:
```python
class SpecialDate(Date):
    pass

sd = SpecialDate.from_string("2026-09-13")
print(type(sd))   # <class 'SpecialDate'>  ← Correct!
```

---

## 16. Class vs Static vs Instance — Decision Tree

```
Does the method need instance data (self.name)?
│
├── YES → INSTANCE METHOD
│         def introduce(self):
│             return self.name
│
└── NO → Does it need class data (cls.school)?
         │
         ├── YES → CLASS METHOD
         │         @classmethod
         │         def get_school(cls):
         │             return cls.school
         │
         └── NO → STATIC METHOD
                  @staticmethod
                  def is_valid_name(name):
                      return len(name) > 0
```

---

## 17. Common Errors & Fixes

| Error | Cause | Fix |
| :--- | :--- | :--- |
| `TypeError: __init__() should return None` | `return` in `__init__` | Remove the `return` |
| `TypeError: __str__ returned non-string` | Returned tuple/set/dict | Return an f-string |
| `NameError: name 'greet' is not defined` | Function called before defined | Define before calling |
| `TypeError: missing 1 required argument` | Wrong number of args | Match `__init__` signature |
| `AttributeError: can't set attribute` | No setter defined | Add `@x.setter` |
| `RecursionError` | `self.x = x` inside setter | Use `self._x = x` |
| `NameError` in `@classmethod` | Used `self` instead of `cls` | Use `cls` |

---

## 18. Summary Table

| Concept | Syntax | Purpose |
| :--- | :--- | :--- |
| **Class** | `class Name:` | Blueprint |
| **Object** | `obj = Name(...)` | Instance |
| **`__init__`** | `def __init__(self, ...)` | Initialize |
| **Instance method** | `def m(self):` | Work on object |
| **Class method** | `@classmethod` + `cls` | Work on class |
| **Static method** | `@staticmethod` | Utility |
| **Property** | `@property` | Getter |
| **Setter** | `@x.setter` | Validated assignment |
| **Inheritance** | `class Child(Parent):` | Reuse parent |
| **`super()`** | `super().__init__(...)` | Call parent |
| **`__str__`** | `def __str__(self):` | String representation |
| **`__add__`** | `def __add__(self, other):` | Operator overloading |

---

## 19. Golden Rules

1. **`__init__` must never return anything** — it only sets attributes.
2. **`__str__` must return a string** — never a tuple, list, or set.
3. **Use `self._x` inside setters** — never `self.x` (infinite recursion).
4. **Use `Student.VALID_HOUSES`** — qualify class variables explicitly.
5. **Use `super().__init__()`** — don't rewrite parent validation.
6. **`@classmethod` uses `cls`, not `self`** — it receives the class.
7. **`@staticmethod` receives nothing** — pure utility function.
8. **`self` = left side, `other` = right side** in `__add__`, `__sub__`, etc.
9. **Class variables are shared** — instance variables are unique.
10. **Use f-strings for `__str__`** — never commas or `and`.