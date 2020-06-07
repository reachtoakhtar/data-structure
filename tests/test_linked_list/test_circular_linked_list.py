import unittest

from linked_list.exception import EmptyListError, RangeError
from linked_list.lists import CircularLinkedList

__author__ = "akhtar"


class TestCircularLinkedList(unittest.TestCase):
    def setUp(self):
        self.circular = CircularLinkedList()

    def create_list(self):
        self.circular = CircularLinkedList()
        self.circular.insert_at_end(5)
        self.circular.insert_at_end(10)
        self.circular.insert_at_end(2)
        self.circular.insert_at_end(27)
        self.circular.insert_at_end(99)
        # 5 --> 10 --> 2 --> 27 --> 99 --> 5

    def test_insert_at_beginning(self):
        print("TEST INSERT AT BEGINNING - CIRCULAR LINKED LIST")
        print("===========================================================")

        print("List to operate: <Empty list>")
        self.circular.insert_at_beginning(22)
        print("After inserting 22 in the beginning: " + self.circular.get_list())
        self.circular.insert_at_beginning(39)
        self.assertEqual(self.circular.get_list(), "39 \u27F6 22 \u27F6 39")
        print("After inserting 39 in the beginning: " + self.circular.get_list() + "\n")

        self.create_list()
        print("List to operate: " + self.circular.get_list())
        self.circular.insert_at_beginning(24)
        self.assertEqual(
            self.circular.get_list(),
            "24 \u27F6 5 \u27F6 10 \u27F6 2 \u27F6 27 \u27F6 99 \u27F6 24")
        print("After inserting 24 in the beginning: " + self.circular.get_list())

        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")

    def test_insert_at_end(self):
        print("TEST INSERT AT END - CIRCULAR LINKED LIST")
        print("===========================================================")

        print("List to operate: <Empty list>" + self.circular.get_list())
        self.circular.insert_at_end(38)
        self.assertEqual(self.circular.get_list(), "38")
        print("After inserting 38 at the end: " + self.circular.get_list())

        self.circular.insert_at_end(92)
        self.assertEqual(self.circular.get_list(), "38 \u27F6 92 \u27F6 38")
        print("After inserting 92 at the end: " + self.circular.get_list())

        self.circular.insert_at_end(3)
        self.assertEqual(self.circular.get_list(), "38 \u27F6 92 \u27F6 3 \u27F6 38")
        print("After inserting 3 at the end: " + self.circular.get_list())

        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")

    def test_insert_at_position(self):
        print("TEST INSERT AT POSITION - CIRCULAR LINKED LIST")
        print("===========================================================")

        print("List to operate: <Empty list>" + self.circular.get_list())
        try:
            self.circular.insert_at_position(1, 23)
        except EmptyListError as e:
            print(str(e) + "\n")

        self.create_list()
        print("List to operate: " + self.circular.get_list())
        self.circular.insert_at_position(1, 92)
        self.assertEqual(
            self.circular.get_list(),
            "92 \u27F6 5 \u27F6 10 \u27F6 2 \u27F6 27 \u27F6 99 \u27F6 92")
        print("After inserting 92 at position 1: " + self.circular.get_list())

        self.circular.insert_at_position(3, 34)
        self.assertEqual(
            self.circular.get_list(),
            "92 \u27F6 5 \u27F6 34 \u27F6 10 \u27F6 2 \u27F6 27 \u27F6 99 \u27F6 92")
        print("After inserting 34 at position 3: : " + self.circular.get_list())

        self.circular.insert_at_position(self.circular.get_length(), 61)
        self.assertEqual(
            self.circular.get_list(),
            "92 \u27F6 5 \u27F6 34 \u27F6 10 \u27F6 2 \u27F6 27 \u27F6 61 \u27F6 99 \u27F6 92")
        print("After inserting 61 at position {0}: {1} ".format(
            self.circular.get_length() - 1, self.circular.get_list()))

        self.circular.insert_at_position(self.circular.get_length() + 1, 44)
        self.assertEqual(
            self.circular.get_list(),
            "92 \u27F6 5 \u27F6 34 \u27F6 10 \u27F6 2 \u27F6 27 \u27F6 61 \u27F6 99 \u27F6 44 \u27F6 92")
        print("After inserting 44 at position {0}: {1} ".format(
            self.circular.get_length() - 1, self.circular.get_list()))

        try:
            self.circular.insert_at_position(0, 93)
        except RangeError as e:
            print("Can't insert at position 0. " + str(e))

        try:
            self.circular.insert_at_position(self.circular.get_length() + 2, 61)
        except RangeError as e:
            print("Can't insert at position {0}. {1}".format(
                self.circular.get_length() + 2, str(e)))

        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")

    def test_delete_at_beginning(self):
        print("TEST DELETE AT BEGINNING - CIRCULAR LINKED LIST")
        print("===========================================================")

        print("List to operate: <Empty list>" + self.circular.get_list())
        try:
            self.circular.delete_at_beginning()
        except EmptyListError as e:
            print(str(e) + "\n")

        self.circular.insert_at_beginning(5)
        print("List to operate: " + self.circular.get_list())
        self.circular.delete_at_beginning()
        self.assertEqual(self.circular.get_list(), "")
        print("After deleting a node in the beginning: <Empty list>\n")

        self.create_list()
        print("List to operate: " + self.circular.get_list())
        self.circular.delete_at_beginning()
        self.assertEqual(
            self.circular.get_list(),
            "10 \u27F6 2 \u27F6 27 \u27F6 99 \u27F6 10")
        print("After deleting a node in the beginning: " + self.circular.get_list())

        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")

    def test_delete_at_end(self):
        print("TEST DELETE AT END - CIRCULAR LINKED LIST")
        print("===========================================================")

        print("List to operate: <Empty list>" + self.circular.get_list())
        try:
            self.circular.delete_at_end()
        except EmptyListError as e:
            print(str(e) + "\n")

        self.circular.insert_at_beginning(5)
        print("List to operate: " + self.circular.get_list())
        self.circular.delete_at_end()
        self.assertEqual(self.circular.get_list(), "")
        print("After deleting a node at the end: <Empty list>\n")

        self.create_list()
        print("List to operate: " + self.circular.get_list())
        self.circular.delete_at_end()
        self.assertEqual(
            self.circular.get_list(),
            "5 \u27F6 10 \u27F6 2 \u27F6 27 \u27F6 5")
        print("After deleting a node at the end: " + self.circular.get_list())

        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")

    def test_delete_at_position(self):
        print("TEST DELETE AT POSITION - CIRCULAR LINKED LIST")
        print("===========================================================")

        print("List to operate: <Empty list>" + self.circular.get_list())
        try:
            self.circular.delete_at_position(1)
        except EmptyListError as e:
            print(str(e) + "\n")

        self.circular.insert_at_beginning(5)
        print("List to operate: " + self.circular.get_list())
        self.circular.delete_at_position(1)
        self.assertEqual(self.circular.get_list(), "")
        print("After deleting a node at position 1: <Empty list>\n")

        self.create_list()
        print("List to operate: " + self.circular.get_list())
        self.circular.delete_at_position(3)
        self.assertEqual(
            self.circular.get_list(),
            "5 \u27F6 10 \u27F6 27 \u27F6 99 \u27F6 5")
        print("After deleting a node at position 3: " + self.circular.get_list())

        self.circular.delete_at_position(4)
        self.assertEqual(
            self.circular.get_list(),
            "5 \u27F6 10 \u27F6 27 \u27F6 5")
        print("After deleting a node at position 4: " + self.circular.get_list())

        try:
            self.circular.delete_at_position(0)
        except RangeError as e:
            print("Can't delete at position 0. " + str(e))

        try:
            self.circular.delete_at_position(self.circular.get_length() + 1)
        except RangeError as e:
            print("Can't delete at position {0}. {1}".format(
                self.circular.get_length() + 1, str(e)))

        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")


if __name__ == "__main__":
    unittest.main()
