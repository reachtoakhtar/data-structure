__author__ = "akhtar"


def mirror(node):
    """
    Find the mirror of a given binary tree.

    :param TreeNode node: A node of the tree.
    :return: nothing.
    :rtype: None
    """
    if node is None:
        return
    
    temp = node.left
    mirror(node.left)
    mirror(node.right)
    
    node.left, node.right = node.right, temp
