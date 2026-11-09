# Operators

## Definition

**Operators** are special symbols used to perform operations on variables and values. They help perform calculations, comparisons, logical operations, and more.

Example:

```python
a = 10
b = 5

print(a + b)
```

---

## Why do we use it?

* To perform mathematical calculations.
* To compare values.
* To combine conditions.
* To manipulate data.
* To simplify programming.

---

## Key Points

* Operators work with operands.
* Python has different types of operators.
* Some operators return Boolean values.
* Operators follow precedence rules.

---

## Syntax

```python
operand operator operand
```

Example:

```python
a + b
```

---

## Parameters

**N/A**

---

## Return Value

Returns the result of the operation.

---

## Internal Working

Python evaluates the expression, applies the operator to the operands, and returns the result.

---

## Flow Diagram (if applicable)

```text
Operands
    │
    ▼
Operator
    │
    ▼
Result
```

---

## Rules

* Operators require operands.
* Follow operator precedence (PEMDAS).
* Use parentheses to control evaluation order.

---

## Types (if applicable)

### 1. Arithmetic Operators

| Operator | Description    | Example   |
| -------- | -------------- | --------- |
| +        | Addition       | 5+2 = 7   |
| -        | Subtraction    | 5-2 = 3   |
| *        | Multiplication | 5*2 = 10  |
| /        | Division       | 5/2 = 2.5 |
| //       | Floor Division | 5//2 = 2  |
| %        | Modulus        | 5%2 = 1   |
| **       | Exponent       | 5**2 = 25 |

### 2. Comparison Operators

`==`, `!=`, `>`, `<`, `>=`, `<=`

### 3. Assignment Operators

`=`, `+=`, `-=`, `*=`, `/=`, `%=`

### 4. Logical Operators

`and`, `or`, `not`

### 5. Bitwise Operators

`&`, `|`, `^`, `~`, `<<`, `>>`

### 6. Membership Operators

`in`, `not in`

### 7. Identity Operators

`is`, `is not`

---

## Advantages

* Makes calculations easy.
* Reduces code length.
* Improves readability.

---

## Disadvantages

* Wrong operator may produce incorrect output.
* Operator precedence can confuse beginners.

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
a = 10
b = 5

print(a + b)
```

### Output

```text
15
```

### Explanation

`+` adds two numbers.

---

## Example 2 (Intermediate)

### Code

```python
a = 10

a += 5

print(a)
```

### Output

```text
15
```

### Explanation

`+=` adds and assigns the value.

---

## Example 3 (Interview)

### Code

```python
print(10 > 5 and 5 > 2)
```

### Output

```text
True
```

### Explanation

Both conditions are `True`, so `and` returns `True`.

---

## Example 4 (Real-world)

### Code

```python
marks = 85

if marks >= 35:
    print("Jack Passed")
else:
    print("Jack Failed")
```

### Output

```text
Jack Passed
```

### Explanation

Comparison operator checks eligibility.

---

## Common Errors

| Error             | Reason                | Solution                  |
| ----------------- | --------------------- | ------------------------- |
| TypeError         | Invalid operand types | Use compatible data types |
| ZeroDivisionError | Divide by zero        | Check denominator         |

---

## Common Mistakes

* Using `=` instead of `==`.
* Confusing `is` with `==`.
* Ignoring operator precedence.

---

## Difference Table

| Operator | Purpose    |
| -------- | ---------- |
| `=`      | Assignment |
| `==`     | Comparison |
| `is`     | Identity   |
| `in`     | Membership |

---

## Interview Questions

**Q1. What is an operator?**

A symbol used to perform operations on operands.

**Q2. How many types of operators are there in Python?**

Seven major types:

* Arithmetic
* Comparison
* Assignment
* Logical
* Bitwise
* Membership
* Identity

**Q3. What is the difference between `=` and `==`?**

`=` assigns a value, while `==` compares two values.

---

## MCQs

**1. Which operator is used for exponentiation?**

A. `^`

B. `**` ✅

C. `*`

D. `%`

---

**2. Which operator checks equality?**

A. `=`

B. `==` ✅

C. `!=`

D. `is`

---

**3. Which operator checks membership?**

A. `in` ✅

B. `is`

C. `==`

D. `&`

---

## Practice Questions

1. What are operators?
2. List the types of operators.
3. Differentiate between `=` and `==`.
4. Explain logical operators.
5. Write a program using arithmetic operators.

---

## Real-world Applications

* Calculator programs.
* Student grading systems.
* Banking applications.
* Login validation.
* Data filtering.

---

## Notes

**Remember:** Operators perform operations on operands.

**Shortcut:**

* `=` → Assign
* `==` → Compare
* `is` → Identity
* `in` → Membership

**Interview Tip:** Know the difference between `=`, `==`, and `is`.

**Exam Tip:** Memorize all operator types.

---

## Summary

* Operators perform operations on values.
* Python has seven major operator types.
* `=` assigns, `==` compares, and `is` checks identity.
* Follow operator precedence.
* Operators are essential for calculations and decision-making.

---

## Keywords

Operators, Arithmetic, Comparison, Assignment, Logical, Bitwise, Membership, Identity, Operands

---

## Related Topics

* Variables
* Data Types
* Expressions
* Conditional Statements
* Loops
