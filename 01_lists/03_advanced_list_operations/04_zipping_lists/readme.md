# Python Program:🔗 Zip two lists `[1, 2, 3]` and `['a', 'b', 'c']` into a list of tuples and print the result.

## Description:
This program demonstrates how to combine two lists into a single list of tuples using Python's built-in `zip()` function.

## Code:
```python
# Python Program: Zip Two Lists into a List of Tuples

# Two lists to be zipped
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']

# Zipping the lists into a list of tuples
zipped_list = list(zip(numbers, letters))

# Print the resulting list of tuples
print("Zipped List:", zipped_list)    #output: [(1, 'a'), (2, 'b'), (3, 'c')]
