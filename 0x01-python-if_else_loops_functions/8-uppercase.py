#!/usr/bin/python3

def uppercase(s):
    result = ""
    for char in s:
        ascii_val = ord(char)
        if ord('a') <= ascii_val <= ord('z'):
            ascii_val -= 32
        result += chr(ascii_val)
    print("{}".format(result))
