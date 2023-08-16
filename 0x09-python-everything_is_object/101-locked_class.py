#!/usr/bin/python3
<<<<<<< HEAD
=======
"""Defines a locked class."""


>>>>>>> ab81b446485e2071716cff10b4291090903d79f2
class LockedClass:
    """
    Prevent the user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
