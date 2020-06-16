import unittest

from tree.binary_tree import TreeNode
from tree.problems.binary_tree.find_size import find_size_iterative, \
    find_size_recursive

__author__ = "akhtar"


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

    def test_find_size_recursive(self):
        print("TEST FIND SIZE OF A BINARY TREE - RECURSIVE")
        print("===========================================================")

        TestFindSize.print_sample_tree()
        size = find_size_recursive(self.root)
        self.assertEqual(6, size)
        print("Size of given tree = {0}".format(size), end="\n\n")

        self.root = TreeNode(10)
        print("Tree to operate: ")
        print(" "*20 + "10\n")
        size = find_size_recursive(self.root)
        self.assertEqual(1, size)
        print("Size of given tree = {0}".format(size), end=" ")

        print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")

    def test_find_size_iterative(self):
        print("TEST FIND SIZE OF A BINARY TREE - RECURSIVE")
        print("===========================================================")

        TestFindSize.print_sample_tree()
        size = find_size_iterative(self.root)
        self.assertEqual(6, size)
        print("Size of given tree = {0}".format(size), end="\n\n")

        self.root = TreeNode(10)
        print("Tree to operate: ")
        print(" "*20 + "10\n")
        size = find_size_iterative(self.root)
        self.assertEqual(1, size)
        print("Size of given tree = {0}".format(size), end=" ")

        print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")


if __name__ == "__main__":
    unittest.main()
