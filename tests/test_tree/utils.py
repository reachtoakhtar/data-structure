__author__ = "akhtar"

from tree.nodes import BTreeNode


class SampleBTree:
    @staticmethod
    def create_1():
        """
                 57
        """
        # Root
        root = BTreeNode(57)
        return root

    @staticmethod
    def create_3():
        """
                 67
                /  \
               4   23
        """
        # Root
        root = BTreeNode(67)
    
        # Left subtree
        root.left = BTreeNode(4)
    
        # Right subtree
        root.right = BTreeNode(23)
        
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
        root = BTreeNode(5)
    
        # Left subtree
        root.left = BTreeNode(41)
    
        # Right subtree
        root.right = BTreeNode(6)
        root.right.left = BTreeNode(29)
        
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
        root = BTreeNode(10)
    
        # Left subtree
        root.left = BTreeNode(11)
        root.left.left = BTreeNode(7)
    
        # Right subtree
        root.right = BTreeNode(9)
        root.right.left = BTreeNode(15)
        root.right.right = BTreeNode(8)
        
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
        root = BTreeNode(10)
    
        # Left subtree
        root.left = BTreeNode(11)
        root.left.left = BTreeNode(7)
        root.left.left.right = BTreeNode(33)
    
        # Right subtree
        root.right = BTreeNode(9)
        root.right.left = BTreeNode(15)
        root.right.right = BTreeNode(8)
        root.right.right.left = BTreeNode(62)
        root.right.right.left.right = BTreeNode(4)
        
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
        root = BTreeNode(10)
    
        # Left subtree
        root.left = BTreeNode(11)
        root.left.left = BTreeNode(7)
        root.left.left.right = BTreeNode(33)
        root.left.left.right.left = BTreeNode(8)
        root.left.right = BTreeNode(15)
        root.left.right.right = BTreeNode(62)
        root.left.right.right.right = BTreeNode(4)
    
        # Right subtree
        root.right = BTreeNode(9)
        
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
        root = BTreeNode(10)
    
        # Left subtree
        root.left = BTreeNode(11)
    
        # Right subtree
        root.right = BTreeNode(9)
        root.right.left = BTreeNode(15)
        root.right.left.left = BTreeNode(33)
        root.right.left.left.left = BTreeNode(39)
        root.right.right = BTreeNode(8)
        root.right.right.left = BTreeNode(62)
        root.right.right.left.right = BTreeNode(4)
    
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
