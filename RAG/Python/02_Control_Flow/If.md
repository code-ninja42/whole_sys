# For Loop

## Definition

A **`for` loop** is used to iterate over a sequence such as a list, tuple, string, set, dictionary, or `range()`. It executes a block of code once for each item in the sequence.

---

## Why do we use it?

* To repeat a block of code.
* To iterate through a sequence.
* To reduce repetitive code.
* To automate tasks.

---

## Key Points

* Used for iteration.
* Works with sequences and `range()`.
* Executes until all items are processed.
* Supports nested loops.
* Can be used with `break` and `continue`.

---

## Syntax

```python
for variable in sequence:
    # Code
```

Example:

```python
for i in range(5):
    print(i)
```

---

## Parameters

| Parameter | Description                   |
| --------- | ----------------------------- |
| variable  | Stores the current value      |
| sequence  | Collection or iterable object |

---

## Return Value

**N/A**

---

## Internal Working

The `for` loop takes one element at a time from the sequence, assigns it to the loop variable, executes the loop body, and repeats until all elements are processed.

---

## Flow Diagram (if applicable)

```text
Start
  │
  ▼
Get Next Item
  │
  ▼
Execute Loop Body
  │
  ▼
More Items?
 ┌───────┐
 │ Yes   │ No
 ▼       ▼
Repeat    End
```

---

## Rules

* The sequence must be iterable.
* Proper indentation is required.
* The loop ends automatically after the last item.
* The loop variable updates in every iteration.

---

## Types (if applicable)

### 1. Using `range()`

```python
for i in range(5):
    print(i)
```

### 2. Using String

```python
for ch in "Python":
    print(ch)
```

### 3. Using List

```python
for num in [10, 20, 30]:
    print(num)
```

---

## Advantages

* Easy to use.
* Reduces repetitive code.
* Works with different data types.
* Improves readability.

---

## Disadvantages

* Not suitable when the number of iterations is unknown.
* Nested loops may reduce performance.

---

## Time Complexity

**O(n)**

---

## Space Complexity

**O(1)**

---

# Examples

## Example 1 (Basic)

### Code

```python
for i in range(1, 6):
    print(i)
```

### Output

```text
1
2
3
4
5
```

### Explanation

Prints numbers from 1 to 5.

---

## Example 2 (Intermediate)

### Code

```python
name = "Jack"

for ch in name:
    print(ch)
```

### Output

```text
J
a
c
k
```

### Explanation

The loop prints each character of the string.

---

## Example 3 (Interview)

### Code

```python
total = 0

for i in range(1, 6):
    total += i

print(total)
```

### Output

```text
15
```

### Explanation

Calculates the sum of numbers from 1 to 5.

---

## Example 4 (Real-world)

### Code

```python
marks = [85, 90, 78, 95]

for mark in marks:
    print(mark)
```

### Output

```text
85
90
78
95
```

### Explanation

Displays each student's marks.

---

## Common Errors

| Error            | Reason                 | Solution                  |
| ---------------- | ---------------------- | ------------------------- |
| TypeError        | Object is not iterable | Use an iterable object    |
| IndentationError | Incorrect indentation  | Follow proper indentation |

---

## Common Mistakes

* Forgetting the colon (`:`).
* Incorrect indentation.
* Using a non-iterable object.
* Confusing `range(5)` with numbers 1–5.

---

## Difference Table

| For Loop                 | While Loop                     |
| ------------------------ | ------------------------------ |
| Known iterations         | Unknown iterations             |
| Iterates over a sequence | Runs while a condition is true |
| Simpler syntax           | More flexible                  |

---

## Interview Questions

**Q1. What is a `for` loop?**

A loop used to iterate over a sequence.

**Q2. Which function is commonly used with a `for` loop?**

`range()`

**Q3. Can a `for` loop iterate over a string?**

Yes.

---

## MCQs

**1. Which function is mostly used with a `for` loop?**

A. `type()`

B. `range()` ✅

C. `len()`

D. `print()`

---

**2. A `for` loop is mainly used for**

A. Decision making

B. Iteration ✅

C. Exception handling

D. Input

---

**3. Which of the following is iterable?**

A. List

B. String

C. Tuple

D. All of the above ✅

---

## Practice Questions

1. What is a `for` loop?
2. Write a program using `range()`.
3. Iterate through a string.
4. Print all elements of a list using a `for` loop.
5. Find the sum of numbers from 1 to 10 using a `for` loop.

---

## Real-world Applications

* Processing student marks.
* Reading file data.
* Iterating through lists.
* Data analysis.
* Automation scripts.

---

## Notes

**Remember:** A `for` loop is used when the number of iterations is known.

**Shortcut:** `for variable in sequence:`

**Interview Tip:** Know how `range()` works with a `for` loop.

**Exam Tip:** Practice iterating over lists, strings, and dictionaries.

---

## Summary

* A `for` loop repeats a block of code.
* It iterates over sequences.
* Commonly used with `range()`.
* Supports `break` and `continue`.
* Easy and efficient for repetitive tasks.

---

## Keywords

For Loop, Iteration, Sequence, Iterable, range(), Loop, Control Flow

---

## Related Topics

* While Loop
* Range
* Break
* Continue
* Nested Loops
