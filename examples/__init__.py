"""
Examples Module for Student Utility Library

This module contains demonstration scripts showing how to use
the various utility functions in the library.

Available examples:
- algorithms_examples.py: Algorithm implementations
- string_utils_examples.py: String manipulation utilities  
- math_utils_examples.py: Mathematical operations
- data_structures_examples.py: Data structure implementations
- file_utils_examples.py: File and directory operations

Usage:
Run any example file directly:
    python examples/algorithms_examples.py
    python examples/string_utils_examples.py
    python examples/math_utils_examples.py
    python examples/data_structures_examples.py
    python examples/file_utils_examples.py

Or import and use specific demonstration functions:
    from examples.algorithms_examples import demonstrate_sorting
    from examples.file_utils_examples import demonstrate_basic_operations
"""

# Make example modules easily importable
__all__ = [
    'algorithms_examples',
    'string_utils_examples', 
    'math_utils_examples',
    'data_structures_examples',
    'file_utils_examples'
]

def run_all_examples():
    """
    Run all available examples.
    
    This function executes all example scripts to demonstrate
    the complete functionality of the utility library.
    
    Note: This will only work after students implement the functions!
    """
    print("🚀 Running all Student Utility Library examples...")
    print("=" * 60)
    
    examples = [
        ("Algorithms", "algorithms_examples"),
        ("String Utils", "string_utils_examples"),
        ("Math Utils", "math_utils_examples"), 
        ("Data Structures", "data_structures_examples"),
        ("File Utils", "file_utils_examples")
    ]
    
    for name, module_name in examples:
        try:
            print(f"\n{'='*20} {name} {'='*20}")
            module = __import__(f"examples.{module_name}", fromlist=[module_name])
            if hasattr(module, 'main'):
                module.main()
            else:
                print(f"No main() function found in {module_name}")
        except Exception as e:
            print(f"❌ Error running {name} examples: {e}")
            print("This is expected until functions are implemented!")
    
    print(f"\n{'='*60}")
    print("✅ All examples completed!")


if __name__ == "__main__":
    run_all_examples()