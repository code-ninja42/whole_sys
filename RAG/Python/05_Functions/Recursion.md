# Recursion

## Definition

**Recursion** is a technique where a function calls itself to solve a problem.

---

## Why do we use it?

* To solve complex problems easily.
* To break problems into smaller sub-problems.
* Used in tree and graph problems.
* Useful in mathematical computations.

---

## Key Points

* Function calls itself.
* Must have a base condition.
* Uses stack memory.
* Can replace loops in some cases.

---

## Syntax

```python id="r1"
def function():
    if condition:
        return
    function()
```

---

## Parameters

Depends on function definition.

---

## Return Value

Returns value when base condition is met.

---

## Internal Working

Each function call is stored in the call stack. When base condition is reached, stack starts unwinding.

---

## Rules

* Must have a base case.
* Without base case → infinite recursion.
* Each call reduces problem size.

---

## Types (if applicable)

### 1. Direct recursion

```python id="r2"
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
```

---

### 2. Indirect recursion

```python id="r3"
def A(n):
    if n > 0:
        B(n - 1)

def B(n):
    if n > 0:
        A(n - 1)

A(3)
```

---

## Advantages

* Simple for mathematical problems.
* Reduces code complexity.
* Useful for trees and graphs.

---

## Disadvantages

* Uses more memory.
* Can cause stack overflow.
* Slower than loops sometimes.

---

## Time Complexity

Depends on problem (often O(n)).

---

## Space Complexity

O(n) due to call stack.

---

## Summary

* Recursion is function calling itself.
* Requires base condition.
* Useful for divide-and-conquer problems.

---

## Keywords

recursion, function call, base case, stack, factorial

---

## Related Topics

* Functions
* Stack
* Loops
* Tree
