import unittest

from linked_list.exception import EmptyListError, RangeError
from linked_list.lists import SingleLinkedList
from linked_list.problems.nth_node_from_end import nth_node_from_end, \
    nth_node_from_end_single_scan

__author__ = "akhtar"


class TestNthNodeFromEnd(unittest.TestCase):
    def setUp(self):
        self.linked_list = SingleLinkedList()

    def create_list(self):
        self.linked_list = SingleLinkedList()
        self.linked_list.insert_at_end(5)
        self.linked_list.insert_at_end(10)
        self.linked_list.insert_at_end(2)
        self.linked_list.insert_at_end(27)
        self.linked_list.insert_at_end(99)
        # 5 ==> 10 ==> 2 ==> 27 ==> 99

    def test_nth_from_end_two_scans(self):
        print("TEST NTH NODE FROM END - TWO SCANS")
        print("===========================================================")

        print("List: <Empty list>")
        try:
            print("n = 1, Node = Not found <", end="")
            print(nth_node_from_end(self.linked_list, 1))
        except EmptyListError as e:
            print(str(e), end=">\n\n")

        self.linked_list.insert_at_beginning(22)
        print("List: " + self.linked_list.get_list())
        try:
            print("n = 4, Node = Not found <", end="")
            nth_node_from_end(self.linked_list, 4)
        except RangeError as e:
            print(str(e), end=">\n\n")

        self.create_list()
        print("List: " + self.linked_list.get_list())

        n = nth_node_from_end(self.linked_list, 2)
        print("n = 2, Node =", n)
        self.assertEqual(n, 27)

        n = nth_node_from_end(self.linked_list, 5)
        print("n = 5, Node =", n)
        self.assertEqual(n, 5)

        n = nth_node_from_end(self.linked_list, 1)
        print("n = 1, Node =", n)
        self.assertEqual(n, 99)

        try:
            print("n = 0, Node = Not found <", end="")
            nth_node_from_end(self.linked_list, 0)
        except RangeError as e:
            print(str(e), end=">\n")

        try:
            print("n = 6, Node = Not found <", end="")
            nth_node_from_end(self.linked_list, 6)
        except RangeError as e:
            print(str(e), end=">\n")

        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")

    def test_nth_from_end_one_scan(self):
        print("TEST NTH NODE FROM END - ONE SCAN")
        print("===========================================================")

        print("List: <Empty list>")
        try:
            print("n = 1, Node = Not found <", end="")
            print(nth_node_from_end_single_scan(self.linked_list, 1))
        except EmptyListError as e:
            print(str(e), end=">\n\n")

        self.linked_list.insert_at_beginning(22)
        print("List: " + self.linked_list.get_list())
        try:
            print("n = 4, Node = Not found <", end="")
            nth_node_from_end_single_scan(self.linked_list, 4)
        except RangeError as e:
            print(str(e), end=">\n\n")

        self.create_list()
        print("List: " + self.linked_list.get_list())

        n = nth_node_from_end_single_scan(self.linked_list, 2)
        print("n = 2, Node =", n)
        self.assertEqual(n, 27)

        n = nth_node_from_end_single_scan(self.linked_list, 5)
        print("n = 5, Node =", n)
        self.assertEqual(n, 5)

        n = nth_node_from_end_single_scan(self.linked_list, 1)
        print("n = 1, Node =", n)
        self.assertEqual(n, 99)

        try:
            print("n = 0, Node = Not found <", end="")
            nth_node_from_end_single_scan(self.linked_list, 0)
        except RangeError as e:
            print(str(e), end=">\n")

        try:
            print("n = 6, Node = Not found <", end="")
            nth_node_from_end_single_scan(self.linked_list, 6)
        except RangeError as e:
            print(str(e), end=">\n")

        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")


if __name__ == "__main__":
    unittest.main()
