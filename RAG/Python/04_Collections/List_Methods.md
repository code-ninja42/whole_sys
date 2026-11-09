# List Methods

## Definition

**List Methods** are built-in functions used to add, remove, search, sort, and modify elements in a list.

---

## Why do we use it?

* To add elements.
* To remove elements.
* To sort data.
* To search and count elements.
* To modify lists easily.

---

## Key Points

* Lists are mutable.
* Methods modify the original list.
* Called using the dot (`.`) operator.
* Most methods return `None`.

---

## Syntax

```python
list.method()
```

---

## Parameters

| Method      | Description                            |
| ----------- | -------------------------------------- |
| `append()`  | Adds an element at the end             |
| `extend()`  | Adds multiple elements                 |
| `insert()`  | Inserts an element at a specific index |
| `remove()`  | Removes the first matching element     |
| `pop()`     | Removes an element by index            |
| `clear()`   | Removes all elements                   |
| `index()`   | Returns the index of an element        |
| `count()`   | Counts occurrences of an element       |
| `sort()`    | Sorts the list                         |
| `reverse()` | Reverses the list                      |
| `copy()`    | Creates a shallow copy                 |

---

## Return Value

Returns `None` for most methods. Some methods like `pop()`, `index()`, and `count()` return a value.

---

## Internal Working

Python updates the list in memory by adding, deleting, or rearranging elements.

---

## Rules

* Index must be valid for `insert()` and `pop()`.
* `remove()` deletes only the first occurrence.
* `sort()` works when elements are comparable.
* `copy()` creates a shallow copy.

---

## Types (if applicable)

### 1. Add Methods

```python
numbers = [10, 20]

numbers.append(30)
numbers.extend([40, 50])
numbers.insert(1, 15)

print(numbers)
```

### 2. Remove Methods

```python
numbers = [10, 20, 30]

numbers.remove(20)
numbers.pop()

print(numbers)
```

### 3. Search Methods

```python
numbers = [10, 20, 20, 30]

print(numbers.index(20))
print(numbers.count(20))
```

### 4. Sort and Reverse

```python
numbers = [5, 2, 8, 1]

numbers.sort()
numbers.reverse()

print(numbers)
```

---

## Advantages

* Easy to modify lists.
* Saves coding time.
* Built-in and efficient.
* Improves readability.

---

## Disadvantages

* Some methods modify the original list.
* `sort()` cannot compare incompatible data types.

---

## Time Complexity

| Method      | Complexity                         |
| ----------- | ---------------------------------- |
| `append()`  | **O(1)**                           |
| `insert()`  | **O(n)**                           |
| `remove()`  | **O(n)**                           |
| `pop()`     | **O(1)** (last), **O(n)** (middle) |
| `sort()`    | **O(n log n)**                     |
| `reverse()` | **O(n)**                           |
| `count()`   | **O(n)**                           |
| `index()`   | **O(n)**                           |

---

## Space Complexity

**O(n)**

---

# Examples

## Example 1 (Basic)

### Code

```python
fruits = ["Apple", "Mango"]

fruits.append("Orange")

print(fruits)
```

### Output

```text
['Apple', 'Mango', 'Orange']
```

### Explanation

Adds an element to the end of the list.

---

## Example 2 (Intermediate)

### Code

```python
numbers = [5, 2, 8, 1]

numbers.sort()

print(numbers)
```

### Output

```text
[1, 2, 5, 8]
```

### Explanation

Sorts the list in ascending order.

---

## Example 3 (Interview)

### Code

```python
numbers = [10, 20, 30]

print(numbers.pop())
print(numbers)
```

### Output

```text
30
[10, 20]
```

### Explanation

Removes and returns the last element.

---

## Example 4 (Real-world)

### Code

```python
students = ["Jack", "Alice"]

students.append("John")

print(students)
```

### Output

```text
['Jack', 'Alice', 'John']
```

### Explanation

Adds a new student to the class list.

---

## Common Errors

| Error      | Reason                          | Solution                    |
| ---------- | ------------------------------- | --------------------------- |
| IndexError | Invalid index in `pop()`        | Use a valid index           |
| ValueError | Element not found in `remove()` | Check if the element exists |

---

## Common Mistakes

* Confusing `append()` and `extend()`.
* Forgetting that `sort()` modifies the original list.
* Using invalid indexes.
* Assuming `remove()` removes all occurrences.

---

## Difference Table

| Method      | Purpose               |
| ----------- | --------------------- |
| `append()`  | Add one element       |
| `extend()`  | Add multiple elements |
| `insert()`  | Insert at index       |
| `remove()`  | Remove by value       |
| `pop()`     | Remove by index       |
| `sort()`    | Sort list             |
| `reverse()` | Reverse list          |
| `copy()`    | Shallow copy          |

---

## Interview Questions

**Q1. Which method adds one element to the end of a list?**

`append()`

**Q2. Which method removes and returns an element?**

`pop()`

**Q3. Which method sorts a list?**

`sort()`

---

## MCQs

**1. Which method adds one element at the end?**

A. `extend()`

B. `append()` ✅

C. `insert()`

D. `add()`

---

**2. Which method removes the first matching element?**

A. `pop()`

B. `remove()` ✅

C. `clear()`

D. `delete()`

---

**3. Which method counts occurrences?**

A. `index()`

B. `count()` ✅

C. `find()`

D. `search()`

---

## Practice Questions

1. What are list methods?
2. Write a program using `append()`.
3. Explain the difference between `append()` and `extend()`.
4. Remove an element using `remove()`.
5. Sort a list using `sort()`.

---

## Real-world Applications

* Student records
* Shopping carts
* Task management
* Inventory systems
* Data processing

---

## Notes

**Remember:** Lists are **mutable**, so most methods modify the original list.

**Shortcut:**

* `append()` → Add one
* `extend()` → Add many
* `insert()` → Insert
* `remove()` → Remove by value
* `pop()` → Remove by index
* `sort()` → Sort
* `reverse()` → Reverse
* `copy()` → Shallow copy

**Interview Tip:** Know the difference between `append()`, `extend()`, and `insert()`.

**Exam Tip:** Practice all commonly used list methods.

---

## Summary

* List methods help add, remove, search, and modify elements.
* Lists are mutable.
* Common methods include `append()`, `extend()`, `insert()`, `remove()`, `pop()`, `sort()`, `reverse()`, and `copy()`.
* They simplify list operations.

---

## Keywords

List Methods, append(), extend(), insert(), remove(), pop(), sort(), reverse(), copy(), count(), index()

---

## Related Topics

* Lists
* Shallow Copy
* Deep Copy
* Slicing
* Loops
