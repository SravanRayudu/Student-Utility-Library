"""
String Validation Module

This module contains functions for validating and checking string properties.
Students can contribute by implementing the functions marked with TODO comments.

Author: Student Contributors
Last Updated: February 2026
"""


def is_palindrome(text: str, ignore_case: bool = True, ignore_spaces: bool = True) -> bool:
    """
    Check if a string is a palindrome.
    
    A palindrome reads the same forwards and backwards.
    
    Args:
        text (str): The string to check
        ignore_case (bool): Whether to ignore case differences (default: True)
        ignore_spaces (bool): Whether to ignore spaces and punctuation (default: True)
        
    Returns:
        bool: True if the string is a palindrome, False otherwise
        
    Examples:
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("A man a plan a canal Panama")
        True
        >>> is_palindrome("hello")
        False
    
    TODO: Implement this function
    Hint: Clean the string first based on the parameters, then compare with its reverse
    """
    # TODO: Implement this function
    # Step 1: Clean the string based on ignore_case and ignore_spaces parameters
    # Step 2: Compare the cleaned string with its reverse
    # Step 3: Return the result
    pass


def is_anagram(str1: str, str2: str) -> bool:
    """
    Check if two strings are anagrams of each other.
    
    Anagrams are words with the same characters but in different order.
    This function should ignore case and spaces.
    
    Args:
        str1 (str): First string
        str2 (str): Second string
        
    Returns:
        bool: True if the strings are anagrams, False otherwise
        
    Examples:
        >>> is_anagram("listen", "silent")
        True
        >>> is_anagram("hello", "bello")
        False
        >>> is_anagram("The eyes", "They see")
        True
    
    TODO: Implement this function
    Hint: Clean both strings, then compare sorted character lists
    """
    # TODO: Implement this function
    pass