__author__ = "akhtar"

import unittest

from tests.test_tree.utils import SampleTree
from tree.problems.binary_tree.maximum_sum_level import level_with_maximum_sum


class TestMaxSumLevel(unittest.TestCase):
    def setUp(self):
        return super().setUp()
    
    def test_diameter(self):
        print("TEST LEVEL OF MAXIMUM SUM IN A BINARY TREE")
        print("===========================================================")
        
        root = SampleTree.create_1()
        SampleTree.print_1()
        max_sum_level, sum = level_with_maximum_sum(root)
        print("Maximum sum = {0}".format(sum))
        print("Maximum sum level = {0}".format(max_sum_level), end=" ")
        print("\n\n")
        
        root = SampleTree.create_3()
        SampleTree.print_3()
        max_sum_level, sum = level_with_maximum_sum(root)
        print("Maximum sum = {0}".format(sum))
        print("Maximum sum level = {0}".format(max_sum_level), end=" ")
        print("\n\n")
        
        root = SampleTree.create_4()
        SampleTree.print_4()
        max_sum_level, sum = level_with_maximum_sum(root)
        print("Maximum sum = {0}".format(sum))
        print("Maximum sum level = {0}".format(max_sum_level), end=" ")
        print("\n\n")
        
        root = SampleTree.create_6()
        SampleTree.print_6()
        max_sum_level, sum = level_with_maximum_sum(root)
        print("Maximum sum = {0}".format(sum))
        print("Maximum sum level = {0}".format(max_sum_level), end=" ")
        print("\n\n")
        
        root = SampleTree.create_9()
        SampleTree.print_9()
        max_sum_level, sum = level_with_maximum_sum(root)
        print("Maximum sum = {0}".format(sum))
        print("Maximum sum level = {0}".format(max_sum_level))
        print("\n\n")
        
        root = SampleTree.create_left_weighted()
        SampleTree.print_left_weighted()
        max_sum_level, sum = level_with_maximum_sum(root)
        print("Maximum sum = {0}".format(sum))
        print("Maximum sum level = {0}".format(max_sum_level))
        print("\n\n")
        
        root = SampleTree.create_right_weighted()
        SampleTree.print_right_weighted()
        max_sum_level, sum = level_with_maximum_sum(root)
        print("Maximum sum = {0}".format(sum))
        print("Maximum sum level = {0}".format(max_sum_level))
        
        print(
            "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")


if __name__ == "__main__":
    unittest.main()
