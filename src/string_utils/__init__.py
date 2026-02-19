"""
String Utilities Module

This module contains various utility functions for string manipulation and processing.
Students can contribute by implementing the functions in the individual modules.

Each function includes:
- Detailed docstrings explaining the purpose and parameters
- Type hints for better code clarity
- Examples in the docstrings to guide implementation
- Comments explaining the expected logic

Author: Student Contributors
Last Updated: February 2026
"""

# Import all string utilities from individual modules
from .manipulation import (
    reverse_string,
    capitalize_words,
    remove_duplicates,
    replace_multiple
)

from .analysis import (
    count_words,
    count_characters,
    find_longest_word,
    extract_numbers
)

from .validation import (
    is_palindrome,
    is_anagram
)

# Make all functions available when importing from string_utils module
__all__ = [
    # String manipulation
    'reverse_string',
    'capitalize_words',
    'remove_duplicates',
    'replace_multiple',
    
    # String analysis
    'count_words',
    'count_characters',
    'find_longest_word',
    'extract_numbers',
    
    # String validation
    'is_palindrome',
    'is_anagram'
]