#!/usr/bin/python3
"""Classes for a Singly-Linked List"""

class Node:
    """Node in a Singly-Linked List"""
    def __init__(self, data, next_node=None):
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self._data = data
        self._next_node = next_node

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self._next_node = value


class SinglyLinkedList:
    def __init__(self):
        self._head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        if self._head is None:
            self._head = new_node
        elif value < self._head.data:
            new_node.next_node = self._head
            self._head = new_node
        else:
            current = self._head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        current = self._head
        result = ""
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result
