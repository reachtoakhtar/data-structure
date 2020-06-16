from collections import deque

__author__ = "akhtar"


def find_element_recursive(node, element):
    """
    Find the given element in a binary tree.

    :param TreeNode root: The root of the tree.
    :param int element: The element to be searched.
    :return: true if the element is found else false.
    :rtype: bool
    """
    if node is None:
        return False

    if node.data == element:
        return True

    temp = find_element_recursive(node.left, element)
    if temp:
        return temp
    else:
        return find_element_recursive(node.right, element)


def find_element_iterative(root):
    """
    Find the given element in a binary tree.

    :param TreeNode root: The root of the tree.
    :param int element: The element to be searched.
    :return: true if the element is found else false.
    :rtype: bool
    """
    pass
