# Lambda

## Definition

A **Lambda function** is a small anonymous function defined using the `lambda` keyword. It can have multiple inputs but only one expression.

---

## Why do we use it?

* To write short functions.
* To reduce code length.
* To use with `map()`, `filter()`, `sorted()`.
* For quick operations.

---

## Key Points

* No function name.
* Defined using `lambda`.
* Can take multiple arguments.
* Only one expression allowed.

---

## Syntax

```python id="l1"
lambda arguments: expression
```

---

## Parameters

| Part       | Description      |
| ---------- | ---------------- |
| lambda     | Keyword          |
| arguments  | Input values     |
| expression | Single operation |

---

## Return Value

Returns the result of the expression automatically.

---

## Internal Working

Python evaluates the expression and returns the result without requiring a `return` statement.

---

## Rules

* Only one expression allowed.
* Cannot use multiple statements.
* No return keyword needed.

---

## Types (if applicable)

### 1. Simple lambda

```python id="l2"
add = lambda a, b: a + b

print(add(5, 3))
```

---

### 2. Lambda with filter

```python id="l3"
nums = [1, 2, 3, 4]

even = filter(lambda x: x % 2 == 0, nums)

print(list(even))
```

---

## Advantages

* Short and concise.
* Useful for simple logic.
* Works well with functional programming.

---

## Disadvantages

* Hard to read for complex logic.
* Only single expression allowed.

---

## Time Complexity

Depends on usage.

---

## Space Complexity

**O(1)** (for simple operations)

---

## Summary

* Lambda functions are anonymous functions.
* Defined using `lambda`.
* Used for short operations.

---

## Keywords

lambda, anonymous function, expression, filter, map

---

## Related Topics

* Functions
* Map
* Filter
* Recursion
