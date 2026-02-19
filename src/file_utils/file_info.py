"""
File Information Module

This module contains functions for getting file information and properties.
Students can contribute by implementing the functions marked with TODO comments.

Author: Student Contributors
Last Updated: February 2026
"""

from typing import Dict, Any


def get_file_info(file_path: str) -> Dict[str, Any]:
    """
    Get information about a file.
    
    Args:
        file_path (str): Path to the file
        
    Returns:
        Dict[str, Any]: Dictionary containing file information (size, creation time, etc.)
        
    Examples:
        >>> info = get_file_info('document.pdf')
        >>> print(info['size_bytes'])
        1024000
    
    TODO: Implement file information gathering
    Hint: Use os.path.getsize(), os.path.getctime(), os.path.getmtime()
    """
    # TODO: Implement file info gathering
    pass


def get_file_extension(file_path: str) -> str:
    """
    Get the file extension from a file path.
    
    Args:
        file_path (str): Path to the file
        
    Returns:
        str: File extension (including the dot, e.g., '.txt')
        
    Examples:
        >>> get_file_extension('document.pdf')
        '.pdf'
        >>> get_file_extension('archive.tar.gz')
        '.gz'
    
    TODO: Implement file extension extraction
    """
    # TODO: Implement file extension extraction
    pass


def change_file_extension(file_path: str, new_extension: str) -> str:
    """
    Change the extension of a file path.
    
    Args:
        file_path (str): Original file path
        new_extension (str): New extension (with or without dot)
        
    Returns:
        str: File path with new extension
        
    Examples:
        >>> change_file_extension('report.docx', '.pdf')
        'report.pdf'
        >>> change_file_extension('data.csv', 'json')
        'data.json'
    
    TODO: Implement file extension changing
    """
    # TODO: Implement file extension changing
    pass