"""
Binary Tree Data Structure Module

This module contains the BinaryTree and TreeNode implementations.
Students can contribute by implementing the class methods marked with TODO comments.

Author: Student Contributors
Last Updated: February 2026
"""

from typing import Any, List


class TreeNode:
    """
    A node class for binary tree implementation.
    """
    
    def __init__(self, data: Any):
        """
        Initialize a tree node.
        
        Args:
            data (Any): The data to store in the node
            
        TODO: Initialize node with data, left and right children
        """
        # TODO: Initialize tree node properties
        pass


class BinaryTree:
    """
    A binary tree implementation.
    
    Each node has at most two children: left and right.
    
    Example usage:
        >>> tree = BinaryTree()
        >>> tree.insert(5)
        >>> tree.insert(3)
        >>> tree.insert(7)
        >>> tree.inorder_traversal()
        [3, 5, 7]
    """
    
    def __init__(self):
        """
        Initialize an empty binary tree.
        
        TODO: Initialize the root
        """
        # TODO: Initialize the tree
        pass
    
    def insert(self, data: Any) -> None:
        """
        Insert a new node into the binary search tree.
        
        Args:
            data (Any): The data to insert
            
        TODO: Implement this method
        Hint: For BST, smaller values go left, larger values go right
        """
        # TODO: Implement this method
        pass
    
    def search(self, data: Any) -> bool:
        """
        Search for a value in the tree.
        
        Args:
            data (Any): The data to search for
            
        Returns:
            bool: True if found, False otherwise
            
        TODO: Implement this method
        """
        # TODO: Implement this method
        pass
    
    def inorder_traversal(self) -> List[Any]:
        """
        Perform inorder traversal of the tree.
        
        Inorder: Left -> Root -> Right
        
        Returns:
            List[Any]: List of values in inorder sequence
            
        TODO: Implement this method
        """
        # TODO: Implement this method
        pass
    
    def preorder_traversal(self) -> List[Any]:
        """
        Perform preorder traversal of the tree.
        
        Preorder: Root -> Left -> Right
        
        Returns:
            List[Any]: List of values in preorder sequence
            
        TODO: Implement this method
        """
        # TODO: Implement this method
        pass
    
    def postorder_traversal(self) -> List[Any]:
        """
        Perform postorder traversal of the tree.
        
        Postorder: Left -> Right -> Root
        
        Returns:
            List[Any]: List of values in postorder sequence
            
        TODO: Implement this method
        """
        # TODO: Implement this method
        pass