# Dictionary

## Definition

A **Dictionary** is a collection of **key-value pairs**. It is mutable, ordered, and stores data using unique keys.

---

## Why do we use it?

* To store data in key-value pairs.
* To retrieve values quickly.
* To organize related information.
* To represent real-world objects.

---

## Key Points

* Created using `{}`.
* Stores data as `key: value`.
* Keys must be unique.
* Dictionaries are mutable.
* Values can be of any data type.

---

## Syntax

```python
dictionary = {
    "key": value
}
```

---

## Parameters

| Part    | Description                  |
| ------- | ---------------------------- |
| `key`   | Unique identifier            |
| `value` | Data associated with the key |

---

## Return Value

Returns a dictionary object.

---

## Internal Working

Python stores dictionaries using a **hash table**, allowing fast access to values using keys.

---

## Rules

* Keys must be unique.
* Keys must be immutable.
* Values can be duplicated.
* Dictionaries are mutable.

---

## Types (if applicable)

### 1. Empty Dictionary

```python
data = {}

print(data)
```

### 2. Dictionary with Values

```python
student = {
    "name": "Jack",
    "age": 20
}

print(student)
```

### 3. Nested Dictionary

```python
student = {
    "name": "Jack",
    "marks": {
        "Python": 95
    }
}

print(student)
```

---

## Advantages

* Fast searching.
* Easy to update.
* Stores related data together.
* Flexible data types.

---

## Disadvantages

* Keys must be unique.
* Uses more memory than lists.
* Cannot use mutable objects as keys.

---

## Time Complexity

| Operation | Complexity |
| --------- | ---------- |
| Access    | **O(1)**   |
| Insert    | **O(1)**   |
| Update    | **O(1)**   |
| Delete    | **O(1)**   |

---

## Space Complexity

**O(n)**

---

# Examples

## Example 1 (Basic)

### Code

```python
student = {
    "name": "Jack",
    "age": 20
}

print(student)
```

### Output

```text
{'name': 'Jack', 'age': 20}
```

### Explanation

Creates and prints a dictionary.

---

## Example 2 (Intermediate)

### Code

```python
student = {
    "name": "Jack",
    "age": 20
}

print(student["name"])
```

### Output

```text
Jack
```

### Explanation

Accesses a value using its key.

---

## Example 3 (Interview)

### Code

```python
student = {
    "name": "Jack"
}

student["city"] = "London"

print(student)
```

### Output

```text
{'name': 'Jack', 'city': 'London'}
```

### Explanation

Adds a new key-value pair.

---

## Example 4 (Real-world)

### Code

```python
employee = {
    "id": 101,
    "name": "Jack",
    "salary": 50000
}

print(employee["salary"])
```

### Output

```text
50000
```

### Explanation

Retrieves an employee's salary using the key.

---

## Common Errors

| Error     | Reason             | Solution                                    |
| --------- | ------------------ | ------------------------------------------- |
| KeyError  | Key does not exist | Use an existing key or `get()`              |
| TypeError | Mutable key used   | Use immutable keys like strings or integers |

---

## Common Mistakes

* Using duplicate keys.
* Forgetting quotes around string keys.
* Accessing a missing key.
* Confusing keys with values.

---

## Difference Table

| Dictionary      | List                     |
| --------------- | ------------------------ |
| Key-value pairs | Indexed elements         |
| Uses `{}`       | Uses `[]`                |
| Access by key   | Access by index          |
| Keys are unique | Duplicate values allowed |

---

## Interview Questions

**Q1. What is a dictionary?**

A collection of key-value pairs.

**Q2. Are dictionaries mutable?**

Yes.

**Q3. Can dictionary keys be duplicated?**

No.

---

## MCQs

**1. Which brackets are used to create a dictionary?**

A. `[]`

B. `()`

C. `{}` ✅

D. `<>`

---

**2. Dictionary stores data as**

A. Values only

B. Key-value pairs ✅

C. Indexes

D. Characters

---

**3. Dictionary keys must be**

A. Duplicate

B. Unique ✅

C. Mutable

D. Lists

---

## Practice Questions

1. What is a dictionary?
2. Create a dictionary of student details.
3. Access a value using a key.
4. Add a new key-value pair.
5. Explain why keys must be unique.

---

## Real-world Applications

* Student records
* Employee information
* Product details
* JSON data
* Configuration settings

---

## Notes

**Remember:** Dictionaries store **key-value pairs**.

**Shortcut:**

* `{}` → Dictionary
* `key:value` → Pair
* `dict[key]` → Access value

**Interview Tip:** Dictionaries use a hash table for fast lookup.

**Exam Tip:** Learn creating, accessing, updating, and deleting dictionary items.

---

## Summary

* A dictionary stores data as key-value pairs.
* Keys are unique and immutable.
* Dictionaries are mutable.
* Access values using their keys.

---

## Keywords

Dictionary, Key, Value, Hash Table, Mutable, Key-Value Pair, Mapping

---

## Related Topics

* Lists
* Tuples
* Sets
* Shallow Copy
* Deep Copy
