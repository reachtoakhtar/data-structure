__author__ = "akhtar"


def find_size(node):
    """
    Find the size of a binary tree.

    :param TreeNode node: The root of the tree.
    :return: the maximum element.
    :rtype: int
    """
    
    if node is None:
        return 0
    else:
        return find_size(node.left) + 1 + find_size(node.right)
