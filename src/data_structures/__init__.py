"""
Data Structures Module

This module contains implementations of common data structures.
Students can contribute by implementing the classes and methods in the individual modules.

Covered data structures:
- Stack (LIFO - Last In, First Out)
- Queue (FIFO - First In, First Out)
- Linked List
- Binary Tree
- Hash Table

Author: Student Contributors
Last Updated: February 2026
"""

# Import all data structures from individual modules
from .stack import Stack
from .queue import Queue
from .linked_list import LinkedList, Node
from .binary_tree import BinaryTree, TreeNode
from .hash_table import HashTable

# Make all classes available when importing from data_structures module
__all__ = [
    'Stack',
    'Queue', 
    'LinkedList',
    'Node',
    'BinaryTree',
    'TreeNode',
    'HashTable'
]