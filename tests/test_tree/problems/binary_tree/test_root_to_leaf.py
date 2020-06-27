__author__ = "akhtar"

import unittest

from tests.test_tree.utils import SampleBTree
from tree.problems.binary_tree.root_to_leaf import all_paths_from_root_to_leaf


class TestRootToLeaf(unittest.TestCase):
    def setUp(self):
        return super().setUp()
    
    def test_diameter(self):
        print("TEST ALL PATHS FROM ROOT TO LEAF IN A BINARY TREE")
        print("===========================================================")
        
        root = SampleBTree.create_1()
        SampleBTree.print_1()
        print("All root to leaf paths:")
        all_paths_from_root_to_leaf(root)
        print("\n\n")
        
        root = SampleBTree.create_3()
        SampleBTree.print_3()
        print("All root to leaf paths:")
        all_paths_from_root_to_leaf(root)
        print("\n\n")
        
        root = SampleBTree.create_4()
        SampleBTree.print_4()
        print("All root to leaf paths:")
        all_paths_from_root_to_leaf(root)
        print("\n\n")
        
        root = SampleBTree.create_6()
        SampleBTree.print_6()
        print("All root to leaf paths:")
        all_paths_from_root_to_leaf(root)
        print("\n\n")
        
        root = SampleBTree.create_9()
        SampleBTree.print_9()
        print("All root to leaf paths:")
        all_paths_from_root_to_leaf(root)
        print("\n\n")
        
        root = SampleBTree.create_left_weighted()
        SampleBTree.print_left_weighted()
        print("All root to leaf paths:")
        all_paths_from_root_to_leaf(root)
        print("\n\n")
        
        root = SampleBTree.create_right_weighted()
        SampleBTree.print_right_weighted()
        print("All root to leaf paths:")
        all_paths_from_root_to_leaf(root)
        
        print(
            "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")


if __name__ == "__main__":
    unittest.main()
