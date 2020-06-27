__author__ = "akhtar"

import unittest

from tests.test_tree.utils import SampleBTree
from tree.problems.binary_tree.insert import insert_into_binary_tree
from tree.problems.binary_tree.traversal_inorder import inorder


class TestInsertIntoBinaryTree(unittest.TestCase):
    def setUp(self):
        self.create_tree()
    
    def create_tree(self):
        self.root = SampleBTree.create_9()
    
    def test_insert_into_tree(self):
        print("TEST INSERT INTO BINARY TREE")
        print("===========================================================")
        
        SampleBTree.print_9()
        print("Inorder traversal before insertion  : ", end=" ")
        inorder(self.root)
        print()
        
        insert_into_binary_tree(self.root, 12)
        
        print("Inorder traversal after inserting 12: ", end=" ")
        inorder(self.root)
        
        print(
            "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")


if __name__ == "__main__":
    unittest.main()
