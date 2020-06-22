__author__ = "akhtar"

import unittest

from tests.test_tree.utils import SampleTree
from tree.problems.binary_tree.diameter import find_diameter


class TestDiameter(unittest.TestCase):
    def setUp(self):
        return super().setUp()
    
    def test_diameter(self):
        print("TEST DIAMETER OF A BINARY TREE")
        print("===========================================================")
        
        root = SampleTree.create_1()
        SampleTree.print_1()
        diameter = find_diameter(root)
        print("Diameter of the tree = {0}".format(diameter), end=" ")
        print("\n\n")

        root = SampleTree.create_3()
        SampleTree.print_3()
        diameter = find_diameter(root)
        print("Diameter of the tree = {0}".format(diameter), end=" ")
        print("\n\n")

        root = SampleTree.create_4()
        SampleTree.print_4()
        diameter = find_diameter(root)
        print("Diameter of the tree = {0}".format(diameter), end=" ")
        print("\n\n")

        root = SampleTree.create_6()
        SampleTree.print_6()
        diameter = find_diameter(root)
        print("Diameter of the tree = {0}".format(diameter), end=" ")
        print("\n\n")

        root = SampleTree.create_9()
        SampleTree.print_9()
        diameter = find_diameter(root)
        print("Diameter of the tree = {0}".format(diameter))
        print("\n\n")
        
        root = SampleTree.create_left_weighted()
        SampleTree.print_left_weighted()
        diameter = find_diameter(root)
        print("Diameter of the tree = {0}".format(diameter))
        print("\n\n")
        
        root = SampleTree.create_right_weighted()
        SampleTree.print_right_weighted()
        diameter = find_diameter(root)
        print("Diameter of the tree = {0}".format(diameter))
        
        print(
            "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")


if __name__ == "__main__":
    unittest.main()
