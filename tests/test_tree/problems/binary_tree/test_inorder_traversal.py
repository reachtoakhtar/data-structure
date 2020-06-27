__author__ = "akhtar"

import unittest

from tests.test_tree.utils import SampleBTree
from tree.problems.binary_tree.traversal_inorder import inorder_iterative


class TestInorderTraversal(unittest.TestCase):
    def setUp(self):
        return super().setUp()
    
    def test_inorder_recursive(self):
        print("TEST INORDER TRAVERSAL OF A BINARY TREE - RECURSIVE")
        print("===========================================================")
        
        root = SampleBTree.create_1()
        SampleBTree.print_1()
        print("Inorder traversal:", end=" ")
        inorder_iterative(root)
        print("\n\n")
        
        root = SampleBTree.create_3()
        SampleBTree.print_3()
        print("Inorder traversal:", end=" ")
        inorder_iterative(root)
        print("\n\n")
        
        root = SampleBTree.create_4()
        SampleBTree.print_4()
        print("Inorder traversal:", end=" ")
        inorder_iterative(root)
        print("\n\n")
        
        root = SampleBTree.create_6()
        SampleBTree.print_6()
        print("Inorder traversal:", end=" ")
        inorder_iterative(root)
        print("\n\n")
        
        root = SampleBTree.create_9()
        SampleBTree.print_9()
        print("Inorder traversal:", end=" ")
        inorder_iterative(root)
        print("\n\n")
        
        root = SampleBTree.create_left_weighted()
        SampleBTree.print_left_weighted()
        print("Inorder traversal:", end=" ")
        inorder_iterative(root)
        print("\n\n")
        
        root = SampleBTree.create_right_weighted()
        SampleBTree.print_right_weighted()
        print("Inorder traversal:", end=" ")
        inorder_iterative(root)
        
        print(
            "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")

    def test_inorder_iterative(self):
        print("TEST INORDER TRAVERSAL OF A BINARY TREE - ITERATIVE")
        print("===========================================================")
        
        root = SampleBTree.create_1()
        SampleBTree.print_1()
        print("Inorder traversal:", end=" ")
        inorder_iterative(root)
        print("\n\n")
        
        root = SampleBTree.create_3()
        SampleBTree.print_3()
        print("Inorder traversal:", end=" ")
        inorder_iterative(root)
        print("\n\n")
        
        root = SampleBTree.create_4()
        SampleBTree.print_4()
        print("Inorder traversal:", end=" ")
        inorder_iterative(root)
        print("\n\n")
        
        root = SampleBTree.create_6()
        SampleBTree.print_6()
        print("Inorder traversal:", end=" ")
        inorder_iterative(root)
        print("\n\n")
        
        root = SampleBTree.create_9()
        SampleBTree.print_9()
        print("Inorder traversal:", end=" ")
        inorder_iterative(root)
        print("\n\n")
        
        root = SampleBTree.create_left_weighted()
        SampleBTree.print_left_weighted()
        print("Inorder traversal:", end=" ")
        inorder_iterative(root)
        print("\n\n")
        
        root = SampleBTree.create_right_weighted()
        SampleBTree.print_right_weighted()
        print("Inorder traversal:", end=" ")
        inorder_iterative(root)
        
        print(
            "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")


if __name__ == "__main__":
    unittest.main()
