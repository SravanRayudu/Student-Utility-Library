"""
String Manipulation Module

This module contains basic string manipulation functions.
Students can contribute by implementing the functions marked with TODO comments.

Author: Student Contributors
Last Updated: February 2026
"""

from typing import List, Dict


def reverse_string(text: str) -> str:
    """
    Reverse the given string.
    
    This is a simple function to get students started with string manipulation.
    
    Args:
        text (str): The input string to reverse
        
    Returns:
        str: The reversed string
        
    Examples:
        >>> reverse_string("hello")
        "olleh"
        >>> reverse_string("Python")
        "nohtyP"
        >>> reverse_string("")
        ""
    
    TODO: Implement this function
    Hint: You can use string slicing with [::-1] or a loop
    """
    # TODO: Implement this function
    pass


def capitalize_words(text: str) -> str:
    """
    Capitalize the first letter of each word in a string.
    
    Args:
        text (str): The input string
        
    Returns:
        str: String with each word capitalized
        
    Examples:
        >>> capitalize_words("hello world")
        "Hello World"
        >>> capitalize_words("python programming")
        "Python Programming"
    
    TODO: Implement this function
    Hint: You can use the title() method or split and capitalize each word manually
    """
    # TODO: Implement this function
    pass


def remove_duplicates(text: str, preserve_order: bool = True) -> str:
    """
    Remove duplicate characters from a string.
    
    Args:
        text (str): The input string
        preserve_order (bool): Whether to preserve the order of first occurrence (default: True)
        
    Returns:
        str: String with duplicate characters removed
        
    Examples:
        >>> remove_duplicates("hello")
        "helo"
        >>> remove_duplicates("programming")
        "progamin"
    
    TODO: Implement this function
    Hint: Use a set to track seen characters, build result string iteratively
    """
    # TODO: Implement this function
    pass


def replace_multiple(text: str, replacements: Dict[str, str]) -> str:
    """
    Replace multiple substrings in a text using a replacement dictionary.
    
    Args:
        text (str): The input string
        replacements (Dict[str, str]): Dictionary mapping old strings to new strings
        
    Returns:
        str: String with all replacements applied
        
    Examples:
        >>> replace_multiple("Hello world!", {"Hello": "Hi", "world": "Python"})
        "Hi Python!"
        >>> replace_multiple("I love cats and dogs", {"cats": "Python", "dogs": "programming"})
        "I love Python and programming"
    
    TODO: Implement this function
    Hint: Iterate through the replacements dictionary and apply each replacement
    """
    # TODO: Implement this function
    pass