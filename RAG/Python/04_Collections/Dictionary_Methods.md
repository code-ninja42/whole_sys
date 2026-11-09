# Dictionary Methods

## Definition

**Dictionary Methods** are built-in functions used to access, update, remove, copy, and manipulate dictionary data.

---

## Why do we use it?

* To access values safely.
* To add or update data.
* To remove items.
* To copy dictionaries.
* To retrieve keys and values.

---

## Key Points

* Methods are called using the dot (`.`) operator.
* Dictionaries are mutable.
* Some methods return a new object.
* Some methods modify the original dictionary.

---

## Syntax

```python
dictionary.method()
```

---

## Parameters

| Method      | Description             |
| ----------- | ----------------------- |
| `get()`     | Returns value of a key  |
| `keys()`    | Returns all keys        |
| `values()`  | Returns all values      |
| `items()`   | Returns key-value pairs |
| `update()`  | Updates dictionary      |
| `pop()`     | Removes a key           |
| `popitem()` | Removes last item       |
| `clear()`   | Removes all items       |
| `copy()`    | Creates a shallow copy  |

---

## Return Value

Returns a value, list-like view, copied dictionary, or modifies the dictionary depending on the method.

---

## Internal Working

Python performs the requested operation on the dictionary using its hash table structure.

---

## Rules

* Keys must exist for `pop()`.
* `get()` returns `None` if the key is missing.
* `clear()` empties the dictionary.
* `copy()` creates a shallow copy.

---

## Types (if applicable)

### 1. Access Methods

```python
student = {"name": "Jack", "age": 20}

print(student.get("name"))
print(student.keys())
print(student.values())
```

### 2. Update Method

```python
student = {"name": "Jack"}

student.update({"age": 20})

print(student)
```

### 3. Remove Method

```python
student = {"name": "Jack", "age": 20}

student.pop("age")

print(student)
```

### 4. Copy Method

```python
student = {"name": "Jack"}

new_student = student.copy()

print(new_student)
```

---

## Advantages

* Easy to manipulate data.
* Fast access to values.
* Reduces coding effort.
* Improves readability.

---

## Disadvantages

* Some methods modify the original dictionary.
* `copy()` performs only a shallow copy.

---

## Time Complexity

| Method     | Complexity |
| ---------- | ---------- |
| `get()`    | **O(1)**   |
| `update()` | **O(1)**   |
| `pop()`    | **O(1)**   |
| `keys()`   | **O(n)**   |
| `values()` | **O(n)**   |

---

## Space Complexity

**O(n)**

---

# Examples

## Example 1 (Basic)

### Code

```python
student = {"name": "Jack", "age": 20}

print(student.get("name"))
```

### Output

```text
Jack
```

### Explanation

Returns the value of the given key.

---

## Example 2 (Intermediate)

### Code

```python
student = {"name": "Jack"}

student.update({"city": "London"})

print(student)
```

### Output

```text
{'name': 'Jack', 'city': 'London'}
```

### Explanation

Adds a new key-value pair.

---

## Example 3 (Interview)

### Code

```python
student = {"name": "Jack", "age": 20}

student.pop("age")

print(student)
```

### Output

```text
{'name': 'Jack'}
```

### Explanation

Removes the specified key.

---

## Example 4 (Real-world)

### Code

```python
employee = {
    "id": 101,
    "name": "Jack"
}

print(employee.keys())
print(employee.values())
```

### Output

```text
dict_keys(['id', 'name'])
dict_values([101, 'Jack'])
```

### Explanation

Retrieves all keys and values.

---

## Common Errors

| Error          | Reason                   | Solution                      |
| -------------- | ------------------------ | ----------------------------- |
| KeyError       | Key not found in `pop()` | Use `get()` or check the key  |
| AttributeError | Invalid method           | Use a valid dictionary method |

---

## Common Mistakes

* Using `pop()` on a missing key.
* Expecting `copy()` to perform a deep copy.
* Forgetting parentheses after methods.
* Confusing `keys()` and `values()`.

---

## Difference Table

| Method     | Purpose             |
| ---------- | ------------------- |
| `get()`    | Get value           |
| `keys()`   | Get keys            |
| `values()` | Get values          |
| `items()`  | Get key-value pairs |
| `update()` | Update dictionary   |
| `pop()`    | Remove key          |
| `clear()`  | Remove all items    |
| `copy()`   | Shallow copy        |

---

## Interview Questions

**Q1. Which method returns all dictionary keys?**

`keys()`

**Q2. Which method safely accesses a value?**

`get()`

**Q3. Which method removes all dictionary items?**

`clear()`

---

## MCQs

**1. Which method returns dictionary keys?**

A. `values()`

B. `keys()` ✅

C. `items()`

D. `pop()`

---

**2. Which method removes a specific key?**

A. `clear()`

B. `pop()` ✅

C. `copy()`

D. `get()`

---

**3. Which method creates a shallow copy?**

A. `deepcopy()`

B. `copy()` ✅

C. `clone()`

D. `update()`

---

## Practice Questions

1. What are dictionary methods?
2. Write a program using `get()`.
3. Update a dictionary using `update()`.
4. Remove a key using `pop()`.
5. Differentiate between `keys()` and `values()`.

---

## Real-world Applications

* Student management
* Employee records
* Product catalogs
* JSON processing
* Configuration settings

---

## Notes

**Remember:** `get()` is safer than direct indexing because it does not raise a `KeyError`.

**Shortcut:**

* `get()` → Get value
* `keys()` → All keys
* `values()` → All values
* `items()` → Key-value pairs
* `update()` → Update
* `pop()` → Remove
* `clear()` → Empty
* `copy()` → Shallow copy

**Interview Tip:** Know the difference between `get()` and direct indexing.

**Exam Tip:** Learn the most commonly used dictionary methods.

---

## Summary

* Dictionary methods help access and manipulate key-value pairs.
* Common methods include `get()`, `keys()`, `values()`, `items()`, `update()`, `pop()`, `clear()`, and `copy()`.
* Dictionaries are mutable, so many methods modify the original dictionary.
* These methods make dictionary operations simple and efficient.

---

## Keywords

Dictionary Methods, get(), keys(), values(), items(), update(), pop(), clear(), copy(), Hash Table

---

## Related Topics

* Dictionary
* Shallow Copy
* Deep Copy
* Lists
* Tuples
