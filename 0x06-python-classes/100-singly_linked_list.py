#!/usr/bin/python3

""" a class that defines a node """


class Node:
    """ a class called Node that defines a node """

    def __init__(self, data, next_node=none):
        """ instatiate all object of this class """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ getter method to get private instance attribute (__data) """
        return self.__data

    @data.setter
    def data(self, value):
        """ setter method to set private instance attribute (__data) """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ getter method to get private instance attribute (__next_node) """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ setter method to set private instance attribute (__next_node) """
        if type(value) != None:
            if not isinstance(value, Node):
                raise TypeError("next_node must be a Node object")
        self.__next_node = value




""" singlylinkedlist class """

class SinglyLinkedList:

    """ SinglyLinkedList class that defines a node """

    def __init__(self):
        """ instatiate objects of the SinglyLinkedList """
        self.__head = None

    def __str__(self):
        """ enables the objects of the class printable """
        result = ''
        current = self.__head
        while current:
            result += str(current.data) + '\n'
            current = current.next_node
        return result

    def sorted_insert(self, value):
        """ insert new node into a list """
        new_node = Node(value)
        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
            current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
