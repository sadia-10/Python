# Python Program:🌟 Create a list comprehension that generates a list of numbers from `1 to 100` that are divisible by `both 3 and 5`.

## Description:
This Python program generates a list of numbers from 1 to 100 that are divisible by both 3 and 5 using a list comprehension.

## Code:
```python
# Python Program: Generate Numbers Divisible by Both 3 and 5 Using List Comprehension

# List comprehension to find numbers divisible by both 3 and 5
divisible_by_3_and_5 = [num for num in range(1, 101) if num % 3 == 0 and num % 5 == 0]

# Print the resulting list
print("Numbers divisible by both 3 and 5:", divisible_by_3_and_5)  #output: Numbers divisible by both 3 and 5: [15, 30, 45, 60, 75, 90]

