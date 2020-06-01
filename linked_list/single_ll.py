import logging

from linked_list.node import NodeSingle

__author__ = "akhtar"

logger = logging.getLogger(__name__)


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def get_length(self):
        length = 0

        if self.head:
            pointer = self.head
            while pointer:
                length += 1
                pointer = pointer.get_next()

        return length

    def get_list(self):
        str_list = ""
        node = self.head
        while node:
            str_list += str(node.get_data()) + " ==> "
            node = node.get_next()

        return str_list[:len(str_list) - 5]

    def insert_at_beginning(self, data):
        node = NodeSingle(data)
        node.set_next(self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.insert_at_beginning(data)
        else:
            node = NodeSingle(data)
            pointer = self.head
            while pointer.get_next():
                pointer = pointer.get_next()

            pointer.set_next(node)
