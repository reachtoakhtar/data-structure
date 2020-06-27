__author__ = "akhtar"

import unittest

from tests.test_tree.utils import SampleBTree
from tree.problems.binary_tree.find_maximum_element import \
    find_maximum_element_iterative, \
    find_maximum_element_recursive


class TestFindMaximumInABinaryTree(unittest.TestCase):
    def setUp(self):
        self.create_tree()
    
    def create_tree(self):
        self.root = SampleBTree.create_9()
    
    def test_find_maximum_element_recursive(self):
        print("TEST MAXIMUM ELEMENT - RECURSIVE")
        print("===========================================================")
        
        SampleBTree.print_9()
        maximum = find_maximum_element_recursive(self.root)
        self.assertEqual(62, maximum)
        print("Maximum element: " + str(maximum), end=" ")
        
        print(
            "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")
    
    def test_find_maximum_element_iterative(self):
        print("TEST MAXIMUM ELEMENT - ITERATIVE")
        print("===========================================================")
        
        SampleBTree.print_9()
        maximum = find_maximum_element_iterative(self.root)
        self.assertEqual(62, maximum)
        print("Maximum element: " + str(maximum), end=" ")
        
        print(
            "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")


if __name__ == "__main__":
    unittest.main()
