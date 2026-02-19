"""
String Analysis Module

This module contains functions for analyzing and counting string properties.
Students can contribute by implementing the functions marked with TODO comments.

Author: Student Contributors
Last Updated: February 2026
"""

import re
from typing import List, Dict, Tuple


def count_words(text: str) -> int:
    """
    Count the number of words in a string.
    
    Words are separated by whitespace characters (spaces, tabs, newlines).
    
    Args:
        text (str): The input string
        
    Returns:
        int: The number of words in the string
        
    Examples:
        >>> count_words("Hello world")
        2
        >>> count_words("  Python   is   awesome  ")
        3
        >>> count_words("")
        0
    
    TODO: Implement this function
    Hint: Use the split() method or regular expressions
    """
    # TODO: Implement this function
    pass


def count_characters(text: str, ignore_spaces: bool = False) -> Dict[str, int]:
    """
    Count the frequency of each character in a string.
    
    Args:
        text (str): The input string
        ignore_spaces (bool): Whether to ignore space characters (default: False)
        
    Returns:
        Dict[str, int]: A dictionary with characters as keys and their counts as values
        
    Examples:
        >>> count_characters("hello")
        {'h': 1, 'e': 1, 'l': 2, 'o': 1}
        >>> count_characters("hello world", ignore_spaces=True)
        {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
    
    TODO: Implement this function
    Hint: Use a dictionary to store counts, iterate through each character
    """
    # TODO: Implement this function
    pass


def find_longest_word(text: str) -> str:
    """
    Find the longest word in a string.
    
    If there are multiple words with the same maximum length, return the first one.
    
    Args:
        text (str): The input string
        
    Returns:
        str: The longest word in the string
        
    Examples:
        >>> find_longest_word("The quick brown fox")
        "quick"
        >>> find_longest_word("Python is awesome")
        "awesome"
    
    TODO: Implement this function
    Hint: Split the string into words, then find the one with maximum length
    """
    # TODO: Implement this function
    pass


def extract_numbers(text: str) -> List[int]:
    """
    Extract all numbers from a string and return them as a list of integers.
    
    Args:
        text (str): The input string containing numbers and other characters
        
    Returns:
        List[int]: List of integers found in the string
        
    Examples:
        >>> extract_numbers("I have 5 apples and 3 oranges")
        [5, 3]
        >>> extract_numbers("Phone: 123-456-7890")
        [123, 456, 7890]
    
    TODO: Implement this function
    Hint: Use regular expressions to find number patterns
    """
    # TODO: Implement this function
    pass