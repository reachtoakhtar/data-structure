__author__ = "akhtar"

import unittest

from tree.binary_tree import TreeNode
from tree.problems.binary_tree.find_height import find_height_iterative, \
    find_height_recursive


class TestFindSize(unittest.TestCase):
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

    def test_find_height_recursive(self):
        print("TEST FIND HEIGHT OF A BINARY TREE - RECURSIVE")
        print("===========================================================")

        TestFindSize.print_sample_tree()
        height = find_height_recursive(self.root)
        self.assertEqual(3, height)
        print("Height of given tree = {0}".format(height), end="\n\n")

        self.root = TreeNode(10)
        print("Tree to operate: ")
        print(" "*20 + "10\n")
        height = find_height_recursive(self.root)
        self.assertEqual(1, height)
        print("Height of given tree = {0}".format(height), end=" ")

        print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")

    def test_find_height_iterative(self):
        print("TEST FIND HEIGHT OF A BINARY TREE - ITERATIVE")
        print("===========================================================")

        TestFindSize.print_sample_tree()
        size = find_height_iterative(self.root)
        self.assertEqual(3, size)
        print("Height of given tree = {0}".format(size), end="\n\n")

        self.root = TreeNode(10)
        print("Tree to operate: ")
        print(" "*20 + "10\n")
        size = find_height_iterative(self.root)
        self.assertEqual(1, size)
        print("Height of given tree = {0}".format(size), end=" ")

        print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")


if __name__ == "__main__":
    unittest.main()
