# Python Program: 🔄List Comprehension to Create Tuples of `Numbers and Their Squares`.

## Description:
This Python program demonstrates how to use list comprehension to generate a list of tuples where each tuple contains a number and its square. The program iterates through a given list of numbers and creates a tuple for each number consisting of the number and its square.

## Code:
```python
# List of numbers
numbers = [1, 2, 3, 4, 5]

# Using list comprehension to create a list of tuples (number, square)
number_square_tuples = [(x, x**2) for x in numbers]

# Printing the list of tuples
print(number_square_tuples)   #output: [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
