# Regular Expressions in Python 🔄

## Overview
Regular Expressions (regex) are a powerful tool for pattern matching and text manipulation. They allow you to find, extract, and manipulate strings based on specific patterns. Python provides the `re` module to work with regex, making tasks like data validation, searching, and replacing text efficient and straightforward.

---

## Why Use Regular Expressions?
- **🔍 Searching Text:** Find specific words or patterns in large data.
- **🎛️ Data Validation:** Validate formats like email addresses, phone numbers, etc.
- **✏️ Text Manipulation:** Replace, split, or extract parts of text based on patterns.
- **🔄 Efficiency:** Handle complex string processing tasks in fewer lines of code.

---

## Key Regex Functions in Python
Here are the commonly used functions in the `re` module:

1. `re.match()` - Checks for a match only at the beginning of the string.
2. `re.search()` - Searches the entire string for the first match.
3. `re.findall()` - Returns a list of all matches.
4. `re.sub()` - Replaces occurrences of a pattern with a given string.
5. `re.split()` - Splits a string by the occurrences of a pattern.

---

## Real-World Examples 🌍

### 1. Validating Email Addresses 📧
```python
import re

def validate_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))

# Example Usage
email = "example@gmail.com"
print(validate_email(email))  # Output: True
```
**How it works:**
- `^` and `$` ensure the pattern matches the entire string.
- `[a-zA-Z0-9._%+-]+` matches the username part.
- `@` matches the @ symbol.
- `[a-zA-Z0-9.-]+` matches the domain.
- `\.[a-zA-Z]{2,}` ensures the domain ends with at least two letters.

---

### 2. Extracting Phone Numbers 📞
```python
import re

def extract_phone_numbers(text):
    pattern = r"\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b"
    return re.findall(pattern, text)

# Example Usage
text = "Contact me at 123-456-7890 or 987.654.3210."
print(extract_phone_numbers(text))  # Output: ['123-456-7890', '987.654.3210']
```
**How it works:**
- `\b` ensures the match is a whole word.
- `\d{3}` matches the first three digits.
- `[-.\s]?` matches optional separators (-, ., or space).
- `\d{4}` matches the last four digits.

---

### 3. Replacing Sensitive Information with Asterisks 🛡️
```python
import re

def mask_credit_card(text):
    pattern = r"\b\d{4}[-.\s]?\d{4}[-.\s]?\d{4}[-.\s]?\d{4}\b"
    return re.sub(pattern, "****-****-****-****", text)

# Example Usage
text = "My credit card number is 1234-5678-9101-1121."
print(mask_credit_card(text))  # Output: My credit card number is ****-****-****-****.
```
**How it works:**
- Similar to the phone number pattern, this matches credit card numbers.
- `re.sub()` replaces matched patterns with `****-****-****-****`.

---

### 4. Splitting a Sentence into Words ✉
```python
import re

def split_sentence(sentence):
    pattern = r"\W+"
    return re.split(pattern, sentence)

# Example Usage
sentence = "Hello, world! Welcome to Python programming."
print(split_sentence(sentence))  # Output: ['Hello', 'world', 'Welcome', 'to', 'Python', 'programming']
```
**How it works:**
- `\W+` matches any sequence of non-word characters (punctuation, spaces, etc.).
- `re.split()` uses this pattern to split the string into words.

---

### 5. Finding All Hashtags in a Tweet 🌟
```python
import re

def find_hashtags(tweet):
    pattern = r"#\w+"
    return re.findall(pattern, tweet)

# Example Usage
tweet = "Loving the #Python community! #CodingIsFun #100DaysOfCode"
print(find_hashtags(tweet))  # Output: ['#Python', '#CodingIsFun', '#100DaysOfCode']
```
**How it works:**
- `#` matches the hashtag symbol.
- `\w+` matches the word following the hashtag.
- `re.findall()` returns all matches as a list.

---

## Tips for Writing Regex Patterns 🔧
- **Use Raw Strings:** Always use `r""` to avoid escaping backslashes.
- **Test Patterns:** Use tools like [Regex101](https://regex101.com/) to test your patterns.
- **Keep It Simple:** Write patterns incrementally and test at each step.

---

## Conclusion
Regular Expressions are an essential skill for any developer working with text data. With practice, they become an invaluable tool for solving real-world problems efficiently.

