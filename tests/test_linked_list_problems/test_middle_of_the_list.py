import unittest

from linked_list.exception import EmptyListError
from linked_list.lists import SingleLinkedList
from linked_list.problems.find_intersecting_node import intersecting_node

__author__ = "akhtar"

from linked_list.problems.middle_of_the_list import find_middle_of_the_list


class TestMiddleOfTheList(unittest.TestCase):
    def setUp(self):
        self.linked_list = SingleLinkedList()

    def create_list(self):
        self.linked_list = SingleLinkedList()
        self.linked_list.insert_at_end(5)
        self.linked_list.insert_at_end(81)
        self.linked_list.insert_at_end(23)
        self.linked_list.insert_at_end(8)
        self.linked_list.insert_at_end(99)
        # 5 --> 81 --> 23 --> 8 --> 99

    def test_find_middle_of_the_list(self):
        print("TEST MIDDLE OF THE LIST")
        print("===========================================================")

        # Case 1
        print("Lists: <Empty list>")
        try:
            find_middle_of_the_list(self.linked_list)
        except EmptyListError as e:
            print("<" + str(e) + ">", end="\n\n")

        # Case 2
        self.linked_list = SingleLinkedList()
        self.linked_list.insert_at_end(89)

        print("List: " + self.linked_list.get_list())
        middle_node = find_middle_of_the_list(self.linked_list)
        self.assertEqual(middle_node, 89)
        print("Middle node: " + str(middle_node), end="\n\n")

        # Case 3
        self.linked_list = SingleLinkedList()
        self.linked_list.insert_at_end(34)
        self.linked_list.insert_at_end(62)

        print("List: " + self.linked_list.get_list())
        middle_node = find_middle_of_the_list(self.linked_list)
        self.assertEqual(middle_node, 34)
        print("Middle node: " + str(middle_node), end="\n\n")

        # Case 4
        self.linked_list = SingleLinkedList()
        self.linked_list.insert_at_end(2)
        self.linked_list.insert_at_end(95)
        self.linked_list.insert_at_end(78)
        self.linked_list.insert_at_end(37)

        print("List: " + self.linked_list.get_list())
        middle_node = find_middle_of_the_list(self.linked_list)
        self.assertEqual(middle_node, 95)
        print("Middle node: " + str(middle_node), end="\n\n")

        # Case 5
        self.create_list()
        print("List: " + self.linked_list.get_list())

        middle_node = find_middle_of_the_list(self.linked_list)
        self.assertEqual(middle_node, 23)
        print("Middle node: " + str(middle_node), end="\n\n")

        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")


if __name__ == "__main__":
    unittest.main()
