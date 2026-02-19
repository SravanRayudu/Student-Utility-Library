"""
Stack Data Structure Module

This module contains the Stack implementation.
Students can contribute by implementing the class methods marked with TODO comments.

Author: Student Contributors
Last Updated: February 2026
"""

from typing import Any


class Stack:
    """
    A Stack implementation using a list.
    
    Stack follows LIFO (Last In, First Out) principle.
    Elements are added and removed from the top of the stack.
    
    Example usage:
        >>> stack = Stack()
        >>> stack.push(1)
        >>> stack.push(2) 
        >>> stack.pop()
        2
        >>> stack.peek()
        1
    """
    
    def __init__(self):
        """
        Initialize an empty stack.
        
        TODO: Initialize the internal data structure to store stack elements
        Hint: Use a Python list to store the elements
        """
        # TODO: Initialize the stack
        pass
    
    def push(self, item: Any) -> None:
        """
        Add an item to the top of the stack.
        
        Args:
            item (Any): The item to add to the stack
            
        TODO: Implement this method
        Hint: Add the item to the end of the list
        """
        # TODO: Implement this method
        pass
    
    def pop(self) -> Any:
        """
        Remove and return the top item from the stack.
        
        Returns:
            Any: The item that was at the top of the stack
            
        Raises:
            IndexError: If the stack is empty
            
        TODO: Implement this method
        Hint: Remove and return the last item from the list
        """
        # TODO: Implement this method
        pass
    
    def peek(self) -> Any:
        """
        Return the top item without removing it.
        
        Returns:
            Any: The item at the top of the stack
            
        Raises:
            IndexError: If the stack is empty
            
        TODO: Implement this method
        """
        # TODO: Implement this method
        pass
    
    def is_empty(self) -> bool:
        """
        Check if the stack is empty.
        
        Returns:
            bool: True if stack is empty, False otherwise
            
        TODO: Implement this method
        """
        # TODO: Implement this method
        pass
    
    def size(self) -> int:
        """
        Get the number of items in the stack.
        
        Returns:
            int: The number of items in the stack
            
        TODO: Implement this method
        """
        # TODO: Implement this method
        pass