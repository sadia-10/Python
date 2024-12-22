# Python Program:  🧮 Create a list comprehension that generates a list of the squares of numbers from `1 to 10`.

## Description:
This Python program demonstrates how to use list comprehension to generate a list of the squares of numbers from 1 to 10. The program uses a concise and efficient way to calculate the square of each number in the given range.

## Code:
```python
# Using list comprehension to generate the squares of numbers from 1 to 10
squares = [x**2 for x in range(1, 11)]

# Printing the list of squares
print(squares)    #output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
