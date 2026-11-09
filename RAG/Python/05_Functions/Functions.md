# Functions

## Definition

A **Function** is a reusable block of code that performs a specific task. It helps reduce repetition and improves modularity.

---

## Why do we use it?

* To reuse code.
* To make programs modular.
* To improve readability.
* To reduce redundancy.

---

## Key Points

* Defined using `def`.
* Can take arguments.
* Can return values.
* Can be reused multiple times.

---

## Syntax

```python id="fn001"
def function_name():
    # code
    pass
```

---

## Parameters

| Part          | Description             |
| ------------- | ----------------------- |
| Function Name | Name of the function    |
| Parameters    | Input values (optional) |
| Return        | Output value (optional) |

---

## Return Value

Returns a value using the `return` statement. If no return is used, returns `None`.

---

## Internal Working

Python stores function definitions in memory and executes them only when called.

---

## Rules

* Must be defined before calling.
* Use `def` keyword.
* Indentation is required.
* Can return multiple values.

---

## Types (if applicable)

### 1. Function without parameters

```python id="fn002"
def greet():
    print("Hello")

greet()
```

### 2. Function with parameters

```python id="fn003"
def add(a, b):
    return a + b

print(add(5, 3))
```

---

## Advantages

* Code reusability.
* Easy debugging.
* Better structure.
* Reduces repetition.

---

## Disadvantages

* Slight overhead.
* Complex if overused.

---

## Time Complexity

Depends on logic inside function.

---

## Space Complexity

Depends on variables used.

---

## Summary

* Functions are reusable blocks of code.
* Defined using `def`.
* Improve modularity and readability.

---

## Keywords

Function, def, return, parameters, reusable code

---

## Related Topics

* Arguments
* Filters
* Loops
