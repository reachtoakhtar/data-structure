import unittest

from tests.test_tree.utils import SampleTree
from tree.binary_tree import TreeNode, Tree

__author__ = "akhtar"


class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        self.create_tree()

    def create_tree(self):
        self.root = SampleTree.create_9()
    
    def test_tree_traversal(self):
        print("TEST TREE TRAVERSAL")
        print("===========================================================")
        SampleTree.print_9()

        print("Levelorder traversal (BFS):", end=" ")
        Tree.levelorder(self.root)
        print("\n")

        print("Preorder traversal (iterative):", end=" ")
        Tree.preorder_iterative(self.root)
        print()

        print("Preorder traversal (recursive):", end=" ")
        Tree.preorder_recursive(self.root)
        print("\n")

        print("Inorder traversal (iterative):", end=" ")
        Tree.inorder_iterative(self.root)
        print()

        print("Inorder traversal (recursive):", end=" ")
        Tree.inorder_recursive(self.root)
        print("\n")

        print("Postorder traversal (iterative):", end=" ")
        Tree.postorder_iterative(self.root)
        print()

        print("Postorder traversal (recursive):", end=" ")
        Tree.postorder_recursive(self.root)

        print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")


if __name__ == "__main__":
    unittest.main()
