# Python Program:📄 Split a list `[1, 2, 3, 4, 5, 6, 7, 8]` into two halves and print `both halves`.

## Description:
This Python program demonstrates how to split a list into two equal halves. If the number of elements in the list is even, both halves will have the same number of elements. If the number of elements is odd, the second half will have one more element than the first half.

## Code:
```python
# Python Program: Split a List into Two Halves

# Original list
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# Find the middle index
mid_index = len(numbers) // 2

# Split the list into two halves
first_half = numbers[:mid_index]
second_half = numbers[mid_index:]

# Print both halves
print("First Half:", first_half)     #output: First Half: [1, 2, 3, 4]
print("Second Half:", second_half)   #output: Second Half: [5, 6, 7, 8]
