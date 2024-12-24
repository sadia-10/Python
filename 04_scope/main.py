def my_function():
    x = 10  # Local variable
    print(f"Inside the function, x = {x}")

my_function()
# print(x)  # This will raise an error because x is not accessible outside the function.


# Global Scope Example
x = 20  # Global variable

def my_function():
    print(f"Inside the function, x = {x}")

my_function()
print(f"Outside the function, x = {x}")


x = 30
def update_global():
    global x  # Declare x as global
    x = 50

update_global()
print(f"Updated global x = {x}")


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
