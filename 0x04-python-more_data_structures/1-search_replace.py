#!/usr/bin/python3

def search_replace(my_list, search, replace):
    # Create a new list to store the modified elements
    new_list = []
    for item in my_list:
        # Check if the item matches the search element
        if item == search:
            # If it matches, append the replace element to the new list
            new_list.append(replace)
        else:
            # If it doesn't match, append the original item to the new list
            new_list.append(item)
    return new_list
