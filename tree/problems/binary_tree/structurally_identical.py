__author__ = "akhtar"


def structurally_identical(root1, root2):
    """
    Given two binary trees, find if they are structurally identical.

    :param BTreeNode root1: The root of the first tree.
    :param BTreeNode root2: The root of the second tree.
    :return: whether trees are structurally identical.
    :rtype: bool
    """
    
    if root1 is None and root2 is None:
        return True
    elif not all([root1, root2]):
        return False
    else:
        a = root1.data == root2.data
        b = structurally_identical(root1.left, root2.left)
        c = structurally_identical(root1.right, root2.right)
        
        return a and b and c
