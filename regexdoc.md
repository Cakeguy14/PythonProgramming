# Python Regular Expressions — Complete Reference

## 1. Import

```python
import re
```

---

## 2. Raw Strings

Always use `r"..."` for regex patterns. The `r` means "raw string" — backslashes are literal.

```python
r"\d"    # ✅ Correct — backslash + d
"\d"     # ⚠️ May be interpreted as escape sequence
```

---

## 3. Core Functions

### `re.search()` — Find first match anywhere
```python
match = re.search(r"\d+", "abc123def")
print(match.group())   # "123"
```

### `re.match()` — Match only at start
```python
re.match(r"abc", "abcdef")   # ✅ Match
re.match(r"def", "abcdef")   # ❌ None
```

### `re.fullmatch()` — Match entire string
```python
re.fullmatch(r"\d{4}", "2026")     # ✅ Match
re.fullmatch(r"\d{4}", "2026ab")   # ❌ None
```

### `re.findall()` — All matches as list
```python
re.findall(r"\d+", "a1b22c333")   # ['1', '22', '333']
```

### `re.finditer()` — All matches as objects
```python
for m in re.finditer(r"\w+at", "cat bat rat"):
    print(m.group(), m.start())
```

### `re.sub()` — Replace matches
```python
re.sub(r"\d", "#", "abc123")   # "abc###"
```

### `re.subn()` — Replace and count
```python
result, count = re.subn(r"\d", "#", "abc123")
# result="abc###", count=3
```

### `re.split()` — Split by pattern
```python
re.split(r"[,;]", "a,b;c")   # ['a', 'b', 'c']
```

### `re.compile()` — Pre-compile
```python
pattern = re.compile(r"\d+")
pattern.findall("a1b22")   # ['1', '22']
```

### `re.escape()` — Escape special chars
```python
re.escape("1 + 1 = 2?")   # '1\\ \\+\\ 1\\ =\\ 2\\?'
```

---

## 4. Match Object Methods

```python
m = re.search(r"(\w+)@(\w+)\.(\w+)", "senthur@gmail.com")

m.group()      # "senthur@gmail.com" (whole match)
m.group(0)     # Same as group()
m.group(1)     # "senthur"
m.group(2)     # "gmail"
m.groups()     # ('senthur', 'gmail', 'com')
m.start()      # 0
m.end()        # 17
m.span()       # (0, 17)
```

---

## 5. Common Metacharacters

| Pattern | Meaning | Example |
| :--- | :--- | :--- |
| `.` | Any character (except newline) | `a.c` matches `abc` |
| `\d` | Digit `[0-9]` | `\d+` matches `123` |
| `\w` | Word char `[a-zA-Z0-9_]` | `\w+` matches `hello_1` |
| `\s` | Whitespace | `\s+` matches spaces/tabs |
| `\D` | Non-digit | `\D+` matches `abc` |
| `\W` | Non-word char | `\W+` matches `!@#` |
| `\S` | Non-whitespace | `\S+` matches `hello` |
| `^` | Start of string | `^Hello` |
| `$` | End of string | `World$` |
| `*` | Zero or more | `ab*` matches `a`, `ab`, `abb` |
| `+` | One or more | `ab+` matches `ab`, `abb` |
| `?` | Zero or one | `ab?` matches `a`, `ab` |
| `{n}` | Exactly n | `\d{4}` matches `2026` |
| `{n,m}` | n to m | `\d{2,4}` matches `12`, `123` |
| `[...]` | Character class | `[abc]` matches a, b, or c |
| `[^...]` | Negated class | `[^@]` any char except @ |
| `(...)` | Capture group | `(\d+)` captures digits |
| `(?:...)` | Non-capture group | `(?:www)` groups without capturing |
| `\|` | OR | `cat\|dog` matches cat or dog |

---

## 6. Flags

| Flag | Meaning |
| :--- | :--- |
| `re.IGNORECASE` / `re.I` | Case-insensitive |
| `re.MULTILINE` / `re.M` | `^` and `$` match at line breaks |
| `re.DOTALL` / `re.S` | `.` matches newlines too |
| `re.VERBOSE` / `re.X` | Allow whitespace and comments in pattern |

```python
re.search(r"hello", "HELLO", re.I)   # ✅ Match
```

---

## 7. Email Regex Breakdown

```python
r"^[^@]+@[^@]+\.com$"
```

| Piece | Meaning |
| :--- | :--- |
| `^` | Start of string |
| `[^@]+` | One or more chars that are NOT `@` (username) |
| `@` | Literal @ |
| `[^@]+` | One or more chars that are NOT `@` (domain) |
| `\.` | Literal dot |
| `com` | Literal "com" |
| `$` | End of string |

| Input | Matches? |
| :--- | :--- |
| `"user@domain.com"` | ✅ |
| `"a@b.com"` | ✅ |
| `"@domain.com"` | ❌ (empty username) |
| `"user@.com"` | ❌ (empty domain) |
| `"user@domain.org"` | ❌ (must end in .com) |

---

## 8. URL Regex Breakdown

```python
r"^(?:https?://)?(?:www\.)?test\.com/(.+)"
```

| Piece | Meaning |
| :--- | :--- |
| `^` | Start of string |
| `(?:https?://)?` | Optional `http://` or `https://` |
| `(?:www\.)?` | Optional `www.` |
| `test\.com` | Literal `test.com` |
| `/` | Literal slash |
| `(.+)` | Capture the rest |

| Input | Captured |
| :--- | :--- |
| `"www.test.com/page"` | `"page"` |
| `"https://www.test.com/home"` | `"home"` |
| `"test.com/contact"` | `"contact"` |
| `"google.com/search"` | ❌ No match |

---

## 9. `/` in Regex

| Context | Meaning |
| :--- | :--- |
| **Python** | Literal slash |
| **JavaScript** | Delimiter (start/end of pattern) |
| **Escaped `\/`** | Literal slash (in JS) |

**In Python:** Never escape `/` — just use `/`.

---

## 10. `.*` vs `.+` vs `..*`

| Pattern | Meaning | Matches `"@"`? |
| :--- | :--- | :--- |
| `.*` | Zero or more | ✅ Yes |
| `..*` | One or more (old syntax) | ❌ No |
| `.+` | One or more (modern) | ❌ No |

**Use `.+`** instead of `..*` — it's cleaner.

---

## 11. Walrus Operator with Regex

```python
import re

url = input("Enter URL: ")

if (match := re.search(r"^www\.test\.com/(.+)", url, re.I)):
    print(match.group(1))
```

The walrus `:=` assigns `match` **and** checks it in one line.

---

## Golden Rules

1. **Always use `r"..."`** for regex patterns.
2. **Escape dots** — `.` → `\.` for literal dots.
3. **Use `search()`** for finding anywhere.
4. **Use `findall()`** for collecting all matches.
5. **Use `sub()`** for replacing.
6. **Use `split()`** for breaking apart.
7. **`^` and `$`** anchor to start/end.
8. **`[^@]`** means "any char except @".
9. **`+`** is one or more, `*` is zero or more.
10. **`/`** is literal in Python — no escaping needed.