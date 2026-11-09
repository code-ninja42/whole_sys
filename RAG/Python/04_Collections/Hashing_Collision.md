# Hashing Collision

## Definition

A **Hashing Collision** occurs when **two or more different keys produce the same hash value** and are stored at the same location in a hash table.

---

## Why do we use it?

* To understand how hash tables work.
* To handle duplicate hash indexes.
* To improve data retrieval.
* To design efficient data structures.

---

## Key Points

* Different keys can generate the same hash value.
* Collisions are common in hash tables.
* Python dictionaries handle collisions automatically.
* Collision handling improves performance.

---

## Syntax

```python
hash(key)
```

---

## Parameters

| Parameter | Description                    |
| --------- | ------------------------------ |
| `key`     | Value whose hash is calculated |

---

## Return Value

Returns an integer hash value.

---

## Internal Working

Python computes a hash value for each key. If two keys get the same hash location, Python resolves the collision internally using its hash table mechanism.

---

## Rules

* Different keys may have the same hash value.
* Keys should be immutable.
* Python handles collisions automatically.
* Collisions do not mean keys are equal.

---

## Types (if applicable)

### 1. Separate Chaining

Multiple values are stored at the same index using a linked structure.

### 2. Open Addressing

If a collision occurs, Python searches for another empty location.

---

## Advantages

* Enables fast data lookup.
* Efficient storage.
* Automatic collision handling in Python.

---

## Disadvantages

* Too many collisions reduce performance.
* Large hash tables consume more memory.

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

```python
print(hash("Jack"))
```

### Output

```text
123456789
```

### Explanation

Returns the hash value of the string. (The number may differ on different systems.)

---

## Example 2 (Intermediate)

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

Python automatically handles any hash collisions internally.

---

## Example 3 (Interview)

### Code

```python
print(hash(10))
print(hash(20))
```

### Output

```text
10
20
```

### Explanation

Different values usually produce different hash values.

---

## Example 4 (Real-world)

### Code

```python
employee = {
    101: "Jack",
    102: "Alice"
}

print(employee[101])
```

### Output

```text
Jack
```

### Explanation

Hashing allows quick retrieval using keys.

---

## Common Errors

| Error     | Reason                     | Solution                                    |
| --------- | -------------------------- | ------------------------------------------- |
| TypeError | Mutable object used as key | Use immutable keys like strings or integers |
| KeyError  | Key not found              | Check if the key exists                     |

---

## Common Mistakes

* Thinking equal hash values mean equal objects.
* Using mutable objects as dictionary keys.
* Assuming collisions cause data loss.

---

## Difference Table

| Hashing                | Hash Collision                        |
| ---------------------- | ------------------------------------- |
| Generates a hash value | Two keys share the same hash location |
| Fast lookup            | Needs collision handling              |
| Used in dictionaries   | Occurs occasionally                   |

---

## Interview Questions

**Q1. What is a hashing collision?**

When two different keys generate the same hash value.

**Q2. Does Python handle hash collisions automatically?**

Yes.

**Q3. Do collisions cause data loss?**

No.

---

## MCQs

**1. A hashing collision occurs when**

A. Keys are deleted

B. Two keys have the same hash value ✅

C. Values are duplicated

D. Dictionary is empty

---

**2. Python dictionaries are based on**

A. Arrays

B. Linked Lists

C. Hash Tables ✅

D. Trees

---

**3. Which function returns a hash value?**

A. `len()`

B. `type()`

C. `hash()` ✅

D. `id()`

---

## Practice Questions

1. What is a hashing collision?
2. Why do collisions occur?
3. How does Python handle collisions?
4. Explain hash tables.
5. What is the purpose of the `hash()` function?

---

## Real-world Applications

* Python dictionaries
* Python sets
* Database indexing
* Caching systems
* Password storage

---

## Notes

**Remember:** A collision means **different keys map to the same hash location**, not that they are equal.

**Shortcut:**

* `hash()` → Generate hash value
* Same hash location → Collision
* Python → Handles collisions automatically

**Interview Tip:** Python dictionaries use hash tables with built-in collision handling.

**Exam Tip:** Know the definition of hashing collision and its impact on performance.

---

## Summary

* Hashing converts keys into hash values.
* A hashing collision occurs when different keys map to the same location.
* Python dictionaries automatically resolve collisions.
* Excessive collisions can reduce performance.

---

## Keywords

Hashing, Hash Collision, Hash Table, hash(), Dictionary, Key, Collision Resolution

---

## Related Topics

* Dictionary
* Dictionary Methods
* Sets
* Hash Table
* Data Structures
