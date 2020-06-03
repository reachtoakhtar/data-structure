import logging

from linked_list.exception import EmptyListError, RangeError
from linked_list.node import NodeCircular, NodeDouble, NodeSingle

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

    def delete_at_position(self, position):
        """ Position is 1 based. """
        if self.head is None:
            raise EmptyListError("List is empty, can't delete.")

        list_length = self.get_length()
        if not (1 <= position <= list_length):
            raise RangeError("Position range must be 1 through {0}.".format(
                list_length))

        if position == 1:
            self.delete_at_beginning()
        else:
            pointer = self.head
            pos = 1
            while pos != position - 1:
                pointer = pointer.get_next()
                pos += 1

            next = pointer.get_next().get_next()
            pointer.get_next().set_next(None)
            pointer.set_next(next)


class DoubleLinkedList:
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
            str_list += str(node.get_data()) + " <==> "
            node = node.get_next()

        return str_list[:len(str_list) - 6]

    def insert_at_beginning(self, data):
        node = NodeDouble(data)
        node.set_next(self.head)
        node.set_previous(None)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.insert_at_beginning(data)
        else:
            node = NodeDouble(data)
            pointer = self.head
            while pointer.get_next():
                pointer = pointer.get_next()

            node.set_previous(pointer)
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

            node = NodeDouble(data)
            node.set_next(pointer.get_next())
            node.set_previous(pointer)
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
            pointer = self.head
            while pointer.get_next():
                pointer = pointer.get_next()

            pointer.get_previous().set_next(None)

    def delete_at_position(self, position):
        """ Position is 1 based. """
        if self.head is None:
            raise EmptyListError("List is empty, can't delete.")

        list_length = self.get_length()
        if not (1 <= position <= list_length):
            raise RangeError("Position range must be 1 through {0}.".format(
                list_length))

        if position == 1:
            self.delete_at_beginning()
        else:
            pointer = self.head
            pos = 1
            while pos != position:
                pointer = pointer.get_next()
                pos += 1

            pointer.get_previous().set_next(pointer.get_next())
            if pointer.get_next() is not None:
                pointer.get_next().set_previous(pointer.get_previous())
                pointer.set_previous(None)
                pointer.set_next(None)


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def get_length(self):
        length = 0

        if self.head:
            pointer = self.head
            while pointer:
                length += 1
                pointer = pointer.get_next()
                if pointer == self.head:
                    break

        return length

    def get_list(self):
        str_list = ""
        node = self.head
        while node:
            str_list += str(node.get_data()) + " ==> "
            node = node.get_next()
            if node == self.head:
                break

        list_length = self.get_length()
        if list_length == 0:
            return ""
        elif list_length == 1:
            return str_list[:len(str_list) - 5]
        else:
            return str_list[:len(str_list)] + str(self.head.data)

    def insert_at_beginning(self, data):
        node = NodeCircular(data)
        node.set_next(node)

        if self.get_length() == 0:
            self.head = node
        else:
            node.set_next(self.head)

            pointer = self.head
            while pointer:
                if pointer.get_next() == self.head:
                    break
                pointer = pointer.get_next()

            pointer.set_next(node)
            self.head = node

    def insert_at_end(self, data):
        if self.get_length() == 0:
            self.insert_at_beginning(data)
        else:
            node = NodeCircular(data)
            node.set_next(node)

            pointer = self.head
            while pointer:
                if pointer.get_next() == self.head:
                    break
                pointer = pointer.get_next()

            pointer.set_next(node)
            node.set_next(self.head)

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
        elif position == list_length + 1:
            self.insert_at_end(data)
        else:
            pointer = self.head
            pos = 1
            while pos != position - 1:
                pointer = pointer.get_next()
                pos += 1

            node = NodeCircular(data)
            node.set_next(pointer.get_next())
            pointer.set_next(node)

    def delete_at_beginning(self):
        if self.head is None:
            raise EmptyListError("List is empty, can't delete.")

        if self.get_length() == 1:
            self.head = None
        else:
            pointer = self.head
            while pointer:
                if pointer.get_next() == self.head:
                    break
                pointer = pointer.get_next()

            temp = self.head
            self.head = temp.get_next()
            temp.set_next(None)
            pointer.set_next(self.head)

    def delete_at_end(self):
        if self.head is None:
            raise EmptyListError("List is empty, can't delete.")

        if self.get_length() == 1:
            self.delete_at_beginning()
        else:
            # Keep track of 2 pointers, one is the traversing and
            # the other one is the node previous to it. The `previous`
            # moves 1 step ahead after `pointer` has moved 2 steps.
            pointer = self.head
            previous = self.head
            steps = 1

            while pointer.get_next() != self.head:
                pointer = pointer.get_next()
                if steps == 2:
                    previous = previous.get_next()
                    steps = 1

                steps += 1

            previous.set_next(self.head)
            pointer.set_next(None)

    def delete_at_position(self, position):
        """ Position is 1 based. """
        if self.head is None:
            raise EmptyListError("List is empty, can't delete.")

        list_length = self.get_length()
        if not (1 <= position <= list_length):
            raise RangeError("Position range must be 1 through {0}.".format(
                list_length))

        if position == 1:
            self.delete_at_beginning()
        elif position == list_length:
            self.delete_at_end()
        else:
            pointer = self.head
            pos = 1
            while pos != position - 1:
                pointer = pointer.get_next()
                pos += 1

            next = pointer.get_next().get_next()
            pointer.get_next().set_next(None)
            pointer.set_next(next)
