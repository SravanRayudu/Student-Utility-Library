"""
File Utilities Module Examples

This file demonstrates the usage of various file utility functions.
Students can run this file to see examples of how each function works.

Run with: python examples/file_utils_examples.py
"""

import os
import tempfile
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


def demonstrate_basic_operations():
    """Demonstrate basic file reading and writing operations."""
    print("\n" + "="*50)
    print("BASIC FILE OPERATIONS")
    print("="*50)
    
    # Create a temporary file for demonstration
    demo_file = "demo_file.txt"
    demo_content = """Welcome to the Student Utility Library!
    
This is a demonstration of file operations.
We can read files, write files, and manipulate them.
Python makes file handling easy and powerful.

Key concepts:
- File reading and writing
- Text processing
- Error handling
- File system operations"""
    
    try:
        print("1. Writing content to file...")
        write_file(demo_file, demo_content)
        print(f"   ✓ Content written to '{demo_file}'")
        
        print("\n2. Reading file content...")
        content = read_file(demo_file)
        print(f"   ✓ Read {len(content)} characters from file")
        print(f"   Preview: {content[:50]}...")
        
        print("\n3. Reading file as lines...")
        lines = read_lines(demo_file)
        print(f"   ✓ File has {len(lines)} lines")
        print(f"   First line: {lines[0].strip()}")
        
        print("\n4. Counting lines and words...")
        line_count = count_lines(demo_file)
        word_count = count_words(demo_file)
        print(f"   ✓ Lines: {line_count}")
        print(f"   ✓ Words: {word_count}")
        
        print("\n5. Searching in file...")
        matches = find_in_file(demo_file, "Python")
        print(f"   ✓ Found 'Python' in {len(matches)} lines")
        for line_num, line_content in matches:
            print(f"      Line {line_num}: {line_content.strip()}")
        
        # Clean up
        delete_file(demo_file)
        print(f"\n   ✓ Demo file deleted")
        
    except Exception as e:
        print(f"   ✗ Error: {e}")


def demonstrate_file_operations():
    """Demonstrate file copy, move, and delete operations."""
    print("\n" + "="*50)
    print("FILE MANIPULATION OPERATIONS")
    print("="*50)
    
    original_file = "original.txt"
    copied_file = "copied.txt"
    moved_file = "moved.txt"
    
    try:
        print("1. Creating original file...")
        write_file(original_file, "This is the original file content.")
        print(f"   ✓ Created '{original_file}'")
        
        print("\n2. Copying file...")
        success = copy_file(original_file, copied_file)
        if success:
            print(f"   ✓ Copied to '{copied_file}'")
            
            # Verify copy
            original_content = read_file(original_file)
            copied_content = read_file(copied_file)
            if original_content == copied_content:
                print("   ✓ Copy verified - contents match")
        
        print("\n3. Moving file...")
        success = move_file(copied_file, moved_file)
        if success:
            print(f"   ✓ Moved '{copied_file}' to '{moved_file}'")
            print(f"   ✓ Original copy no longer exists: {not os.path.exists(copied_file)}")
        
        print("\n4. Getting file information...")
        info = get_file_info(original_file)
        print(f"   ✓ File size: {info.get('size_bytes', 'N/A')} bytes")
        print(f"   ✓ Created: {info.get('created_time', 'N/A')}")
        print(f"   ✓ Modified: {info.get('modified_time', 'N/A')}")
        
        print("\n5. Cleaning up...")
        delete_file(original_file)
        delete_file(moved_file)
        print("   ✓ All demo files deleted")
        
    except Exception as e:
        print(f"   ✗ Error: {e}")
        # Clean up in case of error
        for file in [original_file, copied_file, moved_file]:
            if os.path.exists(file):
                os.unlink(file)


def demonstrate_directory_operations():
    """Demonstrate directory creation and file listing."""
    print("\n" + "="*50)
    print("DIRECTORY OPERATIONS")
    print("="*50)
    
    demo_dir = "demo_directory"
    
    try:
        print("1. Creating directory...")
        success = create_directory(demo_dir)
        if success:
            print(f"   ✓ Created directory '{demo_dir}'")
        
        print("\n2. Creating files in directory...")
        test_files = [
            ("readme.txt", "This is a readme file."),
            ("data.csv", "name,age,city\nAlice,25,NYC\nBob,30,SF"),
            ("config.json", '{"debug": true, "port": 8080}'),
            ("script.py", "print('Hello from Python!')"),
            ("notes.md", "# Notes\n\nThis is a markdown file.")
        ]
        
        for filename, content in test_files:
            file_path = os.path.join(demo_dir, filename)
            write_file(file_path, content)
            print(f"   ✓ Created {filename}")
        
        print("\n3. Listing all files...")
        all_files = list_files(demo_dir)
        print(f"   ✓ Found {len(all_files)} files:")
        for file in all_files:
            print(f"      - {file}")
        
        print("\n4. Listing files by extension...")
        extensions = ['.txt', '.py', '.json']
        for ext in extensions:
            files = list_files(demo_dir, extension=ext)
            print(f"   ✓ {ext} files: {files}")
        
        print("\n5. Cleaning up...")
        # Delete all files in directory first
        for file in all_files:
            delete_file(file)
        # Then remove the directory
        os.rmdir(demo_dir)
        print(f"   ✓ Directory '{demo_dir}' and contents removed")
        
    except Exception as e:
        print(f"   ✗ Error: {e}")


