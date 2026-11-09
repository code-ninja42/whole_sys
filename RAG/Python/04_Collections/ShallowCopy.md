# Shallow Copy

## Definition

**Shallow Copy** creates a new object, but the nested objects are shared with the original object. Changes to nested objects affect both copies.

---

## Why do we use it?

* To create a quick copy of an object.
* To save memory.
* To copy only the outer object.
* Faster than deep copy.

---

## Key Points

* Uses the `copy()` function.
* Available in the `copy` module.
* Copies only the outer object.
* Nested objects are shared.

---

## Syntax

```python
import copy

new_object = copy.copy(old_object)
```

---

## Parameters

| Parameter    | Description         |
| ------------ | ------------------- |
| `old_object` | Object to be copied |

---

## Return Value

Returns a new object that shares nested objects with the original.

---

## Internal Working

`copy.copy()` creates a new outer object, but nested objects still point to the same memory location.

---

## Rules

* Import the `copy` module.
* Nested objects are shared.
* Changes to nested objects affect both copies.

---

## Types (if applicable)

### 1. Shallow Copy of a List

```python
import copy

a = [1, 2, 3]
b = copy.copy(a)

print(b)
```

### 2. Shallow Copy of a Nested List

```python
import copy

a = [[1, 2], [3, 4]]
b = copy.copy(a)

b[0][0] = 100

print(a)
print(b)
```

---

## Advantages

* Faster than deep copy.
* Uses less memory.
* Simple to create.

---

## Disadvantages

* Nested objects are shared.
* Changes in nested objects affect both copies.
* Not suitable for complex nested data.

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
import copy

a = [10, 20, 30]
b = copy.copy(a)

print(b)
```

### Output

```text
[10, 20, 30]
```

### Explanation

Creates a new outer list.

---

## Example 2 (Intermediate)

### Code

```python
import copy

a = [[1, 2], [3, 4]]
b = copy.copy(a)

b[0][0] = 100

print(a)
print(b)
```

### Output

```text
[[100, 2], [3, 4]]
[[100, 2], [3, 4]]
```

### Explanation

Changing the nested list affects both copies.

---

## Example 3 (Interview)

### Code

```python
import copy

a = {"name": "Jack", "marks": [80, 90]}
b = copy.copy(a)

b["marks"][0] = 100

print(a)
print(b)
```

### Output

```text
{'name': 'Jack', 'marks': [100, 90]}
{'name': 'Jack', 'marks': [100, 90]}
```

### Explanation

The nested list is shared between both dictionaries.

---

## Example 4 (Real-world)

### Code

```python
import copy

original = {
    "user": "Jack",
    "skills": ["Python", "SQL"]
}

backup = copy.copy(original)

backup["skills"].append("AI")

print(original)
print(backup)
```

### Output

```text
{'user': 'Jack', 'skills': ['Python', 'SQL', 'AI']}
{'user': 'Jack', 'skills': ['Python', 'SQL', 'AI']}
```

### Explanation

The nested list is shared, so both objects change.

---

## Common Errors

| Error          | Reason                     | Solution          |
| -------------- | -------------------------- | ----------------- |
| NameError      | `copy` module not imported | Use `import copy` |
| AttributeError | Wrong function name        | Use `copy.copy()` |

---

## Common Mistakes

* Confusing shallow copy with deep copy.
* Assuming nested objects are copied.
* Forgetting to import the `copy` module.

---

## Difference Table

| Shallow Copy          | Deep Copy             |
| --------------------- | --------------------- |
| Shares nested objects | Copies nested objects |
| Faster                | Slower                |
| Less memory           | More memory           |
| `copy.copy()`         | `copy.deepcopy()`     |

---

## Interview Questions

**Q1. What is shallow copy?**

It creates a new object but shares nested objects with the original.

**Q2. Which function performs shallow copy?**

`copy.copy()`

**Q3. Which module provides shallow copy?**

The `copy` module.

---

## MCQs

**1. Which function creates a shallow copy?**

A. `deepcopy()`

B. `copy()` ✅

C. `clone()`

D. `duplicate()`

---

**2. In shallow copy, nested objects are**

A. Copied

B. Shared ✅

C. Deleted

D. Encrypted

---

**3. Which module contains `copy()`?**

A. `math`

B. `copy` ✅

C. `os`

D. `random`

---

## Practice Questions

1. What is shallow copy?
2. Write a program using `copy.copy()`.
3. Differentiate between shallow copy and deep copy.
4. Why are nested objects shared?
5. When should shallow copy be used?

---

## Real-world Applications

* Fast object duplication
* Temporary data copies
* Simple lists
* Configuration objects
* Performance optimization

---

## Notes

**Remember:** Shallow copy copies only the outer object.

**Shortcut:**

* `copy.copy()` → Shallow copy
* Nested objects → Shared

**Interview Tip:** Nested objects remain linked in shallow copy.

**Exam Tip:** Learn the difference between shallow copy and deep copy.

---

## Summary

* Shallow copy creates a new outer object.
* Uses `copy.copy()`.
* Nested objects are shared.
* Changes to nested objects affect both the original and copied object.

---

## Keywords

Shallow Copy, copy(), copy Module, Nested Objects, Shared Reference, Mutable Objects

---

## Related Topics

* Deep Copy
* Lists
* Dictionaries
* Mutable Objects
* Copy Module
