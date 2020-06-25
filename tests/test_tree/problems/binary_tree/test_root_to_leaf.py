__author__ = "akhtar"

import unittest

from tests.test_tree.utils import SampleTree
from tree.problems.binary_tree.root_to_leaf import all_paths_from_root_to_leaf


class TestRootToLeaf(unittest.TestCase):
    def setUp(self):
        return super().setUp()
    
    def test_diameter(self):
        print("TEST ALL PATHS FROM ROOT TO LEAF IN A BINARY TREE")
        print("===========================================================")
        
        root = SampleTree.create_1()
        SampleTree.print_1()
        print("All root to leaf paths:")
        all_paths_from_root_to_leaf(root)
        print("\n\n")
        
        root = SampleTree.create_3()
        SampleTree.print_3()
        print("All root to leaf paths:")
        all_paths_from_root_to_leaf(root)
        print("\n\n")
        
        root = SampleTree.create_4()
        SampleTree.print_4()
        print("All root to leaf paths:")
        all_paths_from_root_to_leaf(root)
        print("\n\n")
        
        root = SampleTree.create_6()
        SampleTree.print_6()
        print("All root to leaf paths:")
        all_paths_from_root_to_leaf(root)
        print("\n\n")
        
        root = SampleTree.create_9()
        SampleTree.print_9()
        print("All root to leaf paths:")
        all_paths_from_root_to_leaf(root)
        print("\n\n")
        
        root = SampleTree.create_left_weighted()
        SampleTree.print_left_weighted()
        print("All root to leaf paths:")
        all_paths_from_root_to_leaf(root)
        print("\n\n")
        
        root = SampleTree.create_right_weighted()
        SampleTree.print_right_weighted()
        print("All root to leaf paths:")
        all_paths_from_root_to_leaf(root)
        
        print(
            "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")


if __name__ == "__main__":
    unittest.main()
