# While Loop

## Definition

A **`while` loop** is used to repeatedly execute a block of code **as long as a given condition is `True`**. The loop stops when the condition becomes `False`.

---

## Why do we use it?

* To repeat a task.
* When the number of iterations is unknown.
* To execute code based on a condition.
* To automate repetitive tasks.

---

## Key Points

* Runs while the condition is `True`.
* Stops when the condition becomes `False`.
* The condition is checked before every iteration.
* Can be used with `break` and `continue`.
* May create an infinite loop if the condition never becomes `False`.

---

## Syntax

```python
while condition:
    # Code
```

---

## Parameters

| Parameter | Description                               |
| --------- | ----------------------------------------- |
| condition | Boolean expression that controls the loop |

---

## Return Value

**N/A**

---

## Internal Working

Python checks the condition before each iteration. If it is `True`, the loop body executes. If it is `False`, the loop terminates.

---

## Flow Diagram (if applicable)

```text
Start
  │
  ▼
Check Condition
  │
 ┌┴┐
 │ │
T   F
│   │
▼   ▼
Execute End
Code
 │
 └──────► Check Again
```

---

## Rules

* The condition must return `True` or `False`.
* Update the loop variable inside the loop.
* Proper indentation is required.
* Avoid infinite loops.

---

## Types (if applicable)

### 1. Simple While Loop

```python
i = 1

while i <= 5:
    print(i)
    i += 1
```

### 2. Infinite While Loop

```python
while True:
    print("Running")
```

---

## Advantages

* Best when the number of iterations is unknown.
* Flexible and easy to use.
* Useful for user input and menu-driven programs.

---

## Disadvantages

* Can create infinite loops.
* Requires manual updating of the loop variable.

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
i = 1

while i <= 5:
    print(i)
    i += 1
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

The loop prints numbers from 1 to 5.

---

## Example 2 (Intermediate)

### Code

```python
num = 5

while num > 0:
    print(num)
    num -= 1
```

### Output

```text
5
4
3
2
1
```

### Explanation

The loop counts down from 5 to 1.

---

## Example 3 (Interview)

### Code

```python
i = 1
total = 0

while i <= 5:
    total += i
    i += 1

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
password = ""

while password != "python":
    password = input("Enter Password: ")

print("Welcome Jack")
```

### Output

```text
Enter Password: python
Welcome Jack
```

### Explanation

The loop continues until the correct password is entered.

---

## Common Errors

| Error            | Reason                          | Solution                 |
| ---------------- | ------------------------------- | ------------------------ |
| Infinite Loop    | Condition never becomes `False` | Update the loop variable |
| IndentationError | Incorrect indentation           | Use proper indentation   |

---

## Common Mistakes

* Forgetting to update the loop variable.
* Writing an incorrect condition.
* Creating an infinite loop accidentally.

---

## Difference Table

| While Loop         | For Loop            |
| ------------------ | ------------------- |
| Unknown iterations | Known iterations    |
| Uses a condition   | Uses a sequence     |
| Manual update      | Automatic iteration |

---

## Interview Questions

**Q1. What is a `while` loop?**

A loop that runs as long as the condition is `True`.

**Q2. When should you use a `while` loop?**

When the number of iterations is unknown.

**Q3. What is an infinite loop?**

A loop that never ends because the condition is always `True`.

---

## MCQs

**1. A `while` loop executes until**

A. The condition becomes `False` ✅

B. The condition becomes `True`

C. The program ends

D. None of these

---

**2. Which loop is suitable when the number of iterations is unknown?**

A. `for`

B. `while` ✅

C. `if`

D. `elif`

---

**3. Which statement can terminate a `while` loop immediately?**

A. `pass`

B. `continue`

C. `break` ✅

D. `print`

---

## Practice Questions

1. What is a `while` loop?
2. Write a program to print numbers from 1 to 10.
3. Print numbers in reverse using a `while` loop.
4. Explain an infinite loop.
5. Differentiate between `for` and `while`.

---

## Real-world Applications

* ATM systems.
* Login authentication.
* Menu-driven programs.
* Game loops.
* Password validation.

---

## Notes

**Remember:** `while` repeats until the condition becomes `False`.

**Shortcut:** `while condition:`

**Interview Tip:** Always update the loop variable.

**Exam Tip:** Know the difference between `for` and `while`.

---

## Summary

* `while` executes code while a condition is `True`.
* Best when the number of iterations is unknown.
* Supports `break` and `continue`.
* Always update the loop variable.
* Avoid infinite loops.

---

## Keywords

While Loop, Condition, Iteration, Infinite Loop, Break, Continue, Control Flow

---

## Related Topics

* For Loop
* Break
* Continue
* Pass
* If Statement
