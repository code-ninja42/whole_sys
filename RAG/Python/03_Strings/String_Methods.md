# String Methods

## Definition

**String Methods** are built-in functions that perform operations on strings such as changing case, searching, replacing, splitting, and joining text.

---

## Why do we use it?

* To modify text.
* To search within strings.
* To replace characters or words.
* To split and combine text.
* To validate string content.

---

## Key Points

* String methods are built into Python.
* Strings are immutable.
* Most methods return a new string.
* Methods are called using the dot (`.`) operator.

---

## Syntax

```python
string.method()
```

---

## Parameters

| Method         | Description                                     |
| -------------- | ----------------------------------------------- |
| `upper()`      | Converts to uppercase                           |
| `lower()`      | Converts to lowercase                           |
| `title()`      | Converts first letter of each word to uppercase |
| `capitalize()` | Capitalizes first letter                        |
| `strip()`      | Removes leading and trailing spaces             |
| `replace()`    | Replaces text                                   |
| `find()`       | Finds first occurrence                          |
| `count()`      | Counts occurrences                              |
| `split()`      | Splits a string into a list                     |
| `join()`       | Joins elements into a string                    |
| `startswith()` | Checks starting text                            |
| `endswith()`   | Checks ending text                              |

---

## Return Value

Returns a new string, list, integer, or boolean depending on the method.

---

## Internal Working

Python processes the original string and returns a new result without modifying the original string.

---

## Rules

* Strings remain unchanged.
* Methods are case-sensitive.
* Parentheses `()` are required.
* Some methods accept parameters.

---

## Types (if applicable)

### 1. Case Methods

```python
text = "python"

print(text.upper())
print(text.lower())
print(text.title())
```

### 2. Search Methods

```python
text = "Python Programming"

print(text.find("Python"))
print(text.count("m"))
```

### 3. Replace Method

```python
text = "Hello World"

print(text.replace("World", "Jack"))
```

### 4. Split and Join

```python
text = "Python Java C++"

print(text.split())
```

```python
words = ["Python", "Java"]

print("-".join(words))
```

---

## Advantages

* Easy to use.
* Saves coding time.
* Improves readability.
* Powerful text manipulation.

---

## Disadvantages

* Strings cannot be modified directly.
* Some methods are case-sensitive.

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
text = "python"

print(text.upper())
```

### Output

```text
PYTHON
```

### Explanation

Converts all characters to uppercase.

---

## Example 2 (Intermediate)

### Code

```python
text = "Python Programming"

print(text.replace("Python", "Java"))
```

### Output

```text
Java Programming
```

### Explanation

Replaces one word with another.

---

## Example 3 (Interview)

### Code

```python
text = "apple apple mango"

print(text.count("apple"))
```

### Output

```text
2
```

### Explanation

Counts the number of occurrences.

---

## Example 4 (Real-world)

### Code

```python
email = "   jack@gmail.com   "

print(email.strip())
```

### Output

```text
jack@gmail.com
```

### Explanation

Removes extra spaces from user input.

---

## Common Errors

| Error          | Reason               | Solution                  |
| -------------- | -------------------- | ------------------------- |
| AttributeError | Method doesn't exist | Use a valid string method |
| TypeError      | Incorrect arguments  | Pass correct parameters   |

---

## Common Mistakes

* Forgetting parentheses.
* Expecting methods to modify the original string.
* Using incorrect capitalization in method names.
* Passing wrong arguments.

---

## Difference Table

| Method      | Purpose               |
| ----------- | --------------------- |
| `upper()`   | Uppercase             |
| `lower()`   | Lowercase             |
| `replace()` | Replace text          |
| `find()`    | Find substring        |
| `count()`   | Count occurrences     |
| `split()`   | Split into list       |
| `join()`    | Join list into string |

---

## Interview Questions

**Q1. Are string methods able to modify the original string?**

No. They return a new string.

**Q2. Which method converts text to uppercase?**

`upper()`

**Q3. Which method removes extra spaces?**

`strip()`

---

## MCQs

**1. Which method converts a string to uppercase?**

A. `lower()`

B. `upper()` ✅

C. `title()`

D. `find()`

---

**2. Which method replaces text?**

A. `replace()` ✅

B. `count()`

C. `join()`

D. `find()`

---

**3. Which method splits a string into a list?**

A. `join()`

B. `split()` ✅

C. `replace()`

D. `strip()`

---

## Practice Questions

1. What are string methods?
2. Write a program using `upper()`.
3. Replace one word with another.
4. Count occurrences of a word.
5. Split a sentence into words.

---

## Real-world Applications

* Data cleaning
* Form validation
* Text processing
* Search functionality
* File name manipulation

---

## Notes

**Remember:** String methods return a **new string** because strings are immutable.

**Shortcut:**

* `upper()` → Uppercase
* `lower()` → Lowercase
* `replace()` → Replace
* `find()` → Search
* `count()` → Count
* `split()` → Split
* `join()` → Join
* `strip()` → Remove spaces

**Interview Tip:** Know that strings are immutable.

**Exam Tip:** Learn the most commonly used string methods.

---

## Summary

* String methods perform operations on text.
* They return new strings without changing the original.
* Common methods include `upper()`, `lower()`, `replace()`, `find()`, `count()`, `split()`, `join()`, and `strip()`.
* They simplify text processing and manipulation.

---

## Keywords

String Methods, upper(), lower(), replace(), find(), count(), split(), join(), strip(), title(), capitalize()

---

## Related Topics

* String Basics
* Slicing
* String Formatting
* Escape Characters
* Variables
