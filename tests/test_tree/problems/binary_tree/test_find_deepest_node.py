__author__ = "akhtar"

import unittest

from tests.test_tree.utils import SampleTree
from tree.problems.binary_tree.deepest_node import find_deepest_node


class TestFindDeepestNode(unittest.TestCase):
    def setUp(self):
        self.create_tree()
    
    def create_tree(self):
        self.root = SampleTree.create()
    
    def test_find_deepest_node(self):
        print("TEST FIND DEEPEST NODE OF A BINARY TREE")
        print("===========================================================")
        
        SampleTree.print()
        node = find_deepest_node(self.root)
        self.assertEqual(4, node)
        print("Deepest node = {0}".format(node), end=" ")
        
        print(
            "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")


if __name__ == "__main__":
    unittest.main()
