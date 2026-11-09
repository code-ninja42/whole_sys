# Variables

## Definition

A **variable** is a named memory location used to store data. The value of a variable can change during program execution.

Example:

```python
name = "Jack"
age = 20
```

---

## Why do we use it?

* To store data.
* To reuse values.
* To make programs dynamic.
* To simplify calculations.
* To improve code readability.

---

## Key Points

* Variables store values.
* No need to declare a data type.
* Variable names are called identifiers.
* Variables are case-sensitive.
* A variable can hold different data types.

---

## Syntax

```python
variable_name = value
```

Example:

```python
age = 20
```

---

## Parameters

**N/A**

---

## Return Value

**N/A**

---

## Internal Working

When a value is assigned, Python creates an object in memory and binds the variable name to that object.

---

## Flow Diagram (if applicable)

```text
Create Variable
       │
       ▼
Assign Value
       │
       ▼
Store in Memory
       │
       ▼
Use Variable
```

---

## Rules

* Must start with a letter or `_`.
* Cannot start with a digit.
* Cannot contain spaces.
* Cannot use Python keywords.
* Use meaningful names.

---

## Types (if applicable)

### 1. Integer Variable

```python
age = 20
```

### 2. Float Variable

```python
salary = 45000.50
```

### 3. String Variable

```python
name = "Jack"
```

### 4. Boolean Variable

```python
is_student = True
```

---

## Advantages

* Stores data efficiently.
* Makes code reusable.
* Easy to update values.
* Improves readability.

---

## Disadvantages

* Poor variable names reduce readability.
* Using undefined variables causes errors.

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
name = "Jack"

print(name)
```

### Output

```text
Jack
```

### Explanation

The variable `name` stores the string `"Jack"`.

---

## Example 2 (Intermediate)

### Code

```python
a = 10

a = 25

print(a)
```

### Output

```text
25
```

### Explanation

Variables can be updated by assigning a new value.

---

## Example 3 (Interview)

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

Python is dynamically typed, so a variable can store different data types.

---

## Example 4 (Real-world)

### Code

```python
product = "Laptop"
price = 50000

print(product)
print(price)
```

### Output

```text
Laptop
50000
```

### Explanation

Variables are used to store product details in real-world applications.

---

## Common Errors

| Error       | Reason                | Solution                  |
| ----------- | --------------------- | ------------------------- |
| NameError   | Variable not defined  | Define the variable first |
| SyntaxError | Invalid variable name | Follow naming rules       |

---

## Common Mistakes

* Using spaces in variable names.
* Starting variable names with digits.
* Using keywords as variable names.
* Using unclear names like `x`, `a`, `b`.

---

## Difference Table

| Variable                 | Constant                     |
| ------------------------ | ---------------------------- |
| Value can change         | Value should not change      |
| Created using assignment | Usually written in uppercase |
| Example: `age = 20`      | Example: `PI = 3.14`         |

---

## Interview Questions

**Q1. What is a variable?**

A named memory location used to store data.

**Q2. Does Python require variable declaration?**

No.

**Q3. Can a variable store different data types?**

Yes.

---

## MCQs

**1. Which symbol is used to assign a value?**

A. `==`

B. `=` ✅

C. `!=`

D. `+`

---

**2. Which is a valid variable name?**

A. `2age`

B. `my-age`

C. `student_name` ✅

D. `class`

---

**3. Python variables are**

A. Statically typed

B. Dynamically typed ✅

C. Compile-time typed

D. None of these

---

## Practice Questions

1. What is a variable?
2. Write the rules for naming variables.
3. Differentiate between variables and constants.
4. Explain dynamic typing.
5. Write a program using different variable types.

---

## Real-world Applications

* Student Management System
* Banking Applications
* E-commerce Websites
* Employee Records
* Inventory Management

---

## Notes

**Remember:** Variables store values.

**Shortcut:** `variable = value`

**Interview Tip:** Python variables are dynamically typed.

**Exam Tip:** Remember all variable naming rules.

---

## Summary

* Variables store data in memory.
* Python does not require data type declaration.
* Variables can change during execution.
* Follow proper naming rules.
* Use meaningful variable names.

---

## Keywords

Variable, Assignment, Identifier, Dynamic Typing, Memory, Value

---

## Related Topics

* Identifiers
* Keywords
* Data Types
* Type Casting
* Operators
