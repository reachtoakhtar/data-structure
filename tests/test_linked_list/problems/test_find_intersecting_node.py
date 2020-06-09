import unittest

from linked_list.exception import EmptyListError
from linked_list.lists import SingleLinkedList
from linked_list.problems.find_intersecting_node import intersecting_node

__author__ = "akhtar"


class TestFindIntersectingNode(unittest.TestCase):
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

    def test_find_intersecting_node(self):
        print("TEST INTERSECTION BETWEEN TWO LISTS")
        print("===========================================================")

        # Case 1
        print("Lists: <Empty list>")
        try:
            intersecting_node(None, None)
        except EmptyListError as e:
            print("<" + str(e) + ">", end="\n\n")

        # Case 2
        self.create_list()
        print("Lists: \n" + self.linked_list.get_list())
        try:
            intersecting_node(self.linked_list, None)
        except EmptyListError as e:
            print("<" + str(e) + ">", end="\n\n")

        # Case 3
        self.create_list()
        position = 1
        pointer = self.linked_list.head
        while position != 3:
            pointer = pointer.get_next()
            position += 1

        self.linked_list2 = SingleLinkedList()
        self.linked_list2.insert_at_end(43)
        self.linked_list2.insert_at_end(7)
        self.linked_list2.insert_at_end(87)
        self.linked_list2.insert_at_end(56)

        # Set intersecting node
        pointer2 = self.linked_list2.head
        while pointer2.get_next():
            pointer2 = pointer2.get_next()
        pointer2.set_next(pointer)

        print("Lists: ")
        print(" "*13 + self.linked_list.get_list()[:6] + " \u2198 ")
        print(" "*22 + self.linked_list.get_list()[8:])
        print(self.linked_list2.get_list()[:16] + " \u2197 ")

        node = intersecting_node(self.linked_list, self.linked_list2)
        self.assertEqual(node, 23)
        print("\nIntersecting node: " + str(node), end="\n\n")

        # Case 4
        self.linked_list = SingleLinkedList()
        self.linked_list.insert_at_end(89)
        self.linked_list.insert_at_end(54)
        position = 1
        pointer = self.linked_list.head
        while position != 2:
            pointer = pointer.get_next()
            position += 1

        self.linked_list2 = SingleLinkedList()
        self.linked_list2.insert_at_end(43)

        # Set intersecting node
        pointer2 = self.linked_list2.head
        while pointer2.get_next():
            pointer2 = pointer2.get_next()
        pointer2.set_next(pointer)

        print("Lists: ")
        print(self.linked_list.get_list()[:2] + " \u2198 ")
        print(" "*3 + self.linked_list.get_list()[4:])
        print(self.linked_list2.get_list()[:2] + " \u2197 ")

        node = intersecting_node(self.linked_list, self.linked_list2)
        self.assertEqual(node, 54)
        print("\nIntersecting node: " + str(node))

        # Case 5
        self.create_list()
        self.linked_list.insert_at_end(33)
        self.linked_list.insert_at_end(16)
        self.linked_list.insert_at_end(2)
        position = 1
        pointer = self.linked_list.head
        while position != 5:
            pointer = pointer.get_next()
            position += 1

        self.linked_list2 = SingleLinkedList()
        self.linked_list2.insert_at_end(43)
        self.linked_list2.insert_at_end(3)

        # Set intersecting node
        pointer2 = self.linked_list2.head
        while pointer2.get_next():
            pointer2 = pointer2.get_next()
        pointer2.set_next(pointer)

        print("Lists: ")
        print(self.linked_list.get_list()[:15] + " \u2198 ")
        print(" "*22 + self.linked_list.get_list()[18:])
        print(" "*13 + self.linked_list2.get_list()[:6] + " \u2197 ")

        node = intersecting_node(self.linked_list, self.linked_list2)
        self.assertEqual(node, 99)
        print("\nIntersecting node: " + str(node))

        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")


if __name__ == "__main__":
    unittest.main()
