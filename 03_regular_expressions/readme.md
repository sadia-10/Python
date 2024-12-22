# Regular Expressions in Python 🔍🐍

## Overview 
Regular Expressions (regex) are a powerful tool for pattern matching and text manipulation. They allow you to find, extract, and manipulate strings based on specific patterns. Python provides the `re` module to work with regex, making tasks like data validation, searching, and replacing text efficient and straightforward.

---

## History of Regular Expressions 📜
Regular Expressions were first introduced by mathematician Stephen Cole Kleene in the 1950s as a way to describe regular languages. Over the years, they evolved into a practical tool for text processing and have become a standard feature in most programming languages, including Python. Today, regex is widely used in fields like data science, web development, and natural language processing.

---

## Why Use Regular Expressions? 🤔
- **🔍 Searching Text:** Find specific words or patterns in large data.
- **🎛️ Data Validation:** Validate formats like email addresses, phone numbers, etc.
- **✏️ Text Manipulation:** Replace, split, or extract parts of text based on patterns.
- **🔄 Efficiency:** Handle complex string processing tasks in fewer lines of code.

---

## The Many Flavors of Regular Expressions 🌍
Different programming languages and tools have their own "flavors" of regular expressions, meaning there might be slight variations in syntax or features. For example:
- **Python's re Module:** A well-rounded implementation that supports most standard regex features.
- **JavaScript Regex:** Limited to ECMAScript syntax with minor differences from Python.
- **Perl Regex:** Known for its advanced features and influence on other regex flavors.

Despite these differences, the core concepts of regular expressions remain the same, making it easier to transfer your knowledge across platforms.

---

## How to Use the `re` Module 🛠️
Python's `re` module provides a simple interface for working with regular expressions. Here are the main steps:

1. **Import the Module:**
   ```python
   import re
   ```

2. **Define a Pattern:**
   Use raw strings (`r""`) to define regex patterns without escaping backslashes.
   ```python
   pattern = r"\d{3}-\d{3}-\d{4}"
   ```

3. **Match or Search:**
   Use functions like `re.match()`, `re.search()`, or `re.findall()` to find patterns in strings.
   ```python
   result = re.search(pattern, "Call 123-456-7890")
   ```

4. **Manipulate Strings:**
   Replace or split strings using `re.sub()` or `re.split()`.
   ```python
   masked = re.sub(pattern, "XXX-XXX-XXXX", "Call 123-456-7890")
   ```

5. **Compile for Reusability:**
   Compile regex patterns for improved performance when using them multiple times.
   ```python
   compiled_pattern = re.compile(r"\d{3}-\d{3}-\d{4}")
   result = compiled_pattern.findall("Call 123-456-7890")
   ```

---

## Key Regex Functions in Python 📚
Here are the commonly used functions in the `re` module:

1. `re.match()` - Checks for a match only at the beginning of the string.
2. `re.search()` - Searches the entire string for the first match.
3. `re.findall()` - Returns a list of all matches.
4. `re.sub()` - Replaces occurrences of a pattern with a given string.
5. `re.split()` - Splits a string by the occurrences of a pattern.

---

## Real-World Examples 🌟

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

### 4. Splitting a Sentence into Words ✂️
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

### 5. Finding All Hashtags in a Tweet 🏷️
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

## Tips for Writing Regex Patterns 🧰
- **Use Raw Strings:** Always use `r""` to avoid escaping backslashes.
- **Test Patterns:** Use tools like [Regex101](https://regex101.com/) to test your patterns.
- **Keep It Simple:** Write patterns incrementally and test at each step.

---

## Complete Example File: `main.py` 📂
```python
import re

def validate_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))

def extract_phone_numbers(text):
    pattern = r"\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b"
    return re.findall(pattern, text)

def mask_credit_card(text):
    pattern = r"\b\d{4}[-.\s]?\d{4}[-.\s]?\d{4}[-.\s]?\d{4}\b"
    return re.sub(pattern, "****-****-****-****", text)

def split_sentence(sentence):
    pattern = r"\W+"
    return re.split(pattern, sentence)

def find_hashtags(tweet):
    pattern = r"#\w+"
    return re.findall(pattern, tweet)

# Example usages
if __name__ == "__main__":
    print(validate_email("example@gmail.com"))
    print(extract_phone_numbers("Call me at 123-456-7890 or 987.654.3210."))
    print(mask_credit_card("My credit card is 1234-5678-9101-1121."))
    print(split_sentence("Hello, world! Welcome to Python programming."))
    print(find_hashtags("#Python is amazing! #CodingIsFun"))
```

---

## Conclusion 🎉
Regular Expressions are an essential skill for any developer working with text data. With practice, they become an invaluable tool for solving real-world problems efficiently. Happy coding! 🚀

