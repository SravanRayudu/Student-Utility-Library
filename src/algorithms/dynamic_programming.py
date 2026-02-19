"""
Dynamic Programming Algorithms Module

This module contains implementations of dynamic programming algorithms.
Students can contribute by implementing the functions marked with TODO comments.

Author: Student Contributors
Last Updated: February 2026
"""

from typing import List


def fibonacci_dp(n: int) -> int:
    """
    Calculate the nth Fibonacci number using dynamic programming.
    
    This is more efficient than the recursive approach for large n.
    
    Args:
        n (int): The position in the Fibonacci sequence (0-indexed)
        
    Returns:
        int: The nth Fibonacci number
        
    Examples:
        >>> fibonacci_dp(10)
        55
        >>> fibonacci_dp(0)
        0
        >>> fibonacci_dp(1)
        1
    
    TODO: Implement Fibonacci using dynamic programming
    Hint: Use a table to store previously calculated values
    """
    # TODO: Implement fibonacci with dynamic programming
    pass


def longest_common_subsequence(str1: str, str2: str) -> int:
    """
    Find the length of the longest common subsequence between two strings.
    
    A subsequence is a sequence that can be derived from another sequence
    by deleting some or no elements without changing the order of remaining elements.
    
    Args:
        str1 (str): First string
        str2 (str): Second string
        
    Returns:
        int: Length of the longest common subsequence
        
    Examples:
        >>> longest_common_subsequence("ABCDGH", "AEDFHR")
        3  # "ADH"
        >>> longest_common_subsequence("AGGTAB", "GXTXAYB")
        4  # "GTAB"
    
    TODO: Implement LCS using dynamic programming
    """
    # TODO: Implement longest common subsequence
    pass


def knapsack_01(weights: List[int], values: List[int], capacity: int) -> int:
    """
    Solve the 0/1 Knapsack problem using dynamic programming.
    
    Given weights and values of n items, put these items in a knapsack of
    capacity W to get the maximum total value.
    
    Args:
        weights (List[int]): List of item weights
        values (List[int]): List of item values
        capacity (int): Knapsack capacity
        
    Returns:
        int: Maximum value that can be obtained
        
    Examples:
        >>> knapsack_01([10, 20, 30], [60, 100, 120], 50)
        220
    
    TODO: Implement 0/1 knapsack using dynamic programming
    """
    # TODO: Implement 0/1 knapsack problem
    pass