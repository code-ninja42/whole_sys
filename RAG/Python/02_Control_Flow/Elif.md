# Elif Statement

## Definition

The **`elif`** (else if) statement is used to check multiple conditions. If the `if` condition is `False`, Python checks the `elif` condition. You can use multiple `elif` statements in a program.

---

## Why do we use it?

* To check multiple conditions.
* To avoid writing multiple `if` statements.
* To make decision-making easier.
* To improve code readability.

---

## Key Points

* `elif` stands for **else if**.
* It is used after an `if` statement.
* Multiple `elif` statements are allowed.
* Only the first `True` condition is executed.
* `else` is optional.

---

## Syntax

```python
if condition1:
    # Code
elif condition2:
    # Code
else:
    # Code
```

---

## Parameters

**N/A**

---

## Return Value

**N/A**

---

## Internal Working

Python first checks the `if` condition. If it is `False`, it checks each `elif` condition one by one. When a condition becomes `True`, its block is executed and the remaining conditions are skipped.

---

## Flow Diagram (if applicable)

```text
Start
  │
  ▼
if Condition?
 ┌───────┐
 │True   │False
 ▼       ▼
Execute  elif Condition?
            ┌───────┐
            │True   │False
            ▼       ▼
         Execute   else
```

---

## Rules

* `elif` must come after `if`.
* Multiple `elif` statements are allowed.
* `else` must always be the last block.
* Indentation is mandatory.

---

## Types (if applicable)

**N/A**

---

## Advantages

* Handles multiple conditions.
* Makes code cleaner.
* Reduces nested `if` statements.

---

## Disadvantages

* Too many `elif` statements can make code lengthy.
* Conditions are checked one by one.

---

## Time Complexity

**O(n)** (Worst case, where `n` is the number of conditions)

---

## Space Complexity

**O(1)**

---

# Examples

## Example 1 (Basic)

### Code

```python
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")
```

### Output

```text
Grade B
```

### Explanation

The `if` condition is false, so Python checks the `elif` condition, which is true.

---

## Example 2 (Intermediate)

### Code

```python
num = 0

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
```

### Output

```text
Zero
```

### Explanation

Since both `if` and `elif` are false, the `else` block executes.

---

## Example 3 (Interview)

### Code

```python
age = 20

if age < 18:
    print("Minor")
elif age == 18:
    print("Just Adult")
else:
    print("Adult")
```

### Output

```text
Adult
```

### Explanation

Only the first true condition is executed.

---

## Example 4 (Real-world)

### Code

```python
salary = 70000

if salary >= 100000:
    print("High Salary")
elif salary >= 50000:
    print("Medium Salary")
else:
    print("Low Salary")
```

### Output

```text
Medium Salary
```

### Explanation

`elif` helps categorize salary ranges.

---

## Common Errors

| Error              | Reason                | Solution                  |
| ------------------ | --------------------- | ------------------------- |
| `SyntaxError`      | `elif` without `if`   | Use `if` before `elif`    |
| `IndentationError` | Incorrect indentation | Follow proper indentation |

---

## Common Mistakes

* Writing `elif` before `if`.
* Forgetting the colon (`:`).
* Incorrect indentation.
* Using multiple `if` statements instead of `elif`.

---

## Difference Table

| `if`            | `elif`                | `else`        |
| --------------- | --------------------- | ------------- |
| First condition | Additional conditions | Default block |
| Mandatory       | Optional              | Optional      |

---

## Interview Questions

**Q1. What is `elif`?**

It is used to check additional conditions after an `if` statement.

**Q2. Can multiple `elif` statements be used?**

Yes.

**Q3. Does Python execute all `elif` blocks?**

No, only the first true condition is executed.

---

## MCQs

**1. `elif` stands for**

A. Else Loop

B. Else If ✅

C. End If

D. Extra If

---

**2. `elif` is used after**

A. `while`

B. `if` ✅

C. `for`

D. `break`

---

**3. How many `elif` statements can be used?**

A. One

B. Two

C. Unlimited ✅

D. None

---

## Practice Questions

1. What is `elif`?
2. Write a program using multiple `elif` statements.
3. Differentiate between `if` and `elif`.
4. Explain the working of `elif`.
5. Write a grading program using `elif`.

---

## Real-world Applications

* Student grading systems.
* Salary classification.
* ATM menu options.
* Age verification.
* Login access levels.

---

## Notes

**Remember:** `elif` checks another condition only if the previous condition is false.

**Shortcut:** **if → elif → else**

**Interview Tip:** Only the first true condition executes.

**Exam Tip:** `elif` cannot exist without an `if`.

---

## Summary

* `elif` stands for **else if**.
* Used to check multiple conditions.
* Comes after `if`.
* Multiple `elif` statements are allowed.
* Only the first true condition executes.

---

## Keywords

elif, if, else, Conditional Statement, Decision Making, Control Flow

---

## Related Topics

* If Statement
* Else Statement
* Nested If
* Match Case
* Logical Operators
