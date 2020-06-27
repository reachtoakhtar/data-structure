__author__ = "akhtar"


def has_path_with_sum(node, sum):
    """
    Check the existence of path with given sum in a binary tree.

    :param BTreeNode node: A node of the tree.
    :return: whether path with given sum exists or not.
    :rtype: bool
    """
    # Return true if we run out of tree and s = 0
    if node is None:
        return sum == 0

    ans = 0
    sub_sum = sum - node.data

    # If we reach a leaf node and sum becomes 0, then return True
    if sub_sum == 0 and node.left is None and node.right is None:
        return True

    if node.left is not None:
        ans = ans or has_path_with_sum(node.left, sub_sum)
    if node.right is not None:
        ans = ans or has_path_with_sum(node.right, sub_sum)

    return bool(ans)
