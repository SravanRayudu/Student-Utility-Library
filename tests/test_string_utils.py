"""
Test file for string utilities module.

This file contains unit tests for all string utility functions.
Students should run these tests to verify their implementations.

Run tests with: python -m pytest tests/test_string_utils.py -v
"""

import pytest
from src.string_utils import (
    reverse_string,
    is_palindrome,
    count_words,
    count_characters,
    capitalize_words,
    remove_duplicates,
    find_longest_word,
    extract_numbers,
    replace_multiple,
    is_anagram
)


class TestStringUtils:
    """Test cases for string utility functions."""
    
    def test_reverse_string(self):
        """Test the reverse_string function."""
        # Test basic functionality
        assert reverse_string("hello") == "olleh"
        assert reverse_string("Python") == "nohtyP"
        assert reverse_string("") == ""
        assert reverse_string("a") == "a"
        assert reverse_string("12345") == "54321"
    
    def test_is_palindrome(self):
        """Test the is_palindrome function."""
        # Test basic palindromes
        assert is_palindrome("racecar") == True
        assert is_palindrome("hello") == False
        assert is_palindrome("") == True
        assert is_palindrome("a") == True
        
        # Test with spaces and case
        assert is_palindrome("A man a plan a canal Panama") == True
        assert is_palindrome("race a car") == False
        
        # Test case sensitivity
        assert is_palindrome("Aa", ignore_case=True) == True
        assert is_palindrome("Aa", ignore_case=False) == False
    
    def test_count_words(self):
        """Test the count_words function."""
        assert count_words("Hello world") == 2
        assert count_words("  Python   is   awesome  ") == 3
        assert count_words("") == 0
        assert count_words("OneWord") == 1
        assert count_words("a b c d e") == 5
    
    def test_count_characters(self):
        """Test the count_characters function."""
        result = count_characters("hello")
        expected = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
        assert result == expected
        
        result = count_characters("hello world", ignore_spaces=True)
        expected = {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
        assert result == expected
        
        result = count_characters("hello world", ignore_spaces=False)
        expected = {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
        assert result == expected
    
    def test_capitalize_words(self):
        """Test the capitalize_words function."""
        assert capitalize_words("hello world") == "Hello World"
        assert capitalize_words("python programming") == "Python Programming"
        assert capitalize_words("") == ""
        assert capitalize_words("a") == "A"
    
    def test_remove_duplicates(self):
        """Test the remove_duplicates function."""
        assert remove_duplicates("hello") == "helo"
        assert remove_duplicates("programming") == "progamin"
        assert remove_duplicates("") == ""
        assert remove_duplicates("abc") == "abc"
    
    def test_find_longest_word(self):
        """Test the find_longest_word function."""
        assert find_longest_word("The quick brown fox") == "quick"
        assert find_longest_word("Python is awesome") == "awesome"
        assert find_longest_word("a bb ccc") == "ccc"
        assert find_longest_word("hello") == "hello"
    
    def test_extract_numbers(self):
        """Test the extract_numbers function."""
        assert extract_numbers("I have 5 apples and 3 oranges") == [5, 3]
        assert extract_numbers("Phone: 123-456-7890") == [123, 456, 7890]
        assert extract_numbers("No numbers here!") == []
        assert extract_numbers("Year 2024 month 12 day 31") == [2024, 12, 31]
    
    def test_replace_multiple(self):
        """Test the replace_multiple function."""
        result = replace_multiple("Hello world!", {"Hello": "Hi", "world": "Python"})
        assert result == "Hi Python!"
        
        result = replace_multiple("I love cats and dogs", {"cats": "Python", "dogs": "programming"})
        assert result == "I love Python and programming"
    
    def test_is_anagram(self):
        """Test the is_anagram function."""
        assert is_anagram("listen", "silent") == True
        assert is_anagram("hello", "bello") == False
        assert is_anagram("The eyes", "They see") == True
        assert is_anagram("", "") == True
        assert is_anagram("a", "a") == True


# Example usage and demonstration
if __name__ == "__main__":
    print("String Utilities Test Examples")
    print("=" * 40)
    
    # Note: These will fail until students implement the functions
    try:
        print(f"Reverse 'hello': {reverse_string('hello')}")
        print(f"Is 'racecar' a palindrome?: {is_palindrome('racecar')}")
        print(f"Word count in 'Hello world': {count_words('Hello world')}")
        print(f"Character count in 'hello': {count_characters('hello')}")
        print(f"Capitalize 'hello world': {capitalize_words('hello world')}")
        print(f"Remove duplicates from 'hello': {remove_duplicates('hello')}")
        print(f"Longest word in 'The quick brown fox': {find_longest_word('The quick brown fox')}")
        print(f"Extract numbers from 'I have 5 apples': {extract_numbers('I have 5 apples')}")
        print(f"Are 'listen' and 'silent' anagrams?: {is_anagram('listen', 'silent')}")
    except Exception as e:
        print(f"Functions not implemented yet: {e}")
        print("Students need to implement the functions to see results!")