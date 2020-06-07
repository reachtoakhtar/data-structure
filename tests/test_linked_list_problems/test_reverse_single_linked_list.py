import unittest

from linked_list.exception import EmptyListError
from linked_list.lists import SingleLinkedList
from linked_list.problems.nth_node_from_end import nth_node_from_end

__author__ = "akhtar"

from linked_list.problems.reverse_single_linked_list import \
    reverse_single_linked_list


class TestReverseSingleLinkedList(unittest.TestCase):
    def setUp(self):
        self.linked_list = SingleLinkedList()

    def create_list(self):
        self.linked_list = SingleLinkedList()
        self.linked_list.insert_at_end(5)
        self.linked_list.insert_at_end(81)
        self.linked_list.insert_at_end(23)
        self.linked_list.insert_at_end(8)
        self.linked_list.insert_at_end(99)
        self.linked_list.insert_at_end(33)
        self.linked_list.insert_at_end(67)
        # 5 --> 81 --> 23 --> 8 --> 99 --> 33 --> 67

    def test_reverse_single_linked_list(self):
        print("TEST REVERSE SINGLE LINKED LIST")
        print("===========================================================")

        print("List: <Empty list>")
        try:
            print("<", end="")
            print(nth_node_from_end(self.linked_list, 1))
        except EmptyListError as e:
            print(str(e), end=">\n\n")

        self.linked_list.insert_at_beginning(22)
        print("List: " + self.linked_list.get_list())
        reverse_single_linked_list(self.linked_list)
        self.assertEqual(self.linked_list.get_list(), "22")
        print("Reversed list: " + self.linked_list.get_list(), end="\n\n")

        self.linked_list.insert_at_end(53)
        print("List: " + self.linked_list.get_list())
        reverse_single_linked_list(self.linked_list)
        self.assertEqual(self.linked_list.get_list(), "53 \u27F6 22")
        print("Reversed list: " + self.linked_list.get_list(), end="\n\n")

        self.create_list()
        print("List: " + self.linked_list.get_list())
        reverse_single_linked_list(self.linked_list)
        self.assertEqual(
            self.linked_list.get_list(),
            "67 \u27F6 33 \u27F6 99 \u27F6 8 \u27F6 23 \u27F6 81 \u27F6 5")
        print("Reversed list: " + self.linked_list.get_list())

        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")


if __name__ == "__main__":
    unittest.main()
