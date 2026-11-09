# String Basics

## Definition

A **String** is a sequence of characters enclosed in single quotes (`' '`), double quotes (`" "`), or triple quotes (`''' '''` or `""" """`).

---

## Why do we use it?

* To store text data.
* To display messages.
* To manipulate text.
* To process user input.

---

## Key Points

* Strings are immutable.
* Strings are ordered.
* Indexing starts from `0`.
* Supports positive and negative indexing.

---

## Syntax

```python
name = "Jack"
```

```python
city = 'London'
```

```python
text = """Python is easy."""
```

---

## Parameters

Strings do not require any parameters while creating them.

---

## Return Value

A string object.

---

## Internal Working

Python stores strings as immutable sequences of Unicode characters. Every character has an index.

---

## Rules

* Use matching quotes.
* Strings are immutable.
* Triple quotes are used for multi-line strings.
* Strings support indexing and slicing.

---

## Types (if applicable)

### 1. Single Quotes

```python
name = 'Jack'
print(name)
```

### 2. Double Quotes

```python
name = "Jack"
print(name)
```

### 3. Triple Quotes

```python
text = """Hello
World"""
print(text)
```

---

## Advantages

* Easy to store text.
* Supports many built-in methods.
* Unicode support.
* Easy indexing and slicing.

---

## Disadvantages

* Immutable.
* Large strings consume more memory.

---

## Time Complexity

**O(1)** (Creation)

---

## Space Complexity

**O(n)**

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

Creates and prints a string.

---

## Example 2 (Intermediate)

### Code

```python
text = "Python"

print(text[2])
```

### Output

```text
t
```

### Explanation

Accesses the character at index 2.

---

## Example 3 (Interview)

### Code

```python
text = "Python"

print(len(text))
```

### Output

```text
6
```

### Explanation

Returns the number of characters.

---

## Example 4 (Real-world)

### Code

```python
name = "Jack"
city = "London"

print(name + " lives in " + city)
```

### Output

```text
Jack lives in London
```

### Explanation

Combines multiple strings.

---

## Common Errors

| Error       | Reason                | Solution                  |
| ----------- | --------------------- | ------------------------- |
| SyntaxError | Missing closing quote | Close the string properly |
| IndexError  | Invalid index         | Use a valid index         |

---

## Common Mistakes

* Mixing single and double quotes incorrectly.
* Forgetting closing quotes.
* Trying to modify a character directly.
* Using invalid indexes.

---

## Difference Table

| String            | List                 |
| ----------------- | -------------------- |
| Immutable         | Mutable              |
| Stores characters | Stores any data type |
| Uses quotes       | Uses square brackets |

---

## Interview Questions

**Q1. What is a string?**

A sequence of characters.

**Q2. Are strings mutable?**

No.

**Q3. Which quotes can define a string?**

Single, double, and triple quotes.

---

## MCQs

**1. Which data type stores text?**

A. int

B. float

C. String ✅

D. bool

---

**2. Strings are**

A. Mutable

B. Immutable ✅

C. Numeric

D. Boolean

---

**3. Which quotes support multi-line strings?**

A. Single quotes

B. Double quotes

C. Triple quotes ✅

D. None

---

## Practice Questions

1. What is a string?
2. Create a string using single quotes.
3. Create a string using double quotes.
4. Create a multi-line string.
5. Explain why strings are immutable.

---

## Real-world Applications

* User names
* Passwords
* Email addresses
* Messages
* File names

---

## Notes

**Remember:** Strings are **immutable**.

**Shortcut:**

* `' '` → Single quotes
* `" "` → Double quotes
* `""" """` → Multi-line string

**Interview Tip:** Strings are immutable and support indexing.

**Exam Tip:** Learn indexing, slicing, and common string methods.

---

## Summary

* A string is a sequence of characters.
* Strings are immutable.
* Python supports single, double, and triple quotes.
* Strings support indexing, slicing, and many built-in methods.

---

## Keywords

String, Characters, Immutable, Unicode, Indexing, Slicing, Text

---

## Related Topics

* Variables
* Indexing
* Slicing
* Escape Characters
* String Formatting
