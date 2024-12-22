# Python Program:📚 Flatten a list of lists `[[1, 2], [3, 4], [5, 6]]` using list comprehension.

# Discription:
This Python program demonstrates how to use `list comprehension` to generate a list of `tuples` where each tuple contains a number and its square. 🌟

The program iterates through a given list of numbers and creates a tuple for each number consisting of:

- **The number itself**
- **Its square**
For example:

Input: `[1, 2, 3]`
Output: `[(1, 1), (2, 4), (3, 9)]`

# Code:
```
# Nested list
nested_list = [[1, 2], [3, 4], [5, 6]]

# Flattening the list
flattened_list = [item for sublist in nested_list for item in sublist]

print(flattened_list)  # Output: [1, 2, 3, 4, 5, 6]

