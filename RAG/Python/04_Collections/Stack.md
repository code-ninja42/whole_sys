# Stack

## Definition

A **Stack** is a linear data structure that follows the **LIFO (Last In, First Out)** principle. The last element added is the first one to be removed.

---

## Why do we use it?

* To store data in LIFO order.
* To manage function calls.
* To implement undo/redo operations.
* To evaluate expressions.

---

## Key Points

* Follows **LIFO**.
* Insertion is called **Push**.
* Deletion is called **Pop**.
* Top element is accessed using **Peek**.

---

## Syntax

```python
stack = []
```

---

## Parameters

| Operation  | Description            |
| ---------- | ---------------------- |
| `append()` | Push an element        |
| `pop()`    | Remove the top element |
| `[-1]`     | Peek the top element   |
| `len()`    | Returns stack size     |

---

## Return Value

Returns the top element for `pop()` and the stack size for `len()`.

---

## Internal Working

Python stacks are commonly implemented using lists. Elements are added and removed from the end of the list.

---

## Rules

* Follows LIFO.
* Push adds to the top.
* Pop removes from the top.
* Popping an empty stack raises an error.

---

## Types (if applicable)

### 1. Push Operation

```python
stack = []

stack.append(10)
stack.append(20)

print(stack)
```

### 2. Pop Operation

```python
stack = [10, 20, 30]

print(stack.pop())
```

### 3. Peek Operation

```python
stack = [10, 20, 30]

print(stack[-1])
```

---

## Advantages

* Simple implementation.
* Fast insertion and deletion.
* Useful for recursion.
* Efficient memory management.

---

## Disadvantages

* Only top element is accessible.
* No random access.
* Fixed order (LIFO).

---

## Time Complexity

| Operation | Complexity |
| --------- | ---------- |
| Push      | **O(1)**   |
| Pop       | **O(1)**   |
| Peek      | **O(1)**   |
| Search    | **O(n)**   |

---

## Space Complexity

**O(n)**

---

# Examples

## Example 1 (Basic)

### Code

```python
stack = []

stack.append(10)
stack.append(20)

print(stack)
```

### Output

```text
[10, 20]
```

### Explanation

Pushes two elements onto the stack.

---

## Example 2 (Intermediate)

### Code

```python
stack = [10, 20, 30]

stack.pop()

print(stack)
```

### Output

```text
[10, 20]
```

### Explanation

Removes the top element.

---

## Example 3 (Interview)

### Code

```python
stack = [5, 10, 15]

print(stack[-1])
```

### Output

```text
15
```

### Explanation

Displays the top element without removing it.

---

## Example 4 (Real-world)

### Code

```python
browser = []

browser.append("Google")
browser.append("YouTube")

browser.pop()

print(browser)
```

### Output

```text
['Google']
```

### Explanation

Simulates the browser back operation.

---

## Common Errors

| Error      | Reason               | Solution                  |
| ---------- | -------------------- | ------------------------- |
| IndexError | Pop from empty stack | Check if stack is empty   |
| IndexError | Peek on empty stack  | Verify stack has elements |

---

## Common Mistakes

* Confusing Stack with Queue.
* Popping from an empty stack.
* Using the wrong end of the list.

---

## Difference Table

| Stack                      | Queue                       |
| -------------------------- | --------------------------- |
| LIFO                       | FIFO                        |
| Push                       | Enqueue                     |
| Pop                        | Dequeue                     |
| Last element removed first | First element removed first |

---

## Interview Questions

**Q1. What is a stack?**

A linear data structure that follows LIFO.

**Q2. Which method is used to push an element?**

`append()`

**Q3. Which method removes the top element?**

`pop()`

---

## MCQs

**1. Stack follows**

A. FIFO

B. LIFO ✅

C. Random

D. Circular

---

**2. Which method pushes an element?**

A. `append()` ✅

B. `insert()`

C. `add()`

D. `extend()`

---

**3. Which method removes the top element?**

A. `delete()`

B. `remove()`

C. `pop()` ✅

D. `clear()`

---

## Practice Questions

1. What is a stack?
2. Explain the LIFO principle.
3. Write a program to push elements.
4. Write a program to pop an element.
5. Differentiate between Stack and Queue.

---

## Real-world Applications

* Browser history
* Undo/Redo feature
* Function calls
* Expression evaluation
* Backtracking algorithms

---

## Notes

**Remember:** Stack follows **LIFO (Last In, First Out).**

**Shortcut:**

* `append()` → Push
* `pop()` → Pop
* `stack[-1]` → Peek

**Interview Tip:** Python lists are commonly used to implement stacks.

**Exam Tip:** Remember the difference between LIFO and FIFO.

---

## Summary

* A stack follows the LIFO principle.
* Elements are added using `append()`.
* Elements are removed using `pop()`.
* Widely used in recursion, browser history, and undo operations.

---

## Keywords

Stack, LIFO, Push, Pop, Peek, Linear Data Structure

---

## Related Topics

* Queue
* List
* Heap
* Tree
* Data Structures
