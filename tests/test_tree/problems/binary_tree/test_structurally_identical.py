__author__ = "akhtar"

import unittest

from tests.test_tree.utils import SampleTree
from tree.problems.binary_tree.structurally_identical import \
    structurally_identical


class TestStructurallyIdentical(unittest.TestCase):
    def setUp(self):
        return super().setUp()
    
    def test_structurally_identical(self):
        print("TEST WHETHER TWO BINARY TREES ARE STRUCTURALLY IDENTICAL")
        print("===========================================================")
        
        root1 = SampleTree.create_1()
        root2 = SampleTree.create_3()
        print("First Tree:")
        SampleTree.print_1(message=False)
        print("Second Tree:")
        SampleTree.print_3(message=False)
        identical = structurally_identical(root1, root2)
        self.assertEqual(False, identical)
        print("Structurally Identical: {0}".format(identical))
        print("\n---------------------------------\n")

        root1 = SampleTree.create_4()
        root2 = SampleTree.create_4()
        print("First Tree:")
        SampleTree.print_4(message=False)
        print("Second Tree:")
        SampleTree.print_4(message=False)
        identical = structurally_identical(root1, root2)
        self.assertEqual(True, identical)
        print("Structurally Identical: {0}".format(identical))
        print("\n---------------------------------\n")

        root1 = SampleTree.create_4()
        root2 = SampleTree.create_9()
        print("First Tree:")
        SampleTree.print_4(message=False)
        print("Second Tree:")
        SampleTree.print_9(message=False)
        identical = structurally_identical(root1, root2)
        self.assertEqual(False, identical)
        print("Structurally Identical: {0}".format(identical))
        print("\n---------------------------------\n")
        
        root1 = SampleTree.create_6()
        root2 = SampleTree.create_4()
        print("First Tree:")
        SampleTree.print_6(message=False)
        print("Second Tree:")
        SampleTree.print_4(message=False)
        identical = structurally_identical(root1, root2)
        self.assertEqual(False, identical)
        print("Structurally Identical: {0}".format(identical), end="")
        
        print(
            "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")


if __name__ == "__main__":
    unittest.main()
