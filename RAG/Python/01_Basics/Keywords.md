# Keywords

## Definition

**Keywords** are reserved words in Python that have predefined meanings. They are used to define the syntax and structure of a Python program. Keywords cannot be used as identifiers (variable names, function names, or class names).

---

## Why do we use it?

* To define Python syntax.
* To perform specific operations.
* To control the program flow.
* To create functions, classes, and loops.

---

## Key Points

* Keywords are reserved words.
* They have predefined meanings.
* They are case-sensitive.
* They cannot be used as variable names.
* Python provides the `keyword` module to view all keywords.

---

## Syntax

```python
import keyword

print(keyword.kwlist)
```

---

## Parameters

**N/A**

---

## Return Value

`keyword.kwlist` returns a list of all Python keywords.

---

## Internal Working

When the Python interpreter reads the code, it recognizes keywords and performs their predefined actions instead of treating them as normal identifiers.

---

## Flow Diagram (if applicable)

```text
Write Code
     │
     ▼
Interpreter Reads Keyword
     │
     ▼
Performs Reserved Action
```

---

## Rules

* Keywords cannot be used as identifiers.
* Keywords are lowercase except `True`, `False`, and `None`.
* Their spelling cannot be changed.
* Keywords are case-sensitive.

---

## Types (if applicable)

Some common categories of keywords:

* Control Flow (`if`, `else`, `elif`)
* Loops (`for`, `while`, `break`, `continue`)
* Functions (`def`, `return`)
* Exception Handling (`try`, `except`, `finally`, `raise`)
* Logical (`and`, `or`, `not`)
* Boolean (`True`, `False`)
* Special (`None`, `pass`, `import`, `class`)

---

## Advantages

* Makes code readable.
* Provides a fixed syntax.
* Simplifies programming.

---

## Disadvantages

* Cannot be used as variable names.
* Must be remembered while coding.

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
if 10 > 5:
    print("True")
```

### Output

```text
True
```

### Explanation

`if` is a keyword used for decision making.

---

## Example 2 (Intermediate)

### Code

```python
import keyword

print(keyword.iskeyword("for"))
```

### Output

```text
True
```

### Explanation

`iskeyword()` checks whether a word is a Python keyword.

---

## Example 3 (Interview)

### Code

```python
if = 10
```

### Output

```text
SyntaxError: invalid syntax
```

### Explanation

`if` is a keyword, so it cannot be used as a variable name.

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

Keywords `if` and `else` control the program flow.

---

## Common Errors

| Error       | Reason                        | Solution                  |
| ----------- | ----------------------------- | ------------------------- |
| SyntaxError | Using a keyword as a variable | Use another name          |
| NameError   | Misspelled keyword            | Write the correct keyword |

---

## Common Mistakes

* Using keywords as variable names.
* Writing keywords with incorrect capitalization.
* Forgetting that `True`, `False`, and `None` start with capital letters.

---

## Difference Table

| Keyword                      | Identifier                |
| ---------------------------- | ------------------------- |
| Reserved word                | User-defined name         |
| Has predefined meaning       | Created by programmer     |
| Cannot be used as a variable | Can be used as a variable |

---

## Interview Questions

**Q1. What is a keyword?**

A reserved word with a predefined meaning.

**Q2. Can keywords be used as variable names?**

No.

**Q3. Which module is used to display Python keywords?**

`keyword`

---

## MCQs

**1. Which module displays Python keywords?**

A. keywords

B. keyword ✅

C. python

D. sys

---

**2. Which is a Python keyword?**

A. age

B. total

C. if ✅

D. marks

---

**3. Which function checks whether a word is a keyword?**

A. `check()`

B. `keyword.iskeyword()` ✅

C. `type()`

D. `find()`

---

## Practice Questions

1. Define a keyword.
2. List five Python keywords.
3. Why can't keywords be used as variable names?
4. Write a program using `keyword.kwlist`.
5. Differentiate between keywords and identifiers.

---

## Real-world Applications

* Decision making
* Loops
* Function creation
* Exception handling
* Class creation

---

## Notes

**Remember:** Keywords are reserved words.

**Shortcut:** `keyword.kwlist` → Displays all keywords.

**Interview Tip:** Be able to explain the difference between keywords and identifiers.

**Exam Tip:** Remember common keywords like `if`, `for`, `while`, `def`, `class`, `return`, `import`, `try`, `except`.

---

## Summary

* Keywords are reserved words in Python.
* They have predefined meanings.
* They cannot be used as identifiers.
* Use `keyword.kwlist` to display all keywords.
* Use `keyword.iskeyword()` to check whether a word is a keyword.

---

## Keywords

Keyword, Reserved Word, Identifier, `keyword` Module, `keyword.kwlist`, `keyword.iskeyword()`

---

## Related Topics

* Identifiers
* Variables
* Operators
* Comments
* Data Types
