import unittest

from linked_list.exception import EmptyListError, RangeError
from linked_list.lists import DoubleLinkedList

__author__ = "akhtar"


class TestDoubleLinkedList(unittest.TestCase):
    def setUp(self):
        self.double = DoubleLinkedList()

    def create_list(self):
        self.double = DoubleLinkedList()
        self.double.insert_at_end(5)
        self.double.insert_at_end(10)
        self.double.insert_at_end(2)
        self.double.insert_at_end(27)
        self.double.insert_at_end(99)
        # 5 <--> 10 <--> 2 <--> 27 <--> 99

    def test_insert_at_beginning(self):
        print("TEST INSERT AT BEGINNING - DOUBLE LINKED LIST")
        print("===========================================================")

        print("List to operate: <Empty list>")
        self.double.insert_at_beginning(22)
        print("After inserting 22 in the beginning: " + self.double.get_list())
        self.double.insert_at_beginning(39)
        print("After inserting 39 in the beginning: " + self.double.get_list() + "\n")
        self.assertEqual(self.double.get_list(), "39 \u27F7 22")

        self.create_list()
        print("List to operate: " + self.double.get_list())
        self.double.insert_at_beginning(24)
        print("After inserting 24 in the beginning: " + self.double.get_list())
        self.assertEqual(
            self.double.get_list(),
            "24 \u27F7 5 \u27F7 10 \u27F7 2 \u27F7 27 \u27F7 99")

        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")

    def test_insert_at_end(self):
        print("TEST INSERT AT END - DOUBLE LINKED LIST")
        print("===========================================================")

        print("List to operate: <Empty list>" + self.double.get_list())
        self.double.insert_at_end(38)
        print("After inserting 38 at the end: " + self.double.get_list())
        self.assertEqual(self.double.get_list(), "38")

        self.double.insert_at_end(92)
        print("After inserting 92 at the end: " + self.double.get_list())
        self.assertEqual(self.double.get_list(), "38 \u27F7 92")

        self.double.insert_at_end(3)
        print("After inserting 3 at the end: " + self.double.get_list())
        self.assertEqual(self.double.get_list(), "38 \u27F7 92 \u27F7 3")

        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")

    def test_insert_at_position(self):
        print("TEST INSERT AT POSITION - DOUBLE LINKED LIST")
        print("===========================================================")

        print("List to operate: <Empty list>" + self.double.get_list())
        try:
            self.double.insert_at_position(1, 23)
        except EmptyListError as e:
            print(str(e) + "\n")

        self.create_list()
        print("List to operate: " + self.double.get_list())
        self.double.insert_at_position(1, 92)
        print("After inserting 92 at position 1: " + self.double.get_list())
        self.assertEqual(
            self.double.get_list(),
            "92 \u27F7 5 \u27F7 10 \u27F7 2 \u27F7 27 \u27F7 99")

        self.double.insert_at_position(3, 34)
        print("After inserting 34 at position 3: : " + self.double.get_list())
        self.assertEqual(
            self.double.get_list(),
            "92 \u27F7 5 \u27F7 34 \u27F7 10 \u27F7 2 \u27F7 27 \u27F7 99")

        self.double.insert_at_position(self.double.get_length(), 61)
        print("After inserting 61 at position {0}: {1} ".format(
            self.double.get_length() - 1, self.double.get_list()))
        self.assertEqual(
            self.double.get_list(),
            "92 \u27F7 5 \u27F7 34 \u27F7 10 \u27F7 2 \u27F7 27 \u27F7 61 \u27F7 99")

        self.double.insert_at_position(self.double.get_length() + 1, 44)
        print("After inserting 44 at position {0}: {1} ".format(
            self.double.get_length() - 1, self.double.get_list()))
        self.assertEqual(
            self.double.get_list(),
            "92 \u27F7 5 \u27F7 34 \u27F7 10 \u27F7 2 \u27F7 27 \u27F7 61 \u27F7 99 \u27F7 44")

        try:
            self.double.insert_at_position(0, 93)
        except RangeError as e:
            print("Can't insert at position 0. " + str(e))

        try:
            self.double.insert_at_position(self.double.get_length() + 2, 61)
        except RangeError as e:
            print("Can't insert at position {0}. {1}".format(
                self.double.get_length() + 2, str(e)))

        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")

    def test_delete_at_beginning(self):
        print("TEST DELETE AT BEGINNING - DOUBLE LINKED LIST")
        print("===========================================================")

        print("List to operate: <Empty list>" + self.double.get_list())
        try:
            self.double.delete_at_beginning()
        except EmptyListError as e:
            print(str(e) + "\n")

        self.double.insert_at_beginning(5)
        print("List to operate: " + self.double.get_list())
        self.double.delete_at_beginning()
        print("After deleting a node in the beginning: <Empty list>\n")
        self.assertEqual(self.double.get_list(), "")

        self.create_list()
        print("List to operate: " + self.double.get_list())
        self.double.delete_at_beginning()
        print("After deleting a node in the beginning: " + self.double.get_list())
        self.assertEqual(
            self.double.get_list(),
            "10 \u27F7 2 \u27F7 27 \u27F7 99")

        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")

    def test_delete_at_end(self):
        print("TEST DELETE AT END - DOUBLE LINKED LIST")
        print("===========================================================")

        print("List to operate: <Empty list>" + self.double.get_list())
        try:
            self.double.delete_at_end()
        except EmptyListError as e:
            print(str(e) + "\n")

        self.double.insert_at_beginning(5)
        print("List to operate: " + self.double.get_list())
        self.double.delete_at_end()
        print("After deleting a node at the end: <Empty list>\n")
        self.assertEqual(self.double.get_list(), "")

        self.create_list()
        print("List to operate: " + self.double.get_list())
        self.double.delete_at_end()
        print("After deleting a node at the end: " + self.double.get_list())
        self.assertEqual(
            self.double.get_list(),
            "5 \u27F7 10 \u27F7 2 \u27F7 27")

        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")

    def test_delete_at_position(self):
        print("TEST DELETE AT POSITION - DOUBLE LINKED LIST")
        print("===========================================================")

        print("List to operate: <Empty list>" + self.double.get_list())
        try:
            self.double.delete_at_position(1)
        except EmptyListError as e:
            print(str(e) + "\n")

        self.double.insert_at_beginning(5)
        print("List to operate: " + self.double.get_list())
        self.double.delete_at_position(1)
        print("After deleting a node at position 1: <Empty list>\n")
        self.assertEqual(self.double.get_list(), "")

        self.create_list()
        print("List to operate: " + self.double.get_list())
        self.double.delete_at_position(3)
        print("After deleting a node at position 3: " + self.double.get_list())
        self.assertEqual(
            self.double.get_list(),
            "5 \u27F7 10 \u27F7 27 \u27F7 99")

        self.double.delete_at_position(4)
        print("After deleting a node at position 4: " + self.double.get_list())
        self.assertEqual(
            self.double.get_list(),
            "5 \u27F7 10 \u27F7 27")

        try:
            self.double.delete_at_position(0)
        except RangeError as e:
            print("Can't delete at position 0. " + str(e))

        try:
            self.double.delete_at_position(self.double.get_length() + 1)
        except RangeError as e:
            print("Can't delete at position {0}. {1}".format(
                self.double.get_length() + 1, str(e)))

        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")


if __name__ == "__main__":
    unittest.main()
