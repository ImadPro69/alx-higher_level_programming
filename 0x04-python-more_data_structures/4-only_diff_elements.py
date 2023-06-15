#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    # Create an empty set to store the elements present in only one set
    diff_set = set()

    # Iterate over each element in the first set
    for item in set_1:
        # Check if the element is not present in the second set
        if item not in set_2:
            # If it is not, add it to the diff_set
            diff_set.add(item)

    # Iterate over each element in the second set
    for item in set_2:
        # Check if the element is not present in the first set
        if item not in set_1:
            # If it is not, add it to the diff_set
            diff_set.add(item)

    return diff_set
