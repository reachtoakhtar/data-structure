__author__ = "akhtar"

import unittest

from tests.test_tree.utils import SampleTree
from tree.binary_tree import TreeNode
from tree.problems.binary_tree.find_size import find_size_iterative, \
    find_size_recursive


class TestFindSize(unittest.TestCase):
    def setUp(self):
        self.create_tree()
    
    def create_tree(self):
        self.root = SampleTree.create_9()
    
    def test_find_size_recursive(self):
        print("TEST FIND SIZE OF A BINARY TREE - RECURSIVE")
        print("===========================================================")
        
        SampleTree.print_9()
        size = find_size_recursive(self.root)
        self.assertEqual(9, size)
        print("Size of given tree = {0}".format(size), end="\n\n")
        
        self.root = TreeNode(10)
        print("Tree to operate: ")
        print(" " * 20 + "10\n")
        size = find_size_recursive(self.root)
        self.assertEqual(1, size)
        print("Size of given tree = {0}".format(size), end=" ")
        
        print(
            "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")
    
    def test_find_size_iterative(self):
        print("TEST FIND SIZE OF A BINARY TREE - ITERATIVE")
        print("===========================================================")
        
        SampleTree.print_9()
        size = find_size_iterative(self.root)
        self.assertEqual(9, size)
        print("Size of given tree = {0}".format(size), end="\n\n")
        
        self.root = TreeNode(10)
        print("Tree to operate: ")
        print(" " * 20 + "10\n")
        size = find_size_iterative(self.root)
        self.assertEqual(1, size)
        print("Size of given tree = {0}".format(size), end=" ")
        
        print(
            "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")


if __name__ == "__main__":
    unittest.main()
