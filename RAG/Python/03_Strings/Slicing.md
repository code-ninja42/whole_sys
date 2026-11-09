# Slicing

## Definition

**Slicing** is a technique used to access a specific part of a sequence such as a string, list, tuple, or array by specifying a start, stop, and step value.

---

## Why do we use it?

* To extract a portion of a sequence.
* To reverse a sequence.
* To skip characters or elements.
* To copy a sequence.

---

## Key Points

* Uses the slice operator `[:]`.
* Works with strings, lists, tuples, and arrays.
* Start index is inclusive.
* Stop index is exclusive.
* Step decides the increment or decrement.

---

## Syntax

```python
sequence[start:stop:step]
```

---

## Parameters

| Parameter | Description |
|----------|-------------|
| `start` | Starting index (inclusive) |
| `stop` | Ending index (exclusive) |
| `step` | Number of positions to move |

---

## Return Value

Returns a new sliced sequence.

---

## Internal Working

Python creates a new sequence by selecting elements from the original sequence according to the given start, stop, and step values.

---

## Rules

* Indexing starts from `0`.
* Negative indexing starts from `-1`.
* Stop index is not included.
* Step cannot be `0`.
* Omitting values uses default behavior.

---

## Types (if applicable)

### 1. Basic Slicing

```python
text = "Python"

print(text[1:4])
```

### 2. Negative Slicing

```python
text = "Python"

print(text[-4:-1])
```

### 3. Step Slicing

```python
text = "Python"

print(text[::2])
```

### 4. Reverse Slicing

```python
text = "Python"

print(text[::-1])
```

---

## Advantages

* Easy to extract data.
* Supports reverse operations.
* Makes code shorter.
* Works on multiple sequence types.

---

## Disadvantages

* Creates a new sequence.
* Large slices use extra memory.

---

## Time Complexity

**O(k)**

(k = number of selected elements)

---

## Space Complexity

**O(k)**

---

# Examples

## Example 1 (Basic)

### Code

```python
text = "Python"

print(text[1:4])
```

### Output

```text
yth
```

### Explanation

Extracts characters from index 1 to 3.

---

## Example 2 (Intermediate)

### Code

```python
text = "Programming"

print(text[::2])
```

### Output

```text
Pormig
```

### Explanation

Prints every second character.

---

## Example 3 (Interview)

### Code

```python
text = "Python"

print(text[::-1])
```

### Output

```text
nohtyP
```

### Explanation

Reverses the string using slicing.

---

## Example 4 (Real-world)

### Code

```python
account = "1234567890"

print(account[-4:])
```

### Output

```text
7890
```

### Explanation

Displays only the last four digits.

---

## Common Errors

| Error | Reason | Solution |
|-------|--------|----------|
| ValueError | Step is `0` | Use a non-zero step |
| IndexError | Incorrect indexing (rare in slicing) | Check index values |

---

## Common Mistakes

* Forgetting that stop index is excluded.
* Using step as `0`.
* Confusing positive and negative indexing.
* Expecting slicing to modify the original sequence.

---

## Difference Table

| Indexing | Slicing |
|----------|---------|
| Returns one element | Returns multiple elements |
| Uses one index | Uses start:stop:step |
| Example: `text[2]` | Example: `text[1:5]` |

---

## Interview Questions

**Q1. What is slicing in Python?**

It is a method to extract a part of a sequence.

**Q2. Is the stop index included?**

No, it is excluded.

**Q3. Which operator is used for slicing?**

The colon (`:`) operator.

---

## MCQs

**1. Which operator is used for slicing?**

A. `[]`

B. `: ` ✅

C. `()`

D. `{}`

---

**2. Which slice reverses a string?**

A. `[1:]`

B. `[::-1]` ✅

C. `[::1]`

D. `[:1]`

---

**3. What is the output?**

```python
text = "Python"
print(text[:2])
```

A. `yt`

B. `Py` ✅

C. `Pyt`

D. `thon`

---

## Practice Questions

1. What is slicing?
2. Reverse a string using slicing.
3. Print every second character.
4. Extract the last three characters.
5. Explain positive and negative slicing.

---

## Real-world Applications

* Display last four digits of an account number.
* Extract file extensions.
* Reverse strings.
* Process text data.
* Select parts of lists and arrays.

---

## Notes

**Remember:** The stop index is **not included**.

**Shortcut:**

* `[:]` → Copy
* `[::-1]` → Reverse
* `[::2]` → Every second element
* `[-3:]` → Last three elements

**Interview Tip:** Know the difference between indexing and slicing.

**Exam Tip:** Practice positive, negative, and step slicing.

---

## Summary

* Slicing extracts part of a sequence.
* Uses the syntax `sequence[start:stop:step]`.
* Works with strings, lists, tuples, and arrays.
* Supports reversing, skipping, and copying sequences.

---

## Keywords

Slicing, Start, Stop, Step, Positive Index, Negative Index, Reverse, Sequence

---

## Related Topics

* Strings
* Lists
* Tuples
* Indexing
* String Formatting