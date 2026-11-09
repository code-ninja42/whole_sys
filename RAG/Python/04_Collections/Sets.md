# Set

## Definition

A **Set** is an unordered, mutable collection of **unique** elements. Duplicate values are automatically removed.

---

## Why do we use it?

* To store unique values.
* To remove duplicates.
* To perform mathematical set operations.
* For fast searching.

---

## Key Points

* Created using `{}` or `set()`.
* Duplicate values are not allowed.
* Unordered collection.
* Mutable.
* Supports set operations.

---

## Syntax

```python
set_name = {1, 2, 3}
```

or

```python
set_name = set()
```

---

## Parameters

Sets do not require parameters while creating them.

---

## Return Value

Returns a set object.

---

## Internal Working

Python stores sets using a **hash table**, allowing fast insertion, deletion, and searching.

---

## Rules

* Duplicate values are removed.
* Elements must be immutable.
* No indexing or slicing.
* Order is not guaranteed.

---

## Types (if applicable)

### 1. Empty Set

```python
numbers = set()

print(numbers)
```

### 2. Integer Set

```python
numbers = {1, 2, 3}

print(numbers)
```

### 3. Mixed Set

```python
data = {10, "Jack", 3.5, True}

print(data)
```

---

## Advantages

* Removes duplicates automatically.
* Fast searching.
* Supports mathematical operations.
* Efficient for membership testing.

---

## Disadvantages

* Unordered.
* No indexing.
* Cannot store mutable objects.

---

## Time Complexity

| Operation | Complexity |
| --------- | ---------- |
| Add       | **O(1)**   |
| Remove    | **O(1)**   |
| Search    | **O(1)**   |

---

## Space Complexity

**O(n)**

---

# Examples

## Example 1 (Basic)

### Code

```python
fruits = {"Apple", "Mango", "Orange"}

print(fruits)
```

### Output

```text
{'Apple', 'Mango', 'Orange'}
```

### Explanation

Creates and prints a set.

---

## Example 2 (Intermediate)

### Code

```python
numbers = {1, 2, 2, 3, 3}

print(numbers)
```

### Output

```text
{1, 2, 3}
```

### Explanation

Duplicate values are removed automatically.

---

## Example 3 (Interview)

### Code

```python
numbers = {10, 20, 30}

print(20 in numbers)
```

### Output

```text
True
```

### Explanation

Checks whether an element exists in the set.

---

## Example 4 (Real-world)

### Code

```python
emails = {"jack@gmail.com", "alice@gmail.com", "jack@gmail.com"}

print(emails)
```

### Output

```text
{'jack@gmail.com', 'alice@gmail.com'}
```

### Explanation

Stores only unique email addresses.

---

## Common Errors

| Error     | Reason                   | Solution               |
| --------- | ------------------------ | ---------------------- |
| TypeError | Mutable object added     | Use immutable elements |
| KeyError  | Removing missing element | Use `discard()`        |

---

## Common Mistakes

* Expecting sets to maintain order.
* Using indexing.
* Adding duplicate values.
* Using lists as set elements.

---

## Difference Table

| Set           | List                     |
| ------------- | ------------------------ |
| Unique values | Duplicate values allowed |
| Unordered     | Ordered                  |
| No indexing   | Indexing supported       |
| Uses `{}`     | Uses `[]`                |

---

## Interview Questions

**Q1. What is a set?**

A collection of unique elements.

**Q2. Are duplicate values allowed?**

No.

**Q3. Are sets ordered?**

No.

---

## MCQs

**1. Which data structure stores only unique values?**

A. List

B. Tuple

C. Set ✅

D. String

---

**2. Which function creates an empty set?**

A. `{}`

B. `set()` ✅

C. `[]`

D. `()`

---

**3. Can sets be indexed?**

A. Yes

B. No ✅

C. Sometimes

D. Only integers

---

## Practice Questions

1. What is a set?
2. Create a set of five numbers.
3. Explain why duplicates are removed.
4. Differentiate between a list and a set.
5. Why can't sets be indexed?

---

## Real-world Applications

* Removing duplicate data
* Student attendance
* Database operations
* Membership testing
* Data analysis

---

## Notes

**Remember:** Sets store **unique** values only.

**Shortcut:**

* `{}` → Set
* `set()` → Empty set
* No duplicates
* No indexing

**Interview Tip:** Python sets use hash tables internally.

**Exam Tip:** Learn set properties and common operations.

---

## Summary

* A set stores unique elements.
* Duplicate values are removed automatically.
* Sets are mutable and unordered.
* Used for fast searching and removing duplicates.

---

## Keywords

Set, Unique Elements, Hash Table, Mutable, Unordered, Membership Testing

---

## Related Topics

* Set Methods
* Dictionary
* Hash Table
* List
* Tuple
