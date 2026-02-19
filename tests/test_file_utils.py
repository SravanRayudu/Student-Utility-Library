"""
Test file for file utilities module.

This file contains unit tests for all file utility functions.
Students should run these tests to verify their implementations.

Run tests with: python -m pytest tests/test_file_utils.py -v
"""

import pytest
import os
import tempfile
import json
import csv
from src.file_utils import (
    read_file,
    write_file,
    read_lines,
    count_lines,
    count_words,
    find_in_file,
    copy_file,
    move_file,
    delete_file,
    get_file_info,
    list_files,
    create_directory,
    read_csv,
    write_csv,
    read_json,
    write_json,
    get_file_extension,
    change_file_extension
)


class TestFileUtils:
    """Test cases for file utility functions."""
    
    def test_read_write_file(self):
        """Test basic file reading and writing."""
        # Test data
        test_content = "Hello, World!\nThis is a test file.\nPython is awesome!"
        
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            temp_file = f.name
        
        try:
            # Test writing
            write_file(temp_file, test_content)
            
            # Test reading
            read_content = read_file(temp_file)
            assert read_content == test_content
            
            # Test append mode
            append_text = "\nAppended line"
            write_file(temp_file, append_text, append=True)
            
            final_content = read_file(temp_file)
            assert final_content == test_content + append_text
            
        finally:
            if os.path.exists(temp_file):
                os.unlink(temp_file)
    
    def test_read_lines(self):
        """Test reading file lines."""
        test_content = "Line 1\nLine 2\nLine 3"
        
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write(test_content)
            temp_file = f.name
        
        try:
            lines = read_lines(temp_file)
            expected_lines = ["Line 1\n", "Line 2\n", "Line 3"]
            assert lines == expected_lines
            
        finally:
            if os.path.exists(temp_file):
                os.unlink(temp_file)
    
    def test_count_lines(self):
        """Test counting lines in a file."""
        test_content = "Line 1\nLine 2\nLine 3\nLine 4"
        
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write(test_content)
            temp_file = f.name
        
        try:
            line_count = count_lines(temp_file)
            assert line_count == 4
            
        finally:
            if os.path.exists(temp_file):
                os.unlink(temp_file)
    
    def test_count_words(self):
        """Test counting words in a file."""
        test_content = "Hello world this is a test file with ten words"
        
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write(test_content)
            temp_file = f.name
        
        try:
            word_count = count_words(temp_file)
            assert word_count == 10
            
        finally:
            if os.path.exists(temp_file):
                os.unlink(temp_file)
    
    def test_find_in_file(self):
        """Test searching for text in a file."""
        test_content = "Line 1: ERROR occurred\nLine 2: Normal operation\nLine 3: Another ERROR"
        
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write(test_content)
            temp_file = f.name
        
        try:
            matches = find_in_file(temp_file, "ERROR")
            expected_matches = [
                (1, "Line 1: ERROR occurred"),
                (3, "Line 3: Another ERROR")
            ]
            assert len(matches) == 2
            
        finally:
            if os.path.exists(temp_file):
                os.unlink(temp_file)
    
    def test_file_operations(self):
        """Test file copy, move, and delete operations."""
        test_content = "Test file for operations"
        
        # Create original file
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write(test_content)
            original_file = f.name
        
        try:
            # Test copy
            copy_file_path = original_file + '.copy'
            success = copy_file(original_file, copy_file_path)
            assert success == True
            assert os.path.exists(copy_file_path)
            assert read_file(copy_file_path) == test_content
            
            # Test move
            move_file_path = original_file + '.moved'
            success = move_file(copy_file_path, move_file_path)
            assert success == True
            assert not os.path.exists(copy_file_path)
            assert os.path.exists(move_file_path)
            
            # Test delete
            success = delete_file(move_file_path)
            assert success == True
            assert not os.path.exists(move_file_path)
            
        finally:
            # Clean up any remaining files
            for file_path in [original_file, copy_file_path, move_file_path]:
                if os.path.exists(file_path):
                    os.unlink(file_path)
    
    def test_get_file_info(self):
        """Test getting file information."""
        test_content = "Test file for info"
        
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write(test_content)
            temp_file = f.name
        
        try:
            info = get_file_info(temp_file)
            
            # Check that required keys exist
            required_keys = ['size_bytes', 'created_time', 'modified_time']
            for key in required_keys:
                assert key in info
            
            # Check that size is reasonable
            assert info['size_bytes'] > 0
            
        finally:
            if os.path.exists(temp_file):
                os.unlink(temp_file)
    
    def test_directory_operations(self):
        """Test directory creation and file listing."""
        with tempfile.TemporaryDirectory() as temp_dir:
            # Test directory creation
            new_dir = os.path.join(temp_dir, 'new_directory')
            success = create_directory(new_dir)
            assert success == True
            assert os.path.exists(new_dir)
            
            # Create some test files
            test_files = ['file1.txt', 'file2.py', 'file3.txt']
            for filename in test_files:
                file_path = os.path.join(new_dir, filename)
                with open(file_path, 'w') as f:
                    f.write("test content")
            
            # Test file listing
            all_files = list_files(new_dir)
            assert len(all_files) == 3
            
            # Test file listing with extension filter
            txt_files = list_files(new_dir, extension='.txt')
            assert len(txt_files) == 2
    
    def test_csv_operations(self):
        """Test CSV reading and writing."""
        test_data = [
            {'name': 'Alice', 'age': '25', 'city': 'New York'},
            {'name': 'Bob', 'age': '30', 'city': 'San Francisco'},
            {'name': 'Charlie', 'age': '35', 'city': 'Chicago'}
        ]
        
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as f:
            temp_file = f.name
        
        try:
            # Test writing CSV
            write_csv(temp_file, test_data)
            
            # Test reading CSV
            read_data = read_csv(temp_file)
            
            assert len(read_data) == len(test_data)
            assert read_data[0]['name'] == 'Alice'
            assert read_data[1]['age'] == '30'
            assert read_data[2]['city'] == 'Chicago'
            
        finally:
            if os.path.exists(temp_file):
                os.unlink(temp_file)
    
    def test_json_operations(self):
        """Test JSON reading and writing."""
        test_data = {
            'name': 'MyApp',
            'version': '1.0.0',
            'settings': {
                'debug': True,
                'max_connections': 100
            },
            'features': ['auth', 'logging', 'caching']
        }
        
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as f:
            temp_file = f.name
        
        try:
            # Test writing JSON
            write_json(temp_file, test_data)
            
            # Test reading JSON
            read_data = read_json(temp_file)
            
            assert read_data['name'] == 'MyApp'
            assert read_data['version'] == '1.0.0'
            assert read_data['settings']['debug'] == True
            assert read_data['settings']['max_connections'] == 100
            assert 'auth' in read_data['features']
            
        finally:
            if os.path.exists(temp_file):
                os.unlink(temp_file)
    
    def test_file_extension_operations(self):
        """Test file extension functions."""
        # Test getting file extension
        assert get_file_extension('document.pdf') == '.pdf'
        assert get_file_extension('archive.tar.gz') == '.gz'
        assert get_file_extension('file_without_extension') == ''
        
        # Test changing file extension
        assert change_file_extension('report.docx', '.pdf') == 'report.pdf'
        assert change_file_extension('data.csv', 'json') == 'data.json'
        assert change_file_extension('file.old.ext', '.new') == 'file.old.new'


# Example usage and demonstration
if __name__ == "__main__":
    print("File Utilities Test Examples")
    print("=" * 40)
    
    # Note: These will fail until students implement the functions
    try:
        # Create a temporary test file
        test_content = "Hello, World!\nThis is a test file.\nPython is awesome!"
        test_file = "temp_test_file.txt"
        
        print("Testing file operations...")
        write_file(test_file, test_content)
        content = read_file(test_file)
        print(f"✓ File written and read successfully")
        print(f"✓ Content length: {len(content)} characters")
        
        lines = count_lines(test_file)
        words = count_words(test_file)
        print(f"✓ File has {lines} lines and {words} words")
        
        # Clean up
        delete_file(test_file)
        print(f"✓ Test file deleted")
        
        # Test file extensions
        print(f"✓ Extension of 'file.pdf': {get_file_extension('file.pdf')}")
        print(f"✓ Changed extension: {change_file_extension('doc.txt', '.md')}")
        
    except Exception as e:
        print(f"Functions not implemented yet: {e}")
        print("Students need to implement the functions to see results!")