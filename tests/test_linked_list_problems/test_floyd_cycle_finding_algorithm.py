import unittest

from linked_list.exception import EmptyListError
from linked_list.lists import SingleLinkedList
from linked_list.problems.floyd_cycle_finding_algorithm import loop_in_a_list

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
        # 5 ==> 1 ==> 23 ==> 27 ==> 99 ==> 32 ==> 61 ==> 33 ==> 87 ==> 47 ==> 43

    def test_loop_in_a_list(self):
        print("TEST LOOP IN A LIST - FLOYD CYCLE FINDING ALGORITHM")
        print("===========================================================")

        print("List: <Empty list>")
        try:
            print("<", end="")
            loop_in_a_list(self.linked_list)
        except EmptyListError as e:
            print(str(e), end=">\n\n")

        self.create_list()
        print("List: " + self.linked_list.get_list())

        is_cyclic, data = loop_in_a_list(self.linked_list)
        print("Loop does not exist.", end="\n\n")
        self.assertEqual(is_cyclic, False)

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
        print("                     \u21D7 99 ==> 32 ==> 61 \u21D8")
        print("5 ==> 1 ==> 23 ==> 27                    33")
        print("                     \u21D6 43 <== 47 <== 87 \u21D9")

        is_cyclic, data = loop_in_a_list(self.linked_list)
        print("\nLoop exists at node with data = {0}.".format(27), end="\n")
        self.assertEqual(is_cyclic, True)
        self.assertEqual(data, 27)

        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")


if __name__ == "__main__":
    unittest.main()
