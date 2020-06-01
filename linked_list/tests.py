import logging
import unittest

from linked_list.single_ll import SingleLinkedList

__author__ = "akhtar"

logger = logging.getLogger(__name__)


class TestSingleLinkedList(unittest.TestCase):
    def setUp(self):
        self.single = SingleLinkedList()

    def create_list(self):
        self.single = SingleLinkedList()
        self.single.insert_at_end(5)
        self.single.insert_at_end(10)
        self.single.insert_at_end(2)
        self.single.insert_at_end(27)
        self.single.insert_at_end(99)

    def test_insert_at_beginning(self):
        print("List to operate: ")
        self.single.insert_at_beginning(22)
        print("After inserting 22 in the beginning: " + self.single.get_list())
        self.single.insert_at_beginning(39)
        print("After inserting 39 in the beginning: " + self.single.get_list() + "\n")
        self.assertEqual(self.single.get_list(), "39 ==> 22")

        self.create_list()
        print("List to operate: " + self.single.get_list())
        self.single.insert_at_beginning(24)
        print("After inserting 24 in the beginning: " + self.single.get_list() + "\n")
        self.assertEqual(
            self.single.get_list(),
            "24 ==> 5 ==> 10 ==> 2 ==> 27 ==> 99")

    def test_insert_at_end(self):
        print("List to operate: " + self.single.get_list())
        self.single.insert_at_end(38)
        print("After inserting 38 at the end: " + self.single.get_list())
        self.assertEqual(self.single.get_list(), "38")


if __name__ == "__main__":
    unittest.main()
