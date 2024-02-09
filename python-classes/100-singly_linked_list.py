#!/usr/bin/python3

"""
Class Node to define a single linked list
"""

class Node:

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter : Return data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter : set data to value
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Getter : Return next_node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        self.__next_node = value

class SinglyLinkedList:

    def __init__(self):
        self.head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        if not self.head or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next_node
        return "\n".join(elements)