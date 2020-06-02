import logging

from linked_list.exception import EmptyListError, RangeError
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

    def insert_at_position(self, position, data):
        """ Position is 1 based. """
        if self.head is None:
            raise EmptyListError("List is empty, can't insert.")

        list_length = self.get_length()
        if not (1 <= position <= list_length + 1):
            raise RangeError("Position range must be 1 through {0}.".format(
                list_length + 1))

        if position == 1:
            self.insert_at_beginning(data)
        else:
            pointer = self.head
            pos = 1
            while pos != position - 1:
                pointer = pointer.get_next()
                pos += 1

            node = NodeSingle(data)
            node.set_next(pointer.get_next())
            pointer.set_next(node)

    def delete_at_beginning(self):
        if self.head is None:
            raise EmptyListError("List is empty, can't delete.")

        temp = self.head
        self.head = temp.get_next()
        temp.set_next(None)

    def delete_at_end(self):
        if self.head is None:
            raise EmptyListError("List is empty, can't delete.")

        list_length = self.get_length()
        if list_length == 1:
            self.delete_at_beginning()
        else:
            # Keep track of 2 pointers, one is the traversing and
            # the other one is the node previous to it. The `previous`
            # moves 1 step ahead after `pointer` has moved 2 steps.
            pointer = self.head
            previous = self.head
            steps = 1

            while pointer.get_next():
                pointer = pointer.get_next()
                if steps == 2:
                    previous = previous.get_next()
                    steps = 1

                steps += 1

            previous.set_next(None)
