__author__ = "akhtar"

import unittest

from tests.test_tree.utils import SampleBTree
from tree.problems.binary_tree.path_with_sum import has_path_with_sum


class TestPathWithSum(unittest.TestCase):
    def setUp(self):
        return super().setUp()
    
    def test_diameter(self):
        print("TEST PATH WITH SUM EXISTS IN A BINARY TREE")
        print("===========================================================")
        
        root = SampleBTree.create_1()
        SampleBTree.print_1()
        sum = 14
        path_exists = has_path_with_sum(root, sum)
        self.assertEqual(False, path_exists)
        print("Path with sum {0} exists: {1}".format(sum, path_exists))
        print("\n\n")
        
        root = SampleBTree.create_3()
        SampleBTree.print_3()
        sum = 90
        path_exists = has_path_with_sum(root, sum)
        self.assertEqual(True, path_exists)
        print("Path with sum {0} exists: {1}".format(sum, path_exists))
        print("\n\n")
        
        root = SampleBTree.create_4()
        SampleBTree.print_4()
        sum = 45
        path_exists = has_path_with_sum(root, sum)
        self.assertEqual(False, path_exists)
        print("Path with sum {0} exists: {1}".format(sum, path_exists))
        print("\n\n")
        
        root = SampleBTree.create_6()
        SampleBTree.print_6()
        sum = 34
        path_exists = has_path_with_sum(root, sum)
        self.assertEqual(True, path_exists)
        print("Path with sum {0} exists: {1}".format(sum, path_exists))
        print("\n\n")
        
        root = SampleBTree.create_9()
        SampleBTree.print_9()
        sum = 78
        path_exists = has_path_with_sum(root, sum)
        self.assertEqual(False, path_exists)
        print("Path with sum {0} exists: {1}".format(sum, path_exists))
        print("\n\n")
        
        root = SampleBTree.create_left_weighted()
        SampleBTree.print_left_weighted()
        sum = 10
        path_exists = has_path_with_sum(root, sum)
        self.assertEqual(False, path_exists)
        print("Path with sum {0} exists: {1}".format(sum, path_exists))
        print("\n\n")
        
        root = SampleBTree.create_right_weighted()
        SampleBTree.print_right_weighted()
        sum = 21
        path_exists = has_path_with_sum(root, sum)
        self.assertEqual(True, path_exists)
        print("Path with sum {0} exists: {1}".format(sum, path_exists))
        
        print(
            "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")


if __name__ == "__main__":
    unittest.main()