def demonstrate_structured_data():
    """Demonstrate CSV and JSON operations."""
    print("\n" + "="*50)
    print("STRUCTURED DATA OPERATIONS")
    print("="*50)
    
    csv_file = "students.csv"
    json_file = "config.json"
    
    try:
        print("1. Working with CSV data...")
        
        # Sample student data
        student_data = [
            {'name': 'Alice Johnson', 'age': '20', 'major': 'Computer Science', 'gpa': '3.8'},
            {'name': 'Bob Smith', 'age': '21', 'major': 'Mathematics', 'gpa': '3.6'},
            {'name': 'Charlie Brown', 'age': '19', 'major': 'Physics', 'gpa': '3.9'},
            {'name': 'Diana Prince', 'age': '22', 'major': 'Engineering', 'gpa': '3.7'}
        ]
        
        # Write CSV
        write_csv(csv_file, student_data)
        print(f"   ✓ Written {len(student_data)} student records to CSV")
        
        # Read CSV
        loaded_data = read_csv(csv_file)
        print(f"   ✓ Read {len(loaded_data)} records from CSV")
        
        # Display sample data
        print("   Sample records:")
        for i, student in enumerate(loaded_data[:2]):
            print(f"      {i+1}. {student['name']} - {student['major']} (GPA: {student['gpa']})")
        
        print("\n2. Working with JSON data...")
        
        # Sample configuration data
        config_data = {
            "application": {
                "name": "Student Management System",
                "version": "2.1.0",
                "debug": True
            },
            "database": {
                "host": "localhost",
                "port": 5432,
                "name": "students_db"
            },
            "features": {
                "authentication": True,
                "logging": True,
                "email_notifications": False
            },
            "allowed_extensions": [".jpg", ".png", ".pdf", ".docx"],
            "max_file_size_mb": 10
        }
        
        # Write JSON
        write_json(json_file, config_data)
        print(f"   ✓ Configuration data written to JSON")
        
        # Read JSON
        loaded_config = read_json(json_file)
        print(f"   ✓ Configuration data loaded from JSON")
        
        # Display sample configuration
        print("   Configuration summary:")
        print(f"      App: {loaded_config['application']['name']} v{loaded_config['application']['version']}")
        print(f"      Debug mode: {loaded_config['application']['debug']}")
        print(f"      Database: {loaded_config['database']['name']} on {loaded_config['database']['host']}")
        print(f"      Max file size: {loaded_config['max_file_size_mb']} MB")
        
        print("\n3. Cleaning up...")
        delete_file(csv_file)
        delete_file(json_file)
        print("   ✓ Data files deleted")
        
    except Exception as e:
        print(f"   ✗ Error: {e}")


def demonstrate_file_extensions():
    """Demonstrate file extension utilities."""
    print("\n" + "="*50)
    print("FILE EXTENSION UTILITIES")
    print("="*50)
    
    try:
        print("1. Getting file extensions...")
        test_files = [
            "document.pdf",
            "photo.jpg",
            "archive.tar.gz",
            "script.py",
            "README",
            "data.backup.2023.csv"
        ]
        
        for filename in test_files:
            extension = get_file_extension(filename)
            print(f"   '{filename}' → Extension: '{extension}'")
        
        print("\n2. Changing file extensions...")
        changes = [
            ("report.docx", ".pdf", "Converting Word document to PDF"),
            ("data.csv", ".json", "Converting CSV to JSON format"),
            ("backup.old", ".bak", "Standardizing backup extension"),
            ("image.jpeg", ".jpg", "Standardizing image extension")
        ]
        
        for old_name, new_ext, description in changes:
            new_name = change_file_extension(old_name, new_ext)
            print(f"   {description}")
            print(f"      '{old_name}' → '{new_name}'")
        
        print("\n3. Practical use cases...")
        print("   ✓ Batch renaming files")
        print("   ✓ File format conversion preparation")
        print("   ✓ Organizing files by type")
        print("   ✓ Backup file management")
        
    except Exception as e:
        print(f"   ✗ Error: {e}")


def main():
    """Main demonstration function."""
    print("🚀 Student Utility Library - File Utils Examples")
    print("=" * 60)
    print("\nThis demonstration shows how to use the file utility functions.")
    print("Note: Functions must be implemented first!")
    
    try:
        demonstrate_basic_operations()
        demonstrate_file_operations()
        demonstrate_directory_operations()
        demonstrate_structured_data()
        demonstrate_file_extensions()
        
        print("\n" + "="*60)
        print("✅ DEMONSTRATION COMPLETE")
        print("="*60)
        print("\nNext steps for students:")
        print("1. Implement the functions in src/file_utils/ modules")
        print("2. Run the tests: python -m pytest tests/test_file_utils.py -v")
        print("3. Experiment with your own file operations")
        print("4. Add error handling and edge cases")
        print("5. Extend functionality with additional features")
        
    except Exception as e:
        print(f"\n❌ Demo failed: {e}")
        print("\nThis is expected until students implement the functions!")
        print("Check src/file_utils/ for function templates to implement.")


if __name__ == "__main__":
    main()