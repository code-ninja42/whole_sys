# Tuple

## Definition

A **Tuple** is an ordered, immutable collection of elements in Python. Once created, its values cannot be changed.

---

## Why do we use it?

* To store fixed data.
* To protect data from modification.
* To improve performance compared to lists.
* To use as keys in dictionaries.

---

## Key Points

* Created using `()`.
* Ordered collection.
* Immutable (cannot be changed).
* Allows duplicate values.
* Supports indexing and slicing.

---

## Syntax

```python id="tup001"
tuple_name = (value1, value2, value3)
```

---

## Parameters

Tuples do not require parameters for creation.

---

## Return Value

Returns a tuple object.

---

## Internal Working

Tuples store elements in a fixed memory location with ordered indexing. Since they are immutable, Python optimizes them for faster access and lower overhead compared to lists.

---

## Rules

* Use parentheses `()`.
* Index starts from `0`.
* Cannot modify elements.
* Duplicate values are allowed.
* Single element tuple requires a comma.

---

## Types (if applicable)

### 1. Empty Tuple

```python id="tup002"
t = ()

print(t)
```

### 2. Integer Tuple

```python id="tup003"
t = (1, 2, 3)

print(t)
```

### 3. Mixed Tuple

```python id="tup004"
t = (10, "Jack", 3.5, True)

print(t)
```

### 4. Single Element Tuple

```python id="tup005"
t = (10,)

print(t)
```

---

## Advantages

* Faster than lists.
* Immutable (data protection).
* Can be used as dictionary keys.
* Memory efficient.

---

## Disadvantages

* Cannot be modified.
* No add/remove operations.
* Less flexible than lists.

---

## Time Complexity

| Operation | Complexity |
| --------- | ---------- |
| Access    | O(1)       |
| Search    | O(n)       |

---

## Space Complexity

**O(n)**

---

# Examples

## Example 1 (Basic)

```python id="tup006"
t = (1, 2, 3)

print(t)
```

### Output

```text id="tup007"
(1, 2, 3)
```

---

## Example 2 (Accessing Elements)

```python id="tup008"
t = (10, 20, 30)

print(t[1])
```

### Output

```text id="tup009"
20
```

---

## Example 3 (Interview)

```python id="tup010"
t = (5, 10, 15)

print(len(t))
```

### Output

```text id="tup011"
3
```

---

## Example 4 (Real-world)

```python id="tup012"
coordinates = (12.5, 45.8)

print(coordinates)
```

### Output

```text id="tup013"
(12.5, 45.8)
```

---

## Common Errors

| Error      | Reason                 | Solution          |
| ---------- | ---------------------- | ----------------- |
| TypeError  | Trying to modify tuple | Use list instead  |
| IndexError | Invalid index          | Use correct index |

---

## Common Mistakes

* Confusing tuple with list.
* Forgetting comma for single-element tuple.
* Trying to modify tuple values.

---

## Difference Table

| Tuple      | List         |
| ---------- | ------------ |
| Immutable  | Mutable      |
| Uses `()`  | Uses `[]`    |
| Faster     | Slower       |
| Fixed data | Dynamic data |

---

## Interview Questions

**Q1. What is a tuple?**

An ordered and immutable collection of elements.

**Q2. Can tuples be changed?**

No.

**Q3. Why use tuples?**

For fixed and secure data storage.

---

## MCQs

**1. Tuples are**

A. Mutable
B. Immutable ✅
C. Dynamic
D. Random

---

**2. Which brackets are used for tuples?**

A. `{}`
B. `[]`
C. `()` ✅
D. `<>`

---

**3. Can tuples be modified?**

A. Yes
B. No ✅
C. Sometimes
D. Only integers

---

## Practice Questions

1. What is a tuple?
2. Create a tuple with 5 elements.
3. Access tuple elements.
4. Difference between tuple and list.
5. Why are tuples immutable?

---

## Summary

* Tuple is an ordered collection.
* It is immutable.
* Allows duplicate values.
* Used for fixed data storage.

---

## Keywords

Tuple, Immutable, Ordered, Indexing, Sequence

---

## Related Topics

* List
* Set
* Dictionary
* Tuple Methods
* Data Structures
