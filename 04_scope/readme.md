# Python Scope Explained with Examples ✨

## Introduction 🚀
In Python, **scope** refers to the region of a program where a particular variable or name is accessible. Understanding scope is crucial for avoiding bugs and ensuring your code behaves as expected.

---

## Types of Scope in Python 🔍

1. **Local Scope**
2. **Global Scope**
3. **Enclosing Scope**
4. **Built-in Scope**

---

## Scope Levels Explained 🎓

### 1. Local Scope ✅
Variables declared inside a function belong to the **local scope** and can only be accessed within that function.

#### Example:
```python
# Local Scope Example
def my_function():
    x = 10  # Local variable
    print(f"Inside the function, x = {x}")

my_function()
# print(x)  # This will raise an error because x is not accessible outside the function.
```

#### How it works:
- `x` is declared inside `my_function`.
- It is accessible only within `my_function`.
- If you try to access `x` outside the function, Python will throw a `NameError`.

---

### 2. Global Scope 🛠️
A variable declared outside of all functions belongs to the **global scope** and is accessible throughout the program.

#### Example:
```python
# Global Scope Example
x = 20  # Global variable

def my_function():
    print(f"Inside the function, x = {x}")

my_function()
print(f"Outside the function, x = {x}")
```

#### How it works:
- `x` is declared outside the function and is accessible both inside and outside `my_function`.
- Modifying a global variable inside a function requires using the `global` keyword.

#### Example of Modification:
```python
x = 30

def update_global():
    global x  # Declare x as global
    x = 50

update_global()
print(f"Updated global x = {x}")
```

---

### 3. Enclosing Scope (Nonlocal) 🌬️
This scope refers to variables in the **outer function** of a nested function. The `nonlocal` keyword allows you to modify variables from the enclosing scope.

#### Example:
```python
# Enclosing Scope Example
def outer_function():
    y = 5

    def inner_function():
        nonlocal y  # Modify the enclosing variable
        y += 1
        print(f"Inside inner_function, y = {y}")

    inner_function()
    print(f"Inside outer_function, y = {y}")

outer_function()
```

#### How it works:
- `y` is declared in `outer_function` and is accessible inside `inner_function`.
- The `nonlocal` keyword is used to modify `y` inside `inner_function`.

---

### 4. Built-in Scope 🎨
This is the scope of Python’s built-in names like `print`, `len`, etc. These are always available unless overridden.

#### Example:
```python
# Built-in Scope Example
print(len("Hello, World!"))  # len is a built-in function
```

#### How it works:
- The `len` function belongs to Python’s built-in scope.
- Built-in functions can be overridden by defining variables or functions with the same name, but this is not recommended.

#### Overriding Example:
```python
# Overriding Built-in Function
len = 42  # Avoid doing this
# print(len("Hello"))  # This will raise an error
```

---

## LEGB Rule 🥇
Python resolves variables using the **LEGB** rule:

1. **Local**: Variables inside the current function.
2. **Enclosing**: Variables in the outer function (if any).
3. **Global**: Variables defined at the top level.
4. **Built-in**: Predefined Python names.

#### Example:
```python
def outer():
    x = "Enclosing"

    def inner():
        x = "Local"
        print(x)  # Local scope is used

    inner()

outer()
```

---

## Summary 🎯
- Use **local variables** for temporary, function-specific tasks.
- Use **global variables** sparingly to avoid conflicts.
- Use **nonlocal** for modifying variables in the enclosing scope.
- Be cautious when overriding **built-in names**.

---


