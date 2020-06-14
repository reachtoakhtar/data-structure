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
    def setUp(self):
        self.create_tree()

    def create_tree(self):
        self.root = TreeNode(10)
        self.root.left = TreeNode(11)
        self.root.left.left = TreeNode(7)
        self.root.right = TreeNode(9)
        self.root.right.left = TreeNode(15)
        self.root.right.right = TreeNode(8)

    def test_insert_into_tree(self):
        print("TEST INSERT INTO TREE")
        print("===========================================================")

        print("Tree to operate: ")
        print(" "*20 + "10 \n" + " "*18 + " /  \\ \n" + " "*17 + "11    9 \n" +
              " "*16 + "/     / \\ \n" + " "*15 + "7     15  8")

        print("Inorder traversal before insertion:", end=" ")
        Tree.inorder(self.root)
        print()

        Tree.insert(self.root, 12)

        print("Inorder traversal after insertion:", end=" ")
        Tree.inorder(self.root)

        print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")


if __name__ == "__main__":
    unittest.main()
