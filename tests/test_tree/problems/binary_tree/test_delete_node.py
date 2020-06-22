__author__ = "akhtar"

import unittest

from tests.test_tree.utils import SampleTree
from tree.binary_tree import Tree
from tree.problems.binary_tree.delete_node import delete_node


class TestDeletetNode(unittest.TestCase):
    def setUp(self):
        return super().setUp()

    def test_delete_node(self):
        print("TEST DELETE NODE OF A BINARY TREE")
        print("===========================================================")
        
        root = SampleTree.create_1()
        SampleTree.print_1()
        node_to_delete = 15
        print("Node to delete: {0}".format(node_to_delete))
        print("Inorder traversal before delete:", end=" ")
        Tree.inorder(root)
        print()
        delete_node(root, node_to_delete)
        print("Inorder traversal after delete:", end=" ")
        Tree.inorder(root)
        print("\n\n")
        
        root = SampleTree.create_3()
        SampleTree.print_3()
        node_to_delete = 67
        print("Node to delete: {0}".format(node_to_delete))
        print("Inorder traversal before delete:", end=" ")
        Tree.inorder(root)
        print()
        delete_node(root, node_to_delete)
        print("Inorder traversal after delete:", end=" ")
        Tree.inorder(root)
        print("\n\n")
        
        root = SampleTree.create_4()
        SampleTree.print_4()
        node_to_delete = 86
        print("Node to delete: {0}".format(node_to_delete))
        print("Inorder traversal before delete:", end=" ")
        Tree.inorder(root)
        print()
        delete_node(root, node_to_delete)
        print("Inorder traversal after delete:", end=" ")
        Tree.inorder(root)
        print("\n\n")
        
        root = SampleTree.create_6()
        SampleTree.print_6()
        node_to_delete = 9
        print("Node to delete: {0}".format(node_to_delete))
        print("Inorder traversal before delete:", end=" ")
        Tree.inorder(root)
        print()
        delete_node(root, node_to_delete)
        print("Inorder traversal after delete:", end=" ")
        Tree.inorder(root)
        print("\n\n")
        
        root = SampleTree.create_9()
        SampleTree.print_9()
        node_to_delete = 8
        print("Node to delete: {0}".format(node_to_delete))
        print("Inorder traversal before delete:", end=" ")
        Tree.inorder(root)
        print()
        delete_node(root, node_to_delete)
        print("Inorder traversal after delete:", end=" ")
        Tree.inorder(root)
        
        print(
            "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")


if __name__ == "__main__":
    unittest.main()
