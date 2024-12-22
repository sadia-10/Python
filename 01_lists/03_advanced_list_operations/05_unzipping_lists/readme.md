# Python Program 📤 Unzip a list of tuples `[(1, 'a'), (2, 'b'), (3, 'c')]` into two separate lists.

# Discription:
This project demonstrates how to unzip a list of tuples into two separate lists in Python. It uses the `zip` function with unpacking to efficiently separate the elements of each tuple into individual lists.

# code:
```python
# List of tuples
tuple_list = [(1, 'a'), (2, 'b'), (3, 'c')]

# Unzip the list into two separate lists
list1, list2 = zip(*tuple_list)

# Convert the result from tuples to lists (optional)
list1 = list(list1)
list2 = list(list2)

print(list1)  # Output: [1, 2, 3]
print(list2)  # Output: ['a', 'b', 'c']
