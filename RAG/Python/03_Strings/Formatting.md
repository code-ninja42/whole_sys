# String Formatting

## Definition

**String Formatting** is the process of inserting values into a string to create a readable and formatted output.

---

## Why do we use it?

* To display variables in a string.
* To create readable output.
* To print dynamic messages.
* To format reports and invoices.

---

## Key Points

* Python provides multiple ways to format strings.
* Most preferred method is **F-String**.
* Older methods are `%` formatting and `.format()`.
* Supports variables and expressions.

---

## Syntax

### F-String

```python
f"Hello {name}"
```

### format()

```python
"Hello {}".format(name)
```

### % Formatting

```python
"Hello %s" % name
```

---

## Parameters

| Method      | Description                       |
| ----------- | --------------------------------- |
| `f""`       | Formatted string literal          |
| `.format()` | Inserts values using placeholders |
| `%`         | Old-style string formatting       |

---

## Return Value

Returns a formatted string.

---

## Internal Working

Python replaces placeholders with the given values and returns the formatted string.

---

## Rules

* F-Strings require `f` before the string.
* `.format()` uses `{}` placeholders.
* `%` formatting uses `%s`, `%d`, `%f`, etc.

---

## Types (if applicable)

### 1. F-String

```python
name = "Jack"
print(f"Hello {name}")
```

### 2. format()

```python
name = "Jack"
print("Hello {}".format(name))
```

### 3. % Formatting

```python
name = "Jack"
print("Hello %s" % name)
```

---

## Advantages

* Easy to read.
* Produces clean output.
* Supports variables and expressions.

---

## Disadvantages

* `%` formatting is outdated.
* `.format()` is longer than F-Strings.

---

## Time Complexity

**O(n)**

---

## Space Complexity

**O(n)**

---

# Examples

## Example 1 (Basic)

### Code

```python
name = "Jack"

print(f"Hello {name}")
```

### Output

```text
Hello Jack
```

### Explanation

Uses an F-String.

---

## Example 2 (Intermediate)

### Code

```python
name = "Jack"

print("Hello {}".format(name))
```

### Output

```text
Hello Jack
```

### Explanation

Uses the `format()` method.

---

## Example 3 (Interview)

### Code

```python
name = "Jack"

print("Hello %s" % name)
```

### Output

```text
Hello Jack
```

### Explanation

Uses old-style `%` formatting.

---

## Example 4 (Real-world)

### Code

```python
product = "Laptop"
price = 50000

print(f"Product: {product}, Price: ₹{price}")
```

### Output

```text
Product: Laptop, Price: ₹50000
```

### Explanation

Displays formatted product details.

---

## Common Errors

| Error       | Reason               | Solution                  |
| ----------- | -------------------- | ------------------------- |
| NameError   | Variable not defined | Define the variable first |
| SyntaxError | Missing `f` or `{}`  | Use correct syntax        |

---

## Common Mistakes

* Forgetting the `f` in an F-String.
* Incorrect placeholders.
* Using undefined variables.

---

## Difference Table

| F-String     | `.format()`  | `%` Formatting |
| ------------ | ------------ | -------------- |
| Fastest      | Medium       | Old method     |
| Easy to read | Readable     | Less readable  |
| Python 3.6+  | All versions | Older style    |

---

## Interview Questions

**Q1. What is string formatting?**

The process of inserting values into a string.

**Q2. Which is the preferred formatting method?**

F-String.

**Q3. Name three formatting methods.**

F-String, `.format()`, `%` formatting.

---

## MCQs

**1. Which is the recommended string formatting method?**

A. `%`

B. `.format()`

C. F-String ✅

D. `concat()`

---

**2. Which method uses `{}` placeholders?**

A. `%`

B. `.format()` ✅

C. `len()`

D. `split()`

---

**3. Which method is the oldest?**

A. F-String

B. `.format()`

C. `%` Formatting ✅

D. None

---

## Practice Questions

1. What is string formatting?
2. Write a program using an F-String.
3. Write a program using `.format()`.
4. Write a program using `%` formatting.
5. Differentiate between the three methods.

---

## Real-world Applications

* Reports
* Bills and invoices
* User messages
* Logging
* Data display

---

## Notes

**Remember:** **F-Strings are the modern and recommended way** to format strings.

**Shortcut:**

* `f""` → Best
* `.format()` → Good
* `%` → Old

**Interview Tip:** Prefer F-Strings unless asked about older methods.

**Exam Tip:** Know all three formatting methods.

---

## Summary

* String formatting inserts values into strings.
* Python supports **F-Strings**, **`.format()`**, and **`%` formatting**.
* F-Strings are the fastest and easiest to read.
* Used to create dynamic and readable output.

---

## Keywords

String Formatting, F-String, `format()`, `% Formatting`, Placeholder

---

## Related Topics

* Strings
* F-String
* Variables
* Escape Characters
* Print Function
