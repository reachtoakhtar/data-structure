__author__ = "akhtar"

import unittest

from tests.test_tree.utils import SampleBTree
from tree.problems.binary_tree.deepest_node import find_deepest_node


class TestFindDeepestNode(unittest.TestCase):
    def setUp(self):
        self.create_tree()
    
    def create_tree(self):
        self.root = SampleBTree.create_9()
    
    def test_find_deepest_node(self):
        print("TEST FIND DEEPEST NODE OF A BINARY TREE")
        print("===========================================================")
        
        SampleBTree.print_9()
        node = find_deepest_node(self.root)
        self.assertEqual(4, node.data)
        print("Deepest node = {0}".format(node.data), end=" ")
        
        print(
            "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")


if __name__ == "__main__":
    unittest.main()
