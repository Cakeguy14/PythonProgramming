# Python Testing — Complete Reference

## 1. `assert` Statements

`assert` checks a condition and raises `AssertionError` if it's `False`.

```python
assert 2 + 2 == 4          # ✅ Passes silently
assert 2 + 2 == 5          # ❌ AssertionError
```

### With a custom message:
```python
assert square(3) == 9, "square(3) should be 9"
```

### ⚠️ `assert` has NO colon:
```python
assert square(3) == 9:   # ❌ SyntaxError
assert square(3) == 9    # ✅ Correct
```

---

## 2. Catching `AssertionError`

```python
def test_square():
    try:
        assert square(3) == 9
    except AssertionError:
        print("Test failed!")
    else:
        print("Test passed!")
```

---

## 3. Backwards Logic — Common Mistake

```python
# ❌ WRONG — passes when square is CORRECT
assert square(3) != 9   # Fails when square returns 9

# ✅ CORRECT — passes when square is CORRECT
assert square(3) == 9   # Fails when square returns something else
```

---

## 4. `pytest` — The Testing Framework

### Install:
```bash
pip install pytest
```

### Naming rules:
| What | Must start with |
| :--- | :--- |
| Test functions | `test_` |
| Test classes | `Test` |
| Test methods | `test_` |

### ✅ Correct:
```python
def test_square():
    assert square(3) == 9
```

### ❌ Wrong (pytest ignores it):
```python
def check_square():   # Doesn't start with test_
    assert square(3) == 9
```

### Run:
```bash
pytest                        # Run all tests in current folder
pytest test_file.py           # Run a specific file
pytest test_file.py::test_square   # Run one test
pytest -v                     # Verbose output
```

---

## 5. Test File Naming

pytest discovers files named:
- `test_*.py`
- `*_test.py`

### Example structure:
```
my_project/
├── calculator.py
├── test_calculator.py    ← pytest finds this
└── tests/
    ├── test_math.py
    └── test_strings.py
```

---

## 6. Full Test Example

```python
# calculator.py
def square(n):
    return n * n

def add(a, b):
    return a + b
```

```python
# test_calculator.py
from calculator import square, add

def test_square():
    assert square(3) == 9
    assert square(4) == 16
    assert square(0) == 0
    assert square(-2) == 4

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
```

### Run:
```bash
pytest test_calculator.py -v
```

**Output:**
```
test_calculator.py::test_square PASSED
test_calculator.py::test_add PASSED
```

---

## 7. pytest Features

### `pytest.raises()` — Test exceptions:
```python
import pytest

def test_negative_balance():
    with pytest.raises(ValueError):
        BankAccount("Alice", -100)
```

### Parametrized tests:
```python
import pytest

@pytest.mark.parametrize("input,expected", [
    (3, 9),
    (4, 16),
    (0, 0),
    (-2, 4),
])
def test_square(input, expected):
    assert square(input) == expected
```

### `pytest.approx()` — Float comparison:
```python
def test_float():
    assert 0.1 + 0.2 == pytest.approx(0.3)
```

---

## 8. Common pytest Output

```
collected 0 items          ← No tests found (naming issue)
collected 1 item           ← Found 1 test
1 passed                   ← Test succeeded
1 failed                   ← Test failed
1 error                    ← Error during collection
```

---

## 9. Common pytest Issues

| Issue | Cause | Fix |
| :--- | :--- | :--- |
| `collected 0 items` | Function doesn't start with `test_` | Rename to `test_*` |
| `NameError: name 'Senthur' is not defined` | Missing quotes | Use `"Senthur"` |
| `ModuleNotFoundError` | Wrong import path | Check file location |
| `ImportError: cannot import name 'x'` | Function not defined in module | Add it or fix import |

---

## 10. `unittest` — Built-in Framework

```python
import unittest

class TestCalculator(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square(3), 9)
        self.assertEqual(square(4), 16)

    def test_negative(self):
        with self.assertRaises(ValueError):
            raise ValueError("test")

if __name__ == "__main__":
    unittest.main()
```

### Common `unittest` methods:
| Method | Purpose |
| :--- | :--- |
| `assertEqual(a, b)` | `a == b` |
| `assertNotEqual(a, b)` | `a != b` |
| `assertTrue(x)` | `bool(x) is True` |
| `assertFalse(x)` | `bool(x) is False` |
| `assertRaises(Error)` | Error is raised |
| `assertIn(a, b)` | `a in b` |

---

## Golden Rules

1. **`assert` has no colon.**
2. **`assert x == y`** — test for correctness, not incorrectness.
3. **pytest functions must start with `test_`.**
4. **pytest files must be `test_*.py` or `*_test.py`.**
5. **Use `pytest.raises()`** to test exceptions.
6. **Use `pytest.mark.parametrize`** for multiple test cases.
7. **Run `pytest -v`** for detailed output.