# Contributing Guide

Thank you for your interest in contributing to the Student Utility Library! This guide will help you get started with making your first contribution.

## 🎯 How to Contribute

### 1. Choose a Function to Implement

Look through the source code for functions marked with:
```python
# TODO: Implement this function
```

Start with simpler functions and gradually work on more complex ones.

### 2. Recommended Order for Beginners

**Start Here (Easy):**
- `src/string_utils/`: `reverse_string()`, `count_words()`, `capitalize_words()`
- `src/math_utils/`: `factorial()`, `is_prime()`, `mean()`

**Intermediate:**
- `src/string_utils/`: `is_palindrome()`, `count_characters()`, `is_anagram()`
- `src/math_utils/`: `gcd()`, `lcm()`, `fibonacci()`, `median()`
- `src/file_utils/`: `read_file()`, `write_file()`, `count_lines()`

**Advanced:**
- `src/data_structures/`: All classes (`Stack`, `Queue`, `LinkedList`, etc.)
- `src/algorithms/`: Sorting and searching algorithms
- `src/file_utils/`: CSV/JSON handling functions

### 3. Implementation Steps

1. **Read the Documentation**: Each function has detailed docstrings explaining:
   - What the function should do
   - Input parameters and their types
   - Expected return values
   - Usage examples
   - Implementation hints

2. **Understand the Tests**: Look at the corresponding test file in `tests/` to see what behavior is expected.

3. **Implement the Function**: Replace the `pass` statement with your implementation.

4. **Test Your Code**: Run the specific tests for your function:
   ```bash
   python -m pytest tests/test_string_utils.py::TestStringUtils::test_reverse_string -v
   ```

5. **Run All Tests**: Make sure you didn't break anything:
   ```bash
   python -m pytest tests/ -v
   ```

## 🔧 Setup Instructions

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run Tests**:
   ```bash
   python -m pytest tests/ -v
   ```

3. **Try Examples**:
   ```bash
   python examples/basic_usage.py
   ```

## 📝 Coding Standards

### Style Guidelines
- Follow PEP 8 style guidelines
- Use meaningful variable names
- Add type hints to function parameters and return values
- Include docstrings for any new functions you create

### Example Implementation

Here's how you might implement the `reverse_string` function:

```python
def reverse_string(text: str) -> str:
    """
    Reverse the given string.
    
    Args:
        text (str): The input string to reverse
        
    Returns:
        str: The reversed string
    """
    # Method 1: Using string slicing (most Pythonic)
    return text[::-1]
    
    # Alternative methods:
    # Method 2: Using reversed() and join()
    # return ''.join(reversed(text))
    
    # Method 3: Using a loop
    # result = ""
    # for char in text:
    #     result = char + result
    # return result
```

### Testing Your Implementation

After implementing `reverse_string`, you can test it:

```python
# Run the specific test
python -m pytest tests/test_string_utils.py::TestStringUtils::test_reverse_string -v

# Or test it manually
from src.string_utils import reverse_string
print(reverse_string("hello"))  # Should output: "olleh"
```

## 🏆 Recognition

Contributors will be recognized in several ways:

1. **README Contributors Section**: Your name will be added to the contributors list
2. **Git History**: Your commits will be part of the project history
3. **Learning Portfolio**: Use this contribution in your programming portfolio

## 🐛 Found a Bug?

If you find a bug in existing code or tests:

1. Create an issue describing the problem
2. If you know how to fix it, submit a pull request
3. Include test cases that demonstrate the bug

## 💡 Tips for Success

### For Beginners:
- Start with the simplest functions first
- Don't try to implement everything at once
- Read the function's docstring carefully
- Look at the test cases to understand expected behavior
- Use print statements to debug your code

### For Experienced Developers:
- Consider edge cases in your implementations
- Optimize for readability first, then performance
- Add additional test cases if you think of edge cases
- Help review other students' contributions

### Common Pitfalls to Avoid:
- Not handling edge cases (empty strings, negative numbers, etc.)
- Not following the exact function signature (parameter names and types)
- Implementing functionality that doesn't match the docstring
- Not testing your code before submitting

## 📚 Learning Resources

- **Python Basics**: [Python.org Tutorial](https://docs.python.org/3/tutorial/)
- **Style Guide**: [PEP 8](https://pep8.org/)
- **Type Hints**: [Python Type Hints](https://docs.python.org/3/library/typing.html)
- **Testing**: [pytest Documentation](https://docs.pytest.org/)
- **Algorithms**: [Algorithm Visualizations](https://visualgo.net/)

## 🤝 Getting Help

If you're stuck:

1. Read the function's docstring again
2. Look at the test cases for examples
3. Check the hints in the TODO comments
4. Ask for help in project discussions
5. Look up similar functions online for inspiration

## 🎉 Making Your First Contribution

1. Pick a simple function like `reverse_string()`
2. Read its docstring and understand what it should do
3. Look at the test cases in `tests/test_string_utils.py`
4. Implement the function
5. Run the tests to make sure it works
6. Celebrate your contribution! 🎊

Remember: Every expert was once a beginner. Don't be afraid to start small and learn as you go!

---

Happy coding! 🚀