__author__ = "akhtar"

import unittest

from tests.test_tree.utils import SampleTree
from tree.binary_tree import Tree
from tree.problems.binary_tree.mirror import mirror


class TestMirror(unittest.TestCase):
    def setUp(self):
        return super().setUp()
    
    def test_mirror(self):
        print("TEST MIRROR OF A BINARY TREE")
        print("===========================================================")
        
        root = SampleTree.create_1()
        SampleTree.print_1()
        print("Inorder traversal of the tree:", end=" ")
        Tree.inorder(root)
        print()
        mirror(root)
        print("Inorder traversal of the mirror:", end=" ")
        Tree.inorder(root)
        print("\n\n")
        
        root = SampleTree.create_3()
        SampleTree.print_3()
        print("Inorder traversal of the tree:", end=" ")
        Tree.inorder(root)
        print()
        mirror(root)
        print("Inorder traversal of the mirror:", end=" ")
        Tree.inorder(root)
        print("\n\n")
        
        root = SampleTree.create_4()
        SampleTree.print_4()
        print("Inorder traversal of the tree:", end=" ")
        Tree.inorder(root)
        print()
        mirror(root)
        print("Inorder traversal of the mirror:", end=" ")
        Tree.inorder(root)
        print("\n\n")
        
        root = SampleTree.create_6()
        SampleTree.print_6()
        print("Inorder traversal of the tree:", end=" ")
        Tree.inorder(root)
        print()
        mirror(root)
        print("Inorder traversal of the mirror:", end=" ")
        Tree.inorder(root)
        print("\n\n")
        
        root = SampleTree.create_9()
        SampleTree.print_9()
        print("Inorder traversal of the tree:", end=" ")
        Tree.inorder(root)
        print()
        mirror(root)
        print("Inorder traversal of the mirror:", end=" ")
        Tree.inorder(root)
        print("\n\n")
        
        root = SampleTree.create_left_weighted()
        SampleTree.print_left_weighted()
        print("Inorder traversal of the tree:", end=" ")
        Tree.inorder(root)
        print()
        mirror(root)
        print("Inorder traversal of the mirror:", end=" ")
        Tree.inorder(root)
        print("\n\n")
        
        root = SampleTree.create_right_weighted()
        SampleTree.print_right_weighted()
        print("Inorder traversal of the tree:", end=" ")
        Tree.inorder(root)
        print()
        mirror(root)
        print("Inorder traversal of the mirror:", end=" ")
        Tree.inorder(root)
        
        print(
            "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")


if __name__ == "__main__":
    unittest.main()
