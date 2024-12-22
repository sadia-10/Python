# 1️⃣ Basic Function: 
def greet():
    """Prints a welcome message."""
    print("Hello, Sadia! Welcome to Python Functions 🎉")

# Usage:
greet()

 #Output:Hello, Sadia! Welcome to Python Functions 🎉


# 2️⃣ Function with Parameters:
def multiply(a, b):
    """Multiplies two numbers and returns the result."""
    return a * b

# Usage:
result = multiply(4, 5)
print("Multiplication result:", result)

# Output:Multiplication result: 20


# 3️⃣ Default Parameters:
def greet_user(name="Sadia", age=18):
    """Greets a user with their name and age."""
    print(f"Hello! My name is {name}, and I am {age} years old.")

# Usage:
greet_user()  # Uses default values
greet_user("Ali", 25)  # Custom values


#output: 
#Hello! My name is Sadia, and I am 18 years old.
#Hello! My name is Ali, and I am 25 years old.


# 4️⃣ Returning Multiple Values:
def calculate(a, b):
    """Returns the sum and difference of two numbers."""
    return a + b, a - b

# Usage:
sum_result, diff_result = calculate(10, 4)
print("Sum:", sum_result)
print("Difference:", diff_result)

#Output:
#Sum: 14
#Difference: 6


# 5️⃣ Using Lambda Functions:
square = lambda x: x ** 2

# Usage:
print("Square of 7:", square(7))

#output: Square of 7: 49


#  Variable Scope:
x = 10  # Global variable

def example():
    x = 5  # Local variable
    print("Local x:", x)

example()
print("Global x:", x)


# Output:
#Local x: 5
#Global x: 10


# 3. Recursive Functions:
def factorial(n):
    """Returns the factorial of a number."""
    if n == 1:
        return 1
    return n * factorial(n - 1)

# Usage:
print("Factorial of 5:", factorial(5))

#output: Factorial of 5: 120