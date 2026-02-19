"""
Directory Operations Module

This module contains functions for directory and filesystem operations.
Students can contribute by implementing the functions marked with TODO comments.

Author: Student Contributors
Last Updated: February 2026
"""

from typing import List, Optional


def list_files(directory: str, extension: Optional[str] = None, recursive: bool = False) -> List[str]:
    """
    List all files in a directory.
    
    Args:
        directory (str): Path to the directory
        extension (Optional[str]): File extension to filter by (e.g., '.txt')
        recursive (bool): Whether to search subdirectories (default: False)
        
    Returns:
        List[str]: List of file paths
        
    Examples:
        >>> files = list_files('/path/to/dir', extension='.py')
        >>> print(files)
        ['script1.py', 'script2.py', 'utils.py']
    
    TODO: Implement directory listing with filtering
    """
    # TODO: Implement file listing
    pass


def create_directory(directory: str, exist_ok: bool = True) -> bool:
    """
    Create a directory (and parent directories if needed).
    
    Args:
        directory (str): Path to the directory to create
        exist_ok (bool): Don't raise error if directory already exists (default: True)
        
    Returns:
        bool: True if creation was successful, False otherwise
        
    TODO: Implement directory creation
    """
    # TODO: Implement directory creation
    pass