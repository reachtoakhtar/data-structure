__author__ = "akhtar"

import unittest

from tests.test_tree.utils import SampleBTree
from tree.binary_tree import Tree
from tree.problems.binary_tree.mirror import mirror


class TestMirror(unittest.TestCase):
    def setUp(self):
        return super().setUp()
    
    def test_mirror(self):
        print("TEST MIRROR OF A BINARY TREE")
        print("===========================================================")
        
        root = SampleBTree.create_1()
        SampleBTree.print_1()
        print("Inorder traversal of the tree:", end=" ")
        Tree.inorder(root)
        print()
        mirror(root)
        print("Inorder traversal of the mirror:", end=" ")
        Tree.inorder(root)
        print("\n\n")
        
        root = SampleBTree.create_3()
        SampleBTree.print_3()
        print("Inorder traversal of the tree:", end=" ")
        Tree.inorder(root)
        print()
        mirror(root)
        print("Inorder traversal of the mirror:", end=" ")
        Tree.inorder(root)
        print("\n\n")
        
        root = SampleBTree.create_4()
        SampleBTree.print_4()
        print("Inorder traversal of the tree:", end=" ")
        Tree.inorder(root)
        print()
        mirror(root)
        print("Inorder traversal of the mirror:", end=" ")
        Tree.inorder(root)
        print("\n\n")
        
        root = SampleBTree.create_6()
        SampleBTree.print_6()
        print("Inorder traversal of the tree:", end=" ")
        Tree.inorder(root)
        print()
        mirror(root)
        print("Inorder traversal of the mirror:", end=" ")
        Tree.inorder(root)
        print("\n\n")
        
        root = SampleBTree.create_9()
        SampleBTree.print_9()
        print("Inorder traversal of the tree:", end=" ")
        Tree.inorder(root)
        print()
        mirror(root)
        print("Inorder traversal of the mirror:", end=" ")
        Tree.inorder(root)
        print("\n\n")
        
        root = SampleBTree.create_left_weighted()
        SampleBTree.print_left_weighted()
        print("Inorder traversal of the tree:", end=" ")
        Tree.inorder(root)
        print()
        mirror(root)
        print("Inorder traversal of the mirror:", end=" ")
        Tree.inorder(root)
        print("\n\n")
        
        root = SampleBTree.create_right_weighted()
        SampleBTree.print_right_weighted()
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
