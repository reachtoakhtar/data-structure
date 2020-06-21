__author__ = "akhtar"

import unittest

from tests.test_tree.utils import SampleTree
from tree.problems.binary_tree.leaf_nodes import find_leaf_nodes


class TestFindLeafNodes(unittest.TestCase):
    def setUp(self):
        self.create_tree()
    
    def create_tree(self):
        self.root = SampleTree.create()
    
    def test_find_leaf_nodes(self):
        print("TEST FIND DEEPEST NODE OF A BINARY TREE")
        print("===========================================================")
        
        SampleTree.print()
        leaf_count = find_leaf_nodes(self.root)
        print("Count of leaf nodes = {0}".format(leaf_count), end=" ")
        
        print(
            "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")


if __name__ == "__main__":
    unittest.main()
