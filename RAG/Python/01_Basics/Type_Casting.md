# Type Casting

## Definition

**Type Casting** is the process of converting one data type into another. Python provides built-in functions to convert data types.

Example:

* Integer → Float
* String → Integer
* Float → Integer

---

## Why do we use it?

* To convert one data type into another.
* To perform compatible operations.
* To process user input.
* To avoid type-related errors.

---

## Key Points

* Python supports **Implicit** and **Explicit** type casting.
* Implicit casting is done automatically by Python.
* Explicit casting is done using built-in functions.
* Common functions: `int()`, `float()`, `str()`, `bool()`.

---

## Syntax

```python
new_variable = data_type(old_variable)
```

Example:

```python
age = int("20")
```

---

## Parameters

| Function  | Description         |
| --------- | ------------------- |
| `int()`   | Converts to integer |
| `float()` | Converts to float   |
| `str()`   | Converts to string  |
| `bool()`  | Converts to boolean |

---

## Return Value

Returns the converted value in the specified data type.

---

## Internal Working

Python checks the current data type, converts it to the requested type (if possible), and returns the converted value.

---

## Flow Diagram (if applicable)

```text
Original Value
      │
      ▼
Type Casting Function
      │
      ▼
Converted Value
```

---

## Rules

* Conversion must be valid.
* Invalid conversions raise a `ValueError`.
* Implicit casting happens automatically.
* Explicit casting requires conversion functions.

---

## Types (if applicable)

### 1. Implicit Type Casting

Python automatically converts a smaller data type to a larger one.

Example:

```python
a = 10
b = 2.5

print(a + b)
```

---

### 2. Explicit Type Casting

The programmer converts the data type manually.

Example:

```python
age = int("20")
```

---

## Advantages

* Improves compatibility.
* Helps process user input.
* Reduces type mismatch errors.

---

## Disadvantages

* Invalid conversions cause errors.
* Data may be lost (e.g., float to int).

---

## Time Complexity

**O(1)**

---

## Space Complexity

**O(1)**

---

# Examples

## Example 1 (Basic)

### Code

```python
num = "25"

print(int(num))
```

### Output

```text
25
```

### Explanation

The string `"25"` is converted into an integer.

---

## Example 2 (Intermediate)

### Code

```python
a = 10
b = 2.5

print(a + b)
```

### Output

```text
12.5
```

### Explanation

Python automatically converts `10` into `10.0`.

---

## Example 3 (Interview)

### Code

```python
num = 15

print(str(num))
```

### Output

```text
15
```

### Explanation

The integer is converted into a string.

---

## Example 4 (Real-world)

### Code

```python
age = input("Enter Age: ")

age = int(age)

print(age + 5)
```

### Output

```text
Enter Age: 20
25
```

### Explanation

`input()` returns a string, so it is converted to an integer before performing arithmetic.

---

## Common Errors

| Error      | Reason                | Solution                         |
| ---------- | --------------------- | -------------------------------- |
| ValueError | Invalid conversion    | Convert only compatible values   |
| TypeError  | Unsupported operation | Convert to the correct data type |

---

## Common Mistakes

* Forgetting that `input()` returns a string.
* Trying `int("Jack")`.
* Assuming all conversions are possible.

---

## Difference Table

| Implicit Casting   | Explicit Casting            |
| ------------------ | --------------------------- |
| Done by Python     | Done by programmer          |
| Automatic          | Manual                      |
| No function needed | Uses functions like `int()` |

---

## Interview Questions

**Q1. What is type casting?**

Converting one data type into another.

**Q2. How many types of type casting are there?**

Two: Implicit and Explicit.

**Q3. Name four type casting functions.**

`int()`, `float()`, `str()`, `bool()`

---

## MCQs

**1. Which function converts a string to an integer?**

A. `str()`

B. `int()` ✅

C. `float()`

D. `bool()`

---

**2. Which type casting is automatic?**

A. Explicit

B. Implicit ✅

C. Manual

D. User-defined

---

**3. What does `input()` return?**

A. Integer

B. Float

C. String ✅

D. Boolean

---

## Practice Questions

1. What is type casting?
2. Explain implicit and explicit type casting.
3. Write a program using `int()`.
4. Convert a float into an integer.
5. Why is type casting needed?

---

## Real-world Applications

* Taking user input.
* Reading data from files.
* Data processing.
* Mathematical calculations.

---

## Notes

**Remember:** `input()` always returns a string.

**Shortcut:**

* `int()` → Integer
* `float()` → Float
* `str()` → String
* `bool()` → Boolean

**Interview Tip:** Know the difference between implicit and explicit type casting.

**Exam Tip:** Remember common conversion functions.

---

## Summary

* Type casting converts one data type into another.
* Python supports implicit and explicit casting.
* Common functions are `int()`, `float()`, `str()`, and `bool()`.
* Invalid conversions raise `ValueError`.
* Type casting is useful for user input and calculations.

---

## Keywords

Type Casting, Implicit Casting, Explicit Casting, `int()`, `float()`, `str()`, `bool()`, Conversion

---

## Related Topics

* Data Types
* Variables
* Input and Output
* Operators
* Strings
