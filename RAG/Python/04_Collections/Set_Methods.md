# Set Methods

## Definition

**Set Methods** are built-in functions used to add, remove, update, and perform mathematical operations on sets.

---

## Why do we use it?

* To add or remove elements.
* To perform set operations.
* To check relationships between sets.
* To manage unique values.

---

## Key Points

* Sets are mutable.
* Duplicate values are not allowed.
* Methods are called using the dot (`.`) operator.
* Some methods return a new set, while others modify the original.

---

## Syntax

```python
set_name.method()
```

---

## Parameters

| Method                   | Description               |
| ------------------------ | ------------------------- |
| `add()`                  | Adds one element          |
| `update()`               | Adds multiple elements    |
| `remove()`               | Removes an element        |
| `discard()`              | Removes an element safely |
| `pop()`                  | Removes a random element  |
| `clear()`                | Removes all elements      |
| `copy()`                 | Creates a shallow copy    |
| `union()`                | Combines sets             |
| `intersection()`         | Finds common elements     |
| `difference()`           | Finds different elements  |
| `symmetric_difference()` | Finds uncommon elements   |

---

## Return Value

Returns a set, element, or `None` depending on the method.

---

## Internal Working

Python performs operations using a hash table, making most set operations very fast.

---

## Rules

* Duplicate values are ignored.
* Elements must be immutable.
* `remove()` raises an error if the element is missing.
* `discard()` does not raise an error.

---

## Types (if applicable)

### 1. Add Methods

```python
fruits = {"Apple", "Mango"}

fruits.add("Orange")
fruits.update(["Banana", "Grapes"])

print(fruits)
```

### 2. Remove Methods

```python
fruits = {"Apple", "Mango", "Orange"}

fruits.remove("Orange")
fruits.discard("Apple")

print(fruits)
```

### 3. Set Operations

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))
print(a.intersection(b))
```

---

## Advantages

* Fast operations.
* Removes duplicates automatically.
* Useful for mathematical set operations.
* Easy to manage unique data.

---

## Disadvantages

* Elements are unordered.
* No indexing.
* Duplicate values are not stored.

---

## Time Complexity

| Method           | Complexity       |
| ---------------- | ---------------- |
| `add()`          | **O(1)**         |
| `remove()`       | **O(1)**         |
| `discard()`      | **O(1)**         |
| `pop()`          | **O(1)**         |
| `union()`        | **O(n)**         |
| `intersection()` | **O(min(n, m))** |

---

## Space Complexity

**O(n)**

---

# Examples

## Example 1 (Basic)

### Code

```python
numbers = {1, 2, 3}

numbers.add(4)

print(numbers)
```

### Output

```text
{1, 2, 3, 4}
```

### Explanation

Adds an element to the set.

---

## Example 2 (Intermediate)

### Code

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))
```

### Output

```text
{1, 2, 3, 4, 5}
```

### Explanation

Combines both sets.

---

## Example 3 (Interview)

### Code

```python
a = {1, 2, 3}
b = {2, 3, 4}

print(a.intersection(b))
```

### Output

```text
{2, 3}
```

### Explanation

Returns common elements.

---

## Example 4 (Real-world)

### Code

```python
visited = {"India", "Japan"}

visited.add("Canada")

print(visited)
```

### Output

```text
{'India', 'Japan', 'Canada'}
```

### Explanation

Stores unique visited countries.

---

## Common Errors

| Error     | Reason                                | Solution                       |
| --------- | ------------------------------------- | ------------------------------ |
| KeyError  | Using `remove()` on a missing element | Use `discard()` or check first |
| TypeError | Mutable object added                  | Use immutable elements         |

---

## Common Mistakes

* Expecting sets to maintain order.
* Using indexing.
* Confusing `remove()` with `discard()`.
* Adding duplicate values.

---

## Difference Table

| Method           | Purpose               |
| ---------------- | --------------------- |
| `add()`          | Add one element       |
| `update()`       | Add multiple elements |
| `remove()`       | Remove element        |
| `discard()`      | Safe remove           |
| `pop()`          | Remove random element |
| `union()`        | Combine sets          |
| `intersection()` | Common elements       |
| `difference()`   | Different elements    |

---

## Interview Questions

**Q1. Which method safely removes an element?**

`discard()`

**Q2. Which method combines two sets?**

`union()`

**Q3. Which method returns common elements?**

`intersection()`

---

## MCQs

**1. Which method adds one element to a set?**

A. `append()`

B. `add()` ✅

C. `insert()`

D. `push()`

---

**2. Which method removes an element without raising an error?**

A. `remove()`

B. `discard()` ✅

C. `delete()`

D. `pop()`

---

**3. Which method finds common elements?**

A. `union()`

B. `intersection()` ✅

C. `difference()`

D. `update()`

---

## Practice Questions

1. What are set methods?
2. Add elements using `add()` and `update()`.
3. Explain the difference between `remove()` and `discard()`.
4. Find the union of two sets.
5. Find the intersection of two sets.

---

## Real-world Applications

* Removing duplicates
* Student attendance
* Database operations
* Data analysis
* Membership testing

---

## Notes

**Remember:** Sets store **unique** values only.

**Shortcut:**

* `add()` → Add one
* `update()` → Add many
* `remove()` → Remove
* `discard()` → Safe remove
* `union()` → Combine
* `intersection()` → Common

**Interview Tip:** `discard()` is safer than `remove()`.

**Exam Tip:** Learn all basic set methods and set operations.

---

## Summary

* Set methods help add, remove, and manipulate unique elements.
* Common methods include `add()`, `update()`, `remove()`, `discard()`, `union()`, and `intersection()`.
* Sets automatically remove duplicate values.
* They are widely used for mathematical operations and fast lookups.

---

## Keywords

Set Methods, add(), update(), remove(), discard(), union(), intersection(), difference(), pop(), Hash Table

---

## Related Topics

* Set
* Dictionary
* Hash Table
* List
* Tuple
