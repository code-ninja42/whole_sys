# Break Statement

## Definition

The **`break`** statement is used to immediately terminate a loop (`for` or `while`). When `break` is encountered, the control exits the loop and continues with the next statement after the loop.

---

## Why do we use it?

* To stop a loop early.
* To avoid unnecessary iterations.
* To improve program efficiency.
* To exit when a condition is met.

---

## Key Points

* Works with `for` and `while` loops.
* Terminates only the current loop.
* Control moves to the statement after the loop.
* Commonly used with `if` conditions.

---

## Syntax

```python
break
```

---

## Parameters

**N/A**

---

## Return Value

**N/A**

---

## Internal Working

When Python encounters `break`, it immediately exits the current loop without executing the remaining iterations.

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
break Found?
 ┌──┴──┐
No     Yes
 │       │
 ▼       ▼
Next   Exit Loop
Iteration
```

---

## Rules

* Can only be used inside loops.
* Exits only the nearest loop.
* Often used with `if` statements.

---

## Types (if applicable)

**N/A**

---

## Advantages

* Saves execution time.
* Makes loops more efficient.
* Prevents unnecessary processing.

---

## Disadvantages

* Excessive use can reduce code readability.
* May skip expected iterations.

---

## Time Complexity

**O(1)** (for the `break` operation)

---

## Space Complexity

**O(1)**

---

# Examples

## Example 1 (Basic)

### Code

```python
for i in range(1, 6):
    if i == 4:
        break
    print(i)
```

### Output

```text
1
2
3
```

### Explanation

The loop stops when `i` becomes `4`.

---

## Example 2 (Intermediate)

### Code

```python
num = 1

while num <= 10:
    if num == 6:
        break
    print(num)
    num += 1
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

The `while` loop exits when `num` is `6`.

---

## Example 3 (Interview)

### Code

```python
for i in range(3):
    for j in range(3):
        if j == 1:
            break
        print(i, j)
```

### Output

```text
0 0
1 0
2 0
```

### Explanation

`break` exits only the **inner loop**, not the outer loop.

---

## Example 4 (Real-world)

### Code

```python
password = "python123"

while True:
    user = input("Enter Password: ")

    if user == password:
        print("Access Granted")
        break

    print("Try Again")
```

### Output

```text
Enter Password: python123
Access Granted
```

### Explanation

The loop stops once the correct password is entered.

---

## Common Errors

| Error         | Reason                      | Solution                 |
| ------------- | --------------------------- | ------------------------ |
| `SyntaxError` | `break` used outside a loop | Use it only inside loops |

---

## Common Mistakes

* Using `break` outside a loop.
* Assuming `break` exits all nested loops.
* Forgetting that code after `break` in the same block won't execute.

---

## Difference Table

| `break`                        | `continue`                          |
| ------------------------------ | ----------------------------------- |
| Exits the loop                 | Skips current iteration             |
| Loop ends                      | Loop continues                      |
| Control moves outside the loop | Control moves to the next iteration |

---

## Interview Questions

**Q1. What is `break` in Python?**

It immediately terminates the current loop.

**Q2. Can `break` be used in a `while` loop?**

Yes.

**Q3. Does `break` exit all nested loops?**

No, it exits only the nearest loop.

---

## MCQs

**1. `break` is used to**

A. Skip an iteration

B. Exit the loop ✅

C. Restart the loop

D. End the program

---

**2. `break` can be used inside**

A. `for`

B. `while`

C. Both A and B ✅

D. `if` only

---

**3. `break` exits**

A. All loops

B. Current loop only ✅

C. The program

D. A function

---

## Practice Questions

1. What is the purpose of `break`?
2. Write a program using `break` in a `for` loop.
3. Use `break` in a `while` loop.
4. Explain `break` with nested loops.
5. Differentiate between `break` and `continue`.

---

## Real-world Applications

* Password validation.
* Menu-driven programs.
* Searching an element.
* Stopping a process when a condition is met.

---

## Notes

**Remember:** `break` completely exits the current loop.

**Shortcut:** **break = Exit Loop**

**Interview Tip:** `break` affects only the nearest loop.

**Exam Tip:** Don't confuse `break` with `continue`.

---

## Summary

* `break` terminates the current loop.
* Works with `for` and `while` loops.
* Improves efficiency by avoiding unnecessary iterations.
* Exits only the nearest loop.
* Commonly used with `if` conditions.

---

## Keywords

break, Loop, for, while, Exit, Control Flow

---

## Related Topics

* Continue
* Pass
* For Loop
* While Loop
* If Statement
