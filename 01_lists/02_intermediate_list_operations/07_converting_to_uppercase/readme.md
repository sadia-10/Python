# Python Program:🔡 Create a list comprehension that converts all strings in the list `['a', 'b', 'c', 'd']` to `uppercase`.

## Description:
This Python program demonstrates how to use list comprehension to convert all strings in the list `['a', 'b', 'c', 'd']` to uppercase. It iterates over each string in the list and converts it to uppercase using the `upper()` method.

## Code:
```python
# List of strings
letters = ['a', 'b', 'c', 'd']

# Using list comprehension to convert each string to uppercase
uppercase_letters = [letter.upper() for letter in letters]

# Printing the list of uppercase letters
print(uppercase_letters)   #output: ['A', 'B', 'C', 'D']
