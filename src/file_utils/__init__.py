"""
File Utilities Module

This module contains utility functions for file and directory operations.
Students can contribute by implementing the functions in the individual modules.

Covered operations:
- Basic file operations (reading, writing, copying, moving, deleting)
- File content analysis (line counting, word counting, searching)
- Directory operations (listing, creating)
- File information and metadata
- Structured data handling (CSV and JSON)

Author: Student Contributors
Last Updated: February 2026
"""

# Import all file utilities from individual modules
from .basic_operations import (
    read_file,
    write_file,
    copy_file,
    move_file,
    delete_file
)

from .content_analysis import (
    read_lines,
    count_lines,
    count_words,
    find_in_file
)

from .directory_operations import (
    list_files,
    create_directory
)

from .file_info import (
    get_file_info,
    get_file_extension,
    change_file_extension
)

from .structured_data import (
    read_csv,
    write_csv,
    read_json,
    write_json
)

# Make all functions available when importing from file_utils module
__all__ = [
    # Basic file operations
    'read_file',
    'write_file',
    'copy_file',
    'move_file',
    'delete_file',
    
    # Content analysis
    'read_lines',
    'count_lines',
    'count_words',
    'find_in_file',
    
    # Directory operations
    'list_files',
    'create_directory',
    
    # File information
    'get_file_info',
    'get_file_extension',
    'change_file_extension',
    
    # Structured data
    'read_csv',
    'write_csv',
    'read_json',
    'write_json'
]