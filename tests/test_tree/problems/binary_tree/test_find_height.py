__author__ = "akhtar"

import unittest

from tests.test_tree.utils import SampleBTree
from tree.binary_tree import BTreeNode
from tree.problems.binary_tree.find_height import find_height_iterative, \
    find_height_recursive


class TestFindHeight(unittest.TestCase):
    def setUp(self):
        self.create_tree()
    
    def create_tree(self):
        self.root = SampleBTree.create_9()
    
    def test_find_height_recursive(self):
        print("TEST FIND HEIGHT OF A BINARY TREE - RECURSIVE")
        print("===========================================================")
        
        SampleBTree.print_9()
        height = find_height_recursive(self.root)
        self.assertEqual(5, height)
        print("Height of given tree = {0}".format(height), end="\n\n")
        
        self.root = BTreeNode(10)
        print("Tree to operate: ")
        print(" " * 20 + "10\n")
        height = find_height_recursive(self.root)
        self.assertEqual(1, height)
        print("Height of given tree = {0}".format(height), end=" ")
        
        print(
            "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")
    
    def test_find_height_iterative(self):
        print("TEST FIND HEIGHT OF A BINARY TREE - ITERATIVE")
        print("===========================================================")
        
        SampleBTree.print_9()
        size = find_height_iterative(self.root)
        self.assertEqual(5, size)
        print("Height of given tree = {0}".format(size), end="\n\n")
        
        self.root = BTreeNode(10)
        print("Tree to operate: ")
        print(" " * 20 + "10\n")
        size = find_height_iterative(self.root)
        self.assertEqual(1, size)
        print("Height of given tree = {0}".format(size), end=" ")
        
        print(
            "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")


if __name__ == "__main__":
    unittest.main()
