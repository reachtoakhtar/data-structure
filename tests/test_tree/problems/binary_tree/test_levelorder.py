__author__ = "akhtar"

import unittest

from tests.test_tree.utils import SampleBTree
from tree.problems.binary_tree.traversal_levelorder import levelorder


class TestLevelorderTraversal(unittest.TestCase):
    def setUp(self):
        return super().setUp()
    
    def test_levelorder(self):
        print("TEST LEVELORDER TRAVERSAL OF A BINARY TREE")
        print("===========================================================")
        
        root = SampleBTree.create_1()
        SampleBTree.print_1()
        print("Levelorder traversal:", end=" ")
        levelorder(root)
        print("\n\n")
        
        root = SampleBTree.create_3()
        SampleBTree.print_3()
        print("Levelorder traversal:", end=" ")
        levelorder(root)
        print("\n\n")
        
        root = SampleBTree.create_4()
        SampleBTree.print_4()
        print("Levelorder traversal:", end=" ")
        levelorder(root)
        print("\n\n")
        
        root = SampleBTree.create_6()
        SampleBTree.print_6()
        print("Levelorder traversal:", end=" ")
        levelorder(root)
        print("\n\n")
        
        root = SampleBTree.create_9()
        SampleBTree.print_9()
        print("Levelorder traversal:", end=" ")
        levelorder(root)
        print("\n\n")
        
        root = SampleBTree.create_left_weighted()
        SampleBTree.print_left_weighted()
        print("Levelorder traversal:", end=" ")
        levelorder(root)
        print("\n\n")
        
        root = SampleBTree.create_right_weighted()
        SampleBTree.print_right_weighted()
        print("Levelorder traversal:", end=" ")
        levelorder(root)
        
        print(
            "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")
    

if __name__ == "__main__":
    unittest.main()
