# Map

## Definition

The `map()` function applies a given function to all items in an iterable and returns a map object.

---

## Why do we use it?

* To transform data.
* To apply operations to all elements.
* To replace loops.
* To process lists efficiently.

---

## Key Points

* Works with functions and iterables.
* Returns a map object.
* Often used with lambda.
* Reduces loop usage.

---

## Syntax

```python id="m1"
map(function, iterable)
```

---

## Parameters

| Parameter | Description       |
| --------- | ----------------- |
| function  | Function to apply |
| iterable  | List, tuple, etc. |

---

## Return Value

Returns a map object (iterator).

---

## Internal Working

Applies the function to each element one by one and stores results lazily.

---

## Rules

* Function must accept one or more arguments.
* Iterable must be provided.
* Convert result using `list()`.

---

## Types (if applicable)

### 1. Square numbers

```python id="m2"
nums = [1, 2, 3, 4]

result = map(lambda x: x * x, nums)

print(list(result))
```

---

### 2. Convert strings to int

```python id="m3"
nums = ["1", "2", "3"]

result = map(int, nums)

print(list(result))
```

---

## Advantages

* Reduces loops.
* Clean and readable.
* Fast for large datasets.

---

## Disadvantages

* Needs conversion to list.
* Less readable for beginners.

---

## Time Complexity

**O(n)**

---

## Space Complexity

**O(n)**

---

## Summary

* `map()` applies function to all items.
* Returns iterator.
* Commonly used with lambda.

---

## Keywords

map(), iterable, lambda, transformation, function

---

## Related Topics

* Lambda
* Filter
* Functions
* Loops
