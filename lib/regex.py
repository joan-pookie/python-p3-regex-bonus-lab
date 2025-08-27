# lib/regex.py
import re

# ------------------------------
# Name Regex
# Matches names like "John Doe", "Alice Johnson"
# Capitalized first letters, allows spaces in between
name_regex = r"^[A-Z][a-z]+(?: [A-Z][a-z]+)*$"

# ------------------------------
# Phone Number Regex
# Matches patterns like: 123-456-7890, (123) 456-7890, 1234567890
phone_regex = r"^(?:\(\d{3}\)|\d{3})[- ]?\d{3}[- ]?\d{4}$"

# ------------------------------
# Email Address Regex
# Matches emails like: user@example.com, john.doe@school.org
email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"

# ------------------------------
# Sentence Regex (for BONUS lab)
# Matches sentences with letters, numbers, spaces, and common punctuation
sentence_regex = r"[A-Za-z0-9 ,.!?']+"

# ------------------------------
# Helper functions (optional, for BONUS lab)
def match_sentences(text):
    """Return all sentences that match the sentence_regex."""
    return re.findall(sentence_regex, text)

def match_names(text):
    """Return all names that match name_regex."""
    return re.findall(name_regex, text)

def match_phones(text):
    """Return all phone numbers that match phone_regex."""
    return re.findall(phone_regex, text)

def match_emails(text):
    """Return all emails that match email_regex."""
    return re.findall(email_regex, text)
