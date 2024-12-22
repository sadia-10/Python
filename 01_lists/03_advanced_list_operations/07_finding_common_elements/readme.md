# Python Program: 29.🔍 Find the common elements between two lists `[1, 2, 3, 4]` and `[3, 4, 5, 6]` and print the result.

# Discription:
This Python program demonstrates how to find the common elements between two lists. The common elements are those that exist in both lists.

For example:
**Input:**

- List 1: `[1, 2, 3, 4]`
- List 2: `[3, 4, 5, 6]`

**Output:**

- Common Elements: `[3, 4]`
# Code:
```
# Define the two lists
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

# Find common elements using set intersection
common_elements = list(set(list1) & set(list2))

# Print the common elements
print("Common Elements:", common_elements)  #Output:Common Elements: [3, 4]


