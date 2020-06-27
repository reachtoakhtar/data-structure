__author__ = "akhtar"

import unittest

from tests.test_tree.utils import SampleBTree
from tree.problems.binary_tree.traversal_postorder import postorder_iterative


class TestPostorderTraversal(unittest.TestCase):
    def setUp(self):
        return super().setUp()
    
    def test_postorder_recursive(self):
        print("TEST POSTORDER TRAVERSAL OF A BINARY TREE - RECURSIVE")
        print("===========================================================")
        
        root = SampleBTree.create_1()
        SampleBTree.print_1()
        print("Postorder traversal:", end=" ")
        postorder_iterative(root)
        print("\n\n")
        
        root = SampleBTree.create_3()
        SampleBTree.print_3()
        print("Postorder traversal:", end=" ")
        postorder_iterative(root)
        print("\n\n")
        
        root = SampleBTree.create_4()
        SampleBTree.print_4()
        print("Postorder traversal:", end=" ")
        postorder_iterative(root)
        print("\n\n")
        
        root = SampleBTree.create_6()
        SampleBTree.print_6()
        print("Postorder traversal:", end=" ")
        postorder_iterative(root)
        print("\n\n")
        
        root = SampleBTree.create_9()
        SampleBTree.print_9()
        print("Postorder traversal:", end=" ")
        postorder_iterative(root)
        print("\n\n")
        
        root = SampleBTree.create_left_weighted()
        SampleBTree.print_left_weighted()
        print("Postorder traversal:", end=" ")
        postorder_iterative(root)
        print("\n\n")
        
        root = SampleBTree.create_right_weighted()
        SampleBTree.print_right_weighted()
        print("Postorder traversal:", end=" ")
        postorder_iterative(root)
        
        print(
            "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")
    
    def test_postorder_iterative(self):
        print("TEST POSTORDER TRAVERSAL OF A BINARY TREE - ITERATIVE")
        print("===========================================================")
        
        root = SampleBTree.create_1()
        SampleBTree.print_1()
        print("Postorder traversal:", end=" ")
        postorder_iterative(root)
        print("\n\n")
        
        root = SampleBTree.create_3()
        SampleBTree.print_3()
        print("Postorder traversal:", end=" ")
        postorder_iterative(root)
        print("\n\n")
        
        root = SampleBTree.create_4()
        SampleBTree.print_4()
        print("Postorder traversal:", end=" ")
        postorder_iterative(root)
        print("\n\n")
        
        root = SampleBTree.create_6()
        SampleBTree.print_6()
        print("Postorder traversal:", end=" ")
        postorder_iterative(root)
        print("\n\n")
        
        root = SampleBTree.create_9()
        SampleBTree.print_9()
        print("Postorder traversal:", end=" ")
        postorder_iterative(root)
        print("\n\n")
        
        root = SampleBTree.create_left_weighted()
        SampleBTree.print_left_weighted()
        print("Postorder traversal:", end=" ")
        postorder_iterative(root)
        print("\n\n")
        
        root = SampleBTree.create_right_weighted()
        SampleBTree.print_right_weighted()
        print("Postorder traversal:", end=" ")
        postorder_iterative(root)
        
        print(
            "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")


if __name__ == "__main__":
    unittest.main()
