import unittest

from linked_list.exception import EmptyListError
from linked_list.lists import SingleLinkedList
from linked_list.problems.insert_into_sorted_list import insert_into_sorted_list

__author__ = "akhtar"


class TestInsertIntoSortedList(unittest.TestCase):
    def setUp(self):
        self.linked_list = SingleLinkedList()

    def create_list(self):
        self.linked_list = SingleLinkedList()
        self.linked_list.insert_at_end(1)
        self.linked_list.insert_at_end(2)
        self.linked_list.insert_at_end(6)
        self.linked_list.insert_at_end(8)
        self.linked_list.insert_at_end(12)
        # 1 --> 2 --> 6 --> 8 --> 12

    def test_insert_into_sorted_list(self):
        print("TEST INSERT INTO A SORTED LIST")
        print("===========================================================")

        print("List: <Empty list>")
        try:
            print("<", end="")
            insert_into_sorted_list(self.linked_list, 32)
        except EmptyListError as e:
            print(str(e), end=">\n\n")

        self.create_list()
        print("List: " + self.linked_list.get_list())

        insert_into_sorted_list(self.linked_list, -1)
        print("List after inserting -1: ", self.linked_list.get_list())
        self.assertEqual(
            self.linked_list.get_list(),
            "-1 \u27F6 1 \u27F6 2 \u27F6 6 \u27F6 8 \u27F6 12")

        insert_into_sorted_list(self.linked_list, 5)
        print("List after inserting 5: ", self.linked_list.get_list())
        self.assertEqual(
            self.linked_list.get_list(),
            "-1 \u27F6 1 \u27F6 2 \u27F6 5 \u27F6 6 \u27F6 8 \u27F6 12")

        insert_into_sorted_list(self.linked_list, 20)
        print("List after inserting 20: ", self.linked_list.get_list())
        self.assertEqual(
            self.linked_list.get_list(),
            "-1 \u27F6 1 \u27F6 2 \u27F6 5 \u27F6 6 \u27F6 8 \u27F6 12 \u27F6 20")

        insert_into_sorted_list(self.linked_list, 8)
        print("List after inserting 8: ", self.linked_list.get_list())
        self.assertEqual(
            self.linked_list.get_list(),
            "-1 \u27F6 1 \u27F6 2 \u27F6 5 \u27F6 6 \u27F6 8 \u27F6 8 \u27F6 12 \u27F6 20")

        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")


if __name__ == "__main__":
    unittest.main()
