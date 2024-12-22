# Python Program:🌟 Create a list comprehension that replaces each `vowel` in a string with an `asterisk ('*')`.

## Description:
This Python program replaces all vowels (`a, e, i, o, u`) in a given string with an asterisk (`'*'`). The program uses list comprehension to perform this transformation efficiently and combines the result into a new string.

## Code:
```python
# Input string
text = "hello world"

# Using list comprehension to replace vowels with '*'
replaced_text = ''.join(['*' if char in 'aeiouAEIOU' else char for char in text])

# Printing the modified string
print(replaced_text)   #output: h*ll* w*rld
