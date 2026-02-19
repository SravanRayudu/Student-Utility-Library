"""
Linked List Data Structure Module

This module contains the LinkedList and Node implementations.
Students can contribute by implementing the class methods marked with TODO comments.

Author: Student Contributors
Last Updated: February 2026
"""

from typing import Any, List


class Node:
    """
    A node class for linked list implementation.
    
    Each node contains data and a reference to the next node.
    """
    
    def __init__(self, data: Any):
        """
        Initialize a node with data.
        
        Args:
            data (Any): The data to store in the node
            
        TODO: Initialize the node with data and next pointer
        """
        # TODO: Initialize node properties
        pass


class LinkedList:
    """
    A singly linked list implementation.
    
    Each element points to the next element in the sequence.
    
    Example usage:
        >>> ll = LinkedList()
        >>> ll.append(1)
        >>> ll.append(2)
        >>> ll.prepend(0)
        >>> ll.to_list()
        [0, 1, 2]
    """
    
    def __init__(self):
        """
        Initialize an empty linked list.
        
        TODO: Initialize the head pointer
        """
        # TODO: Initialize the linked list
        pass
    
    def append(self, data: Any) -> None:
        """
        Add an element to the end of the list.
        
        Args:
            data (Any): The data to add
            
        TODO: Implement this method
        Hint: Create a new node and link it at the end
        """
        # TODO: Implement this method
        pass
    
    def prepend(self, data: Any) -> None:
        """
        Add an element to the beginning of the list.
        
        Args:
            data (Any): The data to add
            
        TODO: Implement this method
        """
        # TODO: Implement this method
        pass
    
    def delete(self, data: Any) -> bool:
        """
        Delete the first occurrence of data from the list.
        
        Args:
            data (Any): The data to delete
            
        Returns:
            bool: True if the item was found and deleted, False otherwise
            
        TODO: Implement this method
        """
        # TODO: Implement this method
        pass
    
    def find(self, data: Any) -> bool:
        """
        Check if an element exists in the list.
        
        Args:
            data (Any): The data to search for
            
        Returns:
            bool: True if found, False otherwise
            
        TODO: Implement this method
        """
        # TODO: Implement this method
        pass
    
    def size(self) -> int:
        """
        Get the number of elements in the list.
        
        Returns:
            int: The number of elements
            
        TODO: Implement this method
        """
        # TODO: Implement this method
        pass
    
    def to_list(self) -> List[Any]:
        """
        Convert the linked list to a Python list.
        
        Returns:
            List[Any]: A list containing all elements
            
        TODO: Implement this method
        """
        # TODO: Implement this method
        pass