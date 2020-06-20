__author__ = "akhtar"

import unittest

from tests.test_tree.utils import SampleTree
from tree.binary_tree import Tree
from tree.problems.binary_tree.delete_node import delete_node


class TestDeletetNode(unittest.TestCase):
    def setUp(self):
        self.create_tree()
    
    def create_tree(self):
        self.root = SampleTree.create()
    
    def test_delete_node(self):
        print("TEST FIND DEEPEST NODE OF A BINARY TREE")
        print("===========================================================")
        
        SampleTree.print()
        print("Inorder traversal before delete:", end=" ")
        Tree.inorder(self.root)
        print()
        delete_node(self.root, 15)
        print("Inorder traversal after delete:", end=" ")
        Tree.inorder(self.root)
        
        print(
            "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")


if __name__ == "__main__":
    unittest.main()
