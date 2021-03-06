__author__ = "akhtar"

import unittest

from tests.test_tree.utils import SampleBTree
from tree.problems.binary_tree.delete_node import delete_node
from tree.problems.binary_tree.traversal_inorder import inorder


class TestDeletetNode(unittest.TestCase):
    def setUp(self):
        return super().setUp()

    def test_delete_node(self):
        print("TEST DELETE NODE OF A BINARY TREE")
        print("===========================================================")
        
        root = SampleBTree.create_1()
        SampleBTree.print_1()
        node_to_delete = 15
        print("Node to delete: {0}".format(node_to_delete))
        print("Inorder traversal before delete:", end=" ")
        inorder(root)
        print()
        delete_node(root, node_to_delete)
        print("Inorder traversal after delete:", end=" ")
        inorder(root)
        print("\n\n")
        
        root = SampleBTree.create_3()
        SampleBTree.print_3()
        node_to_delete = 67
        print("Node to delete: {0}".format(node_to_delete))
        print("Inorder traversal before delete:", end=" ")
        inorder(root)
        print()
        delete_node(root, node_to_delete)
        print("Inorder traversal after delete:", end=" ")
        inorder(root)
        print("\n\n")
        
        root = SampleBTree.create_4()
        SampleBTree.print_4()
        node_to_delete = 86
        print("Node to delete: {0}".format(node_to_delete))
        print("Inorder traversal before delete:", end=" ")
        inorder(root)
        print()
        delete_node(root, node_to_delete)
        print("Inorder traversal after delete:", end=" ")
        inorder(root)
        print("\n\n")
        
        root = SampleBTree.create_6()
        SampleBTree.print_6()
        node_to_delete = 9
        print("Node to delete: {0}".format(node_to_delete))
        print("Inorder traversal before delete:", end=" ")
        inorder(root)
        print()
        delete_node(root, node_to_delete)
        print("Inorder traversal after delete:", end=" ")
        inorder(root)
        print("\n\n")
        
        root = SampleBTree.create_9()
        SampleBTree.print_9()
        node_to_delete = 8
        print("Node to delete: {0}".format(node_to_delete))
        print("Inorder traversal before delete:", end=" ")
        inorder(root)
        print()
        delete_node(root, node_to_delete)
        print("Inorder traversal after delete:", end=" ")
        inorder(root)
        
        print(
            "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")


if __name__ == "__main__":
    unittest.main()
