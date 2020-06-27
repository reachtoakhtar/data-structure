__author__ = "akhtar"

import unittest

from tests.test_tree.utils import SampleBTree
from tree.problems.binary_tree.traversal_preorder import preorder_iterative


class TestPreorderTraversal(unittest.TestCase):
    def setUp(self):
        return super().setUp()
    
    def test_preorder_recursive(self):
        print("TEST PREORDER TRAVERSAL OF A BINARY TREE - RECURSIVE")
        print("===========================================================")
        
        root = SampleBTree.create_1()
        SampleBTree.print_1()
        print("Preorder traversal:", end=" ")
        preorder_iterative(root)
        print("\n\n")
        
        root = SampleBTree.create_3()
        SampleBTree.print_3()
        print("Preorder traversal:", end=" ")
        preorder_iterative(root)
        print("\n\n")
        
        root = SampleBTree.create_4()
        SampleBTree.print_4()
        print("Preorder traversal:", end=" ")
        preorder_iterative(root)
        print("\n\n")
        
        root = SampleBTree.create_6()
        SampleBTree.print_6()
        print("Preorder traversal:", end=" ")
        preorder_iterative(root)
        print("\n\n")
        
        root = SampleBTree.create_9()
        SampleBTree.print_9()
        print("Preorder traversal:", end=" ")
        preorder_iterative(root)
        print("\n\n")
        
        root = SampleBTree.create_left_weighted()
        SampleBTree.print_left_weighted()
        print("Preorder traversal:", end=" ")
        preorder_iterative(root)
        print("\n\n")
        
        root = SampleBTree.create_right_weighted()
        SampleBTree.print_right_weighted()
        print("Preorder traversal:", end=" ")
        preorder_iterative(root)
        
        print(
            "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")
    
    def test_preorder_iterative(self):
        print("TEST PREORDER TRAVERSAL OF A BINARY TREE - ITERATIVE")
        print("===========================================================")
        
        root = SampleBTree.create_1()
        SampleBTree.print_1()
        print("Preorder traversal:", end=" ")
        preorder_iterative(root)
        print("\n\n")
        
        root = SampleBTree.create_3()
        SampleBTree.print_3()
        print("Preorder traversal:", end=" ")
        preorder_iterative(root)
        print("\n\n")
        
        root = SampleBTree.create_4()
        SampleBTree.print_4()
        print("Preorder traversal:", end=" ")
        preorder_iterative(root)
        print("\n\n")
        
        root = SampleBTree.create_6()
        SampleBTree.print_6()
        print("Preorder traversal:", end=" ")
        preorder_iterative(root)
        print("\n\n")
        
        root = SampleBTree.create_9()
        SampleBTree.print_9()
        print("Preorder traversal:", end=" ")
        preorder_iterative(root)
        print("\n\n")
        
        root = SampleBTree.create_left_weighted()
        SampleBTree.print_left_weighted()
        print("Preorder traversal:", end=" ")
        preorder_iterative(root)
        print("\n\n")
        
        root = SampleBTree.create_right_weighted()
        SampleBTree.print_right_weighted()
        print("Preorder traversal:", end=" ")
        preorder_iterative(root)
        
        print(
            "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")


if __name__ == "__main__":
    unittest.main()
