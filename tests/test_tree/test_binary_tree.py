import unittest

from tree.binary_tree import TreeNode, Tree

__author__ = "akhtar"


class TestBinaryTree(unittest.TestCase):
    """
    Initial tree:
             10
            /  \
           11   9
          /    / \
         7    15  8
    """
    @staticmethod
    def print_sample_tree():
        print("Tree to operate: ")
        print(" "*20 + "10 \n" + " "*18 + " /  \\ \n" + " "*17 + "11    9 \n" +
              " "*16 + "/     / \\ \n" + " "*15 + "7     15  8\n")

    def setUp(self):
        self.create_tree()

    def create_tree(self):
        self.root = SampleTree.create()
def test_tree_traversal(self):
        print("TEST TREE TRAVERSAL")
        print("===========================================================")
        TestBinaryTree.print_sample_tree()

        print("Levelorder traversal (BFS):", end=" ")
        Tree.levelorder(self.root)
        print("\n")

        print("Preorder traversal (iterative):", end=" ")
        Tree.preorder_iterative(self.root)
        print()

        print("Preorder traversal (recursive):", end=" ")
        Tree.preorder_recursive(self.root)
        print("\n")

        print("Inorder traversal (iterative):", end=" ")
        Tree.inorder_iterative(self.root)
        print()

        print("Inorder traversal (recursive):", end=" ")
        Tree.inorder_recursive(self.root)
        print("\n")

        print("Postorder traversal (iterative):", end=" ")
        Tree.postorder_iterative(self.root)
        print()

        print("Postorder traversal (recursive):", end=" ")
        Tree.postorder_recursive(self.root)

        print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")


if __name__ == "__main__":
    unittest.main()
