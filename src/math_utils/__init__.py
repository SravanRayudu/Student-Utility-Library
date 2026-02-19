"""
Mathematical Utilities Module

This module contains various mathematical utility functions and algorithms.
Students can contribute by implementing the functions in the individual modules.

The module covers:  
- Basic mathematical operations
- Number theory functions
- Statistical calculations
- Mathematical sequences and series

Author: Student Contributors
Last Updated: February 2026
"""

# Import all math utilities from individual modules
from .basic_math import (
    factorial,
    power,
    square_root
)

from .number_theory import (
    is_prime,
    gcd,
    lcm,
    is_perfect_number
)

from .sequences import (
    fibonacci
)

from .statistics import (
    mean,
    median,
    mode
)

# Make all functions available when importing from math_utils module
__all__ = [
    # Basic math operations
    'factorial',
    'power', 
    'square_root',
    
    # Number theory
    'is_prime',
    'gcd',
    'lcm', 
    'is_perfect_number',
    
    # Sequences
    'fibonacci',
    
    # Statistics
    'mean',
    'median',
    'mode'
]