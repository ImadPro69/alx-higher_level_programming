#!/usr/bin/python3
""" 3. Same class or inherit from"""

def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of a_class or its subclasses; otherwise False"""
    return isinstance(obj, a_class)

