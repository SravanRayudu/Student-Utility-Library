"""
Number Theory Module

This module contains number theory functions and algorithms.
Students can contribute by implementing the functions marked with TODO comments.

Author: Student Contributors
Last Updated: February 2026
"""


def is_prime(n: int) -> bool:
    """
    Check if a number is prime.
    
    A prime number is a natural number greater than 1 that has no positive 
    divisors other than 1 and itself.
    
    Args:
        n (int): The number to check
        
    Returns:
        bool: True if n is prime, False otherwise
        
    Examples:
        >>> is_prime(17)
        True
        >>> is_prime(4)
        False
        >>> is_prime(2)
        True
        >>> is_prime(1)
        False
    
    TODO: Implement this function
    Hint: Check divisibility only up to sqrt(n) for efficiency
    """
    # TODO: Implement this function
    pass


def gcd(a: int, b: int) -> int:
    """
    Calculate the Greatest Common Divisor (GCD) of two integers.
    
    The GCD is the largest positive integer that divides both numbers.
    
    Args:
        a (int): First integer
        b (int): Second integer
        
    Returns:
        int: The GCD of a and b
        
    Examples:
        >>> gcd(48, 18)
        6
        >>> gcd(17, 13)
        1
        >>> gcd(100, 25)
        25
    
    TODO: Implement this function
    Hint: Use the Euclidean algorithm: gcd(a,b) = gcd(b, a % b)
    """
    # TODO: Implement this function
    pass


def lcm(a: int, b: int) -> int:
    """
    Calculate the Least Common Multiple (LCM) of two integers.
    
    The LCM is the smallest positive integer that is divisible by both numbers.
    Formula: LCM(a,b) = |a*b| / GCD(a,b)
    
    Args:
        a (int): First integer
        b (int): Second integer
        
    Returns:
        int: The LCM of a and b
        
    Examples:
        >>> lcm(12, 18)
        36
        >>> lcm(4, 6)
        12
    
    TODO: Implement this function
    Hint: Use the relationship between LCM and GCD
    """
    # TODO: Implement this function
    pass


def is_perfect_number(n: int) -> bool:
    """
    Check if a number is a perfect number.
    
    A perfect number is a positive integer equal to the sum of its proper 
    positive divisors (excluding itself).
    
    Args:
        n (int): The number to check
        
    Returns:
        bool: True if n is a perfect number, False otherwise
        
    Examples:
        >>> is_perfect_number(6)  # 1 + 2 + 3 = 6
        True
        >>> is_perfect_number(28)  # 1 + 2 + 4 + 7 + 14 = 28
        True
        >>> is_perfect_number(12)
        False
    
    TODO: Implement this function
    Hint: Find all proper divisors and check if their sum equals n
    """
    # TODO: Implement this function
    pass