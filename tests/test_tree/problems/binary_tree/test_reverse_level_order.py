__author__ = "akhtar"

import unittest

from tests.test_tree.utils import SampleTree
from tree.problems.binary_tree.reverse_level_order import reverse_level_order


class TestReverseLevelOrder(unittest.TestCase):
    def setUp(self):
        self.create_tree()
    
    def create_tree(self):
        self.root = SampleTree.create_9()
    
    def test_insert_into_tree(self):
        print("TEST REVERSE LEVEL ORDER")
        print("===========================================================")
        
        SampleTree.print_9()
        
        print("Reverse level order traversal: ", end=" ")
        reverse_level_order(self.root)
        
        print(
            "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")


if __name__ == "__main__":
    unittest.main()
