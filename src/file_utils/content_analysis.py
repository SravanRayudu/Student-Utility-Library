"""
File Content Analysis Module

This module contains functions for analyzing file contents.
Students can contribute by implementing the functions marked with TODO comments.

Author: Student Contributors
Last Updated: February 2026
"""

from typing import List, Tuple


def read_lines(file_path: str, encoding: str = 'utf-8') -> List[str]:
    """
    Read all lines from a file and return as a list.
    
    Args:
        file_path (str): Path to the file to read
        encoding (str): File encoding (default: 'utf-8')
        
    Returns:
        List[str]: List of lines from the file (with newline characters preserved)
        
    TODO: Implement line-by-line file reading
    """
    # TODO: Implement reading lines
    pass


def count_lines(file_path: str, encoding: str = 'utf-8') -> int:
    """
    Count the number of lines in a file.
    
    Args:
        file_path (str): Path to the file
        encoding (str): File encoding (default: 'utf-8')
        
    Returns:
        int: Number of lines in the file
        
    Examples:
        >>> count_lines('data.txt')
        150
    
    TODO: Implement line counting
    """
    # TODO: Implement line counting
    pass


def count_words(file_path: str, encoding: str = 'utf-8') -> int:
    """
    Count the number of words in a file.
    
    Args:
        file_path (str): Path to the file
        encoding (str): File encoding (default: 'utf-8')
        
    Returns:
        int: Number of words in the file
        
    Examples:
        >>> count_words('essay.txt')
        500
    
    TODO: Implement word counting
    Hint: Split the content by whitespace and count the resulting list
    """
    # TODO: Implement word counting
    pass


def find_in_file(file_path: str, search_term: str, case_sensitive: bool = True, encoding: str = 'utf-8') -> List[Tuple[int, str]]:
    """
    Find all occurrences of a search term in a file.
    
    Args:
        file_path (str): Path to the file to search
        search_term (str): Term to search for
        case_sensitive (bool): Whether search should be case sensitive (default: True)
        encoding (str): File encoding (default: 'utf-8')
        
    Returns:
        List[Tuple[int, str]]: List of tuples containing (line_number, line_content)
        
    Examples:
        >>> matches = find_in_file('log.txt', 'ERROR')
        >>> print(matches)
        [(15, 'ERROR: Connection failed'), (23, 'ERROR: Invalid input')]
    
    TODO: Implement text search in file
    """
    # TODO: Implement file search
    pass