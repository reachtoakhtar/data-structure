__author__ = "akhtar"

from tree.binary_tree import TreeNode


class SampleTree:
    """
             10
            /  \
           11   9
          /    / \
         7    15  8
          \      /
          33    62
                 \
                  4
    """
    @staticmethod
    def create():
        # Root
        root = TreeNode(10)
    
        # Left subtree
        root.left = TreeNode(11)
        root.left.left = TreeNode(7)
        root.left.left.right = TreeNode(33)
    
        # Right subtree
        root.right = TreeNode(9)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(8)
        root.right.right.left = TreeNode(62)
        root.right.right.left.right = TreeNode(4)
        
        return root
    
    @staticmethod
    def print():
        print("Tree to operate: ")
        print(" "*20 + "10 \n" + " "*18 + " /  \\ \n" + " "*17 + "11    9 \n"
              + " "*16 + "/     / \\ \n" + " "*15 + "7     15  8\n" + " "*16
              + "\\" + " "*7 + "/ \n" + " "*16 + "33" + " "*5 + "62 \n"
              + " "*24 + "\\ \n" + " "*25 + "4\n")
