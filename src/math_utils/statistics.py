"""
Statistics Module

This module contains statistical calculation functions.
Students can contribute by implementing the functions marked with TODO comments.

Author: Student Contributors
Last Updated: February 2026
"""

from typing import List, Union


def mean(numbers: List[Union[int, float]]) -> float:
    """
    Calculate the arithmetic mean (average) of a list of numbers.
    
    Args:
        numbers (List[Union[int, float]]): List of numbers
        
    Returns:
        float: The arithmetic mean
        
    Raises:
        ValueError: If the list is empty
        
    Examples:
        >>> mean([1, 2, 3, 4, 5])
        3.0
        >>> mean([10, 20])
        15.0
    
    TODO: Implement this function
    Hint: Sum all numbers and divide by the count
    """
    # TODO: Implement this function
    pass


def median(numbers: List[Union[int, float]]) -> float:
    """
    Calculate the median of a list of numbers.
    
    The median is the middle value when numbers are sorted. If there's an even
    number of values, it's the average of the two middle values.
    
    Args:
        numbers (List[Union[int, float]]): List of numbers
        
    Returns:
        float: The median value
        
    Raises:
        ValueError: If the list is empty
        
    Examples:
        >>> median([1, 2, 3, 4, 5])
        3.0
        >>> median([1, 2, 3, 4])
        2.5
    
    TODO: Implement this function
    Hint: Sort the list first, then find the middle value(s)
    """
    # TODO: Implement this function
    pass


def mode(numbers: List[Union[int, float]]) -> List[Union[int, float]]:
    """
    Find the mode(s) of a list of numbers.
    
    The mode is the value(s) that appear most frequently in the dataset.
    
    Args:
        numbers (List[Union[int, float]]): List of numbers
        
    Returns:
        List[Union[int, float]]: List of mode values (can be multiple)
        
    Examples:
        >>> mode([1, 2, 2, 3, 4])
        [2]
        >>> mode([1, 1, 2, 2, 3])
        [1, 2]
    
    TODO: Implement this function
    Hint: Count frequencies, then find values with maximum frequency
    """
    # TODO: Implement this function
    pass