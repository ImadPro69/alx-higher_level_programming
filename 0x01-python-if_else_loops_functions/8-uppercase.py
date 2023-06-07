#!/usr/bin/python3
def uppercase(string):
    for char in string:
        if ord(char) >= ord('a') and ord(char) <= ord('z'):
            uppercase_char = chr(ord(char) - 32)
        else:
            uppercase_char = char
        print(uppercase_char, end="")
    print()
