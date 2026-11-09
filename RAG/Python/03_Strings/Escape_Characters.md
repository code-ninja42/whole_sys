# Escape Characters

## Definition

**Escape characters** are special characters preceded by a backslash (`\`) that represent characters that cannot be typed directly or have special meanings in a string.

Example:

```python
print("Hello\nJack")
```

---

## Why do we use it?

* To print special characters.
* To format text.
* To insert quotes inside strings.
* To improve output readability.

---

## Key Points

* Escape characters start with a backslash (`\`).
* Used only inside strings.
* Help format output.
* Commonly used in file handling and printing.

---

## Syntax

```python
"Text\escape_character"
```

---

## Parameters

**N/A**

---

## Return Value

Returns a formatted string.

---

## Internal Working

When Python encounters a backslash (`\`), it interprets the next character as a special instruction instead of a normal character.

---

## Flow Diagram (if applicable)

```text
String
   │
   ▼
Escape Character (\)
   │
   ▼
Formatted Output
```

---

## Rules

* Escape characters begin with `\`.
* Must be inside a string.
* Invalid escape sequences may generate warnings.

---

## Types (if applicable)

| Escape Character | Description     |
| ---------------- | --------------- |
| `\n`             | New Line        |
| `\t`             | Tab Space       |
| `\\`             | Backslash       |
| `\'`             | Single Quote    |
| `\"`             | Double Quote    |
| `\b`             | Backspace       |
| `\r`             | Carriage Return |

---

## Advantages

* Formats output neatly.
* Allows quotes inside strings.
* Improves readability.

---

## Disadvantages

* Too many escape characters reduce readability.
* Easy to confuse similar escape sequences.

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
print("Hello\nJack")
```

### Output

```text
Hello
Jack
```

### Explanation

`\n` moves the cursor to the next line.

---

## Example 2 (Intermediate)

### Code

```python
print("Python\tProgramming")
```

### Output

```text
Python    Programming
```

### Explanation

`\t` inserts a tab space.

---

## Example 3 (Interview)

### Code

```python
print("He said, \"Python is Easy\"")
```

### Output

```text
He said, "Python is Easy"
```

### Explanation

`\"` prints double quotes inside a string.

---

## Example 4 (Real-world)

### Code

```python
print("Name:\tJack\nAge:\t20")
```

### Output

```text
Name:   Jack
Age:    20
```

### Explanation

Escape characters format the output into a readable form.

---

## Common Errors

| Error            | Reason                  | Solution                        |
| ---------------- | ----------------------- | ------------------------------- |
| Incorrect output | Missing `\`             | Use a valid escape character    |
| Warning          | Invalid escape sequence | Use supported escape characters |

---

## Common Mistakes

* Forgetting the backslash (`\`).
* Mixing `\n` and `/n`.
* Using escape characters outside strings.

---

## Difference Table

| Escape Character | Purpose      |
| ---------------- | ------------ |
| `\n`             | New line     |
| `\t`             | Tab          |
| `\\`             | Backslash    |
| `\"`             | Double quote |
| `\'`             | Single quote |

---

## Interview Questions

**Q1. What is an escape character?**

A special character beginning with `\` used to format strings.

**Q2. Which escape character creates a new line?**

`\n`

**Q3. Which escape character inserts a tab?**

`\t`

---

## MCQs

**1. Which escape character creates a new line?**

A. `\t`

B. `\n` ✅

C. `\\`

D. `\"`

---

**2. Which escape character prints a tab space?**

A. `\t` ✅

B. `\n`

C. `\r`

D. `\b`

---

**3. Which escape character prints a backslash?**

A. `\n`

B. `\\` ✅

C. `\t`

D. `\"`

---

## Practice Questions

1. What are escape characters?
2. Explain `\n` and `\t`.
3. Print double quotes inside a string.
4. List five escape characters.
5. Write a formatted output using escape characters.

---

## Real-world Applications

* Formatting reports.
* Printing tables.
* File handling.
* Console output.
* Generating text files.

---

## Notes

**Remember:** Every escape character starts with `\`.

**Shortcut:**

* `\n` → New Line
* `\t` → Tab
* `\\` → Backslash
* `\"` → Double Quote

**Interview Tip:** Know the most commonly used escape characters.

**Exam Tip:** Practice writing formatted output using `\n` and `\t`.

---

## Summary

* Escape characters format strings.
* They begin with a backslash (`\`).
* Common escape characters are `\n`, `\t`, `\\`, `\"`, and `\'`.
* They improve output readability.
* Used extensively in printing and file handling.

---

## Keywords

Escape Characters, String, `\n`, `\t`, `\\`, `\"`, `\'`, Formatting

---

## Related Topics

* Strings
* String Methods
* Raw Strings
* Print Function
* Input and Output
