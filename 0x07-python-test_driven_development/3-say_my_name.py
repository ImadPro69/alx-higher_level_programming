#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    """
    Prints the name in the format "My name is <first_name> <last_name>".

    Args:
        first_name (str): The First Name.
        last_name (str): The last name. Default is an empty string.

    Raises:
        TypeError: If first_name or last_name is not a string.

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if last_name:
        full_name = f"My name is {first_name} {last_name}"
    else:
        full_name = f"My name is {first_name}"

    print(full_name)

