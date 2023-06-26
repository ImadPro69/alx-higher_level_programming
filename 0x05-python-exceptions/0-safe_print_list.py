def safe_print_list(my_list=[], x=0):
    printed_elements = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            printed_elements += 1
    except IndexError:
        pass  # Ignore index errors when accessing elements beyond the list's length
    finally:
        print()  # Print a new line after all elements are printed
    return printed_elements

