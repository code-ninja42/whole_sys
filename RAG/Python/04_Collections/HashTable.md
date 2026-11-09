# Hash Table

## Definition

A **Hash Table** is a data structure that stores data as **key-value pairs** using a **hash function** for fast insertion, searching, and deletion.

---

## Why do we use it?

* To store key-value pairs.
* To access data quickly.
* To perform fast searching.
* To improve program performance.

---

## Key Points

* Uses a hash function.
* Stores data using keys and values.
* Average lookup time is **O(1)**.
* Python dictionaries and sets use hash tables internally.

---

## Syntax

```python id="r8gk1p"
student = {
    "name": "Jack",
    "age": 20
}
```

---

## Parameters

| Part          | Description                |
| ------------- | -------------------------- |
| Key           | Unique identifier          |
| Value         | Data stored with the key   |
| Hash Function | Converts key into an index |

---

## Return Value

Returns the value associated with the given key.

---

## Internal Working

A hash function converts a key into a hash value. This hash value determines where the key-value pair is stored in the hash table. If two keys map to the same location, a collision occurs and is handled internally.

---

## Rules

* Keys must be unique.
* Keys should be immutable.
* Values can be duplicated.
* Fast access depends on a good hash function.

---

## Types (if applicable)

### 1. Separate Chaining

Stores multiple items at the same index.

### 2. Open Addressing

Searches for another empty location if a collision occurs.

---

## Advantages

* Very fast lookup.
* Fast insertion.
* Fast deletion.
* Efficient for large datasets.

---

## Disadvantages

* Collisions may occur.
* Uses extra memory.
* Performance decreases with many collisions.

---

## Time Complexity

| Operation | Average  | Worst    |
| --------- | -------- | -------- |
| Search    | **O(1)** | **O(n)** |
| Insert    | **O(1)** | **O(n)** |
| Delete    | **O(1)** | **O(n)** |

---

## Space Complexity

**O(n)**

---

# Examples

## Example 1 (Basic)

### Code

```python id="7g3wmt"
student = {
    "name": "Jack",
    "age": 20
}

print(student["name"])
```

### Output

```text id="vrujmv"
Jack
```

### Explanation

Retrieves a value using its key.

---

## Example 2 (Intermediate)

### Code

```python id="uxt4ku"
student = {
    "name": "Jack"
}

student["city"] = "London"

print(student)
```

### Output

```text id="3ty1y2"
{'name': 'Jack', 'city': 'London'}
```

### Explanation

Adds a new key-value pair.

---

## Example 3 (Interview)

### Code

```python id="qqr4tw"
student = {
    "name": "Jack",
    "age": 20
}

print("age" in student)
```

### Output

```text id="6k4ggd"
True
```

### Explanation

Checks whether a key exists.

---

## Example 4 (Real-world)

### Code

```python id="rxc9rj"
products = {
    101: "Laptop",
    102: "Phone"
}

print(products[102])
```

### Output

```text id="aq9zhk"
Phone
```

### Explanation

Retrieves product information quickly using a key.

---

## Common Errors

| Error     | Reason                     | Solution                |
| --------- | -------------------------- | ----------------------- |
| KeyError  | Key not found              | Check if the key exists |
| TypeError | Mutable object used as key | Use immutable keys      |

---

## Common Mistakes

* Using mutable objects as keys.
* Confusing hash tables with lists.
* Assuming collisions cause data loss.

---

## Difference Table

| Hash Table              | List                    |
| ----------------------- | ----------------------- |
| Key-value pairs         | Indexed elements        |
| Fast lookup             | Sequential lookup       |
| Uses hash function      | Uses indexes            |
| Average **O(1)** access | Average **O(n)** search |

---

## Interview Questions

**Q1. What is a hash table?**

A data structure that stores key-value pairs using a hash function.

**Q2. Which Python data structure uses a hash table?**

Dictionary and Set.

**Q3. What is the average lookup time?**

**O(1)**.

---

## MCQs

**1. Which Python data structure uses a hash table?**

A. List

B. Tuple

C. Dictionary ✅

D. String

---

**2. What is the average search time in a hash table?**

A. O(n)

B. O(log n)

C. O(1) ✅

D. O(n²)

---

**3. What converts a key into an index?**

A. Loop

B. Hash Function ✅

C. Variable

D. Array

---

## Practice Questions

1. What is a hash table?
2. Explain the role of a hash function.
3. What is a collision?
4. Why are hash tables fast?
5. Which Python data structures use hash tables?

---

## Real-world Applications

* Python dictionaries
* Python sets
* Database indexing
* Caching
* Password lookup

---

## Notes

**Remember:** A hash table stores **key-value pairs** for very fast access.

**Shortcut:**

* Key + Value → Hash Table
* Hash Function → Index
* Average Search → **O(1)**

**Interview Tip:** Dictionaries and sets in Python are implemented using hash tables.

**Exam Tip:** Learn hash tables, hash functions, and collision handling.

---

## Summary

* A hash table stores key-value pairs.
* It uses a hash function to locate data.
* Average search, insert, and delete operations are **O(1)**.
* Python dictionaries and sets are based on hash tables.

---

## Keywords

Hash Table, Hash Function, Dictionary, Set, Key, Value, Collision, Lookup

---

## Related Topics

* Dictionary
* Dictionary Methods
* Hashing
* Hashing Collision
* Sets
