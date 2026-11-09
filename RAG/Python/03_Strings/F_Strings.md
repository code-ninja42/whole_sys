# F-String

## Definition

An **F-String (Formatted String Literal)** is a string prefixed with `f` or `F` that allows variables and expressions to be embedded directly inside curly braces `{}`.

Example:

```python
name = "Jack"
print(f"Hello {name}")
```

---

## Why do we use it?

* To insert variables into strings.
* To make code more readable.
* To format output easily.
* To evaluate expressions inside strings.

---

## Key Points

* Introduced in Python 3.6.
* Prefix the string with `f` or `F`.
* Variables are enclosed in `{}`.
* Supports expressions and formatting.

---

## Syntax

```python
f"Text {variable}"
```

---

## Parameters

| Parameter | Description                              |
| --------- | ---------------------------------------- |
| `f`       | Indicates an f-string                    |
| `{}`      | Placeholder for variables or expressions |

---

## Return Value

Returns a formatted string.

---

## Internal Working

Python evaluates the expressions inside `{}` and replaces them with their values before printing the string.

---

## Flow Diagram (if applicable)

```text
Variable
   │
   ▼
{}
   │
   ▼
F-String
   │
   ▼
Formatted Output
```

---

## Rules

* Must start with `f` or `F`.
* Variables must be inside `{}`.
* Expressions can also be written inside `{}`.
* Available only in Python 3.6+.

---

## Types (if applicable)

### 1. Variable Formatting

```python
name = "Jack"
print(f"Hello {name}")
```

### 2. Expression Formatting

```python
a = 10
b = 20

print(f"Sum = {a+b}")
```

---

## Advantages

* Easy to read.
* Faster than older formatting methods.
* Supports expressions.
* Cleaner syntax.

---

## Disadvantages

* Works only in Python 3.6+.
* Older Python versions do not support it.

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

The variable is inserted directly into the string.

---

## Example 2 (Intermediate)

### Code

```python
age = 20

print(f"Jack is {age} years old.")
```

### Output

```text
Jack is 20 years old.
```

### Explanation

Multiple values can be formatted easily.

---

## Example 3 (Interview)

### Code

```python
a = 15
b = 5

print(f"Sum = {a+b}")
```

### Output

```text
Sum = 20
```

### Explanation

Expressions inside `{}` are evaluated automatically.

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

F-strings are commonly used to display formatted reports and invoices.

---

## Common Errors

| Error       | Reason               | Solution                  |
| ----------- | -------------------- | ------------------------- |
| NameError   | Variable not defined | Define the variable first |
| SyntaxError | Missing `{}` or `f`  | Use correct syntax        |

---

## Common Mistakes

* Forgetting the `f` before the string.
* Forgetting curly braces `{}`.
* Using undefined variables.

---

## Difference Table

| F-String     | `%` Formatting | `.format()`   |
| ------------ | -------------- | ------------- |
| Fastest      | Older method   | Modern method |
| Easy to read | Less readable  | Readable      |
| Uses `{}`    | Uses `%`       | Uses `{}`     |

---

## Interview Questions

**Q1. What is an F-String?**

A formatted string literal used to insert variables and expressions.

**Q2. Which Python version introduced F-Strings?**

Python **3.6**.

**Q3. Can expressions be used inside `{}`?**

Yes.

---

## MCQs

**1. Which prefix is used for an F-String?**

A. `s`

B. `f` ✅

C. `r`

D. `t`

---

**2. Variables in an F-String are enclosed in**

A. `()`

B. `[]`

C. `{}` ✅

D. `<>`

---

**3. F-Strings were introduced in**

A. Python 2.7

B. Python 3.5

C. Python 3.6 ✅

D. Python 3.10

---

## Practice Questions

1. What is an F-String?
2. Write a program using F-Strings.
3. Print the sum of two numbers using an F-String.
4. Differentiate between F-Strings and `.format()`.
5. Explain the advantages of F-Strings.

---

## Real-world Applications

* Printing reports.
* Invoice generation.
* User messages.
* Logging.
* Displaying formatted output.

---

## Notes

**Remember:** Always prefix the string with `f`.

**Shortcut:** `f"{variable}"`

**Interview Tip:** F-Strings are the preferred way to format strings in modern Python.

**Exam Tip:** Know the difference between F-Strings, `%` formatting, and `.format()`.

---

## Summary

* F-Strings are formatted string literals.
* Introduced in Python 3.6.
* Use `f` before the string.
* Variables and expressions are placed inside `{}`.
* Faster and more readable than older formatting methods.

---

## Keywords

F-String, Formatted String Literal, `{}`, String Formatting, Python 3.6

---

## Related Topics

* Strings
* Escape Characters
* String Methods
* `format()` Method
* Variables
