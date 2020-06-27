__author__ = "akhtar"

import unittest

from tests.test_tree.utils import SampleBTree
from tree.problems.binary_tree.search_element import find_element_iterative, \
    find_element_recursive


class TestFindElementInABinaryTree(unittest.TestCase):
    def setUp(self):
        self.create_tree()
    
    def create_tree(self):
        self.root = SampleBTree.create_9()
    
    def test_find_element_recursive(self):
        print("TEST SEARCH ELEMENT - RECURSIVE")
        print("===========================================================")
        
        SampleBTree.print_9()
        print("Element to search: 15.", end=" ")
        found = find_element_recursive(self.root, 15)
        self.assertEqual(True, found)
        print("Element found: {0}".format(found), end="\n")
        
        print("Element to search: 34.", end=" ")
        found = find_element_recursive(self.root, 34)
        self.assertEqual(False, found)
        print("Element found: {0}".format(found), end="\n")
        
        print("Element to search: 10.", end=" ")
        found = find_element_recursive(self.root, 10)
        self.assertEqual(True, found)
        print("Element found: {0}".format(found), end="\n")
        
        print("Element to search: 11.", end=" ")
        found = find_element_recursive(self.root, 11)
        self.assertEqual(True, found)
        print("Element found: {0}".format(found), end="\n")
        
        print("Element to search: 63.", end=" ")
        found = find_element_recursive(self.root, 63)
        self.assertEqual(False, found)
        print("Element found: {0}".format(found), end=" ")
        
        print(
            "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")
    
    def test_find_element_iterative(self):
        print("TEST SEARCH ELEMENT - ITERATIVE")
        print("===========================================================")
        
        SampleBTree.print_9()
        print("Element to search: 15.", end=" ")
        found = find_element_iterative(self.root, 15)
        self.assertEqual(True, found)
        print("Element found: {0}".format(found), end="\n")
        
        print("Element to search: 34.", end=" ")
        found = find_element_iterative(self.root, 34)
        self.assertEqual(False, found)
        print("Element found: {0}".format(found), end="\n")
        
        print("Element to search: 10.", end=" ")
        found = find_element_iterative(self.root, 10)
        self.assertEqual(True, found)
        print("Element found: {0}".format(found), end="\n")
        
        print("Element to search: 11.", end=" ")
        found = find_element_iterative(self.root, 11)
        self.assertEqual(True, found)
        print("Element found: {0}".format(found), end="\n")
        
        print("Element to search: 63.", end=" ")
        found = find_element_iterative(self.root, 63)
        self.assertEqual(False, found)
        print("Element found: {0}".format(found), end=" ")
        
        print(
            "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")


if __name__ == "__main__":
    unittest.main()
