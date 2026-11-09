# Arguments

## Definition

**Arguments** are values passed to a function when it is called.

---

## Why do we use it?

* To pass data into functions.
* To make functions dynamic.
* To reuse functions with different inputs.

---

## Key Points

* Passed during function call.
* Used inside function parameters.
* Can be multiple types.
* Makes functions flexible.

---

## Syntax

```python id="arg001"
def add(a, b):
    return a + b

add(5, 10)
```

---

## Types of Arguments

### 1. Positional Arguments

```python id="arg002"
def show(name, age):
    print(name, age)

show("Jack", 20)
```

### 2. Keyword Arguments

```python id="arg003"
def show(name, age):
    print(name, age)

show(age=20, name="Jack")
```

### 3. Default Arguments

```python id="arg004"
def show(name="Jack"):
    print(name)

show()
```

### 4. Variable-Length Arguments

```python id="arg005"
def add(*nums):
    return sum(nums)

print(add(1, 2, 3))
```

---

## Advantages

* Makes functions flexible.
* Supports dynamic input.
* Improves reusability.

---

## Disadvantages

* Too many arguments can confuse code.
* Incorrect order may cause errors.

---

## Common Mistakes

* Wrong order in positional arguments.
* Missing required arguments.
* Confusing `*args` and `**kwargs`.

---

## Summary

* Arguments are values passed to functions.
* Types: positional, keyword, default, variable-length.
* Make functions dynamic.

---

## Keywords

Arguments, parameters, *args, keyword arguments, default arguments

---

## Related Topics

* Functions
* Filters
* Loops
