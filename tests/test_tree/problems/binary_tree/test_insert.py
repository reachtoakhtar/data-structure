__author__ = "akhtar"

import unittest

from tests.test_tree.utils import SampleTree
from tree.binary_tree import Tree
from tree.problems.binary_tree.insert import insert_into_binary_tree


class TestInsertIntoBinaryTree(unittest.TestCase):
    def setUp(self):
        self.create_tree()
    
    def create_tree(self):
        self.root = SampleTree.create()
    
    def test_insert_into_tree(self):
        print("TEST INSERT INTO BINARY TREE")
        print("===========================================================")
        
        SampleTree.print()
        print("Inorder traversal before insertion  : ", end=" ")
        Tree.inorder(self.root)
        print()
        
        insert_into_binary_tree(self.root, 12)
        
        print("Inorder traversal after inserting 12: ", end=" ")
        Tree.inorder(self.root)
        
        print(
            "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")


if __name__ == "__main__":
    unittest.main()
