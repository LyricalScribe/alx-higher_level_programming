#!/usr/bin/python3
""" This module contains a class for singly linked list """


class Node:
    """ Defines singly linked list """

    def __init__(self, data, next_node=None):
        """ Initialize data """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ Retrieves the data """
        return self.__data

    @data.setter
    def data(self, value):
        """ sets the data """
        if type(value) != int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """ retrieves the next node """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ sets the value for the next_node """

        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """ creates a singly linked list class """
    def __init__(self):
        """ initialize linkedlist """
        self.__head = None

    def sorted_insert(self, value):
        """ insert node in the correct sorted position """

        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node

            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
