# Introduction to Python

---

# Definition

Python is a **high-level**, **interpreted**, **general-purpose**, **dynamically typed**, and **object-oriented** programming language created by **Guido van Rossum** and first released in **1991**. It was designed with the goal of making programming simple, readable, and easy to learn.

Python follows the philosophy of **"Readability Counts"**, which means programs written in Python should be easy for humans to read and understand. Its clean syntax allows developers to focus more on solving problems rather than worrying about complex programming rules.

Python is one of the most popular programming languages in the world and is used in Web Development, Data Science, Machine Learning, Artificial Intelligence, Automation, Cybersecurity, Cloud Computing, Game Development, Desktop Applications, and many other fields.

### Understanding the Terms

### High-Level Language

A **high-level language** is a programming language that is easy for humans to read and write. It uses English-like keywords instead of binary (0s and 1s) or assembly instructions.

**Example**

Instead of writing machine instructions, we simply write:

```python
print("Hello World")
```

The Python Interpreter converts this into machine-understandable instructions.

---

### Interpreted Language

Python is an **interpreted language**, which means the source code is executed **line by line** by the Python Interpreter instead of being converted directly into machine code before execution.

When you run a Python program:

1. Python checks the code for syntax errors.
2. It converts the source code into **Bytecode (.pyc)**.
3. The **Python Virtual Machine (PVM)** executes the bytecode.
4. The output is displayed.

Because execution happens through an interpreter, debugging is easier. However, interpreted languages are generally slower than compiled languages.

---

### General-Purpose Language

A **general-purpose programming language** can be used to develop many different types of applications instead of being limited to one specific area.

Python can be used for:

* Web Development
* Data Science
* Machine Learning
* Artificial Intelligence
* Automation
* Cybersecurity
* Cloud Computing
* Desktop Applications
* Mobile Backends
* APIs
* Robotics
* Game Development

---

### Dynamically Typed Language

Python is a **dynamically typed language**, meaning you do **not** have to declare the data type of a variable.

Python automatically determines the data type while the program is running.

Example:

```python
x = 10
print(type(x))

x = 15.5
print(type(x))

x = "Python"
print(type(x))
```

Output

```
<class 'int'>
<class 'float'>
<class 'str'>
```

The same variable **x** stores an integer, then a float, and finally a string without any explicit type declaration.

---

### Object-Oriented Language

Python supports **Object-Oriented Programming (OOP)**.

Everything in Python is treated as an object. OOP allows developers to organize programs using Classes and Objects, making large applications easier to develop and maintain.

---

# Why do we use Python?

Python is widely used because it combines simplicity with powerful features. Beginners can learn it quickly, while professionals use it to build large-scale applications.

Python is used because it:

* Has simple and readable syntax.
* Requires fewer lines of code than many other languages.
* Is easy to learn for beginners.
* Has thousands of built-in libraries and third-party packages.
* Supports multiple programming paradigms.
* Works on Windows, Linux, and macOS.
* Is free and open source.
* Has a huge global community.
* Is widely used by top technology companies.
* Can be integrated with C, C++, Java, and databases.

---

# Key Points

* Created by **Guido van Rossum**.
* First released in **1991**.
* Current major version is Python 3.
* High-level programming language.
* Interpreted language.
* Dynamically typed.
* Object-oriented.
* Cross-platform.
* Open source.
* Free to use.
* Large Standard Library.
* Supports Functional Programming.
* Supports Procedural Programming.
* Huge developer community.
* One of the most popular programming languages.

---

# Syntax

Python syntax is designed to be simple and readable.

Basic Syntax:

```python
print("Hello, World!")
```

Output

```
Hello, World!
```

Unlike many programming languages, Python does **not** require semicolons (`;`) at the end of statements.

Python uses **indentation (spaces)** instead of curly braces `{}` to define code blocks.

Example:

```python
age = 20

if age >= 18:
    print("Eligible to vote")
```

---

# Parameters

**Not Applicable (N/A)**

This topic is conceptual and does not require parameters.

---

# Return Value

**Not Applicable (N/A)**

This topic explains Python as a programming language and does not return any value.

---

# Internal Working

The execution of a Python program involves several steps.

### Step 1: Write the Source Code

The programmer writes Python code inside a file with the `.py` extension.

Example:

```python
print("Hello")
```

↓

### Step 2: Python Interpreter

The Python Interpreter reads the source code.

↓

### Step 3: Compilation to Bytecode

The interpreter converts the source code into **Bytecode (.pyc)**.

↓

### Step 4: Python Virtual Machine (PVM)

The PVM executes the bytecode instruction by instruction.

↓

### Step 5: Output

The final result is displayed to the user.

---

# Flow Diagram (if applicable)

```text
Python Program (.py)
        │
        ▼
Python Interpreter
        │
        ▼
Bytecode (.pyc)
        │
        ▼
Python Virtual Machine (PVM)
        │
        ▼
Execution
        │
        ▼
Output
```

---

# Rules

* Python is case-sensitive.
* Indentation is mandatory.
* Variables do not require explicit data type declarations.
* Keywords cannot be used as variable names.
* Statements usually end with a new line.
* Follow proper naming conventions.
* Avoid mixing tabs and spaces.
* Use meaningful variable names.
* Follow PEP 8 coding guidelines for better readability.

---

# Types (if applicable)

Python supports multiple programming paradigms.

### 1. Procedural Programming

Programs are written as a sequence of instructions.

### 2. Object-Oriented Programming (OOP)

Programs are built using Classes and Objects.

### 3. Functional Programming

Programs make use of functions as first-class objects and support concepts like lambda functions, map(), filter(), and reduce().

---

# Advantages

* Easy to learn.
* Beginner-friendly syntax.
* Readable code.
* Open source.
* Cross-platform compatibility.
* Huge Standard Library.
* Thousands of third-party packages.
* Large developer community.
* Excellent support for AI and Machine Learning.
* Rapid application development.
* Easy integration with databases.
* Supports automation.
* Strong community support.

---

# Disadvantages

* Slower than compiled languages such as C and C++.
* Higher memory usage.
* Not ideal for mobile application development.
* Global Interpreter Lock (GIL) limits true multithreading.
* Runtime errors can occur because of dynamic typing.
