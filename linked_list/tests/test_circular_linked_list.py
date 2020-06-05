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
        # 5 ==> 10 ==> 2 ==> 27 ==> 99 ==> 5

    def test_insert_at_beginning(self):
        print("TEST INSERT AT BEGINNING - CIRCULAR LINKED LIST")
        print("===========================================================")

        print("List to operate: <Empty list>")
        self.circular.insert_at_beginning(22)
        print("After inserting 22 in the beginning: " + self.circular.get_list())
        self.circular.insert_at_beginning(39)
        print("After inserting 39 in the beginning: " + self.circular.get_list() + "\n")
        self.assertEqual(self.circular.get_list(), "39 ==> 22 ==> 39")

        self.create_list()
        print("List to operate: " + self.circular.get_list())
        self.circular.insert_at_beginning(24)
        print("After inserting 24 in the beginning: " + self.circular.get_list())
        self.assertEqual(
            self.circular.get_list(),
            "24 ==> 5 ==> 10 ==> 2 ==> 27 ==> 99 ==> 24")

        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")

    def test_insert_at_end(self):
        print("TEST INSERT AT END - CIRCULAR LINKED LIST")
        print("===========================================================")

        print("List to operate: <Empty list>" + self.circular.get_list())
        self.circular.insert_at_end(38)
        print("After inserting 38 at the end: " + self.circular.get_list())
        self.assertEqual(self.circular.get_list(), "38")

        self.circular.insert_at_end(92)
        print("After inserting 92 at the end: " + self.circular.get_list())
        self.assertEqual(self.circular.get_list(), "38 ==> 92 ==> 38")

        self.circular.insert_at_end(3)
        print("After inserting 3 at the end: " + self.circular.get_list())
        self.assertEqual(self.circular.get_list(), "38 ==> 92 ==> 3 ==> 38")

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
        print("After inserting 92 at position 1: " + self.circular.get_list())
        self.assertEqual(
            self.circular.get_list(),
            "92 ==> 5 ==> 10 ==> 2 ==> 27 ==> 99 ==> 92")

        self.circular.insert_at_position(3, 34)
        print("After inserting 34 at position 3: : " + self.circular.get_list())
        self.assertEqual(
            self.circular.get_list(),
            "92 ==> 5 ==> 34 ==> 10 ==> 2 ==> 27 ==> 99 ==> 92")

        self.circular.insert_at_position(self.circular.get_length(), 61)
        print("After inserting 61 at position {0}: {1} ".format(
            self.circular.get_length() - 1, self.circular.get_list()))
        self.assertEqual(
            self.circular.get_list(),
            "92 ==> 5 ==> 34 ==> 10 ==> 2 ==> 27 ==> 61 ==> 99 ==> 92")

        self.circular.insert_at_position(self.circular.get_length() + 1, 44)
        print("After inserting 44 at position {0}: {1} ".format(
            self.circular.get_length() - 1, self.circular.get_list()))
        self.assertEqual(
            self.circular.get_list(),
            "92 ==> 5 ==> 34 ==> 10 ==> 2 ==> 27 ==> 61 ==> 99 ==> 44 ==> 92")

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
        print("After deleting a node in the beginning: <Empty list>\n")
        self.assertEqual(self.circular.get_list(), "")

        self.create_list()
        print("List to operate: " + self.circular.get_list())
        self.circular.delete_at_beginning()
        print("After deleting a node in the beginning: " + self.circular.get_list())
        self.assertEqual(
            self.circular.get_list(),
            "10 ==> 2 ==> 27 ==> 99 ==> 10")

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
        print("After deleting a node at the end: <Empty list>\n")
        self.assertEqual(self.circular.get_list(), "")

        self.create_list()
        print("List to operate: " + self.circular.get_list())
        self.circular.delete_at_end()
        print("After deleting a node at the end: " + self.circular.get_list())
        self.assertEqual(
            self.circular.get_list(),
            "5 ==> 10 ==> 2 ==> 27 ==> 5")

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
        print("After deleting a node at position 1: <Empty list>\n")
        self.assertEqual(self.circular.get_list(), "")

        self.create_list()
        print("List to operate: " + self.circular.get_list())
        self.circular.delete_at_position(3)
        print("After deleting a node at position 3: " + self.circular.get_list())
        self.assertEqual(
            self.circular.get_list(),
            "5 ==> 10 ==> 27 ==> 99 ==> 5")

        self.circular.delete_at_position(4)
        print("After deleting a node at position 4: " + self.circular.get_list())
        self.assertEqual(
            self.circular.get_list(),
            "5 ==> 10 ==> 27 ==> 5")

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
