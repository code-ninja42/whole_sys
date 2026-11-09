# Continue Statement

## Definition

The **`continue`** statement is used to skip the current iteration of a loop and move to the next iteration. Unlike `break`, it does **not** terminate the loop.

---

## Why do we use it?

* To skip specific iterations.
* To avoid executing unwanted code.
* To simplify loop conditions.
* To improve code readability.

---

## Key Points

* Works with `for` and `while` loops.
* Skips only the current iteration.
* The loop continues with the next iteration.
* Commonly used with `if` statements.

---

## Syntax

```python
continue
```

---

## Parameters

**N/A**

---

## Return Value

**N/A**

---

## Internal Working

When Python encounters `continue`, it skips the remaining statements in the current iteration and immediately starts the next iteration of the loop.

---

## Flow Diagram (if applicable)

```text
Start Loop
    │
    ▼
Condition True?
    │
   Yes
    │
    ▼
continue Found?
 ┌──┴──┐
No     Yes
 │       │
 ▼       ▼
Execute  Next
Code   Iteration
```

---

## Rules

* Can only be used inside loops.
* Skips only the current iteration.
* Does not terminate the loop.

---

## Types (if applicable)

**N/A**

---

## Advantages

* Reduces unnecessary code execution.
* Makes loops cleaner.
* Improves readability.

---

## Disadvantages

* Overuse can make code difficult to understand.
* May accidentally skip important statements.

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
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

### Output

```text
1
2
4
5
```

### Explanation

When `i` becomes `3`, that iteration is skipped.

---

## Example 2 (Intermediate)

### Code

```python
num = 0

while num < 5:
    num += 1
    if num == 3:
        continue
    print(num)
```

### Output

```text
1
2
4
5
```

### Explanation

The value `3` is skipped, but the loop continues.

---

## Example 3 (Interview)

### Code

```python
for ch in "Python":
    if ch == "h":
        continue
    print(ch)
```

### Output

```text
P
y
t
o
n
```

### Explanation

The character `h` is skipped.

---

## Example 4 (Real-world)

### Code

```python
marks = [85, 25, 90, 30, 75]

for mark in marks:
    if mark < 35:
        continue
    print(mark)
```

### Output

```text
85
90
75
```

### Explanation

Students with marks below `35` are skipped.

---

## Common Errors

| Error         | Reason                         | Solution                 |
| ------------- | ------------------------------ | ------------------------ |
| `SyntaxError` | `continue` used outside a loop | Use it only inside loops |

---

## Common Mistakes

* Using `continue` outside a loop.
* Confusing `continue` with `break`.
* Forgetting that the loop continues after `continue`.

---

## Difference Table

| `continue`                  | `break`                  |
| --------------------------- | ------------------------ |
| Skips current iteration     | Exits the loop           |
| Loop continues              | Loop stops               |
| Used to ignore an iteration | Used to terminate a loop |

---

## Interview Questions

**Q1. What is the purpose of `continue`?**

It skips the current iteration and moves to the next one.

**Q2. Does `continue` terminate a loop?**

No.

**Q3. Can `continue` be used in both `for` and `while` loops?**

Yes.

---

## MCQs

**1. `continue` is used to**

A. Exit the loop

B. Skip the current iteration ✅

C. Stop the program

D. Restart the loop

---

**2. `continue` works with**

A. `for`

B. `while`

C. Both A and B ✅

D. `if` only

---

**3. Which statement skips only one iteration?**

A. `break`

B. `continue` ✅

C. `pass`

D. `return`

---

## Practice Questions

1. What is the `continue` statement?
2. Write a program using `continue` in a `for` loop.
3. Write a program using `continue` in a `while` loop.
4. Differentiate between `break` and `continue`.
5. Explain the working of `continue`.

---

## Real-world Applications

* Skipping invalid records.
* Ignoring failed inputs.
* Filtering data.
* Processing only valid entries.

---

## Notes

**Remember:** `continue` skips only the current iteration.

**Shortcut:** **continue = Skip Current Iteration**

**Interview Tip:** `continue` does **not** exit the loop.

**Exam Tip:** Don't confuse `continue` with `break`.

---

## Summary

* `continue` skips the current iteration.
* Works with `for` and `while` loops.
* Does not terminate the loop.
* Commonly used with `if` conditions.
* Makes loop processing more efficient.

---

## Keywords

continue, Loop, for, while, Skip, Control Flow

---

## Related Topics

* Break
* Pass
* For Loop
* While Loop
* If Statement
