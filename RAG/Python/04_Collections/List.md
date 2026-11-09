# List

## Definition

A **List** is an ordered, mutable collection of elements. It can store multiple values of different data types.

---

## Why do we use it?

* To store multiple values.
* To access elements using indexes.
* To modify data easily.
* To perform operations like sorting and searching.

---

## Key Points

* Created using `[]`.
* Lists are mutable.
* Allows duplicate values.
* Supports indexing and slicing.
* Can store different data types.

---

## Syntax

```python
list_name = [value1, value2, value3]
```

---

## Parameters

Lists do not require parameters while creating them.

---

## Return Value

Returns a list object.

---

## Internal Working

Python stores list elements in order. Each element has an index starting from `0`, allowing quick access and modification.

---

## Rules

* Lists use square brackets `[]`.
* Indexing starts from `0`.
* Negative indexing is supported.
* Duplicate values are allowed.
* Lists are mutable.

---

## Types (if applicable)

### 1. Empty List

```python
numbers = []

print(numbers)
```

### 2. Integer List

```python
numbers = [10, 20, 30]

print(numbers)
```

### 3. Mixed List

```python
data = [10, "Jack", 3.5, True]

print(data)
```

### 4. Nested List

```python
matrix = [[1, 2], [3, 4]]

print(matrix)
```

---

## Advantages

* Stores multiple values.
* Easy to modify.
* Supports indexing and slicing.
* Can store mixed data types.

---

## Disadvantages

* Uses more memory.
* Searching is slower than dictionaries.
* Large lists take more time to process.

---

## Time Complexity

| Operation       | Complexity |
| --------------- | ---------- |
| Access          | **O(1)**   |
| Search          | **O(n)**   |
| Insert (End)    | **O(1)**   |
| Insert (Middle) | **O(n)**   |
| Delete          | **O(n)**   |

---

## Space Complexity

**O(n)**

---

# Examples

## Example 1 (Basic)

### Code

```python
fruits = ["Apple", "Mango", "Orange"]

print(fruits)
```

### Output

```text
['Apple', 'Mango', 'Orange']
```

### Explanation

Creates and prints a list.

---

## Example 2 (Intermediate)

### Code

```python
numbers = [10, 20, 30]

print(numbers[1])
```

### Output

```text
20
```

### Explanation

Accesses the element at index `1`.

---

## Example 3 (Interview)

### Code

```python
numbers = [10, 20, 30]

numbers[1] = 50

print(numbers)
```

### Output

```text
[10, 50, 30]
```

### Explanation

Lists are mutable, so elements can be modified.

---

## Example 4 (Real-world)

### Code

```python
students = ["Jack", "Alice", "John"]

print(students[0])
```

### Output

```text
Jack
```

### Explanation

Retrieves the first student's name.

---

## Common Errors

| Error      | Reason            | Solution               |
| ---------- | ----------------- | ---------------------- |
| IndexError | Invalid index     | Use a valid index      |
| TypeError  | Invalid operation | Use correct data types |

---

## Common Mistakes

* Confusing indexing with slicing.
* Using an invalid index.
* Assuming lists are immutable.
* Forgetting square brackets.

---

## Difference Table

| List            | Tuple              |
| --------------- | ------------------ |
| Mutable         | Immutable          |
| Uses `[]`       | Uses `()`          |
| Can be modified | Cannot be modified |
| Slightly slower | Slightly faster    |

---

## Interview Questions

**Q1. What is a list?**

An ordered, mutable collection of elements.

**Q2. Can a list store different data types?**

Yes.

**Q3. Are duplicate values allowed?**

Yes.

---

## MCQs

**1. Which brackets are used for lists?**

A. `{}`

B. `()`

C. `[]` ✅

D. `<>`

---

**2. Lists are**

A. Immutable

B. Mutable ✅

C. Read-only

D. Fixed

---

**3. Indexing starts from**

A. 1

B. -1

C. 0 ✅

D. 2

---

## Practice Questions

1. What is a list?
2. Create a list of five numbers.
3. Access the third element of a list.
4. Modify an element in a list.
5. Explain why lists are mutable.

---

## Real-world Applications

* Student records
* Shopping carts
* To-do lists
* Inventory systems
* Data analysis

---

## Notes

**Remember:** Lists are **ordered** and **mutable**.

**Shortcut:**

* `[]` → List
* `list[index]` → Access element
* `list[start:stop]` → Slice list

**Interview Tip:** Lists allow duplicates and support mixed data types.

**Exam Tip:** Learn indexing, slicing, and common list methods.

---

## Summary

* A list stores multiple values in order.
* Lists are mutable and allow duplicate values.
* Supports indexing, slicing, and built-in methods.
* One of the most commonly used Python data structures.

---

## Keywords

List, Mutable, Ordered, Indexing, Slicing, Duplicate Values, Collection

---

## Related Topics

* List Methods
* Tuple
* Dictionary
* Set
* Slicing
