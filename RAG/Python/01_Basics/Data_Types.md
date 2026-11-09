# Data Types

## Definition

A **data type** defines the type of value a variable can store. It tells Python how to store, process, and manipulate data.

Example:

* `10` → Integer
* `10.5` → Float
* `"Hello"` → String

---

## Why do we use it?

* To store different kinds of data.
* To perform valid operations.
* To improve code readability.
* To manage memory efficiently.

---

## Key Points

* Python is dynamically typed.
* No need to declare data types.
* Use `type()` to check a variable's type.
* Some data types are mutable, others are immutable.

---

## Syntax

```python
x = 10
print(type(x))
```

---

## Parameters

**N/A**

---

## Return Value

`type()` returns the data type of the object.

---

## Internal Working

When a value is assigned to a variable, Python automatically identifies its data type and stores it accordingly.

---

## Flow Diagram (if applicable)

```text
Assign Value
      │
      ▼
Python Detects Type
      │
      ▼
Stores in Memory
```

---

## Rules

* No data type declaration is required.
* One variable can store different data types.
* Use `type()` to check the type.

---

## Types (if applicable)

| Data Type | Example           |
| --------- | ----------------- |
| int       | `10`              |
| float     | `10.5`            |
| complex   | `2+3j`            |
| bool      | `True`            |
| str       | `"Python"`        |
| list      | `[1,2,3]`         |
| tuple     | `(1,2,3)`         |
| set       | `{1,2,3}`         |
| dict      | `{"name":"Rahi"}` |
| NoneType  | `None`            |

---

## Advantages

* Easy to use.
* Automatic type detection.
* Supports multiple data types.

---

## Disadvantages

* Dynamic typing may cause runtime errors.
* Slightly slower than statically typed languages.

---

## Time Complexity

**N/A**

---

## Space Complexity

Depends on the data type.

---

# Examples

## Example 1 (Basic)

### Code

```python
x = 100
print(type(x))
```

### Output

```text
<class 'int'>
```

### Explanation

`100` is an integer.

---

## Example 2 (Intermediate)

### Code

```python
x = 10
x = "Python"
print(type(x))
```

### Output

```text
<class 'str'>
```

### Explanation

Python allows changing the data type of a variable.

---

## Example 3 (Interview)

### Code

```python
print(type(True))
print(type(None))
```

### Output

```text
<class 'bool'>
<class 'NoneType'>
```

### Explanation

`True` is Boolean and `None` represents no value.

---

## Example 4 (Real-world)

### Code

```python
name = "Jack"
age = 20
cgpa = 8.9

print(type(name))
print(type(age))
print(type(cgpa))
```

### Output

```text
<class 'str'>
<class 'int'>
<class 'float'>
```

### Explanation

Different variables store different data types.

---

## Common Errors

| Error       | Reason               | Solution                  |
| ----------- | -------------------- | ------------------------- |
| `NameError` | Variable not defined | Define the variable first |
| `TypeError` | Invalid operation    | Use compatible data types |

---

## Common Mistakes

* Confusing `=` with `==`.
* Assuming all numbers are integers.
* Forgetting that strings use quotes.

---

## Difference Table

| Mutable    | Immutable |
| ---------- | --------- |
| List       | String    |
| Dictionary | Tuple     |
| Set        | Integer   |

---

## Interview Questions

### Q1. What is a data type?

A data type specifies the kind of value a variable stores.

### Q2. Is Python statically or dynamically typed?

Dynamically typed.

### Q3. Which function is used to check a data type?

`type()`

---

## MCQs

### 1. Which function checks a data type?

A. data()

B. type() ✅

C. typeof()

D. check()

---

### 2. Which is immutable?

A. List

B. Set

C. String ✅

D. Dictionary

---

### 3. Which data type stores key-value pairs?

A. List

B. Tuple

C. Dictionary ✅

D. Set

---

## Practice Questions

1. What is a data type?
2. List Python's built-in data types.
3. What is dynamic typing?
4. Differentiate mutable and immutable data types.
5. Write a program using `type()`.

---

## Real-world Applications

* Student records
* Banking systems
* E-commerce applications
* Data analysis

---

## Notes

### Remember

Python automatically detects the data type.

### Shortcut

`type()` → Checks data type.

### Interview Tip

Know the difference between mutable and immutable types.

### Exam Tip

Remember all built-in data types.

---

## Summary

* Data types define the kind of data.
* Python is dynamically typed.
* `type()` checks the data type.
* Python has mutable and immutable data types.
* No explicit type declaration is needed.

---

## Keywords

Data Type, Dynamic Typing, Mutable, Immutable, `type()`, Integer, String, List, Dictionary

---

## Related Topics

* Variables
* Type Casting
* Operators
* Strings
* Lists
