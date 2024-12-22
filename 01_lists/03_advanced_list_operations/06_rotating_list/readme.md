# Python Program:🔄 Rotate a list `[1, 2, 3, 4, 5]` to the right by 2 positions.

# Discription:
This Python program demonstrates how to rotate a list to the right by a given number of positions. When a list is rotated to the right, elements are shifted to the right, and the ones that fall off the end are wrapped around to the beginning.

For example:
**Input:** `[1, 2, 3, 4, 5]` (rotate by 2 positions)
**Output:** `[4, 5, 1, 2, 3]`

# Code:
```
# List to rotate
my_list = [1, 2, 3, 4, 5]

# Number of positions to rotate
n = 2

# Calculate effective rotations (in case n > len(my_list))
n = n % len(my_list)

# Rotate the list using slicing
rotated_list = my_list[-n:] + my_list[:-n]

# Print the rotated list
print("Rotated List:", rotated_list)  #Output: [4, 5, 1, 2, 3]

