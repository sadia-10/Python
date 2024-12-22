
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
