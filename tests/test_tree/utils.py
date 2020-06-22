__author__ = "akhtar"

from tree.binary_tree import TreeNode


class SampleTree:
    @staticmethod
    def create_1():
        """
                 57
        """
        # Root
        root = TreeNode(57)
        return root

    @staticmethod
    def create_3():
        """
                 67
                /  \
               4   23
        """
        # Root
        root = TreeNode(67)
    
        # Left subtree
        root.left = TreeNode(4)
    
        # Right subtree
        root.right = TreeNode(23)
        
        return root

    @staticmethod
    def create_4():
        """
                 5
                / \
               41  6
                  /
                 29
        """
        # Root
        root = TreeNode(5)
    
        # Left subtree
        root.left = TreeNode(41)
    
        # Right subtree
        root.right = TreeNode(6)
        root.right.left = TreeNode(29)
        
        return root

    @staticmethod
    def create_6():
        """
                 10
                /  \
               11   9
              /    / \
             7    15  8
        """
        # Root
        root = TreeNode(10)
    
        # Left subtree
        root.left = TreeNode(11)
        root.left.left = TreeNode(7)
    
        # Right subtree
        root.right = TreeNode(9)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(8)
        
        return root

    @staticmethod
    def create_9():
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
    def create_left_weighted():
        """
                 10
                /  \
               11   9
              /  \
             7   15
              \    \
              33    62
              /      \
             8        4
        """
        # Root
        root = TreeNode(10)
    
        # Left subtree
        root.left = TreeNode(11)
        root.left.left = TreeNode(7)
        root.left.left.right = TreeNode(33)
        root.left.left.right.left = TreeNode(8)
        root.left.right = TreeNode(15)
        root.left.right.right = TreeNode(62)
        root.left.right.right.right = TreeNode(4)
    
        # Right subtree
        root.right = TreeNode(9)
        
        return root

    @staticmethod
    def create_right_weighted():
        """
                 10
                /  \
               11   9
                   / \
                  15  8
                  /   /
                 33  62
                 /    \
                39     4
        """
        # Root
        root = TreeNode(10)
    
        # Left subtree
        root.left = TreeNode(11)
    
        # Right subtree
        root.right = TreeNode(9)
        root.right.left = TreeNode(15)
        root.right.left.left = TreeNode(33)
        root.right.left.left.left = TreeNode(39)
        root.right.right = TreeNode(8)
        root.right.right.left = TreeNode(62)
        root.right.right.left.right = TreeNode(4)
    
        return root

    @staticmethod
    def print_1(message=True):
        if message:
            print("Tree to operate: ")
        
        print(" "*20 + "57 \n")
    
    @staticmethod
    def print_3(message=True):
        if message:
            print("Tree to operate: ")
        
        print(" "*20 + "67 \n"
              + " "*19 + "/  \\ \n"
              + " "*18 + "4   23 \n")
    
    @staticmethod
    def print_4(message=True):
        if message:
            print("Tree to operate: ")
        
        print(" "*20 + "5 \n"
              + " "*19 + "/ \\ \n"
              + " "*17 + " 41  6 \n"
              + " "*21 + "/ \n"
              + " "*20 + "29  \n")
    
    @staticmethod
    def print_6(message=True):
        if message:
            print("Tree to operate: ")
       
        print(" "*20 + "10 \n"
              + " "*19 + "/  \\ \n"
              + " "*17 + "11    9 \n"
              + " "*16 + "/     / \\ \n"
              + " "*15 + "7     15  8\n")
    
    @staticmethod
    def print_9(message=True):
        if message:
            print("Tree to operate: ")
        
        print(" "*20 + "10 \n"
              + " "*19 + "/  \\ \n"
              + " "*17 + "11    9 \n"
              + " "*16 + "/     / \\ \n"
              + " "*15 + "7     15  8\n"
              + " "*16 + "\\" + " "*7 + "/ \n"
              + " "*16 + "33" + " "*5 + "62 \n"
              + " "*24 + "\\ \n"
              + " "*25 + "4\n")

    @staticmethod
    def print_left_weighted(message=True):
        if message:
            print("Tree to operate: ")
        
        print(" "*20 + "10 \n"
              + " "*19 + "/  \\ \n"
              + " "*17 + "11    9 \n"
              + " "*17 + "/ \\ \n"
              + " "*16 + "7  15 \n"
              + " "*17 + "\\   \\ \n"
              + " "*18 + "33  62 \n"
              + " "*18 + "/    \\ \n"
              + " "*17 + "8      4\n")
    
    @staticmethod
    def print_right_weighted(message=True):
        if message:
            print("Tree to operate: ")
       
        print(" "*20 + "10 \n"
              + " "*19 + "/  \\ \n"
              + " "*17 + "11    9 \n"
              + " "*22 + "/ \\ \n"
              + " "*21 + "15   8 \n"
              + " "*21 + "/    / \n"
              + " "*20 + "33  62 \n"
              + " "*20 + "/    \\ \n"
              + " "*19 + "39     4\n")
