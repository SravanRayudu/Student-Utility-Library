"""
Test file for math utilities module.

Run tests with: python -m pytest tests/test_math_utils.py -v
"""

import pytest
from src.math_utils import (
    factorial,
    is_prime,
    gcd,
    lcm,
    fibonacci,
    mean,
    median,
    mode,
    power,
    square_root,
    is_perfect_number
)


class TestMathUtils:
    """Test cases for math utility functions."""
    
    def test_factorial(self):
        """Test the factorial function."""
        assert factorial(0) == 1
        assert factorial(1) == 1
        assert factorial(5) == 120
        assert factorial(3) == 6
        
        with pytest.raises(ValueError):
            factorial(-1)
    
    def test_is_prime(self):
        """Test the is_prime function."""
        assert is_prime(2) == True
        assert is_prime(17) == True
        assert is_prime(4) == False
        assert is_prime(1) == False
        assert is_prime(0) == False
        assert is_prime(97) == True
    
    def test_gcd(self):
        """Test the gcd function."""
        assert gcd(48, 18) == 6
        assert gcd(17, 13) == 1
        assert gcd(100, 25) == 25
        assert gcd(0, 5) == 5
    
    def test_lcm(self):
        """Test the lcm function."""
        assert lcm(12, 18) == 36
        assert lcm(4, 6) == 12
        assert lcm(7, 5) == 35
    
    def test_fibonacci(self):
        """Test the fibonacci function."""
        assert fibonacci(0) == []
        assert fibonacci(1) == [0]
        assert fibonacci(2) == [0, 1]
        assert fibonacci(7) == [0, 1, 1, 2, 3, 5, 8]
    
    def test_mean(self):
        """Test the mean function."""
        assert mean([1, 2, 3, 4, 5]) == 3.0
        assert mean([10, 20]) == 15.0
        assert mean([5]) == 5.0
        
        with pytest.raises(ValueError):
            mean([])
    
    def test_median(self):
        """Test the median function."""
        assert median([1, 2, 3, 4, 5]) == 3.0
        assert median([1, 2, 3, 4]) == 2.5
        assert median([5]) == 5.0
        assert median([3, 1, 2]) == 2.0  # Should handle unsorted
        
        with pytest.raises(ValueError):
            median([])
    
    def test_mode(self):
        """Test the mode function."""
        assert mode([1, 2, 2, 3, 4]) == [2]
        assert set(mode([1, 1, 2, 2, 3])) == {1, 2}  # Multiple modes
        assert mode([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]  # All same frequency
    
    def test_power(self):
        """Test the power function."""
        assert power(2, 3) == 8
        assert power(5, 0) == 1
        assert power(2, -2) == 0.25
        assert power(10, 2) == 100
    
    def test_square_root(self):
        """Test the square_root function."""
        assert abs(square_root(16) - 4.0) < 1e-10
        assert abs(square_root(9) - 3.0) < 1e-10
        assert abs(square_root(2) - 1.4142135623730951) < 1e-10
        
        with pytest.raises(ValueError):
            square_root(-1)
    
    def test_is_perfect_number(self):
        """Test the is_perfect_number function."""
        assert is_perfect_number(6) == True  # 1 + 2 + 3 = 6
        assert is_perfect_number(28) == True  # 1 + 2 + 4 + 7 + 14 = 28
        assert is_perfect_number(12) == False
        assert is_perfect_number(1) == False


# Example usage
if __name__ == "__main__":
    print("Math Utilities Test Examples")
    print("=" * 40)
    
    try:
        print(f"Factorial of 5: {factorial(5)}")
        print(f"Is 17 prime?: {is_prime(17)}")
        print(f"GCD of 48 and 18: {gcd(48, 18)}")
        print(f"LCM of 12 and 18: {lcm(12, 18)}")
        print(f"First 7 Fibonacci numbers: {fibonacci(7)}")
        print(f"Mean of [1,2,3,4,5]: {mean([1, 2, 3, 4, 5])}")
        print(f"Median of [1,2,3,4,5]: {median([1, 2, 3, 4, 5])}")
        print(f"2^3 = {power(2, 3)}")
        print(f"Square root of 16: {square_root(16)}")
        print(f"Is 6 a perfect number?: {is_perfect_number(6)}")
    except Exception as e:
        print(f"Functions not implemented yet: {e}")
        print("Students need to implement the functions to see results!")