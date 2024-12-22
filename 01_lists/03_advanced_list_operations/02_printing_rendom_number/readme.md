# Python Program: .🥈 Find the second largest number in the list `[10, 20, 4, 45, 99, 4, 28]`.

# Discription:
This Python program demonstrates how to find the second largest number in a given list of numbers. 🥈

The program removes duplicates (if any) from the list and sorts the unique elements. After sorting, the second largest number is identified by accessing the second last element in the sorted list.

For example:

**Input:** `[10, 20, 4, 45, 99, 4, 28]`

**Output:** `45` (the second largest number)

# Code:
```
# Define the list of numbers
my_list = [10, 20, 4, 45, 99, 4, 28]

# Remove duplicates using set() and sort the list in ascending order
unique_sorted_list = sorted(set(my_list))

# Access the second last element, which is the second largest number
second_largest = unique_sorted_list[-2]

# Print the second largest number
print(second_largest)  # Output: 45
