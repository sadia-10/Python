### 1. Validating Email Addresses 📧

import re

def validate_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))  # Output: True


### 2. Extracting Phone Numbers 📞

import re

def extract_phone_numbers(text):
    pattern = r"\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b"
    return re.findall(pattern, text)   # Output: ['123-456-7890', '987.654.3210']


### 3. Replacing Sensitive Information with Asterisks 🛡️

import re

def mask_credit_card(text):
    pattern = r"\b\d{4}[-.\s]?\d{4}[-.\s]?\d{4}[-.\s]?\d{4}\b"
    return re.sub(pattern, "****-****-****-****", text)   # Output: My credit card number is ****-****-****-****.


### 4. Splitting a Sentence into Words ✂️

import re

def split_sentence(sentence):
    pattern = r"\W+"
    return re.split(pattern, sentence)  # Output: ['Hello', 'world', 'Welcome', 'to', 'Python', 


### 5. Finding All Hashtags in a Tweet 🏷️

import re

def find_hashtags(tweet):
    pattern = r"#\w+"
    return re.findall(pattern, tweet)   # Output: ['#Python', '#CodingIsFun', '#100DaysOfCode']
