#!/usr/bin/python3
"""Module for loading, adding, and saving arguments to a Python list as JSON"""
from sys import argv

# Importing the required functions to handle JSON file loading and saving
load_file = __import__('6-load_from_json_file').load_from_json_file
save_file = __import__('5-save_to_json_file').save_to_json_file

# Attempt to load data from 'add_item.json'
try:
    json_list = load_file('add_item.json')
except (ValueError, FileNotFoundError):
    json_list = []

# Add the command-line arguments to the existing list
for item in argv[1:]:
    json_list.append(item)

# Serialize the updated list as JSON and save it to 'add_item.json
save_file(json_list, 'add_item.json')

