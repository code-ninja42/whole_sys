# Return

## Definition

The `return` statement is used in a function to send back a value to the caller.

---

## Why do we use it?

* To get output from a function.
* To stop function execution.
* To pass computed values back.
* To make functions reusable.

---

## Key Points

* Used inside functions.
* Ends function execution.
* Can return multiple values.
* Without return → returns `None`.

---

## Syntax

```python id="rt1"
def function():
    return value
```

---

## Parameters

Not applicable (it is a statement, not a function).

---

## Return Value

Returns the value specified after `return`.

---

## Internal Working

When Python encounters `return`, it exits the function and sends the value back to the calling expression.

---

## Rules

* Can only be used inside functions.
* Only one return executes at a time.
* Function stops after return.

---

## Types (if applicable)

### 1. Single return value

```python id="rt2"
def add(a, b):
    return a + b

print(add(5, 3))
```

---

### 2. Multiple return values

```python id="rt3"
def calc(a, b):
    return a + b, a - b

print(calc(10, 5))
```

---

### 3. Return without value

```python id="rt4"
def show():
    return

print(show())
```

---

## Advantages

* Sends output from function.
* Makes functions reusable.
* Helps modular programming.

---

## Disadvantages

* Can make flow harder to track in large functions.
* Improper use may exit function early.

---

## Time Complexity

Depends on function logic.

---

## Space Complexity

Depends on returned data.

---

## Summary

* `return` sends value back from function.
* Stops function execution.
* Essential for functional output.

---

## Keywords

return, function, output, value, exit

---

## Related Topics

* Functions
* Arguments
* Recursion
* Map
