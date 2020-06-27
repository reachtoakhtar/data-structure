__author__ = "akhtar"

import unittest

from tests.test_tree.utils import SampleBTree
from tree.problems.binary_tree.diameter import find_diameter


class TestDiameter(unittest.TestCase):
    def setUp(self):
        return super().setUp()
    
    def test_diameter(self):
        print("TEST DIAMETER OF A BINARY TREE")
        print("===========================================================")
        
        root = SampleBTree.create_1()
        SampleBTree.print_1()
        diameter = find_diameter(root)
        print("Diameter of the tree = {0}".format(diameter), end=" ")
        print("\n\n")

        root = SampleBTree.create_3()
        SampleBTree.print_3()
        diameter = find_diameter(root)
        print("Diameter of the tree = {0}".format(diameter), end=" ")
        print("\n\n")

        root = SampleBTree.create_4()
        SampleBTree.print_4()
        diameter = find_diameter(root)
        print("Diameter of the tree = {0}".format(diameter), end=" ")
        print("\n\n")

        root = SampleBTree.create_6()
        SampleBTree.print_6()
        diameter = find_diameter(root)
        print("Diameter of the tree = {0}".format(diameter), end=" ")
        print("\n\n")

        root = SampleBTree.create_9()
        SampleBTree.print_9()
        diameter = find_diameter(root)
        print("Diameter of the tree = {0}".format(diameter))
        print("\n\n")
        
        root = SampleBTree.create_left_weighted()
        SampleBTree.print_left_weighted()
        diameter = find_diameter(root)
        print("Diameter of the tree = {0}".format(diameter))
        print("\n\n")
        
        root = SampleBTree.create_right_weighted()
        SampleBTree.print_right_weighted()
        diameter = find_diameter(root)
        print("Diameter of the tree = {0}".format(diameter))
        
        print(
            "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")


if __name__ == "__main__":
    unittest.main()
