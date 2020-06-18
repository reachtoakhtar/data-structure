__author__ = "akhtar"

import unittest

from tree.binary_tree import TreeNode
from tree.problems.binary_tree.search_element import find_element_iterative, \
    find_element_recursive


class TestFindElementInABinaryTree(unittest.TestCase):
    """
    Initial tree:
             10
            /  \
           11   9
          /    / \
         7    15  8
    """
    @staticmethod
    def print_sample_tree():
        print("Tree to operate: ")
        print(" "*20 + "10 \n" + " "*18 + " /  \\ \n" + " "*17 + "11    9 \n" +
              " "*16 + "/     / \\ \n" + " "*15 + "7     15  8\n")

    def setUp(self):
        self.create_tree()

    def create_tree(self):
        self.root = TreeNode(10)
        self.root.left = TreeNode(11)
        self.root.left.left = TreeNode(7)
        self.root.right = TreeNode(9)
        self.root.right.left = TreeNode(15)
        self.root.right.right = TreeNode(8)

    def test_find_element_recursive(self):
        print("TEST SEARCH ELEMENT - RECURSIVE")
        print("===========================================================")

        TestFindElementInABinaryTree.print_sample_tree()
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

        print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")

    def test_find_element_iterative(self):
        print("TEST SEARCH ELEMENT - ITERATIVE")
        print("===========================================================")

        TestFindElementInABinaryTree.print_sample_tree()
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

        print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")


if __name__ == "__main__":
    unittest.main()
