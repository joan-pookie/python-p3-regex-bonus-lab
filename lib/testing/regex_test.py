# lib/testing/regex_test.py
import pytest
from lib.regex import name_regex, phone_regex, email_regex, sentence_regex
import re

class TestRegex:
    # ----------------------------
    # Name Regex Tests
    # ----------------------------
    def test_name_valid(self):
        assert re.match(name_regex, "John Doe")
        assert re.match(name_regex, "Alice Johnson")
        assert re.match(name_regex, "Mary Anne Smith")

    def test_name_invalid(self):
        assert not re.match(name_regex, "john doe")
        assert not re.match(name_regex, "JOHN DOE")
        assert not re.match(name_regex, "Alice1 Johnson")

    # ----------------------------
    # Phone Regex Tests
    # ----------------------------
    def test_phone_valid(self):
        assert re.match(phone_regex, "123-456-7890")
        assert re.match(phone_regex, "(123) 456-7890")
        assert re.match(phone_regex, "1234567890")
        assert re.match(phone_regex, "123 456 7890")

    def test_phone_invalid(self):
        assert not re.match(phone_regex, "12-3456-7890")
        assert not re.match(phone_regex, "123-45-67890")
        assert not re.match(phone_regex, "phone1234567890")

    # ----------------------------
    # Email Regex Tests
    # ----------------------------
    def test_email_valid(self):
        assert re.match(email_regex, "john@example.com")
        assert re.match(email_regex, "alice.johnson@school.org")
        assert re.match(email_regex, "user-name@domain.co.uk")

    def test_email_invalid(self):
        assert not re.match(email_regex, "john@example")
        assert not re.match(email_regex, "john@.com")
        assert not re.match(email_regex, "john@@example.com")
        assert not re.match(email_regex, "john example.com")

    # ----------------------------
    # Sentence Regex Tests (BONUS)
    # ----------------------------
    def test_sentence_valid(self):
        text = "It's such a lovely day today."
        matches = re.findall(sentence_regex, text)
        assert "It's such a lovely day today." in matches

    def test_sentence_invalid(self):
        text = "This sentence has #invalid$ characters!"
        matches = re.findall(sentence_regex, text)
        assert "#" not in matches[0]
        assert "$" not in matches[0]
