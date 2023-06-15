#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    return [my_list[0]] + list(map(lambda x: x * number, my_list[1:]))
