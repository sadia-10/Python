# Python Program: 🔢 Filter the even numbers from the list `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` using list comprehension.

## Description:
This Python program demonstrates how to filter even numbers from the list `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` using list comprehension. The program filters out only the numbers that are divisible by 2, leaving the even numbers.

## Code:
```python
# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using list comprehension to filter even numbers
even_numbers = [x for x in numbers if x % 2 == 0]

# Printing the list of even numbers
print(even_numbers)     #output: [2, 4, 6, 8, 10]
