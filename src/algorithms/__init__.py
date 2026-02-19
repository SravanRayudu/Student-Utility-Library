"""
Algorithms Module

This module contains implementations of common algorithms including sorting, 
searching, graph algorithms, dynamic programming, and recursive solutions.
Students can contribute by implementing the functions in the individual modules.

Covered algorithms:
- Sorting algorithms (Bubble Sort, Selection Sort, Merge Sort, Quick Sort)
- Searching algorithms (Linear Search, Binary Search)
- Graph algorithms (BFS, DFS)
- Dynamic Programming examples (Fibonacci, LCS, Knapsack)
- Recursive algorithms (Palindrome check, Tower of Hanoi)

Author: Student Contributors
Last Updated: February 2026
"""

# Import all algorithms from individual modules
from .sorting import (
    bubble_sort,
    selection_sort,
    merge_sort,
    quick_sort
)

from .searching import (
    linear_search,
    binary_search
)

from .graph_algorithms import (
    breadth_first_search,
    depth_first_search
)

from .dynamic_programming import (
    fibonacci_dp,
    longest_common_subsequence,
    knapsack_01
)

from .recursion import (
    is_palindrome_recursive,
    tower_of_hanoi
)

# Make all functions available when importing from algorithms module
__all__ = [
    # Sorting algorithms
    'bubble_sort',
    'selection_sort', 
    'merge_sort',
    'quick_sort',
    
    # Searching algorithms
    'linear_search',
    'binary_search',
    
    # Graph algorithms
    'breadth_first_search',
    'depth_first_search',
    
    # Dynamic programming
    'fibonacci_dp',
    'longest_common_subsequence',
    'knapsack_01',
    
    # Recursive algorithms 
    'is_palindrome_recursive',
    'tower_of_hanoi'
]