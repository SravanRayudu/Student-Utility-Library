"""
Structured Data Module

This module contains functions for handling structured data formats (CSV, JSON).
Students can contribute by implementing the functions marked with TODO comments.

Author: Student Contributors
Last Updated: February 2026
"""

from typing import List, Dict, Any, Union


def read_csv(file_path: str, delimiter: str = ',', encoding: str = 'utf-8') -> List[Dict[str, str]]:
    """
    Read a CSV file and return data as a list of dictionaries.
    
    Args:
        file_path (str): Path to the CSV file
        delimiter (str): CSV delimiter (default: ',')
        encoding (str): File encoding (default: 'utf-8')
        
    Returns:
        List[Dict[str, str]]: List of dictionaries, each representing a row
        
    Examples:
        >>> data = read_csv('employees.csv')
        >>> print(data[0])
        {'name': 'John Doe', 'age': '30', 'department': 'Engineering'}
    
    TODO: Implement CSV reading
    Hint: Use the csv.DictReader class
    """
    # TODO: Implement CSV reading
    pass


def write_csv(file_path: str, data: List[Dict[str, Any]], delimiter: str = ',', encoding: str = 'utf-8') -> None:
    """
    Write data to a CSV file.
    
    Args:
        file_path (str): Path to the CSV file
        data (List[Dict[str, Any]]): Data to write (list of dictionaries)
        delimiter (str): CSV delimiter (default: ',')
        encoding (str): File encoding (default: 'utf-8')
        
    Examples:
        >>> data = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]
        >>> write_csv('people.csv', data)
    
    TODO: Implement CSV writing
    """
    # TODO: Implement CSV writing
    pass


def read_json(file_path: str, encoding: str = 'utf-8') -> Union[Dict[str, Any], List[Any]]:
    """
    Read and parse a JSON file.
    
    Args:
        file_path (str): Path to the JSON file
        encoding (str): File encoding (default: 'utf-8')
        
    Returns:
        Union[Dict[str, Any], List[Any]]: Parsed JSON data
        
    Examples:
        >>> data = read_json('config.json')
        >>> print(data['settings']['debug'])
        True
    
    TODO: Implement JSON reading
    """
    # TODO: Implement JSON reading
    pass


def write_json(file_path: str, data: Union[Dict[str, Any], List[Any]], 
               encoding: str = 'utf-8', indent: int = 2) -> None:
    """
    Write data to a JSON file.
    
    Args:
        file_path (str): Path to the JSON file
        data (Union[Dict[str, Any], List[Any]]): Data to write
        encoding (str): File encoding (default: 'utf-8')
        indent (int): JSON indentation (default: 2)
        
    Examples:
        >>> data = {'name': 'MyApp', 'version': '1.0.0', 'settings': {'debug': False}}
        >>> write_json('config.json', data)
    
    TODO: Implement JSON writing
    """
    # TODO: Implement JSON writing
    pass