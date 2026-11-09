# Filters

## Definition

A **filter** is a function used to select elements from a sequence based on a condition.

---

## Why do we use it?

* To filter data from lists.
* To remove unwanted elements.
* To simplify loops.
* To apply conditions efficiently.

---

## Key Points

* Uses `filter()` function.
* Works with functions and iterables.
* Returns a filter object.
* Needs conversion to list.

---

## Syntax

```python id="flt001"
filter(function, iterable)
```

---

## Parameters

| Parameter | Description        |
| --------- | ------------------ |
| function  | Condition function |
| iterable  | List or sequence   |

---

## Return Value

Returns a filter object (iterator).

---

## Internal Working

`filter()` applies a function to each element and keeps only those that return `True`.

---

## Rules

* Function must return True/False.
* Iterable must be provided.
* Convert result using `list()`.

---

## Types (if applicable)

### 1. Filter even numbers

```python id="flt002"
nums = [1, 2, 3, 4, 5]

result = filter(lambda x: x % 2 == 0, nums)

print(list(result))
```

---

## Advantages

* Reduces loops.
* Clean and readable.
* Efficient processing.

---

## Disadvantages

* Requires function or lambda.
* Output must be converted.

---

## Time Complexity

**O(n)**

---

## Space Complexity

**O(n)**

---

## Summary

* `filter()` selects elements based on condition.
* Returns iterator.
* Used with lambda or function.

---

## Keywords

filter(), lambda, iterable, condition, iterator

---

## Related Topics

* Functions
* Map
* Lambda
* Loops
