"""
Hash Table Data Structure Module

This module contains the HashTable implementation.
Students can contribute by implementing the class methods marked with TODO comments.

Author: Student Contributors
Last Updated: February 2026
"""

from typing import Any, List


class HashTable:
    """
    A simple hash table implementation using separate chaining.
    
    Uses a list of lists to handle collisions.
    
    Example usage:
        >>> ht = HashTable()
        >>> ht.put("key1", "value1")
        >>> ht.get("key1")
        "value1"
    """
    
    def __init__(self, size: int = 10):
        """
        Initialize a hash table with the given size.
        
        Args:
            size (int): The size of the hash table (default: 10)
            
        TODO: Initialize the hash table structure
        """
        # TODO: Initialize the hash table
        pass
    
    def _hash(self, key: str) -> int:
        """
        Hash function to convert key to array index.
        
        Args:
            key (str): The key to hash
            
        Returns:
            int: The hash value (array index)
            
        TODO: Implement a simple hash function
        Hint: You can sum ASCII values of characters and use modulo
        """
        # TODO: Implement hash function
        pass
    
    def put(self, key: str, value: Any) -> None:
        """
        Insert a key-value pair into the hash table.
        
        Args:
            key (str): The key
            value (Any): The value to associate with the key
            
        TODO: Implement this method
        """
        # TODO: Implement this method
        pass
    
    def get(self, key: str) -> Any:
        """
        Retrieve a value by its key.
        
        Args:
            key (str): The key to search for
            
        Returns:
            Any: The value associated with the key
            
        Raises:
            KeyError: If the key is not found
            
        TODO: Implement this method
        """
        # TODO: Implement this method
        pass
    
    def delete(self, key: str) -> bool:
        """
        Delete a key-value pair from the hash table.
        
        Args:
            key (str): The key to delete
            
        Returns:
            bool: True if the key was found and deleted, False otherwise
            
        TODO: Implement this method
        """
        # TODO: Implement this method
        pass
    
    def keys(self) -> List[str]:
        """
        Get all keys in the hash table.
        
        Returns:
            List[str]: List of all keys
            
        TODO: Implement this method
        """
        # TODO: Implement this method
        pass