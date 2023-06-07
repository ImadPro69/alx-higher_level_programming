#!/usr/bin/python3
def remove_char_at(str, n):
for i in range(ord('z'), ord('a') - 1, -1):
    print("{:c}".format(i if i % 2 == 0 else i - 32), end="")
