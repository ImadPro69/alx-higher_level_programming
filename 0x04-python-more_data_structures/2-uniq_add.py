#!/usr/bin/python3

def uniq_add(my_list=[]):
    # Create an empty set to store unique integers
    unique_integers = set()

    # Iterate over each element in the list
    for num in my_list:
        # Add the integer to the set (duplicates will be automatically ignored)
        unique_integers.add(num)

    # Calculate the sum of the unique integers
    total = sum(unique_integers)

    return total
