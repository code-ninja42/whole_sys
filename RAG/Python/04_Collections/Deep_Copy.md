# Deep Copy

## Definition

**Deep Copy** creates a completely independent copy of an object, including all nested objects. Changes made to the copied object do not affect the original object.

---

## Why do we use it?

* To create an independent copy.
* To avoid modifying the original data.
* To copy nested lists and dictionaries safely.
* To prevent shared references.

---

## Key Points

* Uses the `deepcopy()` function.
* Available in the `copy` module.
* Copies nested objects recursively.
* Original and copied objects are independent.

---

## Syntax

```python
import copy

new_object = copy.deepcopy(old_object)
```

---

## Parameters

| Parameter    | Description                |
| ------------ | -------------------------- |
| `old_object` | Object to be copied deeply |

---

## Return Value

Returns a completely new object with independent nested objects.

---

## Internal Working

`deepcopy()` recursively copies every object and nested object, creating new memory locations for all elements.

---

## Rules

* Import the `copy` module.
* Use `deepcopy()` for nested objects.
* Changes in the copied object do not affect the original.

---

## Types (if applicable)

### 1. Deep Copy of a List

```python
import copy

a = [1, 2, 3]
b = copy.deepcopy(a)

print(b)
```

### 2. Deep Copy of a Nested List

```python
import copy

a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)

b[0][0] = 100

print(a)
print(b)
```

---

## Advantages

* Creates a fully independent copy.
* Safe for nested objects.
* Prevents accidental data modification.

---

## Disadvantages

* Slower than shallow copy.
* Uses more memory.
* Extra import (`copy`) is required.

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
b = copy.deepcopy(a)

print(b)
```

### Output

```text
[10, 20, 30]
```

### Explanation

Creates a new independent list.

---

## Example 2 (Intermediate)

### Code

```python
import copy

a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)

b[0][0] = 100

print(a)
print(b)
```

### Output

```text
[[1, 2], [3, 4]]
[[100, 2], [3, 4]]
```

### Explanation

Changing the copied list does not affect the original.

---

## Example 3 (Interview)

### Code

```python
import copy

a = {"name": "Jack", "marks": [80, 90]}
b = copy.deepcopy(a)

b["marks"][0] = 100

print(a)
print(b)
```

### Output

```text
{'name': 'Jack', 'marks': [80, 90]}
{'name': 'Jack', 'marks': [100, 90]}
```

### Explanation

Nested objects are copied independently.

---

## Example 4 (Real-world)

### Code

```python
import copy

original = {
    "user": "Jack",
    "skills": ["Python", "SQL"]
}

backup = copy.deepcopy(original)

backup["skills"].append("AI")

print(original)
print(backup)
```

### Output

```text
{'user': 'Jack', 'skills': ['Python', 'SQL']}
{'user': 'Jack', 'skills': ['Python', 'SQL', 'AI']}
```

### Explanation

Useful for creating safe backups before modifying data.

---

## Common Errors

| Error          | Reason                     | Solution              |
| -------------- | -------------------------- | --------------------- |
| NameError      | `copy` module not imported | Use `import copy`     |
| AttributeError | Incorrect function name    | Use `copy.deepcopy()` |

---

## Common Mistakes

* Forgetting to import the `copy` module.
* Confusing shallow copy with deep copy.
* Assuming nested objects are copied automatically.

---

## Difference Table

| Deep Copy             | Shallow Copy          |
| --------------------- | --------------------- |
| Copies nested objects | Shares nested objects |
| Independent copy      | Partial copy          |
| More memory           | Less memory           |
| Slower                | Faster                |

---

## Interview Questions

**Q1. What is deep copy?**

It creates a completely independent copy of an object.

**Q2. Which module provides deep copy?**

The `copy` module.

**Q3. Which function performs deep copy?**

`copy.deepcopy()`.

---

## MCQs

**1. Which function creates a deep copy?**

A. `copy()`

B. `deepcopy()` ✅

C. `clone()`

D. `duplicate()`

---

**2. Which module contains `deepcopy()`?**

A. `math`

B. `random`

C. `copy` ✅

D. `os`

---

**3. Deep copy is mainly used for**

A. Numbers

B. Nested objects ✅

C. Strings only

D. Booleans

---

## Practice Questions

1. What is deep copy?
2. Write a program using `copy.deepcopy()`.
3. Differentiate between deep copy and shallow copy.
4. Why is deep copy useful for nested lists?
5. Explain why `copy` module is required.

---

## Real-world Applications

* Data backup
* Machine learning datasets
* Configuration files
* Nested dictionaries
* Game state management

---

## Notes

**Remember:** Deep copy creates **completely independent objects**.

**Shortcut:**

* `copy.deepcopy()` → Independent copy
* Nested objects → Also copied

**Interview Tip:** Deep copy copies every nested object.

**Exam Tip:** Know the difference between shallow copy and deep copy.

---

## Summary

* Deep copy creates a completely separate object.
* Uses `copy.deepcopy()`.
* Nested objects are copied recursively.
* Changes in the copied object never affect the original.

---

## Keywords

Deep Copy, deepcopy(), copy Module, Nested Objects, Independent Copy, Mutable Objects

---

## Related Topics

* Shallow Copy
* Lists
* Dictionaries
* Mutable Objects
* Copy Module
