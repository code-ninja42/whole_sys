# Identifiers

## Definition

An **identifier** is the name given to a variable, function, class, module, or any other object in Python. It helps identify and access objects in a program.

---

## Why do we use it?

* To name variables and functions.
* To make code readable.
* To access stored data.

---

## Key Points

* Identifiers are case-sensitive.
* They can contain letters, digits, and underscores (`_`).
* They cannot start with a digit.
* They cannot contain spaces or special characters.
* Keywords cannot be used as identifiers.

---

## Syntax

```python
identifier_name = value
```

---

## Parameters

**N/A**

---

## Return Value

**N/A**

---

## Internal Working

When an identifier is created, Python stores it in memory and links it to the assigned value.

---

## Flow Diagram (if applicable)

```text
Create Identifier
        │
        ▼
Assign Value
        │
        ▼
Store in Memory
```

---

## Rules

* Must start with a letter or `_`.
* Cannot start with a number.
* Cannot use keywords.
* No spaces allowed.
* Only letters, digits, and `_` are allowed.

---

## Types (if applicable)

* Variable Identifier
* Function Identifier
* Class Identifier
* Module Identifier

---

## Advantages

* Improves readability.
* Makes code easier to maintain.
* Helps organize programs.

---

## Disadvantages

* Poor names reduce readability.
* Similar names may cause confusion.

---

## Time Complexity

**N/A**

---

## Space Complexity

**N/A**

---

# Examples

## Example 1 (Basic)

### Code

```python
age = 20
print(age)
```

### Output

```text
20
```

### Explanation

`age` is a valid identifier.

---

## Example 2 (Intermediate)

### Code

```python
jack_name = "Jack"
print(jack_name)
```

### Output

```text
Jack
```

### Explanation

Underscores are allowed in identifiers.

---

## Example 3 (Interview)

### Code

```python
2age = 20
```

### Output

```text
SyntaxError: invalid decimal literal
```

### Explanation

Identifiers cannot start with a digit.

---

## Example 4 (Real-world)

### Code

```python
student_name = "Jack"
student_marks = 90

print(student_name)
print(student_marks)
```

### Output

```text
Jack
90
```

### Explanation

Meaningful identifiers improve code readability.

---

## Common Errors

| Error       | Reason              | Solution                   |
| ----------- | ------------------- | -------------------------- |
| SyntaxError | Starts with a digit | Start with a letter or `_` |
| SyntaxError | Uses a keyword      | Choose another name        |

---

## Common Mistakes

* Starting with numbers.
* Using spaces.
* Using keywords.
* Using unclear names like `a`, `b`, `x1`.

---

## Difference Table

| Identifier                   | Keyword                  |
| ---------------------------- | ------------------------ |
| User-defined name            | Reserved word            |
| Can be created by programmer | Cannot be used as a name |
| Example: `age`               | Example: `if`            |

---

## Interview Questions

**Q1. What is an identifier?**

A name used to identify variables, functions, classes, etc.

**Q2. Can an identifier start with a number?**

No.

**Q3. Are identifiers case-sensitive?**

Yes.

---

## MCQs

**1. Which is a valid identifier?**

A. `2age`

B. `my-name`

C. `student_name` ✅

D. `class`

---

**2. Which character is allowed?**

A. `@`

B. `#`

C. `_` ✅

D. `%`

---

**3. Are Python identifiers case-sensitive?**

A. Yes ✅

B. No

---

## Practice Questions

1. What is an identifier?
2. Write five valid identifiers.
3. Write five invalid identifiers.
4. Can keywords be identifiers?
5. Explain the rules of identifiers.

---

## Real-world Applications

* Naming variables
* Naming functions
* Naming classes
* Naming modules

---

## Notes

**Remember:** Identifiers are user-defined names.

**Shortcut:** Letter/`_` first → Digits allowed later.

**Interview Tip:** Keywords are never valid identifiers.

**Exam Tip:** Remember all identifier naming rules.

---

## Summary

* Identifiers are names given to program elements.
* They are case-sensitive.
* They cannot start with digits.
* Keywords cannot be used as identifiers.
* Use meaningful names for better readability.

---

## Keywords

Identifier, Variable, Function, Class, Module, Naming Rules, Case-sensitive

---

## Related Topics

* Variables
* Keywords
* Data Types
* Operators
* Comments
