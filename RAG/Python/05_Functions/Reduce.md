# Reduce

## Definition

`reduce()` is a function from the `functools` module that applies a function cumulatively to the items of an iterable and returns a single value.

---

## Why do we use it?

* To reduce a sequence into a single value.
* To perform cumulative operations.
* To replace loops for aggregation.
* To compute results like sum, product, etc.

---

## Key Points

* Imported from `functools`.
* Works on iterables.
* Returns a single result.
* Applies function repeatedly.

---

## Syntax

```python id="rd1"
from functools import reduce

reduce(function, iterable)
```

---

## Parameters

| Parameter | Description                   |
| --------- | ----------------------------- |
| function  | Function applied cumulatively |
| iterable  | List, tuple, etc.             |

---

## Return Value

Returns a single computed value.

---

## Internal Working

`reduce()` takes the first two elements, applies the function, then uses the result with the next element repeatedly until one value remains.

---

## Rules

* Function must take two arguments.
* Iterable must not be empty (or default needed).
* Requires import from `functools`.

---

## Types (if applicable)

### 1. Sum using reduce

```python id="rd2"
from functools import reduce

nums = [1, 2, 3, 4]

result = reduce(lambda x, y: x + y, nums)

print(result)
```

---

### 2. Product using reduce

```python id="rd3"
from functools import reduce

nums = [1, 2, 3, 4]

result = reduce(lambda x, y: x * y, nums)

print(result)
```

---

## Advantages

* Useful for cumulative operations.
* Reduces need for loops.
* Clean functional approach.

---

## Disadvantages

* Hard to read for beginners.
* Not always necessary (loops are simpler).

---

## Time Complexity

**O(n)**

---

## Space Complexity

**O(1)** (excluding input data)

---

## Summary

* `reduce()` reduces iterable to a single value.
* Uses cumulative function application.
* Part of `functools`.

---

## Keywords

reduce, functools, cumulative, lambda, iterable

---

## Related Topics

* Map
* Filter
* Lambda
* Functions
