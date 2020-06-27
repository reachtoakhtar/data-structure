__author__ = "akhtar"

import unittest

from tests.test_tree.utils import SampleBTree
from tree.problems.binary_tree.maximum_sum_level import level_with_maximum_sum


class TestMaxSumLevel(unittest.TestCase):
    def setUp(self):
        return super().setUp()
    
    def test_diameter(self):
        print("TEST LEVEL OF MAXIMUM SUM IN A BINARY TREE")
        print("===========================================================")
        
        root = SampleBTree.create_1()
        SampleBTree.print_1()
        max_sum_level, sum = level_with_maximum_sum(root)
        print("Maximum sum = {0}".format(sum))
        print("Maximum sum level = {0}".format(max_sum_level), end=" ")
        print("\n\n")
        
        root = SampleBTree.create_3()
        SampleBTree.print_3()
        max_sum_level, sum = level_with_maximum_sum(root)
        print("Maximum sum = {0}".format(sum))
        print("Maximum sum level = {0}".format(max_sum_level), end=" ")
        print("\n\n")
        
        root = SampleBTree.create_4()
        SampleBTree.print_4()
        max_sum_level, sum = level_with_maximum_sum(root)
        print("Maximum sum = {0}".format(sum))
        print("Maximum sum level = {0}".format(max_sum_level), end=" ")
        print("\n\n")
        
        root = SampleBTree.create_6()
        SampleBTree.print_6()
        max_sum_level, sum = level_with_maximum_sum(root)
        print("Maximum sum = {0}".format(sum))
        print("Maximum sum level = {0}".format(max_sum_level), end=" ")
        print("\n\n")
        
        root = SampleBTree.create_9()
        SampleBTree.print_9()
        max_sum_level, sum = level_with_maximum_sum(root)
        print("Maximum sum = {0}".format(sum))
        print("Maximum sum level = {0}".format(max_sum_level))
        print("\n\n")
        
        root = SampleBTree.create_left_weighted()
        SampleBTree.print_left_weighted()
        max_sum_level, sum = level_with_maximum_sum(root)
        print("Maximum sum = {0}".format(sum))
        print("Maximum sum level = {0}".format(max_sum_level))
        print("\n\n")
        
        root = SampleBTree.create_right_weighted()
        SampleBTree.print_right_weighted()
        max_sum_level, sum = level_with_maximum_sum(root)
        print("Maximum sum = {0}".format(sum))
        print("Maximum sum level = {0}".format(max_sum_level))
        
        print(
            "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")


if __name__ == "__main__":
    unittest.main()
