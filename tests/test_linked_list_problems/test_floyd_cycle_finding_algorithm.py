import unittest

from linked_list.exception import EmptyListError
from linked_list.lists import SingleLinkedList
from linked_list.problems.floyd_cycle_finding_algorithm import \
    lenth_of_the_loop, loop_in_a_list

__author__ = "akhtar"


class TestFloydCycleFindingAlgorithm(unittest.TestCase):
    def setUp(self):
        self.linked_list = SingleLinkedList()

    def create_list(self):
        self.linked_list = SingleLinkedList()
        self.linked_list.insert_at_end(5)
        self.linked_list.insert_at_end(1)
        self.linked_list.insert_at_end(23)
        self.linked_list.insert_at_end(27)
        self.linked_list.insert_at_end(99)
        self.linked_list.insert_at_end(32)
        self.linked_list.insert_at_end(61)
        self.linked_list.insert_at_end(33)
        self.linked_list.insert_at_end(87)
        self.linked_list.insert_at_end(47)
        self.linked_list.insert_at_end(43)
        # 5 --> 1 --> 23 --> 27 --> 99 --> 32 --> 61 --> 33 --> 87 --> 47 --> 43

    def test_loop_in_a_list(self):
        print("TEST LOOP IN A LIST - FLOYD CYCLE FINDING ALGORITHM")
        print("===========================================================")

        print("List: <Empty list>")
        try:
            print("<", end="")
            loop_in_a_list(self.linked_list)
        except EmptyListError as e:
            print(str(e), end=">\n\n")

        # ======================
        # Test with a list.
        # ======================
        self.create_list()
        print("List: " + self.linked_list.get_list())

        is_cyclic, data = loop_in_a_list(self.linked_list)
        self.assertEqual(is_cyclic, False)
        print("Loop does not exist.", end="\n\n")

        # Create loop at 4th node in the list.
        pointer = self.linked_list.head
        position = 1
        while position != 4:
            pointer = pointer.get_next()
            position += 1

        loop_start_node = pointer
        while pointer.get_next():
            pointer = pointer.get_next()

        pointer.set_next(loop_start_node)

        print("List:")
        print("                    \u2197 99 \u27F6 32 \u27F6 61 \u2198")
        print("5 \u27F6 1 \u27F6 23 \u27F6 27                    33")
        print("                    \u2196 43 \u27F5 47 \u27F5 87 \u2199")

        is_cyclic, data = loop_in_a_list(self.linked_list)
        self.assertEqual(is_cyclic, True)
        self.assertEqual(data, 27)
        print("\nLoop exists with start node at {0}.".format(27))

        loop_length = lenth_of_the_loop(self.linked_list)
        self.assertEqual(loop_length, 8)
        print("Length of the loop = {0}.\n\n".format(loop_length))

        # ======================
        # Test with another list.
        # ======================
        self.linked_list = SingleLinkedList()
        self.linked_list.insert_at_end(5)
        self.linked_list.insert_at_end(1)
        self.linked_list.insert_at_end(23)
        self.linked_list.insert_at_end(48)

        # Create loop at 3rd node in the list.
        pointer = self.linked_list.head
        position = 1
        while position != 3:
            pointer = pointer.get_next()
            position += 1

        loop_start_node = pointer
        while pointer.get_next():
            pointer = pointer.get_next()

        pointer.set_next(loop_start_node)

        print("List:")
        print("5 \u27F6 1 \u27F6 23 \u2500\u2500\u2510")
        print("           \u2191    \u2193")
        print("           \u2514\u2500\u2500 48")

        is_cyclic, data = loop_in_a_list(self.linked_list)
        self.assertEqual(is_cyclic, True)
        self.assertEqual(data, 23)
        print("\nLoop exists with start node at {0}.".format(27))

        loop_length = lenth_of_the_loop(self.linked_list)
        self.assertEqual(loop_length, 2)
        print("Length of the loop = {0}.".format(loop_length))

        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")


if __name__ == "__main__":
    unittest.main()
