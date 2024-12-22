# Python Program:🔄 Create a list comprehension that generates a list of strings where each string is the reverse of the corresponding string in the list `['abc', 'def', 'ghi']`.
# Discription:
This Python program demonstrates how to use list comprehension to generate a new list of strings, where each string is the reverse of the corresponding string from the input list.

For example:

**Input List:** `['abc', 'def', 'ghi']`

**Output List:** `['cba', 'fed', 'ihg']`

This approach is concise and makes use of slicing to reverse strings in a Pythonic way.
# Code:
```
# Define the input list
input_list = ['abc', 'def', 'ghi']

# Use list comprehension to reverse each string in the list
reversed_list = [s[::-1] for s in input_list]

# Print the resulting list of reversed strings
print("Reversed List:", reversed_list)  #output: Reversed List: ['cba', 'fed', 'ihg']



