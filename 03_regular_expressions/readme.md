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
## 📋 Table Regular Expression Pattern Syntax

| **🔤 Element**             | **📖 Meaning**                                                                                                                                                    |
|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **`.`**                   | Matches **any single character** except a newline (`\n`). This is like a wildcard that can be any letter, number, or symbol.                                       |
| **`^`**                   | Matches the **start of a string**. If `MULTILINE` mode is enabled, it also matches the position right after a newline (`\n`).                                      |
| **`$`**                   | Matches the **end of a string**. In `MULTILINE` mode, it also matches the position right before a newline (`\n`).                                                  |
| **`*`**                   | Matches **zero or more occurrences** of the preceding pattern; it's **greedy** (tries to match as much as possible).                                               |
| **`+`**                   | Matches **one or more occurrences** of the preceding pattern; **greedy**.                                                                                         |
| **`?`**                   | Matches **zero or one occurrence** of the preceding pattern; **greedy**. It is useful for optional characters or patterns.                                          |
| **`*?`, `+?`, `??`**      | These are **nongreedy** (or **lazy**) versions of `*`, `+`, and `?` respectively. They match as **few characters as possible**.                                    |
| **`{m,n}`**               | Matches **between `m` and `n` occurrences** of the preceding pattern; **greedy**. You can use it to specify exact repetition.                                      |
| **`{m,n}?`**              | Matches **between `m` and `n` occurrences** of the preceding pattern; **nongreedy**.                                                                               |
| **`[...]`**               | Matches **any one character** from a set inside the brackets. For example, `[abc]` matches `a`, `b`, or `c`.                                                       |
| **`[^...]`**              | Matches **any one character not** in the set inside the brackets. For example, `[^abc]` matches any character except `a`, `b`, or `c`.                              |
| **`|`**                   | Acts like a logical **OR**; matches **either** the pattern before or after it. For example, `cat|dog` matches "cat" or "dog".                                       |
| **`(...)`**               | Matches the pattern inside the parentheses and **creates a capturing group**. Use it to group patterns for extraction or backreferences.                           |
| **`(?:...)`**             | Matches the pattern inside the parentheses but **does not create a capturing group**. Useful for grouping without capturing.                                       |
| **`(?P<id>...)`**         | Matches the pattern and **names the group** as `id`. Named groups make patterns more readable and easier to reference.                                             |
| **`(?P=id)`**             | Matches **the same text** as previously matched by the named group `id`. Use it to refer back to the named group.                                                  |
| **`(?#...)`**             | A **comment** inside the regex pattern; helps improve readability without affecting the match.                                                                     |
| **`(?=...)`**             | **Positive lookahead**: Matches if the pattern matches what comes next, but does **not consume** any characters. Used to assert that something follows.            |
| **`(?!...)`**             | **Negative lookahead**: Matches if the pattern does **not** match what comes next, without consuming any characters. Useful for excluding patterns.                 |
| **`(?<=...)`**            | **Positive lookbehind**: Matches if the pattern precedes the current position; must match a fixed length. Ensures something comes before the match.                |
| **`(?<!...)`**            | **Negative lookbehind**: Matches if the pattern does **not** precede the current position; must match a fixed length.                                               |
| **`\number`**             | Matches the text previously matched by the group **numbered `number`**. Useful for reusing matched patterns.                                                      |
| **`\A`**                  | Matches the **start of the entire string**. Unlike `^`, it is not affected by `MULTILINE`.                                                                        |
| **`\b`**                  | Matches a **word boundary** (the start or end of a word). Helps match whole words only.                                                                            |
| **`\B`**                  | Matches a position that is **not a word boundary**. Useful for ensuring a match occurs within a word.                                                             |
| **`\d`**                  | Matches a **digit** (equivalent to `[0-9]`). In Unicode mode, it matches any Unicode digit.                                                                        |
| **`\D`**                  | Matches a **non-digit** (equivalent to `[^0-9]`).                                                                                                                 |
| **`\s`**                  | Matches a **whitespace character** (spaces, tabs, newlines, etc.).                                                                                                |
| **`\S`**                  | Matches a **non-whitespace character**.                                                                                                                           |
| **`\w`**                  | Matches an **alphanumeric character** (letters, digits, underscore). Equivalent to `[a-zA-Z0-9_]`.                                                                |
| **`\W`**                  | Matches a **non-alphanumeric character**.                                                                                                                         |
| **`\Z`**                  | Matches the **end of the entire string**. Unlike `$`, it is not affected by `MULTILINE`.                                                                          |
| **`\\`**                  | Matches a **literal backslash** (`\`) character. Useful for escaping special characters.                                                                           |
| **`(?iLmsux)`**           | Alternate way to **set optional flags** within a pattern. Flags control the regex behavior (case insensitivity, multiline mode, etc.).                             |


## Conclusion 🎉
Regular Expressions are an essential skill for any developer working with text data. With practice, they become an invaluable tool for solving real-world problems efficiently. 

