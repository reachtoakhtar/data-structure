from collections import deque

__author__ = "akhtar"


def find_maximum_element_recursive(node):
    """
    Find the maximum element in a binary tree with given root.

    :param BTreeNode node: The root of the tree.
    :return: the maximum element.
    :rtype: int
    """
    if node is None:
        return float('-inf')

    # Return maximum of 3 values:
    # 1. Node's data 2. Max in Left Subtree  3. Max in right subtree
    res = node.data
    lres = find_maximum_element_recursive(node.left)
    rres = find_maximum_element_recursive(node.right)

    return max(res, lres, rres)


def find_maximum_element_iterative(root):
    """
    Find the maximum element in a binary tree with given root.

    :param BTreeNode root: The root of the tree.
    :return: the maximum element.
    :rtype: int
    """
    maximum = root.data
    q = deque([])
    q.append(root)

    while len(q):
        node = q.popleft()
        if node.data > maximum:
            maximum = node.data

        if node.left is not None:
            q.append(node.left)

        if node.right is not None:
            q.append(node.right)

    return maximum
