# Python Program: 🔠 Create a list comprehension that extracts the vowels from the string `"hello world"`.

## Description:
This Python program demonstrates how to use list comprehension to extract the vowels from the string `"hello world"`. The program checks each character in the string and collects only the vowels.

## Code:
```python
# String to extract vowels from
text = "hello world"

# Using list comprehension to extract vowels
vowels = [char for char in text if char in 'aeiouAEIOU']

# Printing the list of vowels
print(vowels)    #output: ['e', 'o', 'o']
