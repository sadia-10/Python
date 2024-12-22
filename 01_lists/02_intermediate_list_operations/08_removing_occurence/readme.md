# Python Program: 🚫 Remove all occurrences of the value `3` from the list `[1, 3, 5, 3, 7, 3, 9]`.

## Description:
This Python program demonstrates how to remove all occurrences of a specific value (in this case, `3`) from the list `[1, 3, 5, 3, 7, 3, 9]`. The program uses list comprehension to filter out the value `3` and return the updated list.

## Code:
```python
# Original list
numbers = [1, 3, 5, 3, 7, 3, 9]

# Using list comprehension to remove all occurrences of 3
filtered_numbers = [num for num in numbers if num != 3]

# Printing the updated list
print(filtered_numbers)   #output: [1, 5, 7, 9]

