"""
Examples demonstrating how to use the Student Utility Library.

This file shows practical examples of using the various utility functions
once they are implemented by students.

Run this file with: python examples/basic_usage.py
"""

# Import utility functions from different modules
from src.string_utils import reverse_string, is_palindrome, count_words
from src.math_utils import factorial, is_prime, fibonacci
from src.data_structures import Stack, Queue, LinkedList
from src.algorithms import bubble_sort, binary_search
from src.file_utils import read_file, write_file


def string_utils_examples():
    """Examples using string utility functions."""
    print("=== String Utilities Examples ===")
    
    # Example 1: Text processing
    text = "Hello, World!"
    try:
        reversed_text = reverse_string(text)
        print(f"Original: {text}")
        print(f"Reversed: {reversed_text}")
    except Exception as e:
        print(f"reverse_string not implemented: {e}")
    
    # Example 2: Palindrome checking
    test_strings = ["racecar", "hello", "A man a plan a canal Panama"]
    for s in test_strings:
        try:
            result = is_palindrome(s)
            print(f"'{s}' is palindrome: {result}")
        except Exception as e:
            print(f"is_palindrome not implemented: {e}")
            break
    
    # Example 3: Word counting
    sentences = [
        "The quick brown fox jumps over the lazy dog",
        "Python is an amazing programming language",
        "Hello world"
    ]
    for sentence in sentences:
        try:
            word_count = count_words(sentence)
            print(f"'{sentence}' has {word_count} words")
        except Exception as e:
            print(f"count_words not implemented: {e}")
            break
    
    print()


def math_utils_examples():
    """Examples using math utility functions."""
    print("=== Math Utilities Examples ===")
    
    # Example 1: Factorial calculations
    numbers = [0, 1, 5, 10]
    for n in numbers:
        try:
            result = factorial(n)
            print(f"Factorial of {n} = {result}")
        except Exception as e:
            print(f"factorial not implemented: {e}")
            break
    
    # Example 2: Prime number checking
    test_numbers = [2, 4, 17, 25, 97, 100]
    print("\\nPrime number check:")
    for num in test_numbers:
        try:
            is_prime_result = is_prime(num)
            print(f"{num} is prime: {is_prime_result}")
        except Exception as e:
            print(f"is_prime not implemented: {e}")
            break
    
    # Example 3: Fibonacci sequence
    try:
        fib_10 = fibonacci(10)
        print(f"\\nFirst 10 Fibonacci numbers: {fib_10}")
    except Exception as e:
        print(f"fibonacci not implemented: {e}")
    
    print()


def data_structures_examples():
    """Examples using data structures."""
    print("=== Data Structures Examples ===")
    
    # Example 1: Stack usage
    print("Stack Example:")
    try:
        stack = Stack()
        
        # Push some items
        items = [1, 2, 3, 4, 5]
        for item in items:
            stack.push(item)
        
        print(f"Stack size: {stack.size()}")
        
        # Pop items
        while not stack.is_empty():
            print(f"Popped: {stack.pop()}")
            
    except Exception as e:
        print(f"Stack not implemented: {e}")
    
    # Example 2: Queue usage
    print("\\nQueue Example:")
    try:
        queue = Queue()
        
        # Enqueue some items
        items = ["first", "second", "third"]
        for item in items:
            queue.enqueue(item)
        
        print(f"Queue size: {queue.size()}")
        
        # Dequeue items
        while not queue.is_empty():
            print(f"Dequeued: {queue.dequeue()}")
            
    except Exception as e:
        print(f"Queue not implemented: {e}")
    
    # Example 3: Linked List usage
    print("\\nLinked List Example:")
    try:
        ll = LinkedList()
        
        # Add some items
        items = [10, 20, 30, 40]
        for item in items:
            ll.append(item)
        
        print(f"List contents: {ll.to_list()}")
        print(f"List size: {ll.size()}")
        
        # Search for items
        search_items = [20, 50]
        for item in search_items:
            found = ll.find(item)
            print(f"Found {item}: {found}")
            
    except Exception as e:
        print(f"LinkedList not implemented: {e}")
    
    print()


def algorithms_examples():
    """Examples using algorithms."""
    print("=== Algorithms Examples ===")
    
    # Example 1: Sorting algorithms
    unsorted_data = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original array: {unsorted_data}")
    
    try:
        sorted_data = bubble_sort(unsorted_data.copy())
        print(f"Bubble sorted: {sorted_data}")
    except Exception as e:
        print(f"bubble_sort not implemented: {e}")
    
    # Example 2: Binary search
    sorted_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    search_targets = [7, 4, 15, 20]
    
    print(f"\\nSearching in: {sorted_array}")
    for target in search_targets:
        try:
            index = binary_search(sorted_array, target)
            if index != -1:
                print(f"Found {target} at index {index}")
            else:
                print(f"{target} not found")
        except Exception as e:
            print(f"binary_search not implemented: {e}")
            break
    
    print()


def file_utils_examples():
    """Examples using file utilities."""
    print("=== File Utilities Examples ===")
    
    # Example 1: Writing and reading a file
    filename = "example_output.txt"
    content = "Hello from the Student Utility Library!\\nThis is a test file.\\nPython is awesome!"
    
    try:
        # Write file
        write_file(filename, content)
        print(f"✓ Written content to {filename}")
        
        # Read file back
        read_content = read_file(filename)
        print(f"✓ Read content from {filename}:")
        print(read_content)
        
        # Clean up
        import os
        if os.path.exists(filename):
            os.remove(filename)
            print(f"✓ Cleaned up {filename}")
            
    except Exception as e:
        print(f"File utilities not implemented: {e}")
    
    print()


def main():
    """Run all examples."""
    print("Student Utility Library - Usage Examples")
    print("=" * 50)
    print("Note: Some functions may not work until implemented by students!")
    print()
    
    # Run all example categories
    string_utils_examples()
    math_utils_examples() 
    data_structures_examples()
    algorithms_examples()
    file_utils_examples()
    
    print("Examples completed!")
    print("\\n💡 Tip for Students:")
    print("- Look for functions with 'TODO: Implement this function' comments")
    print("- Read the docstrings carefully for implementation guidance")
    print("- Run tests with: python -m pytest tests/ -v")
    print("- Start with simpler functions and work your way up!")


if __name__ == "__main__":
    main()